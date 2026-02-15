**Table of contents:**
1. Square-wave voltammetry (SWV)
2. Electrochemical aptamer-based biosensors (E-AB)
3. Electron transfer kinetics (Butler-Volmer)
4. Gold electrodes and surface quality
5. Numerical simulation (FEM)
6. Software resources
7. Additional educational resources

> All references below are **free and open-access** (PDF, PMC, arXiv, open-access publishers or manufacturer application notes).

---

## 1. Square-wave voltammetry (SWV)

1. **Gamry Instruments**
   *"Square-wave Voltammetry — Introduction."*
   Application note, rev. 1.0.
   - [Direct PDF (Gamry)](https://www.gamry.com/assets/uploads/Square-wave-Voltammetry.pdf)
   - Practical introduction: waveform, parameters ($\delta E_s$, $\delta E_p$, $f$), voltammogram interpretation.

2. **Pine Research Instrumentation**
   *"Square Wave Voltammetry (SWV)."*
   Online tutorial.
   - [Web page (Pine Research)](https://pineresearch.com/support-article/square-wave-voltammetry/)
   - Pedagogical presentation of SWV with interactive diagrams and AfterMath examples.

3. **Mirčeski, V.; Skrzypek, S.; Stojanov, L.**
   *"Square-wave voltammetry."*
   ChemTexts **2018**, 4, 17.
   - [Full text (ResearchGate)](https://www.researchgate.net/publication/328674174_Square-wave_voltammetry)
   - Comprehensive theoretical introduction: kinetic diagnostics, adsorbed systems, numerical simulations.

4. **Metrohm Autolab**
   *"Quantification of paracetamol with square wave voltammetry."*
   Application note AN-SENS-001.
   - [Direct PDF (Metrohm)](https://www.metrohm.com/content/metrohm/id_id/applications/application-notes/autolab-applikationen-anautolab/an-sens-001.download.pdf)
   - Practical example of SWV for analyte quantification.

---

## 2. Electrochemical aptamer-based biosensors

> **E-AB** = *Electrochemical Aptamer-Based sensors*: biosensors using aptamers (DNA/RNA strands) immobilised on an electrode and bearing a redox reporter (methylene blue). The aptamer's conformational change upon target binding modifies the electrochemical signal.

5. **Radi, A.; Abd-Ellatief, M. R.**
   *"Electrochemical Aptasensors: Current Status and Future Perspectives."*
   Diagnostics **2021**, 11(1), 104.
   - [PMC full text (PMC7828092)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7828092/)
   - Comprehensive review: immobilization strategies, assay platforms, clinical perspectives.

6. **White, R. J.; Plaxco, K. W.**
   *"Exploiting Binding-Induced Changes in Probe Flexibility for the Optimization of Electrochemical Biosensors."*
   Anal. Chem. **2010**, 82, 73-76.
   - [PMC full text (PMC2802819)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2802819/)
   - E-AB signal optimization through SWV frequency selection: conformation–electron transfer relationship.

7. **Arroyo-Currás, N. et al.**
   *"Real-time measurement of small molecules directly in awake, ambulatory animals."*
   PNAS **2017**, 114, 645-650.
   - [PNAS article (open access)](https://www.pnas.org/doi/10.1073/pnas.1613458114)
   - In vivo demonstration of E-AB sensors interrogated by continuous SWV in ambulatory rats.

8. **Dauphin-Ducharme, P. et al.**
   *"Electrochemical Aptamer-Based Sensors for Improved Therapeutic Drug Monitoring and High-Precision, Feedback-Controlled Drug Delivery."*
   ACS Sensors **2019**, 4(10), 2832-2837.
   - [PMC full text (PMC6886665)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886665/)
   - E-AB sensors for real-time pharmacological monitoring; feedback-controlled dosing potential.

---

## 3. Electron transfer kinetics (Butler-Volmer)

9. **Bazant, M. Z.**
    *"Lecture 13: Butler-Volmer equation."*
    MIT OCW — Course 10.626, Electrochemical Energy Systems.
    - [Direct PDF (MIT)](https://ocw.mit.edu/courses/10-626-electrochemical-energy-systems-spring-2014/56cfa6e0f28bc8fc1a647cbe679384d1_MIT10_626S14_S11lec13.pdf)
    - Graduate-level course: rigorous derivation of the Butler-Volmer equation from transition state theory.

10. **Middleman, S.**
    *"Chapter 16: Electrochemical Processes."*
    WashU ChE 503 — Lecture Notes.
    - [Direct PDF (WashU)](https://classes.engineering.wustl.edu/che503/che471-08/Electrochemical_Notes.pdf)
    - Course notes: electrochemical kinetics, overpotential, Tafel law, industrial applications.

---

## 4. Gold electrodes and surface quality

11. **Trasatti, S.; Petrii, O. A.**
    *"Real surface area measurements in electrochemistry."*
    Pure Appl. Chem. (IUPAC) **1991**, 63, 711-734.
    - [PDF (IUPAC)](https://publications.iupac.org/pac/63/5/0711/index.html)
    - IUPAC recommendations for real surface area measurement and roughness factor (RF) definition.

12. **PalmSens**
    *"Cyclic Voltammetry — Investigation of a Gold Surface."*
    Application note PSAPP-006.
    - [Direct PDF (PalmSens)](https://assets.palmsens.com/app/uploads/2021/06/PSAPP-006-Electrochemical-Experiment-Cyclic-Voltammetry-Investigation-of-a-Gold-Surface.pdf)
    - Complete protocol: cleaning, oxidative cycling, roughness factor calculation from gold oxide reduction.

13. **Pettersson, J.**
    *"Evaluation of the Electrochemically Active Surface Area of Electrodes."*
    Master's thesis, KTH Stockholm, **2019**.
    - [Direct PDF (DiVA)](http://www.diva-portal.org/smash/get/diva2:1365724/FULLTEXT01.pdf)
    - Experimental methods for active surface area measurement (Au, Pt, C) with RF and double layer capacitance discussion.

---

## 5. Numerical simulation (FEM)

14. **Roy, T. et al.**
    *"EchemFEM: A Firedrake-based Python package for electrochemical transport."*
    J. Open Source Softw. **2024**, 9(97), 6531.
    - [Direct PDF (JOSS)](https://joss.theoj.org/papers/10.21105/joss.06531.pdf)
    - Python package used for the SWV simulations in this application. Open-source license (MIT).

15. **Rathgeber, F.; Ham, D. A. et al.**
    *"Firedrake: automating the finite element method by composing abstractions."*
    ACM Trans. Math. Softw. **2017**, 43(3), 24. (arXiv 2015, 1501.01809)
    - [Direct PDF (arXiv)](https://arxiv.org/pdf/1501.01809)
    - Founding paper of Firedrake: composing abstractions for PDE solving with finite elements.

16. **Logg, A.; Mardal, K.-A.; Wells, G. N. (eds.)**
    *Automated Solution of Differential Equations by the Finite Element Method — The FEniCS Book.*
    Springer, **2012**.
    - [Direct PDF (FEniCS Project)](https://pub.fenicsproject.org/book/book/fenics-book-2011-04-29.pdf)
    - FEniCS reference book (736 pp.): variational formulation, UFL compilation, multi-physics examples.

---

## 6. Software resources

| Software | Type | Website |
|----------|------|---------|
| **Firedrake** | Open-source FEM | [firedrakeproject.org](https://www.firedrakeproject.org/) |
| **EchemFEM** | Electrochemistry for Firedrake | [GitHub](https://github.com/LLNL/echemfem) |
| **FEniCSx** | Open-source FEM | [fenicsproject.org](https://fenicsproject.org/) |
| **numpy** | Scientific computing | [numpy.org](https://numpy.org/) |
| **scipy** | Scientific algorithms | [scipy.org](https://scipy.org/) |
| **matplotlib** | Visualization | [matplotlib.org](https://matplotlib.org/) |
| **pandas** | Data analysis | [pandas.pydata.org](https://pandas.pydata.org/) |

---

## 7. Additional educational resources

| Resource | Subject | Link |
|----------|---------|------|
| Chemistry LibreTexts | Voltammetric and amperometric methods | [LibreTexts](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Analytical_Chemistry_Volume_II_(Harvey)/02:_Electrochemical_Methods/2.04:_Voltammetric_and_Amperometric_Methods) |
| MIT OCW 10.626 | Full course: electrochemical energy systems | [MIT OCW](https://ocw.mit.edu/courses/10-626-electrochemical-energy-systems-spring-2014/pages/lecture-notes/) |
| Metrohm | Electrochemistry application notes (CV, DPV, EIS) | [Metrohm App Notes](https://www.metrohm.com/en/applications/application-notes/autolab-applikationen-anautolab/) |
| Gamry | Electrochemistry application notes | [Gamry App Notes](https://www.gamry.com/application-notes/physechem/) |
