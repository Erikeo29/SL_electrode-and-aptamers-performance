"""Application Streamlit -- SWV aptameres sur electrodes Au/Ni/Cu."""
import os

import pandas as pd
import streamlit as st

# --- Configuration de la page (DOIT etre en premier) ---
st.set_page_config(
    page_title="Electrode & Aptamer Performance -- SWV Analysis",
    page_icon="\U0001f9ec",
    layout="wide",
)

# --- Imports locaux ---
from config import ASSETS_PATH, CSS_PATH, DATA_PATH
from utils.translations import TRANSLATIONS, get_language, t
from utils.data_loaders import (
    load_study_csv,
    get_study_dir,
    get_analysis_dir,
    load_file_content,
)
from utils.media import display_analysis_images, display_analysis_report, display_smart_markdown
from components.filters import (
    render_study1_filters,
    render_study2_filters,
    render_study3_filters,
)


# --- Chargement CSS externe ---
def load_custom_css():
    """Charge le CSS et les boutons de navigation."""
    css_content = ""
    if os.path.exists(CSS_PATH):
        with open(CSS_PATH, "r", encoding="utf-8") as f:
            css_content = f.read()

    nav_buttons_html = """
<a href="#top" class="nav-button back-to-top" title="Retour en haut / Back to top">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
        <path d="M12 4l-8 8h5v8h6v-8h5z"/>
    </svg>
</a>
<a href="#bottom" class="nav-button scroll-to-bottom" title="Aller en bas / Go to bottom">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white">
        <path d="M12 20l8-8h-5V4h-6v8H4z"/>
    </svg>
</a>
<div id="top"></div>
"""
    return f"<style>{css_content}</style>{nav_buttons_html}"


st.markdown(load_custom_css(), unsafe_allow_html=True)


# --- Callbacks pour Navigation (INDEX-based) ---
def on_change_gen():
    selected = st.session_state.get("_radio_gen")
    if selected is not None:
        gen_pages = TRANSLATIONS[st.session_state.get("lang", "fr")]["gen_pages"]
        try:
            st.session_state.nav_gen_idx = gen_pages.index(selected)
        except ValueError:
            st.session_state.nav_gen_idx = 0
    st.session_state.nav_study_idx = None
    st.session_state.nav_annex_idx = None


def on_change_study():
    selected = st.session_state.get("_radio_study")
    if selected is not None:
        study_pages = TRANSLATIONS[st.session_state.get("lang", "fr")]["study_pages"]
        try:
            st.session_state.nav_study_idx = study_pages.index(selected)
        except ValueError:
            st.session_state.nav_study_idx = 0
    st.session_state.nav_gen_idx = None
    st.session_state.nav_annex_idx = None


def on_change_annex():
    selected = st.session_state.get("_radio_annex")
    if selected is not None:
        annex_pages = TRANSLATIONS[st.session_state.get("lang", "fr")]["annex_pages"]
        try:
            st.session_state.nav_annex_idx = annex_pages.index(selected)
        except ValueError:
            st.session_state.nav_annex_idx = 0
    st.session_state.nav_gen_idx = None
    st.session_state.nav_study_idx = None


# --- Initialisation Centralisee des Etats ---
DEFAULT_SESSION_STATES = {
    "nav_gen_idx": 0,
    "nav_study_idx": None,
    "nav_annex_idx": None,
    # Study 1
    "run_s1_results": False,
    "files_s1_results": (None, None),
    # Study 2
    "run_s2_results": False,
    "files_s2_results": (None, None),
    # Study 3
    "run_s3_results": False,
    "files_s3_results": (None, None),
}

for key, default in DEFAULT_SESSION_STATES.items():
    if key not in st.session_state:
        st.session_state[key] = default

if (
    st.session_state.nav_gen_idx is None
    and st.session_state.nav_study_idx is None
    and st.session_state.nav_annex_idx is None
):
    st.session_state.nav_gen_idx = 0


# --- Barre Laterale ---

# Selecteur de langue
old_lang = st.session_state.get("lang", "fr")
lang_selection = st.sidebar.radio(
    "Language",
    ["Francais", "English"],
    horizontal=True,
    label_visibility="collapsed",
    index=0 if old_lang == "fr" else 1,
)
new_lang = "fr" if "Francais" in lang_selection else "en"

if new_lang != old_lang:
    st.session_state.lang = new_lang
    st.rerun()

st.session_state.lang = new_lang

st.sidebar.title(t("sidebar_title"))
st.sidebar.markdown("---")

gen_pages = t("gen_pages")
study_pages = t("study_pages")
annex_pages = t("annex_pages")

st.sidebar.subheader(t("gen_header"))
st.sidebar.radio(
    "Nav Gen",
    gen_pages,
    key="_radio_gen",
    index=st.session_state.nav_gen_idx,
    on_change=on_change_gen,
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("studies_header"))
st.sidebar.radio(
    "Nav Studies",
    study_pages,
    key="_radio_study",
    index=st.session_state.nav_study_idx,
    on_change=on_change_study,
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.subheader(t("annex_header"))
st.sidebar.radio(
    "Nav Annex",
    annex_pages,
    key="_radio_annex",
    index=st.session_state.nav_annex_idx,
    on_change=on_change_annex,
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown(t("version_info"))
st.sidebar.markdown("")
st.sidebar.markdown("© 2025 Eric QUEAU — [MIT License](https://opensource.org/licenses/MIT)")

# --- Determiner la page active ---
selected_page = None
if st.session_state.nav_study_idx is not None:
    selected_page = study_pages[st.session_state.nav_study_idx]
elif st.session_state.nav_annex_idx is not None:
    selected_page = annex_pages[st.session_state.nav_annex_idx]
elif st.session_state.nav_gen_idx is not None:
    selected_page = gen_pages[st.session_state.nav_gen_idx]
else:
    selected_page = gen_pages[0]


# ===========================================================================
# HELPER: Affichage des resultats side-by-side
# ===========================================================================
def display_results_side_by_side(f1: dict | None, f2: dict | None, extra_metric_key: str | None = None):
    """Affiche metriques + images pour 2 simulations cote a cote."""
    # --- Metriques ---
    st.markdown("### Metriques")
    for f, sim_label in [(f1, t("sim_1")), (f2, t("sim_2"))]:
        if f and f.get("metrics"):
            m = f["metrics"]
            st.markdown(f"**{sim_label}** -- Run {f['run_id']}")
            cols = st.columns(5 if not extra_metric_key else 6)
            cols[0].metric(t("lbl_ipeak"), f"{m['I_peak_nA']:.1f} nA")
            cols[1].metric(t("lbl_epeak"), f"{m['E_peak_V']:.3f} V")
            cols[2].metric(t("lbl_fwhm"), f"{m['FWHM_mV']:.0f} mV")
            cols[3].metric(t("lbl_snr"), f"{m['SNR']:.0f}")
            cols[4].metric(t("lbl_baseline"), f"{m['I_baseline_uA']:.2f} uA")
            if extra_metric_key == "IR_drop_mV" and "IR_drop_mV" in m:
                cols[5].metric(t("lbl_ir_drop"), f"{m['IR_drop_mV']:.2f} mV")
            elif extra_metric_key == "K_dimensionless" and "K_dimensionless" in m:
                cols[5].metric(t("lbl_k_dim"), f"{m['K_dimensionless']:.2f}")

    st.markdown("---")

    # --- Images: 3 lignes, chacune 2 colonnes ---
    image_keys = [
        ("swv_png", "Voltammogramme SWV"),
        ("components_png", "Decomposition des courants"),
        ("baseline_png", "Zoom baseline"),
    ]
    for img_key, caption in image_keys:
        st.markdown(f"### {caption}")
        c1, c2 = st.columns(2)
        for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
            with col:
                if f and os.path.exists(f[img_key]):
                    st.markdown(f"**{sim_label}** -- Run {f['run_id']}")
                    st.image(f[img_key], use_container_width=True)
                else:
                    st.warning(t("image_unavailable"))
        st.markdown("---")

    # --- Donnees brutes (expander) ---
    with st.expander(t("raw_data_header")):
        c1, c2 = st.columns(2)
        for col, f, sim_label in [(c1, f1, t("sim_1")), (c2, f2, t("sim_2"))]:
            with col:
                if f and os.path.exists(f.get("data_csv", "")):
                    st.markdown(f"**{sim_label}** -- Run {f['run_id']}")
                    try:
                        df_raw = pd.read_csv(f["data_csv"], sep=";")
                        st.dataframe(df_raw, use_container_width=True, hide_index=True)
                    except Exception:
                        st.warning("CSV not readable")


def render_study_page(
    study_key: str,
    title_key: str,
    filter_func,
    filter_prefix: str,
    session_run_key: str,
    session_files_key: str,
    extra_metric_key: str | None = None,
    filter_cols_for_popover: list[str] | None = None,
):
    """Rendu generique d'une page d'etude avec 4 tabs."""
    st.title(t(title_key))

    tabs = st.tabs(t("tabs_study"))

    # Tab Physique
    with tabs[0]:
        st.markdown(load_file_content(f"physics/{study_key}.md"))

    # Tab Code
    with tabs[1]:
        st.markdown(load_file_content(f"code/{study_key}.md"))

    # Tab Resultats
    with tabs[2]:
        df = load_study_csv(study_key)

        if not df.empty:
            with st.container(border=True):
                # Popover simulations disponibles
                c_pop, _ = st.columns([0.3, 0.7])
                with c_pop:
                    with st.popover(t("lbl_avail_sims"), use_container_width=True):
                        if filter_cols_for_popover:
                            st.dataframe(
                                df[["run_id"] + filter_cols_for_popover],
                                use_container_width=True,
                                hide_index=True,
                            )
                        else:
                            st.dataframe(df, use_container_width=True, hide_index=True)

                # Filtres sim 1 et sim 2
                files1 = filter_func(df, filter_prefix, 1)
                st.divider()
                files2 = filter_func(df, filter_prefix, 2)

                # Boutons
                _, btn1, btn2, _ = st.columns([1, 1, 1, 1])
                with btn1:
                    if st.button(
                        t("btn_launch"),
                        type="primary",
                        key=f"btn_{session_run_key}",
                    ):
                        st.session_state[session_run_key] = True
                        st.session_state[session_files_key] = (files1, files2)
                with btn2:
                    if st.button(
                        t("btn_reset"),
                        type="secondary",
                        key=f"rst_{session_run_key}",
                    ):
                        st.session_state[session_run_key] = False
                        st.rerun()

            # Affichage des resultats
            if st.session_state.get(session_run_key, False):
                f1, f2 = st.session_state[session_files_key]
                display_results_side_by_side(f1, f2, extra_metric_key)
        else:
            st.info(t("placeholder_coming_soon"))

    # Tab Analyse
    with tabs[3]:
        # Commentaire d'analyse (si fichier existe)
        analysis_md = load_file_content(f"analysis/{study_key}.md")
        if analysis_md and not analysis_md.startswith("Document not found"):
            st.markdown(analysis_md)
            st.markdown("---")
        analysis_dir = get_analysis_dir(study_key)
        display_analysis_images(analysis_dir)
        st.markdown("---")
        display_analysis_report(analysis_dir)


# ===========================================================================
# PAGES
# ===========================================================================

# ===== PAGE ACCUEIL =====
if selected_page == gen_pages[0]:
    st.title(t("title"))
    st.markdown(load_file_content("accueil/accueil.md"))

# ===== PAGE INTRODUCTION =====
elif selected_page == gen_pages[1]:
    st.title(t("title_intro"))
    display_smart_markdown(load_file_content("physics/introduction.md"), "physics/introduction.md")

# ===== ETUDE 1 =====
elif selected_page == study_pages[0]:
    render_study_page(
        study_key="study1",
        title_key="title_study_1",
        filter_func=render_study1_filters,
        filter_prefix="s1",
        session_run_key="run_s1_results",
        session_files_key="files_s1_results",
        filter_cols_for_popover=["RF", "Ni_pct", "Cu_pct", "contamination"],
    )

# ===== ETUDE 2 =====
elif selected_page == study_pages[1]:
    render_study_page(
        study_key="study2",
        title_key="title_study_2",
        filter_func=render_study2_filters,
        filter_prefix="s2",
        session_run_key="run_s2_results",
        session_files_key="files_s2_results",
        extra_metric_key="K_dimensionless",
        filter_cols_for_popover=["RF", "Ni_pct", "frequency"],
    )

# ===== ETUDE 3 =====
elif selected_page == study_pages[2]:
    render_study_page(
        study_key="study3",
        title_key="title_study_3",
        filter_func=render_study3_filters,
        filter_prefix="s3",
        session_run_key="run_s3_results",
        session_files_key="files_s3_results",
        extra_metric_key="IR_drop_mV",
        filter_cols_for_popover=["RF", "Ni_pct", "R_u"],
    )

# ===== SYNTHESE COMPARATIVE =====
elif selected_page == annex_pages[0]:
    st.title(t("synthesis_title"))
    st.markdown(load_file_content("annexes/synthese.md"))

# ===== LEXIQUE =====
elif selected_page == annex_pages[1]:
    st.title(t("lexique_title"))
    st.markdown(load_file_content("annexes/lexique.md"))

# ===== EQUATIONS CLES =====
elif selected_page == annex_pages[2]:
    st.title(t("title_equations"))
    st.markdown(load_file_content("annexes/equations.md"))

# ===== UN PEU D'HISTOIRE =====
elif selected_page == annex_pages[3]:
    st.title(t("title_histoire"))
    st.markdown(load_file_content("annexes/histoire.md"))

# ===== REFERENCES BIBLIOGRAPHIQUES =====
elif selected_page == annex_pages[4]:
    st.title(t("title_biblio"))
    st.markdown(load_file_content("annexes/biblio.md"))

# --- Ancre de fin de page ---
st.markdown('<div id="bottom"></div>', unsafe_allow_html=True)
