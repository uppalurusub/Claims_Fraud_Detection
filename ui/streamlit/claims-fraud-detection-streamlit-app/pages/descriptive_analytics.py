import pandas as pd
import plotly.express as px
import streamlit as st
from api.client import fetch_data

def render() -> None:
    st.title("Descriptive Analytics")
    tabs = st.tabs(["State", "Provider", "Procedure"])
    endpoints = ["fraud-by-state", "fraud-by-provider", "fraud-by-procedure"]
    titles = ["Fraud by State", "Fraud by Provider", "Fraud by Procedure"]
    for tab, endpoint, title in zip(tabs, endpoints, titles):
        with tab:
            data = fetch_data(endpoint)
            if data:
                df = pd.DataFrame(data)
                if endpoint == "fraud-by-state" and len(df.columns) >= 2:
                    st.plotly_chart(px.bar(df, x=df.columns[0], y=df.columns[1], title=title),
                                    use_container_width=True)
                st.dataframe(df, use_container_width=True)
