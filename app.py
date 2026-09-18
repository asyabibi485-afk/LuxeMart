import streamlit as st
from supabase import create_client
from datetime import datetime
import html

# =========================================================
# LuxeMart — Luxury Marketplace
# =========================================================

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🖤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LUXURY DESIGN
# =========================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700;800;900&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --black: #07080A;
    --dark: #0D0F13;
    --panel: #151820;
    --panel2: #1C2029;
    --gold: #D4AF37;
    --gold2: #F4D875;
    --white: #FFFFFF;
    --text: #F7F7F9;
    --muted: #C4C7CF;
    --border: #3A3E49;
    --green: #48D597;
}

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background: #07080A !important;
    color: #FFFFFF !important;
}

[data-testid="stHeader"] {
    background: #07080A !important;
}

[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    max-width: 1250px;
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
}

* {
    font-family: 'DM Sans', sans-serif;
}

h1,
h2,
h3 {
    font-family: 'Playfair Display', serif !important;
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

p,
span,
div,
label {
    color: #F7F7F9;
}

.luxe-logo {
    font-family: 'Playfair Display', serif !important;
    font-size: 3.4rem;
    line-height: 1;
    font-weight: 800;
    letter-spacing: -2px;
    color: #FFFFFF !important;
}

.luxe-logo span {
    color: #F4D875 !important;
}

.kicker {
    color: #F4D875 !important;
    font-size: 0.78rem;
    font-weight: 900;
    letter-spacing: 0.25em;
    margin-top: 8px;
    margin-bottom: 12px;
}

.gold-line {
    height: 2px;
    margin: 18px 0 25px 0;
    background: linear-gradient(
        90deg,
        #F4D875,
        #D4AF37,
        transparent
    );
}

/* HERO */

.hero {
    margin: 18px 0 28px 0;
    padding: 55px 45px;
    border-radius: 28px;
    border: 1px solid #3A3E49;
    background:
        radial-gradient(
            circle at 85% 15%,
            rgba(212,175,55,0.25),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #20242D,
            #0A0B0E
        );
    box-shadow:
        0 25px 70px rgba(0,0,0,0.55);
}

.hero h1 {
    font-size: clamp(3rem, 8vw, 6.5rem) !important;
    line-height: 0.95 !important;
    margin: 12px 0 25px 0 !important;
    color: #FFFFFF !important;
}

.hero p {
    color: #E4E5EA !important;
    font-size: 1.08rem;
    line-height: 1.8;
    max-width: 720px;
    font-weight: 600;
}

/* CARDS */

.card {
    background:
        linear-gradient(
            145deg,
            #1A1D25,
            #101216
        );
    border: 1px solid #393D47;
    border-radius: 22px;
    padding: 25px;
    margin-bottom: 18px;
    box-shadow:
        0 14px 35px rgba(0,0,0,0.30);
}

.card-title {
    color: #FFFFFF !important;
    font-size: 1.25rem;
    font-weight: 900;
    margin-top: 14px;
}

.card-text {
    color: #C9CCD4 !important;
    font-size: 0.95rem;
    font-weight: 600;
    margin-top: 6px;
}

.price {
    color: #F4D875 !important;
    font-size: 1.35rem;
    font-weight: 900;
    margin-top: 15px;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 50px;
    border: 1px solid #D4AF37;
    background: rgba(212,175,55,0.10);
    color: #F4D875 !important;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.08em;
}

/* STATS */

.stat {
    text-align: center;
    padding: 24px 15px;
    border: 1px solid #393D47;
    border-radius: 20px;
    background: #11141A;
    margin-bottom: 18px;
}

.stat-number {
    font-family: 'Playfair Display', serif !important;
    color: #F4D875 !important;
    font-size: 2.2rem;
    font-weight: 900;
}

.stat-label {
    color: #D2D4DA !important;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.10em;
}

/* BUTTONS */

.stButton > button {
    min-height: 48px !important;
    width: 100%;
    border-radius: 14px !important;
    border: 1px solid #555A66 !important;
    background: #1B1E26 !important;
    color: #FFFFFF !important;
    font-size: 0.88rem !important;
    font-weight: 900 !important;
    letter-spacing: 0.04em !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.22);
}

.stButton > button:hover {
    border-color: #F4D875 !important;
    color: #F4D875 !important;
    background: #242832 !important;
    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background:
        linear-gradient(
            135deg,
            #F4D875,
            #C49B28
        ) !important;
    color: #090909 !important;
    border: 1px solid #F4D875 !important;
    font-weight: 900 !important;
    text-shadow: none !important;
}

.stButton > button[kind="primary"]:hover {
    background:
        linear-gradient(
            135deg,
            #FFE994,
            #D4AF37
        ) !important;
    color: #000000 !important;
}

/* INPUTS */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #151820 !important;
    color: #FFFFFF !important;
    border: 1px solid #454A56 !important;
    border-radius: 13px !important;
    font-weight: 700 !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #AEB2BC !important;
}

.stTextInput label,
.stTextArea label,
.stNumberInput label,
.stSelectbox label {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* CHECKBOX */

.stCheckbox label {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* ALERTS */

[data-testid
