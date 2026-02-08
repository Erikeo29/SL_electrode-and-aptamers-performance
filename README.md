# Electrode & Aptamer Performance -- SWV Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aptamer-v1.streamlit.app/)

Bilingual (FR/EN) Streamlit application for visualizing three parametric studies on electrochemical aptamer-based (E-AB) biosensor performance using square wave voltammetry (SWV).

## Studies

| Study | Parameters | Key result |
|-------|-----------|------------|
| **1. Electrode parameters** | RF, exposed Ni, exposed Cu, contamination | Exposed Ni is the dominant factor (SNR drops ~10x at 10%) |
| **2. SWV frequency** | Frequency (10--500 Hz) x RF x Ni | Kinetic parameter K = k0_eff/f determines the reversibility regime |
| **3. Uncompensated resistance** | Ru (0--1000 Ohm) x RF x Ni | Ohmic drop stays moderate at nA currents; main effect is FWHM broadening |

## Features

- **Bilingual FR/EN** interface with full translation
- **Cascade filters** for navigating 306 simulation runs
- **Side-by-side comparison** of any two simulations
- **Four tabs per study**: Physics, Code, Results, Analysis
- **Appendices**: glossary, key equations, history, bibliography

## Project structure

```
app.py              # Streamlit application
config.py           # Global configuration
utils/              # Translations, media, navigation helpers
views/              # Page renderers (home, intro, studies, appendices)
docs/               # Bilingual markdown content
  fr/, en/          #   Physics, analysis, appendices
data/               # CSV parameter mappings
assets/             # Illustrations, CSS
```

## Installation

```bash
git clone https://github.com/Erikeo29/SL_electrode-and-aptamers-performance.git
cd SL_electrode-and-aptamers-performance
pip install -r requirements.txt
streamlit run app.py
```

## Model

All results come from deterministic numerical simulations based on a surface ODE model (Butler-Volmer kinetics for adsorbed species, implicit Euler integration). This is a results viewer, not a real-time simulator.

## Version

**v1.2.0 (November 2025)** -- Initial public release with 3 parametric studies, bilingual support, and full documentation.

## License

Research project -- open-source for learning purposes.
