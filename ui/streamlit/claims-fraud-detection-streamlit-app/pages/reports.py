import pandas as pd
import plotly.express as px
import streamlit as st
from api.client import fetch_data
from utils.formatters import format_currency, format_integer, format_percent

def _executive_summary() -> None:
    data = fetch_data("executive-summary")
    if not data:
        return
    st.subheader("📊 Executive Summary")
    cols = st.columns(4)
    cols[0].metric("Total Claims", format_integer(data.get("total_claims")))
    cols[1].metric("Fraud Claims", format_integer(data.get("fraud_claims")))
    cols[2].metric("Fraud Rate %", format_percent(data.get("fraud_rate")))
    cols[3].metric("High Risk Claims", format_integer(data.get("high_risk_claims")))
    left, right = st.columns(2)
    left.info(f"### 💰 Fraud Exposure\n\n**Fraud Amount**\n\n{format_currency(data.get('fraud_amount'), 2)}")
    right.warning(f"### 🔍 Key Finding\n\n{data.get('key_finding', 'N/A')}")
    st.success(f"### ✅ Recommended Business Action\n\n{data.get('business_action', 'N/A')}")

def _fraud_report() -> None:
    data = fetch_data("fraud-report")
    if not data:
        return
    st.header("🚨 Healthcare Claims Fraud Report")
    kpi = data.get("kpis", {})
    cols = st.columns(4)
    cols[0].metric("Total Claims", format_integer(kpi.get("total_claims")))
    cols[1].metric("Fraud Claims", format_integer(kpi.get("fraud_claims")))
    cols[2].metric("Fraud Rate", format_percent(kpi.get("fraud_rate_pct")))
    cols[3].metric("Fraud Amount", format_currency(kpi.get("fraud_amount")))

    summary = data.get("executive_summary", {})
    left, right = st.columns(2)
    left.info(summary.get("key_finding", "N/A"))
    right.success(summary.get("business_action", "N/A"))

    trend_df = pd.DataFrame(data.get("fraud_trend", []))
    if not trend_df.empty:
        trend_df["claim_date"] = pd.to_datetime(trend_df["claim_date"])
        st.plotly_chart(px.line(trend_df, x="claim_date", y="is_fraud", markers=True,
                                title="Monthly Fraud Claims Trend"), use_container_width=True)

    chart_specs = [
        ("🗺 Fraud by State", "fraud_by_state", "state", "fraud_claims", "fraud_rate", "Fraud Claims by State"),
        ("🏥 High Risk Providers", "fraud_by_provider", "provider_id", "fraud_claims", "fraud_rate", "Top Fraud Providers"),
        ("🩺 Fraud by Procedure", "fraud_by_procedure", "procedure_code", "is_fraud", None, "Top Fraud Procedures"),
    ]
    for heading, key, x, y, color, title in chart_specs:
        df = pd.DataFrame(data.get(key, []))
        if not df.empty:
            st.subheader(heading)
            kwargs = {"data_frame": df.head(10), "x": x, "y": y, "title": title}
            if color:
                kwargs["color"] = color
            st.plotly_chart(px.bar(**kwargs), use_container_width=True)
            if key == "fraud_by_provider":
                st.dataframe(df, use_container_width=True)

    risk_df = pd.DataFrame(data.get("risk_distribution", []))
    if not risk_df.empty:
        st.subheader("⚠ Risk Distribution")
        st.plotly_chart(px.pie(risk_df, names="risk_category", values="count", hole=0.5,
                               title="Risk Category Distribution"), use_container_width=True)

    root = data.get("root_cause_analysis", {})
    st.subheader("🔍 Root Cause Analysis")
    cols = st.columns(2)
    cols[0].metric("Highest Fraud Provider", root.get("highest_fraud_provider", "N/A"))
    cols[1].metric("Highest Fraud Procedure", root.get("highest_fraud_procedure", "N/A"))
    st.warning(root.get("recommendation", "N/A"))

def _model_report() -> None:
    data = fetch_data("model-report")
    if not data:
        return
    metrics = data.get("metrics", {})
    st.header("🤖 Fraud Detection Model Report")
    st.subheader("🎯 Model Performance")
    cols = st.columns(5)
    for col, label, key in zip(cols, ["Accuracy", "Precision", "Recall", "F1 Score", "ROC AUC"],
                               ["accuracy", "precision", "recall", "f1_score", "roc_auc"]):
        col.metric(label, format_percent(metrics.get(key), ratio=True))

    cm = metrics.get("confusion_matrix")
    if cm:
        st.subheader("📊 Confusion Matrix")
        cm_df = pd.DataFrame(cm, columns=["Predicted Normal", "Predicted Fraud"],
                             index=["Actual Normal", "Actual Fraud"])
        st.plotly_chart(px.imshow(cm_df, text_auto=True, aspect="auto", title="Confusion Matrix"),
                        use_container_width=True)
        st.dataframe(cm_df, use_container_width=True)

    report = metrics.get("classification_report")
    if report:
        st.subheader("📋 Classification Report")
        st.dataframe(pd.DataFrame(report).T, use_container_width=True)

    fi_df = pd.DataFrame(data.get("feature_importance", []))
    if not fi_df.empty:
        fi_df = fi_df.sort_values("importance", ascending=False)
        st.subheader("🔥 Top Feature Importance")
        fig = px.bar(fi_df.head(15), x="importance", y="feature", orientation="h",
                     title="Top Fraud Predictors")
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(fi_df, use_container_width=True)

    anomaly = data.get("anomaly_detection", {})
    if anomaly:
        st.subheader("🚨 Anomaly Detection")
        cols = st.columns(2)
        cols[0].metric("Normal Claims", format_integer(anomaly.get("normal_claims")))
        cols[1].metric("Anomalies", format_integer(anomaly.get("anomalies")))
        anomaly_df = pd.DataFrame({
            "Category": ["Normal Claims", "Anomalies"],
            "Count": [anomaly.get("normal_claims", 0), anomaly.get("anomalies", 0)],
        })
        st.plotly_chart(px.pie(anomaly_df, names="Category", values="Count", hole=0.55,
                               title="Anomaly Distribution"), use_container_width=True)

def render() -> None:
    st.title("Fraud Reports")
    tabs = st.tabs(["Executive Summary", "Fraud Report", "Model Report"])
    with tabs[0]:
        _executive_summary()
    with tabs[1]:
        _fraud_report()
    with tabs[2]:
        _model_report()
