import pandas as pd
import plotly.express as px
import streamlit as st
from api.client import fetch_data

def render() -> None:
    st.title("Fraud Trend Analysis")
    data = fetch_data("fraud-trend")
    if data:
        df = pd.DataFrame(data)
        if len(df.columns) >= 2:
            st.plotly_chart(px.line(df, x=df.columns[0], y=df.columns[1], markers=True,
                                    title="Fraud Trend"), use_container_width=True)
        st.dataframe(df, use_container_width=True)
