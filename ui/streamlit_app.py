import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ==================================================
# CONFIG
# ==================================================

API_BASE_URL = "http://localhost:8000/fraud"

st.set_page_config(
    page_title="Healthcare Claims Fraud Detection",
    page_icon="🚨",
    layout="wide"
)

# ==================================================
# API HELPER
# ==================================================

def fetch_data(endpoint):

    try:
        response = requests.get(
            f"{API_BASE_URL}/{endpoint}"
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        st.error(f"API Error: {e}")

        return None


def post_data(endpoint):

    try:

        response = requests.post(
            f"{API_BASE_URL}/{endpoint}"
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        st.error(f"API Error: {e}")

        return None


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🚨 Fraud Analytics")

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "KPIs",
        "Descriptive Analytics",
        "Trend Analysis",
        "Diagnostic Analysis",
        "Predictive Analytics",
        "Anomaly Detection",
        "Risk Analysis",
        "Reports",
        "Summary"
    ]
)

# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    st.title("Healthcare Claims Fraud Dashboard")

    data = fetch_data("dashboard")

    if data:
        st.subheader("📊 Fraud Overview")

        kpi = data["kpis"]

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Total Claims",
                f"{kpi['total_claims']:,}"
            )

        with c2:
            st.metric(
                "Fraud Claims",
                f"{kpi['fraud_claims']:,}"
            )

        with c3:
            st.metric(
                "Fraud Rate",
                f"{kpi['fraud_rate_pct']:.2f}%"
            )

        with c4:
            st.metric(
                "Fraud Amount",
                f"${kpi['fraud_amount']:,.0f}"
            )

        c5, c6, c7 = st.columns(3)

        with c5:
            st.metric(
                "Avg Claim Amount",
                f"${kpi['avg_claim_amount']:,.2f}"
            )

        with c6:
            st.metric(
                "Avg Fraud Amount",
                f"${kpi['avg_fraud_amount']:,.2f}"
            )

        with c7:
            st.metric(
                "High Risk Claims",
                f"{kpi['high_risk_claims']:,}"
            )

    summary = data["executive_summary"]

    st.subheader("📋 Executive Summary")

    left, right = st.columns(2)

    with left:
            st.error(
                f"""
        ### 🔍 Key Finding

        {summary['key_finding']}
        """
            )

    with right:
            st.success(
                f"""
        ### ✅ Recommended Action

        {summary['business_action']}
        """
            )

    

    st.subheader("🗺️ Fraud by State")

    state_df = pd.DataFrame(
        data["fraud_by_state"]
    )

    state_df["fraud_rate"] = (
        state_df["fraud_rate"] * 100
    )

    fig = px.bar(
        state_df,
        x="state",
        y="fraud_claims",
        color="fraud_rate",
        title="Fraud Claims by State"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.subheader("🏥 High Risk Providers")

    provider_df = pd.DataFrame(
        data["fraud_by_provider"]
    )

    provider_df = provider_df.sort_values(
        "fraud_rate",
        ascending=False
    )

    fig = px.bar(
        provider_df.head(10),
        x="provider_id",
        y="fraud_rate",
        text="fraud_claims",
        title="Top Fraud Providers"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.subheader("🩺 Fraud Procedures")

    proc_df = pd.DataFrame(
        data["fraud_by_procedure"]
    )

    fig = px.bar(
        proc_df.head(15),
        x="procedure_code",
        y="is_fraud",
        title="Top Fraud Procedures"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.subheader("⚠️ Risk Distribution")

    risk_df = pd.DataFrame(
        data["risk_distribution"]
    )

    fig = px.pie(
        risk_df,
        names="risk_category",
        values="count",
        hole=0.55,
        title="Risk Category Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    with st.expander("📄 Fraud by State Details"):
        st.dataframe(
            state_df,
            width='stretch'
        )

    with st.expander("📄 Fraud by Provider Details"):
        st.dataframe(
            provider_df,
            width='stretch'
        )

    with st.expander("📄 Fraud by Procedure Details"):
        st.dataframe(
            proc_df,
            width='stretch'
        )

    st.subheader("📝 Executive Insights")

    st.info(
        f"""
    • Total Claims Processed: {kpi['total_claims']:,}

    • Fraudulent Claims Detected: {kpi['fraud_claims']:,}

    • Fraud Rate: {kpi['fraud_rate_pct']:.2f}%

    • Financial Exposure: ${kpi['fraud_amount']:,.0f}

    • High-Risk Claims Identified: {kpi['high_risk_claims']}

    • Fraud is concentrated among a limited number of providers and procedures.

    • Immediate audit attention should focus on Provider 43 and Procedure 13.
    """
    )
# ==================================================
# KPIs
# ==================================================

elif page == "KPIs":

    st.title("Fraud KPI Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    total_claims = fetch_data("total-claims") or {}
    fraud_claims = fetch_data("fraud-claims") or {}
    fraud_rate = fetch_data("fraud-rate") or {}
    fraud_amount = fetch_data("fraud-amount") or {}

    

    with col1:
        st.metric(
            "Total Claims",
            total_claims.get("total_claims", 0)
        )

    with col2:
        st.metric(
            "Fraud Claims",
            fraud_claims.get("fraud_claims", 0)
        )

    with col3:
        st.metric(
            "Fraud Rate %",
            fraud_rate.get("fraud_rate_pct", 0)
        )

    with col4:
        st.metric(
            "Fraud Amount",
            f"${fraud_amount.get('fraud_amount',0):,.0f}"
        )

# ==================================================
# DESCRIPTIVE ANALYTICS
# ==================================================

elif page == "Descriptive Analytics":

    st.title("Descriptive Analytics")

    tab1, tab2, tab3 = st.tabs([
        "State",
        "Provider",
        "Procedure"
    ])

    with tab1:

        data = fetch_data("fraud-by-state")

        if data:

            df = pd.DataFrame(data)

            fig = px.bar(
                df,
                x=df.columns[0],
                y=df.columns[1],
                title="Fraud by State"
            )

            st.plotly_chart(
                fig,
                width='stretch'
            )

            st.dataframe(df)

    with tab2:

        data = fetch_data("fraud-by-provider")

        if data:

            df = pd.DataFrame(data)

            st.dataframe(df)

    with tab3:

        data = fetch_data("fraud-by-procedure")

        if data:

            df = pd.DataFrame(data)

            st.dataframe(df)

# ==================================================
# TREND ANALYSIS
# ==================================================

elif page == "Trend Analysis":

    st.title("Fraud Trend Analysis")

    data = fetch_data("fraud-trend")

    if data:

        df = pd.DataFrame(data)

        fig = px.line(
            df,
            x=df.columns[0],
            y=df.columns[1],
            markers=True,
            title="Fraud Trend"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

        st.dataframe(df)

# ==================================================
# DIAGNOSTIC ANALYSIS
# ==================================================

elif page == "Diagnostic Analysis":

    st.title("Root Cause Analysis")

    data = fetch_data("root-cause-analysis")

    if data:

        c1, c2 = st.columns(2)

        c1.metric(
            "Highest Fraud Provider",
            f"{data['highest_fraud_provider']:.2%}"
        )

        c2.metric(
            "Highest Fraud Procedure",
            f"{data['highest_fraud_procedure']:.2%}"
        )

        st.success(
                    f"""
            ### ✅ Recommended

            {data['recommendation']}
            """
                )

        

# ==================================================
# PREDICTIVE ANALYTICS
# ==================================================

elif page == "Predictive Analytics":

    st.title("Fraud Prediction Model")

    if st.button("Train Model"):

        result = post_data("train-model")

        st.success("Model Training Completed")

        st.json(result)

    st.subheader("Model Metrics")

    metrics = fetch_data("model-metrics")

    if metrics:
        st.subheader("🎯 Model Performance")

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric(
            "Accuracy",
            f"{metrics['accuracy']:.2%}"
        )

        c2.metric(
            "Precision",
            f"{metrics['precision']:.2%}"
        )

        c3.metric(
            "Recall",
            f"{metrics['recall']:.2%}"
        )

        c4.metric(
            "F1 Score",
            f"{metrics['f1_score']:.2%}"
        )

        c5.metric(
            "ROC-AUC",
            f"{metrics['roc_auc']:.2%}"
        )

    st.subheader("Feature Importance")

    fi = fetch_data("feature-importance")

    if fi:

        df = pd.DataFrame(fi)

        st.dataframe(df)

# ==================================================
# ANOMALY DETECTION
# ==================================================

elif page == "Anomaly Detection":

    st.title("Anomaly Detection")

    data = fetch_data("anomaly-detection")

    

    

    if data:

        df = pd.DataFrame([
            {
                "Category": "Normal Claims",
                "Count": data["normal_claims"]
            },
            {
                "Category": "Anomalies",
                "Count": data["anomalies"]
            }
        ])

        st.dataframe(df)

        fig = px.pie(
            df,
            names="Category",
            values="Count",
            title="Anomaly Detection Distribution"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

# ==================================================
# RISK ANALYSIS
# ==================================================

elif page == "Risk Analysis":

    st.title("Risk Distribution")

    data = fetch_data("risk-distribution")

    if data:

        df = pd.DataFrame(data)

        fig = px.pie(
            df,
            names=df.columns[0],
            values=df.columns[1],
            title="Risk Distribution"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

        st.dataframe(df)

# ==================================================
# REPORTS
# ==================================================

elif page == "Reports":

    st.title("Fraud Reports")

    tab1, tab2, tab3 = st.tabs([
        "Executive Summary",
        "Fraud Report",
        "Model Report"
    ])

    with tab1:

        data = fetch_data(
            "executive-summary"
        )

        if data:
            if data:

                st.subheader("📊 Executive Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Total Claims",
                        f"{data.get('total_claims',0):,}"
                    )

                with col2:
                    st.metric(
                        "Fraud Claims",
                        f"{data.get('fraud_claims',0):,}"
                    )

                with col3:
                    st.metric(
                        "Fraud Rate %",
                        f"{data.get('fraud_rate',0):.2f}%"
                    )

                with col4:
                    st.metric(
                        "High Risk Claims",
                        f"{data.get('high_risk_claims',0):,}"
                    )

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.info(
                        f"""
            ### 💰 Fraud Exposure

            **Fraud Amount**

            ${data.get('fraud_amount',0):,.2f}
            """
                    )

                with col2:

                    st.warning(
                        f"""
            ### 🔍 Key Finding

            {data.get('key_finding','N/A')}
            """
                    )

                st.success(
                    f"""
            ### ✅ Recommended Business Action

            {data.get('business_action','N/A')}
            """
                )

    with tab2:

        data = fetch_data(
            "fraud-report"
        )

        if data:
            st.header("🚨 Healthcare Claims Fraud Report")

    # ==================================================
    # KPIs
    # ==================================================

    kpi = data["kpis"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Claims",
            f"{kpi['total_claims']:,}"
        )

    with c2:
        st.metric(
            "Fraud Claims",
            f"{kpi['fraud_claims']:,}"
        )

    with c3:
        st.metric(
            "Fraud Rate",
            f"{kpi['fraud_rate_pct']:.2f}%"
        )

    with c4:
        st.metric(
            "Fraud Amount",
            f"${kpi['fraud_amount']:,.0f}"
        )

    st.divider()

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    summary = data["executive_summary"]

    st.subheader("📋 Executive Summary")

    left, right = st.columns(2)

    with left:
        st.info(summary["key_finding"])

    with right:
        st.success(summary["business_action"])

    st.divider()

    # ==================================================
    # FRAUD TREND
    # ==================================================

    st.subheader("📈 Fraud Trend")

    trend_df = pd.DataFrame(
        data["fraud_trend"]
    )

    trend_df["claim_date"] = pd.to_datetime(
        trend_df["claim_date"]
    )

    fig = px.line(
        trend_df,
        x="claim_date",
        y="is_fraud",
        markers=True,
        title="Monthly Fraud Claims Trend"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    # ==================================================
    # FRAUD BY STATE
    # ==================================================

    st.subheader("🗺 Fraud by State")

    state_df = pd.DataFrame(
        data["fraud_by_state"]
    )

    fig = px.bar(
        state_df,
        x="state",
        y="fraud_claims",
        color="fraud_rate",
        title="Fraud Claims by State"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    # ==================================================
    # TOP FRAUD PROVIDERS
    # ==================================================

    st.subheader("🏥 High Risk Providers")

    provider_df = pd.DataFrame(
        data["fraud_by_provider"]
    )

    fig = px.bar(
        provider_df.head(10),
        x="provider_id",
        y="fraud_claims",
        color="fraud_rate",
        title="Top Fraud Providers"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
        provider_df,
        width='stretch'
    )

    # ==================================================
    # PROCEDURES
    # ==================================================

    st.subheader("🩺 Fraud by Procedure")

    proc_df = pd.DataFrame(
        data["fraud_by_procedure"]
    )

    fig = px.bar(
        proc_df.head(10),
        x="procedure_code",
        y="is_fraud",
        title="Top Fraud Procedures"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    # ==================================================
    # RISK DISTRIBUTION
    # ==================================================

    st.subheader("⚠ Risk Distribution")

    risk_df = pd.DataFrame(
        data["risk_distribution"]
    )

    fig = px.pie(
        risk_df,
        names="risk_category",
        values="count",
        hole=0.5,
        title="Risk Category Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    # ==================================================
    # ROOT CAUSE
    # ==================================================

    root = data["root_cause_analysis"]

    st.subheader("🔍 Root Cause Analysis")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Highest Fraud Provider",
            root["highest_fraud_provider"]
        )

    with c2:
        st.metric(
            "Highest Fraud Procedure",
            root["highest_fraud_procedure"]
        )

    st.warning(
        root["recommendation"]
    )

    with tab3:

        data = fetch_data(
            "model-report"
        )

        if data:
            metrics = data["metrics"]

    st.header("🤖 Fraud Detection Model Report")

    # ==================================================
    # MODEL PERFORMANCE KPIs
    # ==================================================

    st.subheader("🎯 Model Performance")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Accuracy",
        f"{metrics['accuracy']:.2%}"
    )

    c2.metric(
        "Precision",
        f"{metrics['precision']:.2%}"
    )

    c3.metric(
        "Recall",
        f"{metrics['recall']:.2%}"
    )

    c4.metric(
        "F1 Score",
        f"{metrics['f1_score']:.2%}"
    )

    c5.metric(
        "ROC AUC",
        f"{metrics['roc_auc']:.2%}"
    )

    st.divider()

    # ==================================================
    # CONFUSION MATRIX
    # ==================================================

    st.subheader("📊 Confusion Matrix")

    cm = metrics["confusion_matrix"]

    cm_df = pd.DataFrame(
        cm,
        columns=["Predicted Normal", "Predicted Fraud"],
        index=["Actual Normal", "Actual Fraud"]
    )

    fig = px.imshow(
        cm_df,
        text_auto=True,
        aspect="auto",
        title="Confusion Matrix"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(cm_df)

    st.divider()

    # ==================================================
    # CLASSIFICATION REPORT
    # ==================================================

    st.subheader("📋 Classification Report")

    report = metrics["classification_report"]

    report_df = pd.DataFrame(
        report
    ).T

    st.dataframe(
        report_df,
        width='stretch'
    )

    st.divider()

    # ==================================================
    # FEATURE IMPORTANCE
    # ==================================================

    st.subheader("🔥 Top Feature Importance")

    fi_df = pd.DataFrame(
        data["feature_importance"]
    )

    fi_df = fi_df.sort_values(
        "importance",
        ascending=False
    )

    fig = px.bar(
        fi_df.head(15),
        x="importance",
        y="feature",
        orientation="h",
        title="Top Fraud Predictors"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    st.dataframe(
        fi_df,
        width='stretch'
    )

    st.divider()

    # ==================================================
    # ANOMALY DETECTION
    # ==================================================

    st.subheader("🚨 Anomaly Detection")

    anomaly = data["anomaly_detection"]

    a1, a2 = st.columns(2)

    with a1:
        st.metric(
            "Normal Claims",
            f"{anomaly['normal_claims']:,}"
        )

    with a2:
        st.metric(
            "Anomalies",
            f"{anomaly['anomalies']:,}"
        )

    anomaly_df = pd.DataFrame({
        "Category": [
            "Normal Claims",
            "Anomalies"
        ],
        "Count": [
            anomaly["normal_claims"],
            anomaly["anomalies"]
        ]
    })

    fig = px.pie(
        anomaly_df,
        names="Category",
        values="Count",
        hole=0.55,
        title="Anomaly Distribution"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

    

elif page == "Summary":

    st.title("Model Summary")
    st.success(
        """
    ✅ Excellent overall performance (98.33% Accuracy)

    ✅ Very strong fraud detection capability (86.11% Recall)

    ✅ Outstanding ROC-AUC (99.35%)

    ✅ Top fraud drivers:
    • Fraud Risk Score
    • Amount × Procedures
    • High Claim Flag
    • Prior Claims Activity

    ⚠ Model misses very few fraud cases and is suitable for
    real-time fraud screening and provider audit prioritization.
    """
    )