import plotly.express as px
import streamlit as st

def line_transactions(df):
    import plotly.express as px
    import streamlit as st

    # aggregation
    df_grouped = df.groupby(['annees', 'mois'])['total_montant'].sum().reset_index()
    df_grouped = df_grouped.sort_values(by=['annees', 'mois'])

    # title + description (Streamlit)
    st.subheader("📈 Evolution mensuelle du chiffre d'affaires")
    st.caption("Analyse de l'évolution du volume des transactions au fil du temps (par mois et par année).")

    # plot
    fig = px.line(
        df_grouped,
        x='mois',
        y='total_montant',
        color='annees',
        markers=True
    )

    fig.update_layout(
        xaxis_title="Mois",
        yaxis_title="Total Montant (€)",
        xaxis=dict(tickmode='linear')
    )

    st.plotly_chart(fig, use_container_width=True)

def bar_ca_agence(df):
    import plotly.express as px
    import streamlit as st

    st.subheader("🏦 Chiffre d'affaires par agence")
    st.caption("Comparaison des performances financières entre les différentes agences.")

    fig = px.bar(
        df,
        x='nom_agence',
        y='total_ca',
        color='nom_agence',  
        text_auto=True
    )

    fig.update_layout(
        xaxis_title="Agence",
        yaxis_title="Chiffre d'affaires (€)",
        showlegend=False  # optional
    )

    st.plotly_chart(fig, use_container_width=True)

def pie_segment(df):
    import plotly.express as px
    import streamlit as st

    st.subheader("👥 Répartition des clients par segment")
    st.caption("Distribution des clients selon leur segment (Premium, Standard, Risqué).")

    fig = px.pie(
        df,
        names='nom_segment',
        hole=0.4  # donut style 🔥
    )

    st.plotly_chart(fig, use_container_width=True)