The square wave voltammetry frequency is a powerful optimisation lever for aptamer biosensors. Increasing the frequency raises the peak current (better sensitivity), but risks shifting the system into an irreversible kinetic regime where the signal degrades. This study systematically explores the interaction between frequency and electrode surface condition to identify optimal measurement conditions.

**Contents:**
1. Physics of the frequency effect
2. Frequency--electrode interactions
3. Experimental design
4. Expected results
5. Bibliographical references

---

## 1. Physics of the frequency effect

### 1.1 Current--frequency relationship

For a quasi-reversible system with adsorbed species (the case of MB bound to the aptamer), the SWV peak current depends on frequency according to:

$$I_{peak} \sim n \cdot F \cdot A \cdot \Gamma_{eff} \cdot f \cdot \Delta\psi$$

where:
- $n = 2$ (number of electrons for MB)
- $F = 96\,485$ C/mol (Faraday constant)
- $A$ = real electrode surface area (cm²)
- $\Gamma_{eff}$ = effective surface density of aptamers (mol/cm²)
- $f$ = SWV frequency (Hz)
- $\Delta\psi$ = dimensionless net current function, dependent on $K$ and $\delta E_p$

In the quasi-reversible regime, $I_{peak}$ increases approximately linearly with $f$. This linearity is exploited to optimise biosensor sensitivity.

### 1.2 Dimensionless kinetic parameter $K$

The parameter $K$ relates the electron transfer rate constant to the frequency:

$$K = \frac{k^0_{eff}}{f}$$

As $f$ increases, $K$ decreases and the system evolves from the reversible regime toward the irreversible regime:

| Frequency (Hz) | $K$ (for $k^0_{eff} = 50$ s⁻¹) | Regime |
|-----------------|----------------------------------|--------|
| 10 | 5.0 | Reversible |
| 25 | 2.0 | Quasi-reversible |
| 50 | 1.0 | Quasi-reversible |
| 100 | 0.5 | Quasi-reversible |
| 200 | 0.25 | Quasi-reversible / irreversible |
| 500 | 0.1 | Irreversible |

### 1.3 Peak potential shift

At high frequency (low $K$), the SWV peak splits into two components: the forward component shifts toward more negative potentials and the reverse component toward more positive potentials. The net peak ($I_{forward} - I_{reverse}$) shows an apparent shift in $E_{peak}$ and broadening.

For a purely reversible system ($K \gg 1$), $E_{peak}$ remains constant and equal to $E^0$ regardless of frequency.

### 1.4 FWHM broadening

FWHM increases with frequency due to the transition toward the irreversible regime:

- At 10 Hz ($K = 5$): FWHM close to the ideal value (45.3 mV)
- At 500 Hz ($K = 0.1$): FWHM significantly broadened ($> 100$ mV)

The broadening follows a monotonic relationship with $1/K$ and can be modelled by the Lovric equations for SWV of adsorbed systems.

---

## 2. Frequency--electrode interactions

### 2.1 RF $\times$ frequency interaction

The roughness factor amplifies the frequency effect on $I_{peak}$ because it multiplies the effective surface area:

$$I_{peak}(\text{RF}, f) \sim \text{RF} \cdot f \cdot (\text{constant})$$

However, $I_{baseline}$ also increases with RF, so the gain in SNR is not proportional to RF.

### 2.2 Ni $\times$ frequency interaction

At low frequency (high $K$), the system has time to reach equilibrium even with a reduced $k^0_{eff}$ due to nickel exposure. At high frequency, the $k^0_{eff}$ reduction due to Ni translates into a more pronounced current drop because the system transitions to the irreversible regime earlier.

The Ni $\times$ frequency interaction is therefore synergistic and negative: electrodes with exposed Ni are even more penalised at high frequency.

| Condition | $k^0_{eff}$ (s⁻¹) | $K$ at 25 Hz | $K$ at 200 Hz | Consequence at high frequency |
|-----------|---------------------|-------------|--------------|-------------------------------|
| Ni = 0 % | $\sim 50$ | 2.0 | 0.25 | Quasi-reversible |
| Ni = 10 % | $\sim 20$ | 0.8 | 0.10 | Irreversible |

---

## 3. Experimental design

### 3.1 Objective

This study examines the influence of Square Wave Voltammetry frequency on the aptamer biosensor response, in interaction with electrode surface parameters (RF and exposed Ni). The goal is to understand how the kinetic regime evolves with frequency and to identify optimal measurement conditions.

### 3.2 Factors and levels

| Factor | Levels | Values |
|--------|--------|--------|
| RF | 4 | 1.0, 1.5, 2.0, 3.0 |
| $\text{Ni}_{exposed}$ | 3 | 0, 2, 5 % |
| Frequency | 6 | 10, 25, 50, 100, 200, 500 Hz |

### 3.3 Total number of combinations

$$4 \;(\text{RF}) \times 3 \;(\text{Ni}) \times 6 \;(\text{frequency}) = 72 \text{ combinations}$$

### 3.4 Fixed parameters

| Parameter | Value | Justification |
|-----------|-------|---------------|
| $\text{Cu}_{exposed}$ | 0 % | Isolate frequency--electrode effect |
| Contamination | 0 % | Clean reference surface |
| $R_u$ | 0 $\Omega$ | No ohmic drop |
| $\delta E_s$ | 4 mV | Standard SWV |
| $\delta E_p$ | 25 mV | Standard SWV |

Exposed copper, contamination, and uncompensated resistance are set to zero to exclusively isolate the interaction between frequency and the dominant electrode parameters (RF and Ni).

---

## 4. Expected results

### 4.1 Summary by metric

| Metric | Expected behaviour |
|--------|-------------------|
| $I_{peak}$ vs $f$ | Growth $\approx$ linear without Ni; sub-linear with exposed Ni |
| $E_{peak}$ vs $f$ | Stable at low $f$, negative shift at high $f$; amplified by Ni |
| FWHM vs $f$ | Progressive broadening; more pronounced for electrodes with exposed Ni |
| SNR vs $f$ | Increases then degrades at high $f$; optimal frequency depends on surface condition |
| $K$ vs $f$ | Hyperbolic decrease ($K = k^0_{eff}/f$) |

### 4.2 Physical interpretation

1. **$I_{peak}$ vs $f$**: approximately linear growth for electrodes without Ni. Sub-linear for electrodes with exposed Ni (transition toward irreversibility).
2. **$E_{peak}$ vs $f$**: stable at low frequency, negative shift at high frequency. Shift amplified by Ni exposure.
3. **FWHM vs $f$**: progressive broadening with frequency. More pronounced for electrodes with exposed Ni.
4. **SNR vs $f$**: increases first with $f$ (more signal), then degrades at high frequency (peak broadening and current loss). Optimal frequency depends on the surface condition.
5. **$K$ vs $f$**: hyperbolic decrease ($K = k^0_{eff} / f$). Allows mapping the kinetic regime for each electrode--frequency combination.

---

## 5. Bibliographical references

*For the complete list of references, see the Bibliographical References section in the Appendices menu.*
