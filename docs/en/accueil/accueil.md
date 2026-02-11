**Author's note** — *This project was designed entirely by the author, from a blank page to its deployment. Content creation was carried out with the support of artificial intelligence tools, particularly for writing and debugging code and for internet research. All results shown in this project come from deterministic physical models (Butler-Volmer kinetics for surface-adsorbed species). This work is made available to be freely copied, duplicated and adapted for learning purposes.*

&nbsp;

**Contents:**
1. Objective
2. Available studies
3. Navigation
4. Methodological note

---

## 1. Objective

**Electrochemical aptamer-based biosensors** (E-AB, *Electrochemical Aptamer-Based biosensors*) enable real-time detection of target molecules in biological fluids. An aptamer is a synthetic DNA or RNA strand, selected to bind specifically to a given target (protein, small molecule, ion, etc.). When the target binds to the aptamer, it changes shape (*conformation*), which modifies a measurable electrical signal.

Their signal relies on **square wave voltammetry** (SWV, *Square Wave Voltammetry*), a pulsed electrochemical technique which interrogates a redox reporter — methylene blue — attached to the end of an aptamer anchored on a gold electrode.

Signal quality depends on many factors: electrode surface condition (roughness, composition, contamination), instrumental parameters (SWV frequency) and measurement conditions (contact resistance). This application gathers **three parametric studies** simulated numerically to quantify the influence of each factor on voltammogram metrics:

- $I_{peak}$ — peak current (nA)
- $E_{peak}$ — peak potential (V)
- FWHM (*Full Width at Half Maximum*) — peak width at half maximum (mV)
- SNR (*Signal-to-Noise Ratio*) — signal-to-noise ratio
- RF (*Roughness Factor*) — electrode roughness factor

---

## 2. Available studies

### Study 1: electrode parameters

Influence of four surface parameters — roughness factor (RF), exposed nickel, exposed copper and contamination — on the biosensor's SWV response. Main result: exposed nickel is the dominant factor, degrading SNR by a factor of $\sim 10$ between 0 and 10%.

### Study 2: SWV frequency

Influence of frequency (10 to 500 Hz) interacting with roughness and exposed nickel. Main result: the kinetic parameter $K = k^0_{eff}/f$ determines the regime (reversible → irreversible) and the optimal frequency depends on the surface condition.

### Study 3: uncompensated resistance

Influence of uncompensated resistance $R_u$ (0 to 1000 $\Omega$) interacting with roughness and exposed nickel. Main result: at 25 Hz and nA currents, the ohmic drop remains moderate even at $R_u = 1000\;\Omega$; the main effect is FWHM broadening.

---

## 3. Navigation

Navigation in this application is structured around the following tools:

1. **Side menu (left)**: main navigation between project sections.
   - **Introduction**: SWV principle, methylene blue peak, extracted metrics.
   - **Study pages**: each study contains tabs for Physics (physical models and equations), Code (commented source code), Results (cascade filters and side-by-side comparison of 2 simulations) and Analysis (overview plots and statistical report).
   - **Appendices**: synthesis and conclusion, glossary, key equations, a bit of history, bibliographical references.

2. **Floating navigation buttons (right)**: quick scroll up/down the page.

---

## 4. Methodological note

The results presented come from numerical simulations based on a **surface ODE model** (adsorbed species, no spatial mesh). The solver resolves Butler-Volmer kinetics for the adsorbed redox species coverage fractions ($\Gamma_{ox}$, $\Gamma_{red}$), coupled to the SWV protocol (staircase + pulses). Time integration uses an **implicit Euler** scheme (Python/NumPy). Metric extraction ($I_{peak}$, $E_{peak}$, FWHM, SNR) is performed by Gaussian fitting of the SWV peak. This work is part of a broader project using **Firedrake** and **EchemFEM** for finite element electrochemical modelling.

This application is a **results viewer**, not a real-time simulator. The source code is available in the "Code" tabs of each study to allow reproduction.
