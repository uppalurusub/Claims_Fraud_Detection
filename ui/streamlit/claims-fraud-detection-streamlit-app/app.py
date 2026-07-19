import streamlit as st
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Healthcare Claims Fraud Detection",
    page_icon="🚨",
    layout="wide",
)

page = render_sidebar()

PAGE_MODULES = {
    "Dashboard": "pages.dashboard",
    "KPIs": "pages.kpis",
    "Descriptive Analytics": "pages.descriptive_analytics",
    "Trend Analysis": "pages.trend_analysis",
    "Diagnostic Analysis": "pages.diagnostic_analysis",
    "Predictive Analytics": "pages.predictive_analytics",
    "Anomaly Detection": "pages.anomaly_detection",
    "Risk Analysis": "pages.risk_analysis",
    "Reports": "pages.reports",
    "Summary": "pages.summary",
}

module = __import__(PAGE_MODULES[page], fromlist=["render"])
module.render()
