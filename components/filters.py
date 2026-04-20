import streamlit as st

def apply_filters(df):
    st.sidebar.title("Filtres")

    agence = st.sidebar.multiselect("Agence", df['nom_agence'].unique())
    segment = st.sidebar.multiselect("Segment", df['nom_segment'].dropna().unique())
    produit = st.sidebar.multiselect("Produit", df['nom_produit'].unique())

    if agence:
        df = df[df['nom_agence'].isin(agence)]

    if segment:
        df = df[df['nom_segment'].isin(segment)]

    if produit:
        df = df[df['nom_produit'].isin(produit)]

    return df