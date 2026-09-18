import streamlit as st

# =========================================================
# LUXEMART — CRAFTWORK-INSPIRED LUXURY STORE
# =========================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []


# =========================================================
# LUXURY DESIGN
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #f8f7f4;
        color: #151515;
    }

    .block-container {
        max-width: 1280px;
        padding: 1.2rem 28px 50px 28px;
    }

    h1, h2, h3, h4 {
        color: #151515 !important;
    }

    p, label {
        color: #666 !important;
    }

    /* TOP BAR */

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #ffffff;
        border: 1px solid #e8e6e0;
        border-radius: 18px;
        padding: 14px 20px;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px rgba(0,0,0,.025);
    }

    .brand {
        font-size: 23px;
        font-weight: 850;
        letter-spacing: 2px;
        color: #111;
    }

    .brand span {
        color: #a47b45;
    }

    .nav-note {
        font-size: 13px;
        color: #777;
    }

    /* HERO */

    .hero {
        position: relative;
        overflow: hidden;
        min-height: 390px;
        border-radius: 28px;
        background:
            radial-gradient(
                circle at 90% 15%,
                rgba(196,165,116,.20),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #e9e3d8 0%,
                #f7f5ef 55%,
                #eee9df 100%
            );
        border: 1px solid #e2ded5;
        padding: 60px 55px;
        margin-bottom: 32px;
    }

    .hero-small {
        display: inline-block;
        padding: 8px 13px;
        border-radius: 100px;
        background: #171717;
        color: #e4c58e;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
    }

    .hero-title {
        max-width: 700px;
        font-size: clamp(42px, 6vw, 76px);
        line-height: .95;
        letter-spacing: -4px;
        font-weight: 850;
        color: #111;
    }

    .hero-title span {
        color: #a47b45;
    }

    .hero-description {
        max-width: 570px;
        font-size: 17px;
        line-height: 1.7;
        color: #666;
        margin-top: 22px;
    }

    .hero-circle {
        position: absolute;
        right: -90px;
        bottom: -130px;
        width: 390px;
        height: 390px;
        border-radius: 50%;
        background: rgba(255,255,255,.42);
        border: 1px solid rgba(164,123,69,.15);
    }

    /* SECTION */

    .section-head {
        display: flex;
        justify-content: space-between;
        align-items: end;
        margin: 35px 0 18px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 850;
        letter-spacing: -1px;
        color: #151515;
    }

    .section-caption {
        color: #888;
        font-size: 13px;
    }

    /* SEARCH */

    div[data-testid="stTextInput"] input {
        border-radius: 14px !important;
        border: 1px solid #dedbd4 !important;
        background: white !important;
        color: #111 !important;
        padding: 13px 16px !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #a47b45 !important;
        box-shadow: 0 0 0 1px #a
