import streamlit as st
from api.client import fetch_data
from utils.formatters import format_currency, format_integer, format_percent

def render() -> None:
    st.title("Fraud KPI Dashboard")
    total_claims = fetch_data("total-claims") or {}
    fraud_claims = fetch_data("fraud-claims") or {}
    fraud_rate = fetch_data("fraud-rate") or {}
    fraud_amount = fetch_data("fraud-amount") or {}
    cols = st.columns(4)
    cols[0].metric("Total Claims", format_integer(total_claims.get("total_claims")))
    cols[1].metric("Fraud Claims", format_integer(fraud_claims.get("fraud_claims")))
    cols[2].metric("Fraud Rate %", format_percent(fraud_rate.get("fraud_rate_pct")))
    cols[3].metric("Fraud Amount", format_currency(fraud_amount.get("fraud_amount")))
