# Study 2 code -- SWV frequency effect

**Contents:**
1. Architecture
2. Experimental design
3. Kinetic parameter $K$
4. Time step adaptation
5. Orchestration and CSV
6. Frequency-specific analysis
7. Dependencies

---

## 1. Architecture

Study 2 reuses the shared simulation engine and adds a frequency-specific orchestrator:

| File | Role |
|------|------|
| `parameters_swv.py` | Physical parameters (shared with studies 1 and 3) |
| `swv_simulation.py` | SWV simulation engine (shared) |
| `parametric_study_frequency.py` | Study 2 orchestrator (full factorial design) |

Butler-Volmer kinetics, the implicit ODE solver and metric extraction are identical to study 1 (see study 1 code documentation).

---

## 2. Experimental design

Study 2 varies the **SWV frequency** together with RF and Ni, while other parameters are fixed:

```python
STUDY_PARAMS = {
    'RF':        [1.0, 1.5, 2.0, 3.0],          # 4 levels
    'Ni_pct':    [0, 2, 5],                       # 3 levels
    'frequency': [10, 25, 50, 100, 200, 500],     # 6 levels [Hz]
}

FIXED_PARAMS = {
    'Cu_pct': 0,
    'contamination': 0,
    'R_u': 0,
}
# Total: 4 x 3 x 6 = 72 runs
```

---

## 3. Kinetic parameter $K$

The dimensionless parameter $K = k^0_{eff} / f$ determines the kinetic regime. It is computed in `extract_metrics()`:

```python
K_dimensionless = self.params.k0_eff / self.params.swv.frequency
```

| Regime | $K$ | Expected behavior |
|--------|-----|-------------------|
| Reversible | $K > 5$ | Sharp peak, $E_{peak} = E^0$ |
| Quasi-reversible | $0.1 < K < 5$ | Broadened peak, $E_{peak}$ shifts |
| Irreversible | $K < 0.1$ | Very broad peak, reduced current |

Frequency directly modifies the period $\tau = 1/f$ and thus the time step:

```python
@property
def tau(self) -> float:
    """Period [s]."""
    return 1.0 / self.frequency

@property
def effective_scan_rate(self) -> float:
    """Effective scan rate [V/s]."""
    return self.delta_Es * self.frequency
```

---

## 4. Time step adaptation

The simulation time step automatically adapts to the frequency through the half-period calculation:

```python
tau = swv.tau                      # 1/f [s] -- ranges from 100 ms (10 Hz) to 2 ms (500 Hz)
dt_half = tau / 2.0                # Half-period
dt_sub = dt_half / n_substeps      # Sub-step
```

At 500 Hz, $\tau = 2$ ms and $dt_{sub} \approx 33\;\mu$s (with `n_substeps=30`), requiring fine temporal resolution to capture fast kinetics.

---

## 5. Orchestration and CSV

The orchestrator creates parameters with variable frequency via `create_params()`:

```python
for i, combo in enumerate(combos):
    params = create_params(
        RF=combo['RF'],
        Ni_pct=combo['Ni_pct'],
        Cu_pct=combo['Cu_pct'],
        contamination=combo['contamination'],
        frequency=combo['frequency'],    # Study 2 specific variable
        R_u=combo['R_u'],
        seed=42 + run_id,
    )
    sim = SWVSimulation(params, study_dir)
    sim.run(n_substeps=30)
    metrics = sim.save_results(run_dir)
```

Run naming encodes the frequency: `003_RF1.5_Ni0_f50Hz`.

---

## 6. Frequency-specific analysis

The `generate_analysis_plots()` function produces 4 analysis plots specific to the frequency study:

```python
# Plot 1: SNR vs frequency (Lovric quasi-reversible maximum identification)
ax.plot(subset['frequency'], subset['SNR'], marker='o', ...)
ax.set_xscale('log')

# Plot 2: K vs SNR (kinetic regime mapping)
ax.plot(subset['K_dimensionless'], subset['SNR'], 'o-', ...)
ax.axvline(x=1, color='gray', linestyle='--', label='K=1')
ax.axvline(x=5, color='gray', linestyle=':', label='K=5')

# Plot 3: FWHM vs frequency (peak broadening with scan rate)
ax.axhline(y=45.3, color='k', linestyle='--', label='Ideal FWHM (45 mV, n=2)')

# Plot 4: I_peak vs frequency (current evolution)
ax.plot(subset['frequency'], subset['I_peak_nA'], ...)
```

The `RAPPORT_ANALYSE.md` report automatically identifies the optimal $K$ and corresponding frequency for the clean electrode (Ni = 0%).

---

## 7. Dependencies

- `numpy`, `scipy`, `matplotlib`: computation, fitting, plotting (shared)
- `pandas`: CSV analysis and report generation
- `itertools.product`: factorial design generation
