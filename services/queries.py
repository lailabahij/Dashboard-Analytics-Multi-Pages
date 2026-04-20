import pandas as pd
from config.db import get_engine

engine = get_engine()

def get_global_data():
    
    return pd.read_sql("SELECT * FROM vw_transactions_global", engine)

def get_ca_agence():
    return pd.read_sql("SELECT * FROM vw_ca_agence", engine)

def get_risk_data():
    return pd.read_sql("SELECT * FROM vw_anomalies", engine)

def get_time_data():
    return pd.read_sql("SELECT * FROM vw_transactions_temps", engine)