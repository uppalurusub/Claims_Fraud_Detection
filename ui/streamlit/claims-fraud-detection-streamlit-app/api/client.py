from typing import Any
import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000/fraud"
TIMEOUT_SECONDS = 30

def _request(method: str, endpoint: str) -> Any | None:
    try:
        response = requests.request(
            method=method,
            url=f"{API_BASE_URL}/{endpoint.lstrip('/')}",
            timeout=TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        st.error(f"API Error: {exc}")
        return None

def fetch_data(endpoint: str) -> Any | None:
    return _request("GET", endpoint)

def post_data(endpoint: str) -> Any | None:
    return _request("POST", endpoint)
