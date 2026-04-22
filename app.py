import streamlit as st
import pandas as pd
from services.queries import get_global_data
from services.metrics import compute_kpis
import logging

# ======================
# CONFIG
# ======================
logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="FinanceCore Dashboard",
    layout="wide"
)

# ======================
# HEADER
# ======================
st.title("🏦 FinanceCore Dashboard")
st.markdown("Bienvenue dans le système d'analyse financière de **FinanceCore SA**.")

st.divider()

# ======================
# LOAD DATA
# ======================
@st.cache_data
def load_data():
    return get_global_data()

df = load_data()

# ======================
# KPIs GLOBAL
# ======================
st.subheader("📊 Vue Rapide")

kpis = compute_kpis(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 CA Total", f"{kpis['ca']:,.0f} €")
col2.metric("📦 Transactions", kpis['tx'])
col3.metric("👥 Clients", kpis['clients'])
col4.metric("📊 Panier Moyen", f"{kpis['avg']:.2f} €")

st.divider()

# ======================
# DESCRIPTION PAGES
# ======================
st.subheader("🧭 Navigation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📊 Vue Exécutive
    - KPIs détaillés
    - Evolution temporelle
    - CA par agence
    - Répartition des segments
    """)

with col2:
    st.markdown("""
    ### ⚠️ Analyse des Risques
    - Corrélations (Heatmap)
    - Analyse score vs montant
    - Clients à risque
    """)

st.divider()

# ======================
# PREVIEW DATA
# ======================
st.subheader("🔍 Aperçu des Données")

st.dataframe(df.head(10), use_container_width=True)

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("📌 Projet Data Analytics - FinanceCore | Streamlit Dashboard")