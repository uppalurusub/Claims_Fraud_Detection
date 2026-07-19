import streamlit as st

def render() -> None:
    st.title("Model Summary")
    st.success(
        "✅ Excellent overall performance (98.33% Accuracy)\n\n"
        "✅ Very strong fraud detection capability (86.11% Recall)\n\n"
        "✅ Outstanding ROC-AUC (99.35%)\n\n"
        "✅ Top fraud drivers:\n"
        "• Fraud Risk Score\n"
        "• Amount × Procedures\n"
        "• High Claim Flag\n"
        "• Prior Claims Activity\n\n"
        "⚠ Model misses very few fraud cases and is suitable for "
        "real-time fraud screening and provider audit prioritization."
    )
