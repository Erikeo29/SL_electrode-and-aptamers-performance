"""Fonctions de chargement des donnees -- SWV aptameres."""
import os

import pandas as pd
import streamlit as st

from config import DATA_PATH, DOC_PATH
from utils.translations import get_language


# --- Mapping study_key -> directory name ---
STUDY_DIRS = {
    "study1": "01_parametric_RF_Ni_Cu",
    "study2": "02_frequency_study",
    "study3": "03_Ru_study",
}


@st.cache_data(ttl=600)
def load_study_csv(study_key: str) -> pd.DataFrame:
    """Charge le CSV parametric_study.csv d'une etude (sep=';')."""
    study_dir = STUDY_DIRS.get(study_key, "")
    csv_path = os.path.join(DATA_PATH, study_dir, "parametric_study.csv")
    try:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8")
        return df
    except Exception:
        return pd.DataFrame()


def get_study_dir(study_key: str) -> str:
    """Retourne le chemin absolu du dossier d'une etude."""
    return os.path.join(DATA_PATH, STUDY_DIRS.get(study_key, ""))


def get_analysis_dir(study_key: str) -> str:
    """Retourne le chemin absolu du dossier analysis/ d'une etude."""
    return os.path.join(get_study_dir(study_key), "analysis")


def load_file_content(relative_path: str) -> str:
    """Charge un fichier depuis docs/<lang>/relative_path."""
    lang = get_language()
    full_path = os.path.join(DOC_PATH, lang, relative_path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return f"Document not found: {relative_path}"
