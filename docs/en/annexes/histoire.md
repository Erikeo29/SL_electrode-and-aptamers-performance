**Contents:**
1. The era of polarography and pulsed methods (1922-1969)
2. Birth of modern SWV (1969-1990)
3. The rise of aptamers (1990-2010)
4. Electrochemical aptamer-based biosensors: the current era (2010-)
5. Towards numerical modelling of biosensors
6. Bibliographical references

---

Square wave voltammetry (SWV) is today the technique of choice for interrogating aptamer-based biosensors. Its history intersects those of analytical electrochemistry, combinatorial biology and numerical simulation. Let us trace the major milestones that led to the parametric studies in this project.

## 1. The era of polarography and pulsed methods (1922-1969)

Everything begins, as with cyclic voltammetry, with Heyrovský's mercury drop in Prague. Its constantly renewed surface offered unprecedented reproducibility. But very soon, electrochemists sought to overcome the limitations of classical polarography -- too slow, too sensitive to capacitive current -- by superimposing pulses on the continuous signal.

| Year | Event |
|------|-------|
| 1922 | **Jaroslav Heyrovský** invents polarography using the dropping mercury electrode (DME) in Prague |
| 1942 | **Barker** begins his work on pulsed techniques at the Harwell laboratory (United Kingdom) |
| 1952 | **Barker & Jenkins** develop the first square wave polarography (*The Analyst*, 1952), superimposing a low-amplitude square wave signal on the potential ramp |
| 1959 | Heyrovský receives the **Nobel Prize in Chemistry** for his work on polarography |
| 1969 | **Ramaley & Krause** couple the square wave to a staircase signal, laying the foundations of modern SWV (*Anal. Chem.*, 1969) |

*The key idea*: by applying pulses rather than a continuous ramp, the faradaic current is sampled at the moment when the capacitive current has decayed, considerably improving the signal-to-noise ratio. This trick, simple in appearance, would transform analytical electrochemistry.

## 2. Birth of modern SWV (1969-1990)

SWV gradually distinguishes itself from differential pulse voltammetry (DPV) through its superior speed and sensitivity. Where DPV requires several minutes to sweep a potential window, SWV achieves this in a few seconds.

| Contribution | Impact |
|--------------|--------|
| **Osteryoung & O'Dea** | Refinement of the theory for reversible and quasi-reversible systems; SWV can acquire a complete voltammogram in a few seconds |
| **Lovrić & Komorsky-Lovrić** | Development of the theory for surface-adsorbed species, directly applicable to aptamer-based biosensors |
| **Net current** | The net signal $I_{net} = I_{forward} - I_{reverse}$ eliminates the capacitive component, offering superior sensitivity compared to CV and DPV |
| **Ramaley & Krause** | First theoretical work (1969) relating the SWV peak shape to the kinetic parameters of the system |

The measurement principle relies on three currents measured at each potential step: the forward current, the reverse current and the net current which is their difference. This decomposition not only eliminates capacitive noise but also allows diagnosis of the system's reversibility.

For a surface-adsorbed species (the case of aptamers), the SWV peak current is expressed as:

$$ I_{pic} \propto n \cdot F \cdot A \cdot \Gamma \cdot f $$

where $n$ is the number of electrons, $F$ Faraday's constant, $A$ the electrode area, $\Gamma$ the surface density of the redox species and $f$ the square wave frequency. This linear relationship with frequency is a characteristic signature of the adsorption regime, in contrast to the diffusional regime ($I_{pic} \propto f^{1/2}$).

## 3. The rise of aptamers (1990-2010)

At the turn of the 1990s, a parallel revolution occurred in molecular biology: the in vitro selection of oligonucleotides capable of recognising specific targets with affinity comparable to that of antibodies.

| Year | Event |
|------|-------|
| 1990 | **Ellington & Szostak** (Harvard) coin the term "aptamer" (from the Latin *aptus*, fit) and demonstrate in vitro selection of oligonucleotides (*Nature*, 1990) |
| 1990 | **Tuerk & Gold** (Colorado) independently develop the same in vitro selection method, coining the term SELEX (*Systematic Evolution of Ligands by EXponential enrichment*) (*Science*, 1990) |
| 1996 | First DNA aptamers selected for small-molecule targets (ATP, theophylline) |
| 2005 | **Xiao, Lubin, Heeger & Plaxco** (UCSB) produce the first electrochemical aptamer-based biosensor (E-AB) for thrombin detection (*Angew. Chem. Int. Ed.*, 2005) |
| 2005 | Extension of the E-AB concept to the detection of small molecules (cocaine, ATP) |

*The fundamental principle*: the aptamer, immobilised on the electrode via a thiol-gold bond, carries a redox label (typically methylene blue, MB). Upon target recognition, the conformational change of the aptamer brings the MB closer to or further from the electrode surface, modulating electron transfer and hence the current measured by SWV.

Aptamers present several advantages over traditional antibodies:
- **Thermal stability** superior (resistance to denaturation)
- **Chemical synthesis** reproducible and inexpensive
- **Regeneration** of the sensor surface possible by simple rinsing
- **Direct compatibility** with electrochemical transduction (terminal redox labelling)

## 4. Electrochemical aptamer-based biosensors: the current era (2010-)

Since 2010, E-AB biosensors have experienced considerable growth, driven notably by **Kevin Plaxco**'s group at UCSB.

| Advance | Description |
|---------|-------------|
| **Structure-switching platform** | Plaxco and collaborators generalise the conformational switching concept to numerous targets (small molecules, proteins, antibiotics) |
| **Real-time in vivo measurements** | Demonstration of implantable E-AB sensors continuously measuring drug concentrations in the blood of living animals |
| **SWV as the technique of choice** | SWV prevails over CV and DPV for E-AB sensors owing to its superior signal-to-noise ratio and its ability to discriminate faradaic signal from capacitive noise |
| **Kinetic differential measurement (KDM)** | Development of correction methods based on the frequency dependence of the SWV signal, enabling compensation for sensor drift |

**Current challenges:**
- Electrode surface quality (roughness, Au/Ni/Cu crystallinity)
- Non-specific adsorption of interfering molecules
- Long-term stability of the aptamer monolayer (thiol degradation)
- Optimisation of SWV parameters (frequency, amplitude, potential step) for each electrode-aptamer pair
- Transition from the laboratory to portable point-of-care diagnostic devices

## 5. Towards numerical modelling of biosensors

The experimental approach alone is no longer sufficient to understand and optimise E-AB biosensors. Numerical modelling enables systematic exploration of the parameter space and prediction of sensor behaviour before fabrication.

| Approach | Tools |
|----------|-------|
| **Electrochemical transport** | Firedrake, FEniCSx: finite element solution of the Nernst-Planck equations coupled to Butler-Volmer kinetics |
| **Electron transfer kinetics** | Modelling of the transfer rate constant $k_0$ and its relationship with the optimal SWV frequency |
| **Parametric studies** | This project: simulations sweeping the electrode (Au, Ni, Cu) $\times$ frequency $\times$ resistance space |
| **Performance analysis** | Automated extraction of peak currents, signal-to-noise ratios and figures of merit for each configuration |

The transition from empirical characterisation to numerical simulation makes it possible to identify optimal configurations (electrode material, SWV frequency, solution resistance) without resorting to exhaustive experimental campaigns.

This is precisely the objective of the simulations presented in this application: by systematically exploring the parameter space, one can map the performance of each configuration and guide experimental choice towards the most promising combinations.

---

## 6. Bibliographical references

*For the complete list of references, see the Bibliographical References section in the Appendices menu.*
