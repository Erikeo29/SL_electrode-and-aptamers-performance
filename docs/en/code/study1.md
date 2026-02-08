# Study 1 code -- electrode parameters

**Contents:**
1. Architecture
2. Parameters and constants
3. Butler-Volmer kinetics
4. Implicit ODE solver
5. SWV loop (forward/reverse)
6. Factorial design and orchestration
7. Metric extraction
8. Dependencies

---

## 1. Architecture

The code is organized into modular files:

| File | Role |
|------|------|
| `parameters_swv.py` | Physical parameters (constants, MB, electrode, impurities, noise) |
| `swv_simulation.py` | SWV simulation engine (BV kinetics, time loop, metrics) |
| `parametric_study_swv.py` | Study 1 orchestrator (full factorial design) |

---

## 2. Parameters and constants

Parameters are organized as nested `dataclass` objects. The main container `SWVModelParameters` groups all subsets:

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

Two derived properties are central to study 1:

```python
@property
def k0_eff(self) -> float:
    """Effective k0, degraded by roughness (disordered SAM)."""
    beta_SAM = 0.3
    return self.mb.k0 * np.exp(-beta_SAM * (self.electrode.RF - 1.0))

@property
def Gamma_eff(self) -> float:
    """Effective aptamer density [mol/m2]. Only the clean Au fraction is functionalizable."""
    return self.mb.Gamma_total * self.electrode.Au_fraction
```

The free gold fraction $f_{Au}$ is computed by:

```python
@property
def Au_fraction(self) -> float:
    return max(0.0, 1.0 - self.Ni_fraction - self.Cu_fraction - self.contamination)
```

---

## 3. Butler-Volmer kinetics

The surface flux is computed using Butler-Volmer kinetics for the surface-confined $\text{MB}_{ox}$ / $\text{MB}_{red}$ couple. Rate constants $k_f$ (reduction) and $k_b$ (oxidation) are in $\text{s}^{-1}$ (adsorbed species, not in solution):

```python
def bv_rates_surface(E: float, params: SWVModelParameters):
    k0 = params.k0_eff          # Degraded by roughness
    eta = E - params.mb.E0      # Overpotential [V]

    # Clamp to avoid numerical overflow
    exp_f = np.clip(-mb.alpha * mb.n * c.f * eta, -30, 30)
    exp_b = np.clip((1 - mb.alpha) * mb.n * c.f * eta, -30, 30)

    k_f = k0 * np.exp(exp_f)    # Reduction
    k_b = k0 * np.exp(exp_b)    # Oxidation
    return k_f, k_b
```

---

## 4. Implicit ODE solver

The surface ODE $d\Gamma_{ox}/dt = k_b \cdot \Gamma_{red} - k_f \cdot \Gamma_{ox}$ is linear in $\Gamma_{ox}$, which allows an analytical implicit Euler scheme:

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

This scheme is unconditionally stable and does not require a nonlinear solver (Newton).

---

## 5. SWV loop (forward/reverse)

The `run()` method of the `SWVSimulation` class applies the full SWV sequence. For each step of the potential staircase:

```python
def run(self, n_substeps=50):
    tau = swv.tau                      # Period [s]
    dt_half = tau / 2.0                # Half-period
    dt_sub = dt_half / n_substeps      # Sub-step

    Gamma_ox = params.Gamma_eff        # IC: MB oxidized at E_start >> E0

    for i_step in range(n_steps):
        E_base = swv.E_start + direction * i_step * swv.delta_Es

        # --- Forward pulse (+dEp) ---
        E_fwd = E_base + swv.delta_Ep
        (Gamma_ox, theta_Cu, I_MB_fwd, I_cap_fwd, I_Ni_fwd, I_Cu_fwd,
         I_total_fwd, ir_drop_fwd) = self._run_half_period(
            E_fwd, Gamma_ox, theta_Cu, n_substeps, dt_sub, R_u)

        # --- Reverse pulse (-dEp) ---
        E_rev = E_base - swv.delta_Ep
        (Gamma_ox, theta_Cu, I_MB_rev, ...) = self._run_half_period(
            E_rev, Gamma_ox, theta_Cu, n_substeps, dt_sub, R_u)

        # --- Net current (capacitive cancellation) ---
        I_net_step = I_total_fwd - I_total_rev
```

The current for each half-period is calculated using the **transferred charge** method:

$$I_{MB} = \frac{n \cdot F \cdot A_{eff} \cdot \Delta\Gamma_{ox}}{\tau / 2}$$

```python
Delta_Gamma = Gamma_ox_new - Gamma_ox
I_MB = mb.n * c.F * A_eff_MB * Delta_Gamma / dt_half
```

Parasitic currents (Ni, Cu) and capacitive current are added to the total:

```python
I_cap = elec.C_dl_eff * elec.A_real * swv.delta_Ep / dt_half
I_total = I_MB + I_cap + I_Ni + I_Cu
```

---

## 6. Factorial design and orchestration

Study 1 explores **180 combinations** from the full factorial design:

```python
STUDY_PARAMS = {
    'RF':            [1.0, 1.5, 2.0, 3.0, 5.0],    # 5 levels
    'Ni_pct':        [0, 2, 5, 10],                   # 4 levels
    'Cu_pct':        [0, 2, 5],                        # 3 levels
    'contamination': [0, 0.1, 0.3],                    # 3 levels
}
# Total: 5 x 4 x 3 x 3 = 180 runs
```

The orchestrator generates all combinations via `itertools.product`, creates parameters with the `create_params()` factory, runs the simulation and records results in a CSV (`;` separator):

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

The script supports **resumption** (`--resume`) by checking already completed runs in the existing CSV.

---

## 7. Metric extraction

The `extract_metrics()` method performs voltammogram post-processing:

**Baseline subtraction** (linear interpolation between scan endpoints):

```python
n_bl = min(15, len(I) // 5)
bl_left = np.mean(I[:n_bl])
bl_right = np.mean(I[-n_bl:])
I_baseline_linear = bl_left + (bl_right - bl_left) * np.arange(len(I)) / (len(I) - 1)
I_corrected_curve = I - I_baseline_linear
```

**Gaussian fit** to evaluate peak quality:

```python
def gaussian(x, A, mu, sigma, offset):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2)) + offset

popt, _ = curve_fit(gaussian, E, I_corrected_curve, p0=p0, maxfev=5000)
```

**Extracted metrics**: $I_{peak}$ (nA), $E_{peak}$ (V), FWHM (mV), $I_{baseline}$ ($\mu$A), SNR $= I_{peak} / \sigma_{residuals}$, Gaussian $R^2$, $K = k^0_{eff} / f$.

---

## 8. Dependencies

- `numpy`: numerical computation
- `scipy.optimize.curve_fit`: Gaussian fitting
- `matplotlib`: voltammogram and analysis plots
- `pandas`: analysis report generation
- No FEM dependency (surface ODE model, no mesh)
