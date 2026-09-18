import streamlit as st
from supabase import create_client
from datetime import datetime

# =========================================================
# LuxeMart — Dark & Bold Luxury Marketplace
# =========================================================

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🖤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LUXURY DARK DESIGN
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --black: #08090B;
    --panel: #111318;
    --panel2: #181A20;
    --gold: #D4AF37;
    --gold-light: #F2D77A;
    --white: #FFFFFF;
    --muted: #A8AAB2;
    --border: #30323A;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--black) !important;
    color: var(--white) !important;
}

[data-testid="stHeader"] {
    background: rgba(8,9,11,.95) !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
}

* {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: white !important;
}

.luxe-logo {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -2px;
    color: white;
}

.luxe-logo span {
    color: var(--gold);
}

.kicker {
    color: var(--gold-light);
    font-size: .78rem;
    font-weight: 800;
    letter-spacing: .28em;
    margin-bottom: 12px;
}

.hero {
    margin-top: 25px;
    padding: 55px 45px;
    border-radius: 28px;
    border: 1px solid var(--border);
    background:
        radial-gradient(circle at 85% 15%, rgba(212,175,55,.18), transparent 30%),
        linear-gradient(135deg,#17191F,#090A0D);
    box-shadow: 0 25px 80px rgba(0,0,0,.45);
}

.hero h1 {
    font-size: clamp(3rem,8vw,7rem) !important;
    line-height: .95;
    margin: 12px 0 25px;
}

.hero p {
    max-width: 720px;
    color: #C9CAD0;
    font-size: 1.1rem;
    line-height: 1.8;
}

.gold-line {
    height: 2px;
    margin: 25px 0;
    background: linear-gradient(
        90deg,
        var(--gold),
        transparent
    );
}

.card {
    background: linear-gradient(
        145deg,
        #191B21,
        #101115
    );
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 15px 35px rgba(0,0,0,.25);
}

.card:hover {
    border-color: var(--gold);
}

.product-name {
    color: white;
    font-size: 1.2rem;
    font-weight: 800;
}

.product-category {
    color: var(--muted);
    margin-top: 5px;
}

.price {
    color: var(--gold-light);
    font-size: 1.3rem;
    font-weight: 800;
    margin-top: 15px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 50px;
    border: 1px solid rgba(212,175,55,.5);
    color: var(--gold-light);
    font-size: .72rem;
    font-weight: 800;
    letter-spacing: .08em;
}

.stat {
    text-align: center;
    padding: 22px;
    border: 1px solid var(--border);
    border-radius: 18px;
    background: var(--panel);
}

.stat-number {
    font-family: 'Playfair Display', serif;
    color: var(--gold-light);
    font-size: 2rem;
    font-weight: 800;
}

.stat-label {
    color: var(--muted);
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08em;
}

/* Buttons */

.stButton > button {
    width: 100%;
    min-height: 46px;
    border-radius: 13px !important;
    border: 1px solid #41434B !important;
    background: #181A20 !important;
    color: white !important;
    font-weight: 800 !important;
}

.stButton > button:hover {
    border-color: var(--gold) !important;
    color: var(--gold-light) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        #D4AF37,
        #A98217
    ) !important;
    color: #090909 !important;
    border: none !important;
}

/* Inputs */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background: #15171C !important;
    color: white !important;
    border: 1px solid #353740 !important;
    border-radius: 12px !important;
}

label {
    color: #E8E8EC !important;
}

/* Tabs */

.stTabs [data-baseweb="tab"] {
    color: #A5A6AD !important;
    font-weight: 800 !important;
}

.stTabs [aria-selected="true"] {
    color: var(--gold-light) !important;
}

/* Footer */

.footer {
    margin-top: 60px;
    padding: 30px 10px;
    text-align: center;
    color: var(--muted);
    border-top: 1px solid var(--border);
}

@media(max-width:700px) {

    .block-container {
        padding-left: .8rem;
        padding-right: .8rem;
    }

    .hero {
        padding: 30px 22px;
        border-radius: 20px;
    }

    .hero h1 {
        font-size: 3.4rem !important;
    }

    .luxe-logo {
        font-size: 2.4rem;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SUPABASE CONNECTION
# =========================================================

try:
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]

    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

except Exception:
    st.error(
        "Supabase is not configured. "
        "Open Streamlit → Manage app → Settings → Secrets."
    )
    st.stop()


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# =========================================================
# DATABASE HELPERS
# =========================================================
