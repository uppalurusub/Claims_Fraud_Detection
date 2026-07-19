from typing import Any
import pandas as pd
import streamlit as st

def render_training_response(result: Any) -> None:
    if isinstance(result, dict):
        message = result.get("message") or result.get("status")
        if message:
            st.info(str(message))
        scalar_values = {
            key: value for key, value in result.items()
            if isinstance(value, (str, int, float, bool)) and key not in {"message", "status"}
        }
        if scalar_values:
            st.dataframe(pd.DataFrame([scalar_values]), use_container_width=True)
    elif isinstance(result, list):
        st.dataframe(pd.DataFrame(result), use_container_width=True)
    else:
        st.write(result)

def render_dataframe(data: Any) -> pd.DataFrame:
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    return df
