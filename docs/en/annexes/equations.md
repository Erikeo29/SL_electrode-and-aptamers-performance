**Contents:**
1. SWV waveform
2. Butler-Volmer kinetics (adsorbed species)
3. Faradaic current (adsorbed species)
4. Dimensionless kinetic parameter
5. Electrode surface parameters
6. Ohmic drop and RC filtering
7. Extracted metrics
8. Bibliographical references

---

In square-wave voltammetry (SWV), the applied signal combines a potential staircase with symmetric pulses. Unlike classical cyclic voltammetry (CV) where diffusion transport dominates, the parametric studies in this application deal with **surface-adsorbed species** (methylene blue on aptamers). The kinetics are therefore governed by the surface coverage fraction rather than a concentration gradient in solution.

## 1. SWV waveform

The applied potential $E(t)$ is decomposed into a staircase onto which square pulses are superimposed:

### 1.1 Potential staircase

At each step $k$ (period $\tau = 1/f$), the base potential advances by $\delta E_s$:

$$ E_{base}(k) = E_{start} + k \times \delta E_s $$

### 1.2 Forward and reverse pulses

On each staircase step, a pulse of amplitude $\delta E_p$ is applied:

$$ E_{forward} = E_{base}(k) + \delta E_p $$
$$ E_{reverse} = E_{base}(k) - \delta E_p $$

### 1.3 Net current

The current is sampled at the end of each half-period. The net current is the difference:

$$ I_{net} = I_{forward} - I_{reverse} $$

This differential current **eliminates the capacitive current** (which is identical in magnitude on both pulses) and maximises the faradaic component.

### Waveform parameters

| Symbol | Name | Typical value | Unit |
|--------|------|---------------|------|
| $f$ | SWV frequency | 1 -- 500 | Hz |
| $\delta E_s$ | step potential (staircase) | 1 -- 10 | mV |
| $\delta E_p$ | pulse amplitude | 10 -- 100 | mV |
| $E_{start}$ | initial potential | variable | V |
| $E_{end}$ | final potential | variable | V |

---

## 2. Butler-Volmer kinetics (adsorbed species)

For species confined at the surface (methylene blue bound to an aptamer), the forward and reverse rate constants are expressed as:

$$ k_f = k^0_{eff} \exp\left(-\frac{\alpha \, n \, F}{R \, T} \, \eta \right) $$

$$ k_b = k^0_{eff} \exp\left(\frac{(1-\alpha) \, n \, F}{R \, T} \, \eta \right) $$

With the overpotential corrected for ohmic drop:

$$ \eta = E(t) - E^0 - I \times R_u $$

Where:
- $k^0_{eff}$ = effective surface kinetic constant [s$^{-1}$] (not m/s, since species are adsorbed)
- $\alpha$ = charge transfer coefficient (dimensionless)
- $n$ = number of electrons transferred (2 for MB)
- $F$ = Faraday constant (96 485 C/mol)
- $R$ = ideal gas constant (8.314 J/(mol$\cdot$K))
- $T$ = temperature [K]
- $E^0$ = formal potential of the MB/LB couple [V]
- $R_u$ = uncompensated resistance [$\Omega$]

### Kinetic parameters

| Symbol | Name | Value | Unit |
|--------|------|-------|------|
| $F$ | Faraday constant | 96 485 | C/mol |
| $R$ | gas constant | 8.314 | J/(mol$\cdot$K) |
| $T$ | temperature | 298.15 | K |
| $\alpha$ | transfer coefficient | 0.5 | -- |
| $n$ | number of electrons (MB) | 2 | -- |
| $E^0$ | formal potential MB/LB | $\approx -0.24$ | V vs Ag/AgCl |

---

## 3. Faradaic current (adsorbed species)

The faradaic current for redox species confined at the surface (not in solution) is:

$$ I_{farad} = n \, F \, A \, \Gamma_{eff} \left( k_f \, \theta_{ox} - k_b \, \theta_{red} \right) $$

With the surface coverage conservation constraint:

$$ \theta_{ox} + \theta_{red} = 1 $$

Where:
- $A$ = geometric electrode area [m$^2$]
- $\Gamma_{eff}$ = effective surface density of the redox species [mol/m$^2$]
- $\theta_{ox}$ = fraction of species in oxidised form (dimensionless)
- $\theta_{red}$ = fraction of species in reduced form (dimensionless)
- $k_f$, $k_b$ = forward and reverse rate constants [s$^{-1}$]

> **Note**: Unlike the solution-phase case (classical CV), there is no diffusion layer. The SWV peak does not result from solution depletion but from the progressive conversion of adsorbed species.

### Faradaic current parameters

| Symbol | Name | Typical value | Unit |
|--------|------|---------------|------|
| $A$ | geometric area | $1.77 \times 10^{-6}$ | m$^2$ |
| $\Gamma_{eff}$ | effective surface density | $10^{-11}$ -- $10^{-10}$ | mol/m$^2$ |
| $\Gamma_0$ | maximum surface density (MB) | $\sim 4.5 \times 10^{-10}$ | mol/m$^2$ |

---

## 4. Dimensionless kinetic parameter

The Lovric dimensionless parameter $K$ compares the charge transfer kinetics to the SWV excitation frequency:

$$ K = \frac{k^0_{eff}}{f} $$

Where $f$ is the SWV frequency [Hz] and $k^0_{eff}$ the effective kinetic constant [s$^{-1}$].

### Kinetic regimes

| $K$ range | Regime | Behaviour |
|-----------|--------|-----------|
| $K > 5$ | reversible | $I_{net}$ proportional to $f$, minimum FWHM |
| $0.1 < K < 5$ | quasi-reversible | maximum net current, optimal sensitivity |
| $K < 0.1$ | irreversible | broad peak, net current decreases |

### Ideal full width at half maximum (FWHM)

In the reversible regime, the full width at half maximum of the net current peak is:

$$ FWHM_{ideal} = \frac{90.6}{n} \text{ mV} $$

For methylene blue ($n = 2$):

$$ FWHM_{ideal} = \frac{90.6}{2} = 45.3 \text{ mV} $$

Broadening beyond this theoretical value indicates lateral interactions between adsorbates, surface heterogeneity, or a quasi-reversible/irreversible regime.

---

## 5. Electrode surface parameters

### 5.1 Effective kinetic constant (Au/Ni/Cu composite electrodes)

For an electrode with variable composition, the effective kinetic constant is the weighted average over the surface fractions:

$$ k^0_{eff} = k^0_{Au} \times f_{Au} + k^0_{Ni} \times f_{Ni} + k^0_{Cu} \times f_{Cu} $$

Where $f_{Au} + f_{Ni} + f_{Cu} = 1$ and each $k^0_i$ is the intrinsic kinetic constant of metal $i$ [s$^{-1}$].

### 5.2 Effective surface density

The effective surface density of electroactive redox species accounts for the roughness factor and contamination:

$$ \Gamma_{eff} = \Gamma_0 \times RF \times \left(1 - \frac{contamination}{100}\right) $$

With the roughness factor:

$$ RF = \frac{A_{real}}{A_{geometric}} $$

### Surface parameters

| Symbol | Name | Typical value | Unit |
|--------|------|---------------|------|
| $k^0_{Au}$ | gold kinetic constant | 10 -- 100 | s$^{-1}$ |
| $k^0_{Ni}$ | nickel kinetic constant | 0.1 -- 10 | s$^{-1}$ |
| $k^0_{Cu}$ | copper kinetic constant | 1 -- 50 | s$^{-1}$ |
| $f_{Au}$, $f_{Ni}$, $f_{Cu}$ | surface fractions | 0 -- 1 | -- |
| $RF$ | roughness factor | 1 -- 3 | -- |
| $\Gamma_0$ | maximum MB coverage | $\sim 4.5 \times 10^{-10}$ | mol/m$^2$ |
| contamination | contamination rate | 0 -- 50 | % |

---

## 6. Ohmic drop and RC filtering

### 6.1 Ohmic drop ($IR$ drop)

The ohmic drop shifts the potential effectively seen by the interface:

$$ IR_{drop} = I_{peak} \times R_u $$

The actual potential at the interface is:

$$ E_{real} = E_{applied} - I \times R_u $$

> Excessive ohmic drop ($IR_{drop} > 5$ mV) distorts the SWV peak: broadening, flattening, and potential shift.

### 6.2 RC time constant

The time constant of the RC circuit formed by the uncompensated resistance and the double-layer capacitance limits the response speed:

$$ \tau_{RC} = R_u \times C_{dl} $$

For the capacitive current to dissipate before sampling, the following condition must hold:

$$ \tau_{RC} \ll \frac{1}{2f} $$

typically $\tau_{RC} < \frac{1}{10f}$.

### Ohmic drop parameters

| Symbol | Name | Typical value | Unit |
|--------|------|---------------|------|
| $R_u$ | uncompensated resistance | 10 -- 1000 | $\Omega$ |
| $C_{dl}$ | double-layer capacitance | 10 -- 100 | $\mu$F/cm$^2$ |
| $\tau_{RC}$ | RC time constant | 0.01 -- 10 | ms |

---

## 7. Extracted metrics

The parametric studies evaluate biosensor performance using seven complementary metrics:

### 7.1 Signal-to-noise ratio (SNR)

$$ SNR = \frac{I_{peak}}{\sigma_{residuals}} $$

Where $\sigma_{residuals}$ is the standard deviation of the residuals after baseline subtraction.

### 7.2 Metrics summary table

| Metric | Symbol | Formula | Unit | Objective |
|--------|--------|---------|------|-----------|
| Peak current | $I_{peak}$ | max($I_{net}$) | $\mu$A | maximise |
| Peak potential | $E_{peak}$ | $E$ at $I_{peak}$ | V | $\approx E^0$ |
| Full width at half maximum | FWHM | width at $I_{peak}/2$ | mV | minimise ($\geq 45.3$ mV) |
| Signal-to-noise ratio | SNR | $I_{peak} / \sigma_{residuals}$ | -- | maximise |
| Ohmic drop | $IR_{drop}$ | $I_{peak} \times R_u$ | mV | minimise ($< 5$ mV) |
| Form factor | $FF$ | $I_{peak} / (FWHM \times I_{base})$ | -- | maximise |
| Global score | $S_{global}$ | weighted normalised average | -- | maximise |

---

## 8. Bibliographical references

*For the complete list of references, see the Bibliographical References section in the Appendices menu.*
