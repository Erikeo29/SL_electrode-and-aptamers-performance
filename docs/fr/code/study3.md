# Code de l'étude 3 — couplage itératif de la chute ohmique

**Sommaire :**
1. Architecture
2. Design expérimental
3. Boucle itérative de correction $IR$
4. Courants parasites (Ni et Cu)
5. Orchestration et CSV
6. Analyse spécifique ($R_u$)
7. Dépendances

---

## 1. Architecture

L'étude 3 réutilise le moteur de simulation commun et active la correction de chute ohmique :

| Fichier | Rôle |
|---------|------|
| `parameters_swv.py` | Paramètres physiques (partagé), dont `CircuitParameters` ($R_u$) |
| `swv_simulation.py` | Moteur SWV avec boucle itérative $IR$ (activée si $R_u > 0$) |
| `parametric_study_Ru.py` | Orchestrateur de l'étude 3 (plan factoriel complet) |

La cinétique de Butler-Volmer, le solveur ODE implicite et l'extraction des métriques sont identiques aux études 1 et 2.

---

## 2. Design expérimental

L'étude 3 fait varier la **résistance non compensée** $R_u$ conjointement avec RF et Ni :

```python
STUDY_PARAMS = {
    'RF':    [1.0, 2.0, 5.0],                        # 3 niveaux
    'Ni_pct': [0, 5, 10],                              # 3 niveaux
    'R_u':   [0, 50, 100, 200, 500, 1000],             # 6 niveaux [Ohm]
}

FIXED_PARAMS = {
    'Cu_pct': 0,
    'contamination': 0,
    'frequency': 25,          # 25 Hz fixe
}
# Total: 3 × 3 × 6 = 54 runs
```

---

## 3. Boucle itérative de correction $IR$

C'est la **spécificité majeure** de l'étude 3. Lorsque $R_u > 0$, le potentiel effectif à l'interface est réduit par la chute ohmique :

$$E_{interface} = E_{appliqué} - I_{total} \times R_u$$

Or $I_{total}$ dépend de $E_{interface}$ via la cinétique BV : il faut donc une résolution **auto-cohérente**. La méthode `_run_half_period()` implémente une boucle itérative :

```python
def _run_half_period(self, E_applied, Gamma_ox, theta_Cu,
                     n_substeps, dt_sub, R_u):
    max_ir_iter = 10 if R_u > 0 else 1
    tol_ir = 1e-9       # [A] tolérance (~1 nA)
    E_interface = E_applied
    IR_drop = 0.0

    for ir_iter in range(max_ir_iter):
        # Résoudre ODE à E_interface courant
        Gamma_ox_new = Gamma_ox
        for _ in range(n_substeps):
            Gamma_ox_new = solve_surface_ode(
                Gamma_ox_new, E_interface, dt_sub, params)

        # Calculer les courants
        Delta_Gamma = Gamma_ox_new - Gamma_ox
        I_MB = mb.n * c.F * A_eff_MB * Delta_Gamma / dt_half
        I_cap = elec.C_dl_eff * elec.A_real * swv.delta_Ep / dt_half
        I_Ni = current_Ni_impurity(E_interface, params)
        I_total = I_MB + I_cap + I_Ni + I_Cu

        if R_u <= 0:
            break

        # Mettre à jour E_interface avec IR drop
        E_interface_new = E_applied - I_total * R_u
        IR_drop = I_total * R_u

        if abs(E_interface_new - E_interface) < tol_ir * R_u:
            E_interface = E_interface_new
            break

        E_interface = E_interface_new
```

La convergence est typiquement atteinte en 3-5 itérations. La tolérance de 1 nA sur le courant assure une précision de $\Delta E < 1\;\mu$V même à $R_u = 1000\;\Omega$.

---

## 4. Courants parasites (Ni et Cu)

Le courant parasite du Ni (dissolution en PBS pH 7.4) est modélisé par une cinétique de Tafel unidirectionnelle :

```python
def current_Ni_impurity(E, params):
    eta = E - ni.E0                                     # E0_Ni = -0.15 V
    exp_arg = np.clip(ni.alpha * ni.n * c.f * eta, -30, 30)
    i_local = ni.i_corr * np.exp(exp_arg)               # i_corr = 1e-3 A/m2
    return elec.Ni_fraction * elec.A_real * i_local
```

Le courant parasite du Cu (formation Cu$_2$O) suit un modèle de Langmuir avec ODE implicite :

```python
def solve_Cu_ode(theta_Cu, E, dt, params):
    k_ox = cu.k0 * np.exp(exp_ox)     # Oxydation Cu -> Cu2O
    k_red = cu.k0 * np.exp(exp_red)    # Réduction Cu2O -> Cu

    theta_new = (theta_Cu + dt * k_ox) / (1.0 + dt * (k_ox + k_red))
    return np.clip(theta_new, 0.0, 1.0)
```

---

## 5. Orchestration et CSV

L'orchestrateur crée les paramètres avec $R_u$ variable :

```python
for i, combo in enumerate(combos):
    params = create_params(
        RF=combo['RF'],
        Ni_pct=combo['Ni_pct'],
        Cu_pct=combo['Cu_pct'],
        contamination=combo['contamination'],
        frequency=combo['frequency'],
        R_u=combo['R_u'],              # Variable spécifique à l'étude 3
        seed=42 + run_id,
    )
    sim = SWVSimulation(params, study_dir)
    sim.run(n_substeps=30)
    metrics = sim.save_results(run_dir)
```

Le nommage des runs encode $R_u$ : `003_RF2.0_Ni5_Ru500`.

Les métriques spécifiques à l'étude 3 sont `IR_drop_mV` (chute ohmique maximale) et le décalage de $E_{peak}$ par rapport à la valeur sans $R_u$.

---

## 6. Analyse spécifique ($R_u$)

La fonction `generate_analysis_plots()` produit 4 plots d'analyse propres à l'étude $R_u$ :

```python
# Plot 1 : SNR vs R_u (dégradation du signal)
ax.plot(subset['R_u'], subset['SNR'], marker='o', ...)
ax.set_xlabel('$R_u$ ($\\Omega$)')

# Plot 2 : IR drop vs R_u (chute ohmique linéaire IR = I_peak × R_u)
ax.plot(subset['R_u'], subset['IR_drop_mV'], 'o-', ...)

# Plot 3 : Décalage E_peak vs R_u
E_shift = (subset['E_peak_V'].values - E_ref[0]) * 1e3    # mV
ax.plot(subset['R_u'], E_shift, ...)

# Plot 4 : FWHM vs R_u (élargissement du pic)
ax.axhline(y=45.3, color='k', linestyle='--', label='FWHM idéal (45 mV, n=2)')
```

Le rapport `RAPPORT_ANALYSE.md` présente un tableau détaillé de l'évolution des métriques en fonction de $R_u$ pour l'électrode propre (RF = 1, Ni = 0 %).

---

## 7. Dépendances

- `numpy`, `scipy`, `matplotlib` : calcul, ajustement, tracé (partagés)
- `pandas` : analyse CSV et génération du rapport
- `itertools.product` : génération du plan factoriel
