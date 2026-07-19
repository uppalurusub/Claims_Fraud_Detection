import streamlit as st
from api.client import post_data
from components.response_view import render_training_response

def render_train_model_form() -> None:
    if st.button("Train Model", type="primary", use_container_width=True):
        with st.spinner("Training fraud detection model..."):
            result = post_data("train-model")
        if result is not None:
            st.success("Model Training Completed")
            render_training_response(result)
