"""Traductions et gestion de la langue -- SWV aptamères."""
import streamlit as st

TRANSLATIONS = {
    "fr": {
        "title": "Performance des électrodes et aptamères — Analyse par SWV",
        "sidebar_title": "SWV Aptamères",
        "gen_header": "Général",
        "studies_header": "Études paramétriques",
        "annex_header": "Annexes",
        "gen_pages": ["Accueil", "Introduction"],
        "study_pages": [
            "1 : Paramètres d'électrode",
            "2 : Fréquence SWV",
            "3 : Résistance R_u",
        ],
        "annex_pages": [
            "Synthèse et conclusion",
            "Lexique",
            "Équations clés",
            "Un peu d'histoire",
            "Références bibliographiques",
        ],
        "tabs_study": ["Physique", "Code", "Résultats", "Analyse"],
        "version_info": """**Version 1.2.0** — Nov 2025

**Nouveautés :**
- Annexes (histoire, équations, biblio)
- Bibliographie 100 % open-access
- Analyse partielle des résultats""",
        # Titres des pages
        "title_intro": "Introduction à la voltammétrie à onde carrée",
        "title_study_1": "Étude 1 : paramètres d'électrode (RF, Ni, Cu, contamination)",
        "title_study_2": "Étude 2 : fréquence SWV",
        "title_study_3": "Étude 3 : résistance non compensée R_u",
        "synthesis_title": "Synthèse et conclusion",
        "lexique_title": "Lexique",
        "title_equations": "Équations clés",
        "title_histoire": "Un peu d'histoire",
        "title_biblio": "Références bibliographiques",
        # Labels filtres
        "lbl_rf": "RF (rugosité)",
        "lbl_ni": "% Ni",
        "lbl_cu": "% Cu",
        "lbl_contam": "Contamination",
        "lbl_freq": "Fréquence (Hz)",
        "lbl_ru": "R_u (Ω)",
        # Métriques
        "lbl_ipeak": "I_peak (nA)",
        "lbl_epeak": "E_peak (V)",
        "lbl_fwhm": "FWHM (mV)",
        "lbl_snr": "SNR",
        "lbl_baseline": "Baseline (µA)",
        "lbl_ir_drop": "IR drop (mV)",
        "lbl_k_dim": "K (adim.)",
        # Common
        "sim_1": "Simulation 1",
        "sim_2": "Simulation 2",
        "btn_launch": "LANCER LA VISUALISATION",
        "btn_reset": "RÉINITIALISER",
        "lbl_avail_sims": "Simulations disponibles",
        "image_unavailable": "Image non disponible",
        "placeholder_coming_soon": "Contenu en cours de préparation",
        "raw_data_header": "Données brutes du voltammogramme",
    },
    "en": {
        "title": "Electrode and Aptamer Performance — SWV Analysis",
        "sidebar_title": "SWV Aptamers",
        "gen_header": "General",
        "studies_header": "Parametric Studies",
        "annex_header": "Appendices",
        "gen_pages": ["Home", "Introduction"],
        "study_pages": [
            "1: Electrode Parameters",
            "2: SWV Frequency",
            "3: Uncompensated Resistance R_u",
        ],
        "annex_pages": [
            "Synthesis and Conclusion",
            "Glossary",
            "Key Equations",
            "A Bit of History",
            "Bibliographical References",
        ],
        "tabs_study": ["Physics", "Code", "Results", "Analysis"],
        "version_info": """**Version 1.2.0** — Nov 2025

**New features:**
- Appendices (history, equations, bibliography)
- 100% open-access bibliography
- Partial results analysis""",
        # Page titles
        "title_intro": "Introduction to Square Wave Voltammetry",
        "title_study_1": "Study 1: electrode parameters (RF, Ni, Cu, contamination)",
        "title_study_2": "Study 2: SWV frequency",
        "title_study_3": "Study 3: uncompensated resistance R_u",
        "synthesis_title": "Synthesis and Conclusion",
        "lexique_title": "Glossary",
        "title_equations": "Key Equations",
        "title_histoire": "A Bit of History",
        "title_biblio": "Bibliographical References",
        # Filter labels
        "lbl_rf": "RF (roughness)",
        "lbl_ni": "% Ni",
        "lbl_cu": "% Cu",
        "lbl_contam": "Contamination",
        "lbl_freq": "Frequency (Hz)",
        "lbl_ru": "R_u (Ohm)",
        # Metrics
        "lbl_ipeak": "I_peak (nA)",
        "lbl_epeak": "E_peak (V)",
        "lbl_fwhm": "FWHM (mV)",
        "lbl_snr": "SNR",
        "lbl_baseline": "Baseline (uA)",
        "lbl_ir_drop": "IR drop (mV)",
        "lbl_k_dim": "K (dimless.)",
        # Common
        "sim_1": "Simulation 1",
        "sim_2": "Simulation 2",
        "btn_launch": "LAUNCH VISUALIZATION",
        "btn_reset": "RESET",
        "lbl_avail_sims": "Available Simulations",
        "image_unavailable": "Image not available",
        "placeholder_coming_soon": "Content under preparation",
        "raw_data_header": "Raw voltammogram data",
    },
}


def get_language() -> str:
    """Retourne la langue actuelle."""
    if "lang" not in st.session_state:
        st.session_state.lang = "fr"
    return st.session_state.lang


def t(key: str):
    """Retourne la traduction pour la clé donnée."""
    lang = get_language()
    return TRANSLATIONS[lang].get(key, key)
