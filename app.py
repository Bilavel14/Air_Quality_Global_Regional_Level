# app.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Global & Regional Air Quality Levels", layout="wide")

st.markdown(
    """
    <style>
      .block-container {padding-top: 1rem; padding-bottom: 0rem;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Global & Regional Air Quality Levels")

# Detect available HTML dashboards in the repo
CANDIDATES = [
    "Air_Quality_Dashboard_MERGED.html",
    "index.html",
    "NDMA_Pakistan_AOD_Dashboard.html",
    "PM25_UN_Dashboard.html",
]
choices = [c for c in CANDIDATES if Path(c).is_file()]

if not choices:
    st.error("No dashboard HTML found in the repository.")
    st.stop()

selected = st.sidebar.selectbox("Choose dashboard", choices, index=0)
height = st.sidebar.slider("Viewport height (px)", 700, 2000, 900, 50)

# Render selected HTML inline
html = Path(selected).read_text(encoding="utf-8", errors="ignore")
st.components.v1.html(html, height=height, scrolling=True)
