# Code de l'étude 2 — effet de la fréquence SWV

**Sommaire :**
1. Architecture
2. Design expérimental
3. Paramètre cinétique $K$
4. Adaptation du pas de temps
5. Orchestration et CSV
6. Analyse spécifique (fréquence)
7. Dépendances

---

## 1. Architecture

L'étude 2 réutilise le moteur de simulation commun et ajoute un orchestrateur spécifique :

| Fichier | Rôle |
|---------|------|
| `parameters_swv.py` | Paramètres physiques (partagé avec les études 1 et 3) |
| `swv_simulation.py` | Moteur de simulation SWV (partagé) |
| `parametric_study_frequency.py` | Orchestrateur de l'étude 2 (plan factoriel complet) |

La cinétique de Butler-Volmer, le solveur ODE implicite et l'extraction des métriques sont identiques à l'étude 1 (voir documentation code de l'étude 1).

---

## 2. Design expérimental

L'étude 2 fait varier la **fréquence SWV** conjointement avec RF et Ni, les autres paramètres étant fixés :

```python
STUDY_PARAMS = {
    'RF':        [1.0, 1.5, 2.0, 3.0],          # 4 niveaux
    'Ni_pct':    [0, 2, 5],                       # 3 niveaux
    'frequency': [10, 25, 50, 100, 200, 500],     # 6 niveaux [Hz]
}

FIXED_PARAMS = {
    'Cu_pct': 0,
    'contamination': 0,
    'R_u': 0,
}
# Total: 4 × 3 × 6 = 72 runs
```

---

## 3. Paramètre cinétique $K$

Le paramètre sans dimension $K = k^0_{eff} / f$ détermine le régime cinétique. Il est calculé dans `extract_metrics()` :

```python
K_dimensionless = self.params.k0_eff / self.params.swv.frequency
```

| Régime | $K$ | Comportement attendu |
|--------|-----|----------------------|
| Réversible | $K > 5$ | Pic fin, $E_{peak} = E^0$ |
| Quasi-réversible | $0.1 < K < 5$ | Pic élargi, $E_{peak}$ se déplace |
| Irréversible | $K < 0.1$ | Pic très large, courant réduit |

La fréquence modifie directement la période $\tau = 1/f$ et donc le pas de temps :

```python
@property
def tau(self) -> float:
    """Période [s]."""
    return 1.0 / self.frequency

@property
def effective_scan_rate(self) -> float:
    """Vitesse de balayage effective [V/s]."""
    return self.delta_Es * self.frequency
```

---

## 4. Adaptation du pas de temps

Le pas de temps de la simulation s'adapte automatiquement à la fréquence via le calcul de la demi-période :

```python
tau = swv.tau                      # 1/f [s] — varie de 100 ms (10 Hz) à 2 ms (500 Hz)
dt_half = tau / 2.0                # Demi-période
dt_sub = dt_half / n_substeps      # Sous-pas temporel
```

À 500 Hz, $\tau = 2$ ms et $dt_{sub} \approx 33\;\mu$s (avec `n_substeps=30`), ce qui impose une résolution temporelle fine pour capturer la cinétique rapide.

---

## 5. Orchestration et CSV

L'orchestrateur crée les paramètres avec la fréquence variable via `create_params()` :

```python
for i, combo in enumerate(combos):
    params = create_params(
        RF=combo['RF'],
        Ni_pct=combo['Ni_pct'],
        Cu_pct=combo['Cu_pct'],
        contamination=combo['contamination'],
        frequency=combo['frequency'],    # Variable spécifique à l'étude 2
        R_u=combo['R_u'],
        seed=42 + run_id,
    )
    sim = SWVSimulation(params, study_dir)
    sim.run(n_substeps=30)
    metrics = sim.save_results(run_dir)
```

Le nommage des runs encode la fréquence : `003_RF1.5_Ni0_f50Hz`.

---

## 6. Analyse spécifique (fréquence)

La fonction `generate_analysis_plots()` produit 4 plots d'analyse propres à l'étude fréquence :

```python
# Plot 1 : SNR vs fréquence (identification du maximum quasi-réversible de Lovric)
ax.plot(subset['frequency'], subset['SNR'], marker='o', ...)
ax.set_xscale('log')

# Plot 2 : K vs SNR (cartographie des régimes cinétiques)
ax.plot(subset['K_dimensionless'], subset['SNR'], 'o-', ...)
ax.axvline(x=1, color='gray', linestyle='--', label='K=1')
ax.axvline(x=5, color='gray', linestyle=':', label='K=5')

# Plot 3 : FWHM vs fréquence (élargissement avec la vitesse de balayage)
ax.axhline(y=45.3, color='k', linestyle='--', label='FWHM idéal (45 mV, n=2)')

# Plot 4 : I_peak vs fréquence (évolution du courant)
ax.plot(subset['frequency'], subset['I_peak_nA'], ...)
```

Le rapport `RAPPORT_ANALYSE.md` identifie automatiquement le $K$ optimal et la fréquence correspondante pour l'électrode propre (Ni = 0 %).

---

## 7. Dépendances

- `numpy`, `scipy`, `matplotlib` : calcul, ajustement, tracé (partagés)
- `pandas` : analyse CSV et génération du rapport
- `itertools.product` : génération du plan factoriel
