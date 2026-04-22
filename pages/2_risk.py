import streamlit as st
import plotly.express as px
from services.queries import get_global_data, get_risk_data
from components.filters import apply_filters
import logging

logging.warning("⚠️ Risk page loaded")

# ======================
# 🧭 HEADER
# ======================
st.title("⚠️ Analyse des Risques")
st.markdown("Analyse approfondie des facteurs de risque liés aux clients et aux transactions.")

# ======================
# 📊 DATA
# ======================
df = get_global_data()
df = apply_filters(df)

# ======================
# 🧠 HEATMAP
# ======================
st.subheader("🧠 Analyse de Corrélation")
st.caption("Relation entre le score crédit, le montant des transactions et le taux de rejet.")

corr_df = df[['score_credit', 'montant_eur', 'taux_rejet']].copy()
corr_df = corr_df.dropna()
corr_matrix = corr_df.corr()

fig2 = px.imshow(
    corr_matrix,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Blues"
)

fig2.update_layout(
    title="📊 Matrice de Corrélation",
)

st.plotly_chart(fig2, use_container_width=True)

# ======================
# 🔥 SCATTER
# ======================
st.subheader("🔥 Analyse du Risque par Client")
st.caption("Visualisation des relations entre score crédit et montant, segmentées par catégorie de risque.")

fig = px.scatter(
    df,
    x='score_credit',
    y='montant_eur',
    color='categorie_risque',
    title="📈 Score Crédit vs Montant des Transactions"
)

st.plotly_chart(fig, use_container_width=True)

# ======================
# 🚨 TABLE
# ======================
st.subheader("🚨 Top Clients à Risque")
st.caption("Liste des clients présentant le plus haut niveau de risque.")

risk_df = get_risk_data()

st.dataframe(
    risk_df.head(10),
    use_container_width=True
)