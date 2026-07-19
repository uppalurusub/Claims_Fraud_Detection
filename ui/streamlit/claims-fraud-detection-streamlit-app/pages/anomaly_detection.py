import pandas as pd
import plotly.express as px
import streamlit as st
from api.client import fetch_data

def render() -> None:
    st.title("Anomaly Detection")
    data = fetch_data("anomaly-detection")
    if data:
        df = pd.DataFrame([
            {"Category": "Normal Claims", "Count": data.get("normal_claims", 0)},
            {"Category": "Anomalies", "Count": data.get("anomalies", 0)},
        ])
        st.dataframe(df, use_container_width=True)
        st.plotly_chart(px.pie(df, names="Category", values="Count",
                               title="Anomaly Detection Distribution"), use_container_width=True)
