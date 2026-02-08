# Code de l'étude 1 — paramètres d'électrode

**Sommaire :**
1. Architecture
2. Paramètres et constantes
3. Cinétique de Butler-Volmer
4. Solveur ODE implicite
5. Boucle SWV (forward/reverse)
6. Plan factoriel et orchestration
7. Extraction des métriques
8. Dépendances

---

## 1. Architecture

Le code est structuré en fichiers modulaires :

| Fichier | Rôle |
|---------|------|
| `parameters_swv.py` | Paramètres physiques (constantes, MB, électrode, impuretés, bruit) |
| `swv_simulation.py` | Moteur de simulation SWV (cinétique BV, boucle temporelle, métriques) |
| `parametric_study_swv.py` | Orchestrateur de l'étude 1 (plan factoriel complet) |

---

## 2. Paramètres et constantes

Les paramètres sont organisés en `dataclass` imbriquées. Le conteneur principal `SWVModelParameters` regroupe tous les sous-ensembles :

```python
@dataclass
class SWVModelParameters:
    constants: Constants = None       # F, R, T
    mb: MBParameters = None           # E0=-0.24 V, n=2, k0=50 s-1
    swv: SWVParameters = None         # f=25 Hz, dEp=25 mV, dEs=4 mV
    electrode: ElectrodeParameters = None  # A_geo, RF, Ni%, Cu%, contamination
    ni_impurity: NiImpurityParams = None
    cu_impurity: CuImpurityParams = None
    circuit: CircuitParameters = None      # R_u
    noise: NoiseParameters = None
```

Deux propriétés dérivées sont centrales pour l'étude 1 :

```python
@property
def k0_eff(self) -> float:
    """k0 effectif, dégradé par la rugosité (SAM désordonnée)."""
    beta_SAM = 0.3
    return self.mb.k0 * np.exp(-beta_SAM * (self.electrode.RF - 1.0))

@property
def Gamma_eff(self) -> float:
    """Densité effective d'aptamères [mol/m2]. Seule la fraction Au propre est fonctionnalisable."""
    return self.mb.Gamma_total * self.electrode.Au_fraction
```

La fraction d'or libre $f_{Au}$ est calculée par :

```python
@property
def Au_fraction(self) -> float:
    return max(0.0, 1.0 - self.Ni_fraction - self.Cu_fraction - self.contamination)
```

---

## 3. Cinétique de Butler-Volmer

Le flux de surface est calculé par la cinétique de Butler-Volmer pour le couple $\text{MB}_{ox}$ / $\text{MB}_{red}$ confiné en surface. Les constantes de vitesse $k_f$ (réduction) et $k_b$ (oxydation) sont en $\text{s}^{-1}$ (espèce adsorbée, pas en solution) :

```python
def bv_rates_surface(E: float, params: SWVModelParameters):
    k0 = params.k0_eff          # Dégradé par rugosité
    eta = E - params.mb.E0      # Surtension [V]

    # Clamper pour éviter overflow numérique
    exp_f = np.clip(-mb.alpha * mb.n * c.f * eta, -30, 30)
    exp_b = np.clip((1 - mb.alpha) * mb.n * c.f * eta, -30, 30)

    k_f = k0 * np.exp(exp_f)    # Réduction
    k_b = k0 * np.exp(exp_b)    # Oxydation
    return k_f, k_b
```

---

## 4. Solveur ODE implicite

L'ODE de surface $d\Gamma_{ox}/dt = k_b \cdot \Gamma_{red} - k_f \cdot \Gamma_{ox}$ est linéaire en $\Gamma_{ox}$, ce qui permet une solution analytique du schéma d'Euler implicite :

$$\Gamma_{ox}^{n+1} = \frac{\Gamma_{ox}^{n} + \Delta t \cdot k_b \cdot \Gamma_{total}}{1 + \Delta t \cdot (k_f + k_b)}$$

```python
def solve_surface_ode(Gamma_ox_init, E, dt, params):
    k_f, k_b = bv_rates_surface(E, params)
    Gamma_total = params.Gamma_eff

    numerator = Gamma_ox_init + dt * k_b * Gamma_total
    denominator = 1.0 + dt * (k_f + k_b)
    Gamma_ox_new = numerator / denominator

    return np.clip(Gamma_ox_new, 0.0, Gamma_total)
```

Ce schéma est inconditionnellement stable et ne nécessite pas de solveur non-linéaire (Newton).

---

## 5. Boucle SWV (forward/reverse)

La méthode `run()` de la classe `SWVSimulation` applique la séquence SWV complète. Pour chaque marche de l'escalier de potentiel :

```python
def run(self, n_substeps=50):
    tau = swv.tau                      # Période [s]
    dt_half = tau / 2.0                # Demi-période
    dt_sub = dt_half / n_substeps      # Sous-pas temporel

    Gamma_ox = params.Gamma_eff        # CI : MB oxydé à E_start >> E0

    for i_step in range(n_steps):
        E_base = swv.E_start + direction * i_step * swv.delta_Es

        # --- Pulse forward (+dEp) ---
        E_fwd = E_base + swv.delta_Ep
        (Gamma_ox, theta_Cu, I_MB_fwd, I_cap_fwd, I_Ni_fwd, I_Cu_fwd,
         I_total_fwd, ir_drop_fwd) = self._run_half_period(
            E_fwd, Gamma_ox, theta_Cu, n_substeps, dt_sub, R_u)

        # --- Pulse reverse (-dEp) ---
        E_rev = E_base - swv.delta_Ep
        (Gamma_ox, theta_Cu, I_MB_rev, ...) = self._run_half_period(
            E_rev, Gamma_ox, theta_Cu, n_substeps, dt_sub, R_u)

        # --- Courant net (annulation du capacitif) ---
        I_net_step = I_total_fwd - I_total_rev
```

Le courant de chaque demi-période est calculé par la méthode de la **charge transférée** :

$$I_{MB} = \frac{n \cdot F \cdot A_{eff} \cdot \Delta\Gamma_{ox}}{\tau / 2}$$

```python
Delta_Gamma = Gamma_ox_new - Gamma_ox
I_MB = mb.n * c.F * A_eff_MB * Delta_Gamma / dt_half
```

Les courants parasites (Ni, Cu) et capacitif sont ajoutés au courant total :

```python
I_cap = elec.C_dl_eff * elec.A_real * swv.delta_Ep / dt_half
I_total = I_MB + I_cap + I_Ni + I_Cu
```

---

## 6. Plan factoriel et orchestration

L'étude 1 explore le **plan factoriel complet** de toutes les combinaisons :

```python
STUDY_PARAMS = {
    'RF':            [1.0, 1.5, 2.0, 3.0, 5.0],    # 5 niveaux
    'Ni_pct':        [0, 2, 5, 10],                   # 4 niveaux
    'Cu_pct':        [0, 2, 5],                        # 3 niveaux
    'contamination': [0, 0.1, 0.3],                    # 3 niveaux
}
# Total: 5 × 4 × 3 × 3 = 180 runs
```

L'orchestrateur génère toutes les combinaisons via `itertools.product`, crée les paramètres avec la factory `create_params()`, lance la simulation et enregistre les résultats dans un CSV (séparateur `;`) :

```python
for i, combo in enumerate(combos):
    params = create_params(
        RF=combo['RF'], Ni_pct=combo['Ni_pct'],
        Cu_pct=combo['Cu_pct'], contamination=combo['contamination'],
        seed=42 + run_id,
    )
    sim = SWVSimulation(params, study_dir)
    sim.run(n_substeps=30)
    metrics = sim.save_results(run_dir)
```

Le script supporte la **reprise** (`--resume`) en vérifiant les runs déjà complétés dans le CSV existant.

---

## 7. Extraction des métriques

La méthode `extract_metrics()` effectue le post-traitement du voltammogramme :

**Soustraction de la ligne de base** (interpolation linéaire entre les extrémités du scan) :

```python
n_bl = min(15, len(I) // 5)
bl_left = np.mean(I[:n_bl])
bl_right = np.mean(I[-n_bl:])
I_baseline_linear = bl_left + (bl_right - bl_left) * np.arange(len(I)) / (len(I) - 1)
I_corrected_curve = I - I_baseline_linear
```

**Ajustement gaussien** pour évaluer la qualité du pic :

```python
def gaussian(x, A, mu, sigma, offset):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2)) + offset

popt, _ = curve_fit(gaussian, E, I_corrected_curve, p0=p0, maxfev=5000)
```

**Métriques extraites** : $I_{peak}$ (nA), $E_{peak}$ (V), FWHM (mV), $I_{baseline}$ ($\mu$A), SNR $= I_{peak} / \sigma_{résidus}$, $R^2$ gaussien, $K = k^0_{eff} / f$.

---

## 8. Dépendances

- `numpy` : calcul numérique
- `scipy.optimize.curve_fit` : ajustement gaussien
- `matplotlib` : tracé des voltammogrammes et plots d'analyse
- `pandas` : génération du rapport d'analyse
- Aucune dépendance FEM (modèle ODE de surface, pas de maillage)
