import streamlit as st
from api.client import fetch_data
from utils.formatters import format_percent

def render() -> None:
    st.title("Root Cause Analysis")
    data = fetch_data("root-cause-analysis")
    if not data:
        return
    cols = st.columns(2)
    cols[0].metric("Highest Fraud Provider", format_percent(data.get("highest_fraud_provider"), ratio=True))
    cols[1].metric("Highest Fraud Procedure", format_percent(data.get("highest_fraud_procedure"), ratio=True))
    st.success(f"### ✅ Recommended\n\n{data.get('recommendation', 'N/A')}")
