def compute_kpis(df):
    total_ca = df['montant_eur'].sum()
    total_tx = len(df)
    clients = df['id_client'].nunique()
    avg_ticket = df['montant_eur'].mean()

    return {
        "ca": total_ca,
        "tx": total_tx,
        "clients": clients,
        "avg": avg_ticket
    }