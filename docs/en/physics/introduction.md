Electrochemical aptamer-based biosensors rely on measuring a redox signal to detect target molecules in real time. The sensor is interrogated using square wave voltammetry (SWV), a pulsed technique offering significantly higher sensitivity and signal-to-noise ratio than conventional cyclic voltammetry (CV).

This page presents the SWV principle, the redox reporter used (methylene blue) and the quantitative metrics extracted from the voltammogram. These metrics form the analytical basis for the three parametric studies in this application.

**Contents:**
1. Principle of square wave voltammetry
2. Methylene blue peak
3. Metrics extracted from the voltammogram
4. Metrics summary table

---

## 1. Principle of square wave voltammetry

### 1.1 Why SWV rather than CV?

Cyclic voltammetry (CV) is the most common electrochemical technique, but it mixes faradaic current (useful signal) and capacitive current (background noise). SWV solves this problem by subtracting two current measurements taken at symmetric instants, thereby eliminating the capacitive component. In practice, SWV achieves detection limits 10 to 100 times lower than CV.

![Waveform and voltammogram comparison: CV (top) vs SWV (bottom)](../../../assets/illustrations/swv_vs_cv_waveform.png)

### 1.2 Waveform

Square Wave Voltammetry (SWV) superimposes two signals onto the working potential:

1. **Staircase**: potential increment $\delta E_s = 4$ mV at each cycle.
2. **Symmetric pulses**: amplitude $\pm\,\delta E_p = 25$ mV around each step.

At each staircase step, a positive (*forward*) pulse followed by a negative (*reverse*) pulse is applied. The current is sampled at the end of each pulse, when the capacitive current has decayed exponentially.

### 1.3 Net current

The net current is defined by:

$$I_{net} = I_{forward} - I_{reverse}$$

This subtraction eliminates the capacitive component (double-layer charging current), which is identical in magnitude for both pulses. Only the faradaic current, proportional to the concentration of the electroactive species, is retained. SWV thus provides a significantly better signal-to-noise ratio than CV.

### 1.4 Typical parameters

| Parameter | Symbol | Typical value |
|-----------|--------|---------------|
| Potential increment | $\delta E_s$ | 4 mV |
| Pulse amplitude | $\delta E_p$ | 25 mV |
| Frequency | $f$ | 10 -- 500 Hz |
| Initial potential | $E_{start}$ | −0.05 V |
| Final potential | $E_{end}$ | −0.45 V |

---

## 2. Methylene blue peak

### 2.1 Redox reporter

Methylene blue (MB) is a cationic dye from the **phenothiazine** family, widely used as a redox reporter in E-AB biosensors. Its structure comprises:

- a **tricyclic phenothiazine core**: two benzene rings fused to a central thiazine ring containing a sulfur atom (S) and a nitrogen atom (N);
- two **dimethylamino** groups —N(CH₃)₂ at positions 3 and 7, responsible for the blue colour;
- a **methyl group** —CH₃ on the central nitrogen of the thiazine ring, giving the molecule its permanent positive charge.

> Molecular formula: C₁₆H₁₈N₃S⁺ (cation) · Cl⁻ (counter-ion) — molar mass: 319.85 g/mol.

MB is covalently conjugated to the distal end (5') of the aptamer, which itself is anchored to the gold electrode surface via a thiol bond (3' end).

### 2.2 Redox reaction

The methylene blue redox reaction involves two electrons and two protons:

$$\text{MB}_{ox} + 2e^- + 2H^+ \rightleftharpoons \text{MB}_{red}$$

The current peak is centred around the apparent standard potential:

$$E^0 = -0.24 \text{ V vs Ag/AgCl} \quad (\text{pH } 7.4, \text{ PBS buffer})$$

The potential $E^0$ depends on pH according to the Nernst equation: a shift of approximately $-59$ mV per pH unit at 25 °C for a process involving equal numbers of protons and electrons.

### 2.3 Detection mechanism

In the absence of target, the aptamer adopts a conformation that keeps MB close to the electrode surface, enabling efficient electron transfer. When the target binds to the aptamer, the conformational change moves MB away from the surface, reducing the peak current. The current variation is proportional to the target concentration.

![E-AB biosensor principle: without target (left) vs with target (right)](../../../assets/illustrations/eab_biosensor_structure.png)

---

## 3. Metrics extracted from the voltammogram

### 3.1 $I_{peak}$ -- peak current (nA)

The maximum amplitude of the faradaic peak after baseline subtraction. Directly proportional to:

- The surface density of electroactive aptamers $\Gamma_{eff}$ (mol/cm²)
- The SWV frequency $f$ (Hz)
- The number of electrons exchanged ($n = 2$ for MB)

### 3.2 $E_{peak}$ -- peak potential (V)

The potential at which the net current reaches its maximum. For a reversible system, $E_{peak} \approx E^0$. A shift from the expected value ($-0.24$ V) may indicate:

- Uncompensated resistance (ohmic shift $IR$)
- A change in local environment (pH, ionic strength)
- Kinetic effects at high frequency

### 3.3 FWHM -- full width at half maximum (mV)

The total width at half maximum of the SWV peak. For an ideal Nernstian system with $n$ electrons:

$$\text{FWHM}_{ideal} = \frac{90.6}{n} \text{ mV} \quad (25\,°\text{C})$$

For methylene blue ($n = 2$): $\text{FWHM}_{ideal} = 45.3$ mV. Broadening beyond this value indicates quasi-reversible kinetics, surface heterogeneity, or uncompensated resistance.

### 3.4 SNR -- signal-to-noise ratio

$$\text{SNR} = \frac{I_{peak}}{\sigma_{residuals}}$$

An SNR $> 10$ is generally required for reliable quantitative measurement. An SNR $> 50$ is considered excellent.

### 3.5 $I_{baseline}$ -- baseline current (µA)

The background current measured away from the faradaic peak, reflecting the residual capacitive contribution and parasitic currents. Proportional to the real electrode surface area ($\propto \text{RF}$) and to the double-layer capacitance $C_{dl}$.

### 3.6 $IR_{drop}$ -- ohmic drop (mV)

$$IR_{drop} = I_{peak} \times R_u$$

This shift moves the peak toward more negative potentials and broadens it. At nanoampere-level currents and with $R_u < 100\;\Omega$, the $IR_{drop}$ generally remains negligible ($< 1$ mV).

### 3.7 $K$ -- dimensionless kinetic parameter

$$K = \frac{k^0_{eff}}{f}$$

where $k^0_{eff}$ is the effective electron transfer rate constant (s⁻¹) and $f$ the SWV frequency (Hz).

| Regime | Value of $K$ | Behaviour |
|--------|--------------|-----------|
| Reversible | $K > 5$ | Sharp peak, $E_{peak} = E^0$ |
| Quasi-reversible | $0.1 < K < 5$ | Broadened peak, $E_{peak}$ shifts |
| Irreversible | $K < 0.1$ | Very broad peak, reduced current |

For aptamer biosensors with MB, $k^0_{eff}$ is typically in the range of 10 to 100 s⁻¹, placing the system in the quasi-reversible regime at typical SWV frequencies (25--200 Hz).

---

## 4. Metrics summary table

| Metric | Symbol | Unit | Typical value (25 Hz, clean electrode) | Sensitive to |
|--------|--------|------|----------------------------------------|--------------|
| Peak current | $I_{peak}$ | nA | 30 -- 80 | RF, Ni, contamination, $f$ |
| Peak potential | $E_{peak}$ | V | −0.24 | $R_u$, $f$ (high), Ni |
| Width at half max | FWHM | mV | 45 -- 60 | $f$, $R_u$, Ni |
| Signal-to-noise ratio | SNR | — | 50 -- 200 | Ni (dominant), RF, contamination |
| Baseline current | $I_{baseline}$ | µA | 0.1 -- 1.0 | RF ($\propto$ RF) |
| Ohmic drop | $IR_{drop}$ | mV | < 0.1 | $R_u$, RF × $R_u$ |
| Kinetic parameter | $K$ | — | 0.2 -- 4.0 | $f$, Ni (via $k^0_{eff}$) |
