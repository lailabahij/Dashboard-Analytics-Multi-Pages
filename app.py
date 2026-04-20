import streamlit as st
import logging

# CONFIG LOGGING
logging.basicConfig(level=logging.INFO)
st.set_page_config(page_title="FinanceCore Dashboard", layout="wide")

st.title("🏦 FinanceCore Dashboard")

st.write("Utilise le menu à gauche pour naviguer")