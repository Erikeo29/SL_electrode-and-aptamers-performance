# Study 3 code -- iterative ohmic drop coupling

**Contents:**
1. Architecture
2. Experimental design
3. Iterative $IR$ correction loop
4. Parasitic currents (Ni and Cu)
5. Orchestration and CSV
6. $R_u$-specific analysis
7. Dependencies

---

## 1. Architecture

Study 3 reuses the shared simulation engine and activates the ohmic drop correction:

| File | Role |
|------|------|
| `parameters_swv.py` | Physical parameters (shared), including `CircuitParameters` ($R_u$) |
| `swv_simulation.py` | SWV engine with iterative $IR$ loop (activated when $R_u > 0$) |
| `parametric_study_Ru.py` | Study 3 orchestrator (full factorial design) |

Butler-Volmer kinetics, the implicit ODE solver and metric extraction are identical to studies 1 and 2.

---

## 2. Experimental design

Study 3 varies the **uncompensated resistance** $R_u$ together with RF and Ni:

```python
STUDY_PARAMS = {
    'RF':    [1.0, 2.0, 5.0],                        # 3 levels
    'Ni_pct': [0, 5, 10],                              # 3 levels
    'R_u':   [0, 50, 100, 200, 500, 1000],             # 6 levels [Ohm]
}

FIXED_PARAMS = {
    'Cu_pct': 0,
    'contamination': 0,
    'frequency': 25,          # 25 Hz fixed
}
# Total: 3 x 3 x 6 = 54 runs
```

---

## 3. Iterative $IR$ correction loop

This is the **key feature** of study 3. When $R_u > 0$, the effective interface potential is reduced by the ohmic drop:

$$E_{interface} = E_{applied} - I_{total} \times R_u$$

Since $I_{total}$ depends on $E_{interface}$ through BV kinetics, a **self-consistent** solution is required. The `_run_half_period()` method implements an iterative loop:

```python
def _run_half_period(self, E_applied, Gamma_ox, theta_Cu,
                     n_substeps, dt_sub, R_u):
    max_ir_iter = 10 if R_u > 0 else 1
    tol_ir = 1e-9       # [A] tolerance (~1 nA)
    E_interface = E_applied
    IR_drop = 0.0

    for ir_iter in range(max_ir_iter):
        # Solve ODE at current E_interface
        Gamma_ox_new = Gamma_ox
        for _ in range(n_substeps):
            Gamma_ox_new = solve_surface_ode(
                Gamma_ox_new, E_interface, dt_sub, params)

        # Compute currents
        Delta_Gamma = Gamma_ox_new - Gamma_ox
        I_MB = mb.n * c.F * A_eff_MB * Delta_Gamma / dt_half
        I_cap = elec.C_dl_eff * elec.A_real * swv.delta_Ep / dt_half
        I_Ni = current_Ni_impurity(E_interface, params)
        I_total = I_MB + I_cap + I_Ni + I_Cu

        if R_u <= 0:
            break

        # Update E_interface with IR drop
        E_interface_new = E_applied - I_total * R_u
        IR_drop = I_total * R_u

        if abs(E_interface_new - E_interface) < tol_ir * R_u:
            E_interface = E_interface_new
            break

        E_interface = E_interface_new
```

Convergence is typically reached in 3-5 iterations. The 1 nA tolerance ensures a precision of $\Delta E < 1\;\mu$V even at $R_u = 1000\;\Omega$.

---

## 4. Parasitic currents (Ni and Cu)

The parasitic Ni current (dissolution in PBS pH 7.4) is modeled with unidirectional Tafel kinetics:

```python
def current_Ni_impurity(E, params):
    eta = E - ni.E0                                     # E0_Ni = -0.15 V
    exp_arg = np.clip(ni.alpha * ni.n * c.f * eta, -30, 30)
    i_local = ni.i_corr * np.exp(exp_arg)               # i_corr = 1e-3 A/m2
    return elec.Ni_fraction * elec.A_real * i_local
```

The parasitic Cu current (Cu$_2$O formation) follows a Langmuir model with an implicit ODE:

```python
def solve_Cu_ode(theta_Cu, E, dt, params):
    k_ox = cu.k0 * np.exp(exp_ox)     # Oxidation Cu -> Cu2O
    k_red = cu.k0 * np.exp(exp_red)    # Reduction Cu2O -> Cu

    theta_new = (theta_Cu + dt * k_ox) / (1.0 + dt * (k_ox + k_red))
    return np.clip(theta_new, 0.0, 1.0)
```

---

## 5. Orchestration and CSV

The orchestrator creates parameters with variable $R_u$:

```python
for i, combo in enumerate(combos):
    params = create_params(
        RF=combo['RF'],
        Ni_pct=combo['Ni_pct'],
        Cu_pct=combo['Cu_pct'],
        contamination=combo['contamination'],
        frequency=combo['frequency'],
        R_u=combo['R_u'],              # Study 3 specific variable
        seed=42 + run_id,
    )
    sim = SWVSimulation(params, study_dir)
    sim.run(n_substeps=30)
    metrics = sim.save_results(run_dir)
```

Run naming encodes $R_u$: `003_RF2.0_Ni5_Ru500`.

Study 3 specific metrics are `IR_drop_mV` (maximum ohmic drop) and the $E_{peak}$ shift relative to the value without $R_u$.

---

## 6. $R_u$-specific analysis

The `generate_analysis_plots()` function produces 4 analysis plots specific to the $R_u$ study:

```python
# Plot 1: SNR vs R_u (signal degradation)
ax.plot(subset['R_u'], subset['SNR'], marker='o', ...)
ax.set_xlabel('$R_u$ ($\\Omega$)')

# Plot 2: IR drop vs R_u (linear ohmic drop IR = I_peak x R_u)
ax.plot(subset['R_u'], subset['IR_drop_mV'], 'o-', ...)

# Plot 3: E_peak shift vs R_u
E_shift = (subset['E_peak_V'].values - E_ref[0]) * 1e3    # mV
ax.plot(subset['R_u'], E_shift, ...)

# Plot 4: FWHM vs R_u (peak broadening)
ax.axhline(y=45.3, color='k', linestyle='--', label='Ideal FWHM (45 mV, n=2)')
```

The `RAPPORT_ANALYSE.md` report presents a detailed table of metric evolution as a function of $R_u$ for the clean electrode (RF = 1, Ni = 0%).

---

## 7. Dependencies

- `numpy`, `scipy`, `matplotlib`: computation, fitting, plotting (shared)
- `pandas`: CSV analysis and report generation
- `itertools.product`: factorial design generation
