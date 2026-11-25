import os
from dotenv import load_dotenv

load_dotenv()

# Try Streamlit secrets first (for cloud deployment), fall back to .env
try:
    import streamlit as st
    _secrets = st.secrets
except Exception:
    _secrets = {}


def _get(key):
    """Read from Streamlit secrets if available, otherwise from env."""
    try:
        return _secrets[key]
    except Exception:
        return os.getenv(key)


class Config:
    RAPIDAPI_KEY  = _get("RAPIDAPI_KEY")
    RAPIDAPI_HOST = _get("RAPIDAPI_HOST")
    BASE_URL      = _get("BASE_URL")

    DB_HOST     = _get("DB_HOST")
    DB_PORT     = _get("DB_PORT")
    DB_NAME     = _get("DB_NAME")
    DB_USER     = _get("DB_USER")
    DB_PASSWORD = _get("DB_PASSWORD")
