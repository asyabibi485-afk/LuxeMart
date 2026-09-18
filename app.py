import streamlit as st
from supabase import create_client
from datetime import datetime, timezone


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# LUXURY DESIGN
# =========================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0b0b0b;
    color: #ffffff;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #ffffff !important;
}

p, label, span, div {
    color: #eeeeee;
}

.hero {
    padding: 55px 35px;
    border-radius: 25px;
    margin-bottom: 35px;
    background: linear-gradient(135deg, #171717, #0b0b0b);
    border: 1px solid #333333;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 55px;
    font-weight: 700;
    line-height: 1.05;
    color: #ffffff;
}

.hero-subtitle {
    font-size: 18px;
    color: #bbbbbb;
    margin-top: 15px;
}

.luxury-card {
    background: #151515;
    border: 1px solid #333333;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 20px;
}

.price {
    font-size: 24px;
    font
