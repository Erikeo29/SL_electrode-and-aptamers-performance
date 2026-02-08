"""Fonctions de gestion des medias (images, markdown smart)."""
import os
import re

import streamlit as st

from config import DOC_PATH, ROOT_DIR
from utils.translations import get_language


def display_smart_markdown(content: str, doc_relative_path: str | None = None):
    """Affiche du markdown avec support des images locales.

    Detecte les balises ![alt](path) et les remplace par st.image().
    Les chemins relatifs sont resolus par rapport au fichier .md source.
    """
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    if doc_relative_path:
        lang = get_language()
        doc_dir = os.path.dirname(os.path.join(DOC_PATH, lang, doc_relative_path))
    else:
        doc_dir = ROOT_DIR

    parts = img_pattern.split(content)
    i = 0
    while i < len(parts):
        if i % 3 == 0:
            text = parts[i].strip()
            if text:
                st.markdown(text)
        elif i % 3 == 2:
            img_path = parts[i]
            raw_alt = parts[i - 1]
            # Support width hint: ![alt|400](path) → width=400px
            if "|" in raw_alt:
                alt_text, width_str = raw_alt.rsplit("|", 1)
                alt_text = alt_text.strip()
                try:
                    width = int(width_str.strip())
                except ValueError:
                    width = None
            else:
                alt_text = raw_alt
                width = None
            abs_path = os.path.normpath(os.path.join(doc_dir, img_path))
            if os.path.exists(abs_path):
                if width:
                    st.image(
                        abs_path,
                        caption=alt_text if alt_text else None,
                        width=width,
                    )
                else:
                    st.image(
                        abs_path,
                        caption=alt_text if alt_text else None,
                        use_container_width=True,
                    )
            else:
                st.warning(f"Image not found: {img_path}")
        i += 1


def display_analysis_images(analysis_dir: str):
    """Affiche les images PNG d'un dossier analysis/, 2 par ligne."""
    if not os.path.isdir(analysis_dir):
        st.info("Analysis directory not found.")
        return

    png_files = sorted(
        f for f in os.listdir(analysis_dir) if f.lower().endswith(".png")
    )
    for i in range(0, len(png_files), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(png_files):
                img_path = os.path.join(analysis_dir, png_files[idx])
                with col:
                    st.image(
                        img_path,
                        caption=png_files[idx],
                        use_container_width=True,
                    )


def display_analysis_report(analysis_dir: str):
    """Affiche le RAPPORT_ANALYSE.md avec resolution des images."""
    report_path = os.path.join(analysis_dir, "RAPPORT_ANALYSE.md")
    if not os.path.exists(report_path):
        st.info("Report not found.")
        return

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip metadata lines (date, run count) from display
    content = "\n".join(
        line
        for line in content.splitlines()
        if not line.startswith("Date:") and not line.startswith("Nombre de runs:")
    )

    # Resolve image paths relative to analysis_dir
    img_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    parts = img_pattern.split(content)
    i = 0
    while i < len(parts):
        if i % 3 == 0:
            text = parts[i].strip()
            if text:
                st.markdown(text)
        elif i % 3 == 2:
            img_path = parts[i]
            alt_text = parts[i - 1]
            abs_path = os.path.normpath(os.path.join(analysis_dir, img_path))
            if os.path.exists(abs_path):
                st.image(
                    abs_path,
                    caption=alt_text if alt_text else None,
                    use_container_width=True,
                )
            else:
                st.warning(f"Image not found: {img_path}")
        i += 1
