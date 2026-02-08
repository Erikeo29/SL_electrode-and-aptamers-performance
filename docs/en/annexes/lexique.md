**Contents:**
1. Acronyms and techniques
2. Physical symbols
3. SWV metrics
4. Surface parameters
5. Technical terms

---

## 1. Acronyms and techniques

| Acronym | Full name | Description |
|---------|-----------|-------------|
| **SWV** | Square Wave Voltammetry | Pulsed electroanalytical technique; net current $I_{net} = I_{forward} - I_{reverse}$ eliminates the capacitive component |
| **CV** | Cyclic Voltammetry | Linear potential sweep technique; less sensitive than SWV (no capacitive subtraction) |
| **EIS** | Electrochemical Impedance Spectroscopy | Frequency-domain technique to extract equivalent circuit parameters ($R_u$, $C_{dl}$, $R_{ct}$) |
| **MB** | Methylene Blue | Phenothiazine redox reporter; $\text{MB}_{ox} + 2e^- + 2H^+ \rightleftharpoons \text{MB}_{red}$; $E^0 = -0.24$ V vs Ag/AgCl at pH 7.4 |
| **CPE** | Constant Phase Element | Equivalent circuit element for non-ideal capacitance; $Z_{CPE} = 1/[Q_0(j\omega)^{n_{CPE}}]$ |
| **BV** | Butler-Volmer | Electrochemical kinetic model relating faradaic current to overpotential |
| **FEM** | Finite Element Method | Numerical method for solving PDEs; Firedrake solver used in this project |
| **SELEX** | Systematic Evolution of Ligands by Exponential Enrichment | In vitro selection process for aptamers |
| **PBS** | Phosphate-Buffered Saline | Standard buffer for biosensor measurements (pH 7.4) |
| **WE** | Working Electrode | Electrode where the reaction of interest occurs (Au/Ni/Cu in this project) |
| **RE** | Reference Electrode | Electrode providing a stable reference potential (Ag/AgCl) |
| **CE** | Counter Electrode | Auxiliary electrode that closes the electrical circuit |

---

## 2. Physical symbols

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| $E$ | Electrode potential | V | Applied potential at the working electrode |
| $E^0$ | Apparent standard potential | V | Equilibrium potential of the redox couple ($-0.24$ V vs Ag/AgCl for MB) |
| $\eta$ | Overpotential | V | $\eta = E - E^0$; driving force for the redox reaction |
| $\alpha$ | Transfer coefficient | -- | Symmetry parameter for the activation barrier (typically 0.5) |
| $n$ | Electrons transferred | -- | Number of electrons per redox event ($n = 2$ for MB) |
| $F$ | Faraday constant | C/mol | $F = 96\,485$ C/mol |
| $R$ | Gas constant | J/(mol$\cdot$K) | $R = 8.314$ J/(mol$\cdot$K) |
| $T$ | Temperature | K | Absolute temperature ($T = 298.15$ K at 25 $^\circ$C) |
| $D$ | Diffusion coefficient | m$^2$/s | MB diffusivity in the aptamer film ($\sim 10^{-12}$ m$^2$/s) |
| $C$ | Concentration | mol/m$^3$ | MB concentration in the thin film |
| $C_{dl}$ | Double-layer capacitance | F/cm$^2$ | Electrode--solution interface capacitance (10--40 $\mu$F/cm$^2$ for Au in PBS) |

---

## 3. SWV metrics

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| $I_{peak}$ | Peak current | nA | Maximum amplitude of the faradaic peak after baseline subtraction |
| $E_{peak}$ | Peak potential | V | Potential at which the net current reaches its maximum |
| FWHM | Full width at half maximum | mV | Peak width; ideal value $= 90.6/n$ mV ($= 45.3$ mV for MB, $n = 2$) |
| SNR | Signal-to-noise ratio | -- | $\text{SNR} = I_{peak} / \sigma_{residuals}$; $> 10$ required, $> 50$ excellent |
| $I_{baseline}$ | Baseline current | $\mu$A | Background current far from the faradaic peak ($\propto \text{RF} \cdot C_{dl}$) |
| $IR_{drop}$ | Ohmic drop | mV | $IR_{drop} = I_{peak} \times R_u$; shifts peak toward more negative potentials |
| $K$ | Kinetic parameter | -- | $K = k^0_{eff}/f$; determines the kinetic regime (see table below) |
| $I_{net}$ | Net SWV current | nA | $I_{net} = I_{forward} - I_{reverse}$ |

**Kinetic regime classification:**

| Regime | $K$ range | Behavior |
|--------|-----------|----------|
| Reversible | $K > 5$ | Sharp peak, $E_{peak} = E^0$ |
| Quasi-reversible | $0.1 < K < 5$ | Broadened peak, $E_{peak}$ shifts |
| Irreversible | $K < 0.1$ | Very broad peak, reduced current |

---

## 4. Surface parameters

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| RF | Roughness factor | -- | $\text{RF} = A_{real}/A_{geometric}$; RF $= 1$ for a perfectly flat surface; typical range 1.2--3.0 |
| $A_{geometric}$ | Geometric surface area | cm$^2$ | Projected (2D) electrode area |
| $A_{real}$ | Real surface area | cm$^2$ | $A_{real} = A_{geometric} \cdot \text{RF}$ |
| $f_{Au}$ | Free gold fraction | -- | $f_{Au} = 1 - \text{Ni\%}/100 - \text{Cu\%}/100 - \text{contam.\%}/100$ |
| Ni% | Exposed nickel | % | Fraction of surface occupied by exposed Ni (0--10%) |
| Cu% | Exposed copper | % | Fraction of surface occupied by exposed Cu (0--5%) |
| contam.% | Surface contamination | % | Fraction of blocked surface sites (0--30%) |
| $\Gamma_0$ | Intrinsic aptamer density | mol/cm$^2$ | Surface density on clean flat gold ($\sim 10^{-11}$ to $10^{-10}$ mol/cm$^2$) |
| $\Gamma_{eff}$ | Effective aptamer density | mol/cm$^2$ | $\Gamma_{eff} = \Gamma_0 \cdot \text{RF} \cdot (1 - \text{contam.\%}/100)$ |
| $k^0_{eff}$ | Effective rate constant | s$^{-1}$ | $k^0_{eff} = k^0_{Au} \cdot f_{Au} + k^0_{Ni} \cdot (\text{Ni\%}/100) + k^0_{Cu} \cdot (\text{Cu\%}/100)$ |
| $k^0_{Au}$ | Gold rate constant | s$^{-1}$ | Electron transfer rate for MB on Au ($\sim 10$--$100$ s$^{-1}$) |
| $k^0_{Ni}$ | Nickel rate constant | s$^{-1}$ | Electron transfer rate for MB on Ni ($\ll k^0_{Au}$) |
| $k^0_{Cu}$ | Copper rate constant | s$^{-1}$ | Electron transfer rate for MB on Cu ($< k^0_{Au}$) |
| $R_u$ | Uncompensated resistance | $\Omega$ | Total resistance between WE and RE not corrected by the potentiostat |

---

## 5. Technical terms

### Electrochemistry

| Term | Definition |
|------|------------|
| **Aptamer** | Oligonucleotide (ssDNA or RNA) selected by SELEX for specific target binding; anchored to Au via thiol (3' end), carries MB reporter (5' end) |
| **Voltammogram** | Current vs potential curve $I = f(E)$ obtained during an electroanalytical scan |
| **Overpotential** | Deviation $\eta = E - E^0$ of the applied potential from the standard potential |
| **Faradaic current** | Current arising from electron transfer reactions at the electrode surface |
| **Capacitive current** | Non-faradaic current from double-layer charging; eliminated by the $I_{forward} - I_{reverse}$ subtraction in SWV |
| **Double layer** | Charge-separated interface between the metal electrode and the electrolyte solution |
| **Redox couple** | Pair of oxidized and reduced species ($\text{MB}_{ox}$ / $\text{MB}_{red}$) |
| **Nernst-Planck equation** | Transport equation for ionic species under diffusion, migration, and convection; simplified to pure diffusion in the thin aptamer film |
| **Butler-Volmer equation** | Kinetic model: $j = k^0_{eff}[C_{ox}\exp(-\alpha F\eta/RT) - C_{red}\exp((1{-}\alpha)F\eta/RT)]$ |

### SWV waveform

| Term | Definition |
|------|------------|
| **Staircase** | Potential increment $\delta E_s$ (4 mV) applied at each SWV cycle |
| **Pulse amplitude** | Symmetric square wave amplitude $\delta E_p$ (25 mV) superimposed on the staircase |
| **Forward pulse** | Positive-going pulse; current sampled at end of pulse |
| **Reverse pulse** | Negative-going pulse; current sampled at end of pulse |
| **Net current** | $I_{net} = I_{forward} - I_{reverse}$; eliminates capacitive contribution |

### Numerical methods

| Term | Definition |
|------|------------|
| **Firedrake** | Open-source finite element library (Python) used as the PDE solver in this project |
| **Implicit Euler** | First-order backward time integration scheme; unconditionally stable |
| **Gaussian fit** | Least-squares fit of the SWV peak with $I_{fit}(E) = I_{peak}\exp[-\tfrac{1}{2}((E - E_{peak})/\sigma)^2] + \text{baseline}(E)$ |
| **Baseline** | Degree-2 polynomial fitted on regions far from the faradaic peak ($|E - E_{peak}| > 3\sigma$) |
| **Fixed-point iteration** | Iterative method used to resolve the $I$--$\eta$ coupling in Study 3 (ohmic drop) |
| **P1 elements** | Linear Lagrange finite elements used for the 1D aptamer film mesh |
