import streamlit as st

PAGES = [
    "Dashboard", "KPIs", "Descriptive Analytics", "Trend Analysis",
    "Diagnostic Analysis", "Predictive Analytics", "Anomaly Detection",
    "Risk Analysis", "Reports", "Summary",
]

def render_sidebar() -> str:
    st.sidebar.title("🚨 Fraud Analytics")
    return st.sidebar.radio("Select Module", PAGES)
