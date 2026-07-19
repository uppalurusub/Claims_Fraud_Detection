import pandas as pd
import plotly.express as px
import streamlit as st
from api.client import fetch_data

def render() -> None:
    st.title("Risk Distribution")
    data = fetch_data("risk-distribution")
    if data:
        df = pd.DataFrame(data)
        if len(df.columns) >= 2:
            st.plotly_chart(px.pie(df, names=df.columns[0], values=df.columns[1],
                                   title="Risk Distribution"), use_container_width=True)
        st.dataframe(df, use_container_width=True)
