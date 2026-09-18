import streamlit as st
from supabase import create_client
from datetime import datetime, timezone

st.set_page_config(
    page_title="LuxeMart",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SUPABASE
# =========================================================

try:
    supabase = create_client(
        st.secrets["supabase"]["url"],
        st.secrets["supabase"]["key"]
    )
except Exception as e:
    st.error("Supabase connection failed.")
    st.error(str(e))
    st.stop()


# =========================================================
# SESSION
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# =========================================================
# FUNCTIONS
# =========================================================

def money(value):
    try:
        return f"Rs {float(value):,.0f}"
    except Exception:
        return "Rs 0"


def get_products():
    try:
        result = (
            supabase
            .table("products")
            .select("*")
            .eq("active", True)
            .order("created_at", desc=True)
            .execute()
        )
        return result.data or []
    except Exception as e:
        st.error(str(e))
        return []


def add_cart(product):
    st.session_state.cart.append(product)


def remove_cart(index):
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)


def get_cart_total():
    total = 0

    for item in st.session_state.cart:
        try:
            total += float(item.get("price", 0))
        except Exception:
            pass

    return total


# =========================================================
# LUXURY UI
# =========================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis
