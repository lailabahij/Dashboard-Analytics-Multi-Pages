import streamlit as st
from services.queries import get_global_data, get_ca_agence, get_time_data
from services.metrics import compute_kpis
from components.filters import apply_filters
from components.charts import *
import logging

logging.info("📊 Loading executive dashboard")
st.title("📊 Vue Exécutive")

df = get_global_data()
df = apply_filters(df)

kpis = compute_kpis(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("CA Total", f"{kpis['ca']:.2f}")
col2.metric("Transactions", kpis['tx'])
col3.metric("Clients", kpis['clients'])
col4.metric("Panier Moyen", f"{kpis['avg']:.2f}")

#Evolution mensuelle du chiffre d'affaires
time_df = get_time_data()
line_transactions(time_df)

#Chiffre d'affaires par agence
bar_ca_agence(get_ca_agence())

#Segments
pie_segment(df)