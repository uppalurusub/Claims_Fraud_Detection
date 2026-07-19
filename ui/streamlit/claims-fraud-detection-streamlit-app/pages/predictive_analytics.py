import pandas as pd
import streamlit as st
from api.client import fetch_data
from components.request_form import render_train_model_form
from utils.formatters import format_percent

def render() -> None:
    st.title("Fraud Prediction Model")
    render_train_model_form()
    st.subheader("Model Metrics")
    metrics = fetch_data("model-metrics")
    if metrics:
        st.subheader("🎯 Model Performance")
        cols = st.columns(5)
        for col, label, key in zip(cols, ["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"],
                                   ["accuracy", "precision", "recall", "f1_score", "roc_auc"]):
            col.metric(label, format_percent(metrics.get(key), ratio=True))
    st.subheader("Feature Importance")
    fi = fetch_data("feature-importance")
    if fi:
        st.dataframe(pd.DataFrame(fi), use_container_width=True)
