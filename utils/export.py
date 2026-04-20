import streamlit as st

def export_csv(df):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Télécharger CSV",
        csv,
        "data.csv",
        "text/csv"
    )