import plotly.express as px
import streamlit as st

def line_transactions(df):
    fig = px.line(df, x='mois', y='total_montant', color='annees')
    st.plotly_chart(fig, use_container_width=True)

def bar_ca_agence(df):
    fig = px.bar(df, x='nom_agence', y='total_ca')
    st.plotly_chart(fig, use_container_width=True)

def pie_segment(df):
    fig = px.pie(df, names='nom_segment')
    st.plotly_chart(fig, use_container_width=True)