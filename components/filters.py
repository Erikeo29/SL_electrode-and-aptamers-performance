"""Composants de filtres en cascade -- SWV aptameres.

Chaque etude a ses propres variables de filtre :
  - Etude 1 : RF -> Ni_pct -> Cu_pct -> contamination
  - Etude 2 : RF -> Ni_pct -> frequency
  - Etude 3 : RF -> Ni_pct -> R_u
"""
import os

import pandas as pd
import streamlit as st

from utils.data_loaders import get_study_dir
from utils.translations import t


def render_study1_filters(
    df_origin: pd.DataFrame, key_prefix: str, sim_num: int
) -> dict | None:
    """Filtres en cascade pour l'etude 1 (4 parametres).

    RF -> Ni_pct -> Cu_pct -> contamination
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else min(1, len(df) - 1)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    _, c1, c2, c3, c4, _ = st.columns([0.3, 1, 1, 1, 1, 0.3])

    with c1:
        rf_opts = sorted(df["RF"].unique())
        idx = min(default_idx, len(rf_opts) - 1)
        val_rf = st.selectbox(
            t("lbl_rf"), rf_opts, key=f"{key_prefix}_rf{sim_num}", index=idx
        )
        df = df[df["RF"] == val_rf]

    with c2:
        ni_opts = sorted(df["Ni_pct"].unique())
        val_ni = st.selectbox(
            t("lbl_ni"), ni_opts, key=f"{key_prefix}_ni{sim_num}"
        )
        df = df[df["Ni_pct"] == val_ni]

    with c3:
        cu_opts = sorted(df["Cu_pct"].unique())
        val_cu = st.selectbox(
            t("lbl_cu"), cu_opts, key=f"{key_prefix}_cu{sim_num}"
        )
        df = df[df["Cu_pct"] == val_cu]

    with c4:
        contam_opts = sorted(df["contamination"].unique())
        val_contam = st.selectbox(
            t("lbl_contam"), contam_opts, key=f"{key_prefix}_c{sim_num}"
        )
        df = df[df["contamination"] == val_contam]

    if not df.empty:
        row = df.iloc[0]
        study_dir = get_study_dir("study1")
        return _build_result(row, study_dir)
    return None


def render_study2_filters(
    df_origin: pd.DataFrame, key_prefix: str, sim_num: int
) -> dict | None:
    """Filtres en cascade pour l'etude 2 (3 parametres).

    RF -> Ni_pct -> frequency
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else min(1, len(df) - 1)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    _, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5])

    with c1:
        rf_opts = sorted(df["RF"].unique())
        idx = min(default_idx, len(rf_opts) - 1)
        val_rf = st.selectbox(
            t("lbl_rf"), rf_opts, key=f"{key_prefix}_rf{sim_num}", index=idx
        )
        df = df[df["RF"] == val_rf]

    with c2:
        ni_opts = sorted(df["Ni_pct"].unique())
        val_ni = st.selectbox(
            t("lbl_ni"), ni_opts, key=f"{key_prefix}_ni{sim_num}"
        )
        df = df[df["Ni_pct"] == val_ni]

    with c3:
        freq_opts = sorted(df["frequency"].unique())
        val_freq = st.selectbox(
            t("lbl_freq"), freq_opts, key=f"{key_prefix}_f{sim_num}"
        )
        df = df[df["frequency"] == val_freq]

    if not df.empty:
        row = df.iloc[0]
        study_dir = get_study_dir("study2")
        return _build_result(row, study_dir, extra_metrics=["K_dimensionless"])
    return None


def render_study3_filters(
    df_origin: pd.DataFrame, key_prefix: str, sim_num: int
) -> dict | None:
    """Filtres en cascade pour l'etude 3 (3 parametres).

    RF -> Ni_pct -> R_u
    """
    df = df_origin.copy()
    default_idx = 0 if sim_num == 1 else min(1, len(df) - 1)

    st.markdown(f"**{t('sim_1') if sim_num == 1 else t('sim_2')}**")

    _, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5])

    with c1:
        rf_opts = sorted(df["RF"].unique())
        idx = min(default_idx, len(rf_opts) - 1)
        val_rf = st.selectbox(
            t("lbl_rf"), rf_opts, key=f"{key_prefix}_rf{sim_num}", index=idx
        )
        df = df[df["RF"] == val_rf]

    with c2:
        ni_opts = sorted(df["Ni_pct"].unique())
        val_ni = st.selectbox(
            t("lbl_ni"), ni_opts, key=f"{key_prefix}_ni{sim_num}"
        )
        df = df[df["Ni_pct"] == val_ni]

    with c3:
        ru_opts = sorted(df["R_u"].unique())
        val_ru = st.selectbox(
            t("lbl_ru"), ru_opts, key=f"{key_prefix}_ru{sim_num}"
        )
        df = df[df["R_u"] == val_ru]

    if not df.empty:
        row = df.iloc[0]
        study_dir = get_study_dir("study3")
        return _build_result(row, study_dir, extra_metrics=["IR_drop_mV"])
    return None


def _build_result(
    row: pd.Series, study_dir: str, extra_metrics: list[str] | None = None
) -> dict:
    """Construit le dictionnaire de resultats a partir d'une ligne du CSV."""
    result = {
        "run_id": int(row["run_id"]),
        "swv_png": os.path.join(study_dir, str(row["swv_png"])),
        "components_png": os.path.join(study_dir, str(row["components_png"])),
        "baseline_png": os.path.join(study_dir, str(row["baseline_png"])),
        "data_csv": os.path.join(study_dir, str(row["data_csv"])),
        "metrics": {
            "I_peak_nA": row.get("I_peak_nA", 0),
            "E_peak_V": row.get("E_peak_V", 0),
            "FWHM_mV": row.get("FWHM_mV", 0),
            "SNR": row.get("SNR", 0),
            "I_baseline_uA": row.get("I_baseline_uA", 0),
        },
    }
    if extra_metrics:
        for col in extra_metrics:
            result["metrics"][col] = row.get(col, 0)
    return result
