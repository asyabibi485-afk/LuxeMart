import streamlit as st

# ============================================================
# LUXEMART — MODERN LUXURY SHOP
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "category" not in st.session_state:
    st.session_state.category = "All"

if "admin_logged" not in st.session_state:
    st.session_state.admin_logged = False


# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Velvet Luxe Handbag",
        "category": "Fashion",
        "price": 3499,
        "emoji": "👜",
        "description": "Elegant everyday handbag with a premium luxury look.",
    },
    {
        "id": 2,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "emoji": "📿",
        "description": "Minimal pearl necklace designed for a timeless style.",
    },
    {
        "id": 3,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "emoji": "⌚",
        "description": "Modern gold-tone watch with an elegant premium finish.",
    },
    {
        "id": 4,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "emoji": "🕶️",
        "description": "Stylish sunglasses for a clean and confident look.",
    },
    {
        "id": 5,
        "name": "Luxury Perfume",
        "category": "Beauty",
        "price": 2999,
        "emoji": "🌸",
        "description": "A sophisticated fragrance with a soft lasting aroma.",
    },
    {
        "id": 6,
        "name": "Silk Evening Scarf",
        "category": "Fashion",
        "price": 1599,
        "emoji": "🧣",
        "description": "Soft statement scarf with an elegant evening aesthetic.",
    },
    {
        "id": 7,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "emoji": "💎",
        "description": "Delicate crystal bracelet for everyday glamour.",
    },
    {
        "id": 8,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "emoji": "💄",
        "description": "Beautiful makeup essentials packed into one stylish set.",
    },
]


# ============================================================
# CSS — DARK, BOLD & VISIBLE TEXT
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap'
);

/* =========================================================
   GLOBAL
   ========================================================= */

:root {
    --dark: #15111c;
    --dark2: #21192d;
    --purple: #7657ff;
    --pink: #ff3f91;
    --text: #15121b;
    --text2: #25202e;
    --muted: #51495b;
    --border: #ddd6e7;
}

.stApp {
    background:
        radial-gradient(
            circle at 0% 0%,
            rgba(255, 63, 145, .12),
            transparent 25%
        ),
        radial-gradient(
            circle at 100% 0%,
            rgba(118, 87, 255, .14),
            transparent 25%
        ),
        linear-gradient(
            180deg,
            #fffaff 0%,
            #f8f6ff 55%,
            #ffffff 100%
        );

    color: var(--text) !important;
}

/* EVERYTHING DARK + VISIBLE */

html,
body,
.stApp,
p,
div,
span,
label,
h1,
h2,
h3,
h4,
h5,
h6 {
    font-family: 'DM Sans', sans-serif;
    color: #15121b;
}

p {
    font-weight: 600;
}

h1,
h2,
h3,
h4 {
    font-weight: 800 !important;
    color: #111018 !important;
}

.block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* HIDE STREAMLIT BRANDING */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* =========================================================
   HEADER
   ========================================================= */

.lux-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 17px 22px;
    margin-bottom: 18px;

    border-radius: 22px;

    background: rgba(255,255,255,.94);

    border: 1px solid #e4deeb;

    box-shadow:
        0 12px 40px rgba(40,25,70,.09);

    backdrop-filter: blur(18px);
}

.lux-logo {
    font-size: 27px;
    font-weight: 900 !important;
    letter-spacing: -1.4
