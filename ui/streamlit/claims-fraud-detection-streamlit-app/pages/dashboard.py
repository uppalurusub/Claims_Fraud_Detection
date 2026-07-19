import pandas as pd
import plotly.express as px
import streamlit as st
from api.client import fetch_data
from utils.formatters import format_currency, format_integer, format_percent

def render() -> None:
    st.title("Healthcare Claims Fraud Dashboard")
    data = fetch_data("dashboard")
    if not data:
        return

    kpi = data.get("kpis", {})
    st.subheader("📊 Fraud Overview")
    cols = st.columns(4)
    cols[0].metric("Total Claims", format_integer(kpi.get("total_claims")))
    cols[1].metric("Fraud Claims", format_integer(kpi.get("fraud_claims")))
    cols[2].metric("Fraud Rate", format_percent(kpi.get("fraud_rate_pct")))
    cols[3].metric("Fraud Amount", format_currency(kpi.get("fraud_amount")))
    cols = st.columns(3)
    cols[0].metric("Avg Claim Amount", format_currency(kpi.get("avg_claim_amount"), 2))
    cols[1].metric("Avg Fraud Amount", format_currency(kpi.get("avg_fraud_amount"), 2))
    cols[2].metric("High Risk Claims", format_integer(kpi.get("high_risk_claims")))

    summary = data.get("executive_summary", {})
    st.subheader("📋 Executive Summary")
    left, right = st.columns(2)
    left.error(f"### 🔍 Key Finding\n\n{summary.get('key_finding', 'N/A')}")
    right.success(f"### ✅ Recommended Action\n\n{summary.get('business_action', 'N/A')}")

    state_df = pd.DataFrame(data.get("fraud_by_state", []))
    if not state_df.empty:
        st.subheader("🗺️ Fraud by State")
        chart_df = state_df.copy()
        if "fraud_rate" in chart_df:
            chart_df["fraud_rate"] = chart_df["fraud_rate"] * 100
        st.plotly_chart(px.bar(chart_df, x="state", y="fraud_claims", color="fraud_rate",
                               title="Fraud Claims by State"), use_container_width=True)
        with st.expander("📄 Fraud by State Details"):
            st.dataframe(chart_df, use_container_width=True)

    provider_df = pd.DataFrame(data.get("fraud_by_provider", []))
    if not provider_df.empty:
        provider_df = provider_df.sort_values("fraud_rate", ascending=False)
        st.subheader("🏥 High Risk Providers")
        st.plotly_chart(px.bar(provider_df.head(10), x="provider_id", y="fraud_rate",
                               text="fraud_claims", title="Top Fraud Providers"),
                        use_container_width=True)
        with st.expander("📄 Fraud by Provider Details"):
            st.dataframe(provider_df, use_container_width=True)

    proc_df = pd.DataFrame(data.get("fraud_by_procedure", []))
    if not proc_df.empty:
        st.subheader("🩺 Fraud Procedures")
        st.plotly_chart(px.bar(proc_df.head(15), x="procedure_code", y="is_fraud",
                               title="Top Fraud Procedures"), use_container_width=True)
        with st.expander("📄 Fraud by Procedure Details"):
            st.dataframe(proc_df, use_container_width=True)

    risk_df = pd.DataFrame(data.get("risk_distribution", []))
    if not risk_df.empty:
        st.subheader("⚠️ Risk Distribution")
        st.plotly_chart(px.pie(risk_df, names="risk_category", values="count", hole=0.55,
                               title="Risk Category Distribution"), use_container_width=True)

    st.subheader("📝 Executive Insights")
    st.info(
        f"• Total Claims Processed: {format_integer(kpi.get('total_claims'))}\n\n"
        f"• Fraudulent Claims Detected: {format_integer(kpi.get('fraud_claims'))}\n\n"
        f"• Fraud Rate: {format_percent(kpi.get('fraud_rate_pct'))}\n\n"
        f"• Financial Exposure: {format_currency(kpi.get('fraud_amount'))}\n\n"
        f"• High-Risk Claims Identified: {format_integer(kpi.get('high_risk_claims'))}\n\n"
        "• Fraud is concentrated among a limited number of providers and procedures."
    )
