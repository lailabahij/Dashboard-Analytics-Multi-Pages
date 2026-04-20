import streamlit as st
import plotly.express as px
from services.queries import get_global_data, get_risk_data
from components.filters import apply_filters
import logging
logging.warning("⚠️ Risk page loaded")
st.title("⚠️ Analyse des Risques")

df = get_global_data()
df = apply_filters(df)

st.subheader("🔥 Scatter Risk")
fig = px.scatter(
    df,
    x='score_credit',
    y='montant_eur',
    color='categorie_risque'
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("🚨 Top clients à risque")

risk_df = get_risk_data()
st.dataframe(risk_df.head(10))