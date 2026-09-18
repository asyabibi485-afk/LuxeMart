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
# SUPABASE
# ============================================================

try:
    from supabase import create_client
except Exception:
    create_client = None


@st.cache_resource
def get_supabase():
    if create_client is None:
        return None

    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        return create_client(url, key)
    except Exception:
        return None


supabase = get_supabase()

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None


# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Velvet Luxe Handbag",
        "category": "Fashion",
        "price": 3499,
        "icon": "👜",
        "description": "Elegant everyday handbag with a premium luxury look.",
    },
    {
        "id": 2,
        "name": "Silk Evening Scarf",
        "category": "Fashion",
        "price": 1599,
        "icon": "🧣",
        "description": "Soft silk-inspired scarf designed for an elegant finish.",
    },
    {
        "id": 3,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
        "description": "Elegant flowing abaya with a sophisticated luxury style.",
    },
    {
        "id": 4,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
        "description": "Beautiful premium lawn outfit designed for everyday elegance.",
    },
    {
        "id": 5,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
        "description": "Stylish evening dress for parties and special occasions.",
    },
    {
        "id": 6,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
        "description": "Comfortable and fashionable kurti for everyday wear.",
    },
    {
        "id": 7,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "icon": "📿",
        "description": "Classic pearl-inspired jewellery for timeless elegance.",
    },
    {
        "id": 8,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "icon": "💎",
        "description": "Sparkling bracelet inspired by modern luxury jewellery.",
    },
    {
        "id": 9,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "icon": "⌚",
        "description": "Sophisticated watch design for a polished appearance.",
    },
    {
        "id": 10,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "icon": "🕶️",
        "description": "Modern sunglasses with a refined luxury aesthetic.",
    },
    {
        "id": 11,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
        "description": "Elegant rose fragrance with a soft luxurious character.",
    },
    {
        "id": 12,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
        "description": "Rich oud-inspired fragrance for a sophisticated presence.",
    },
    {
        "id": 13,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
        "description": "Smooth vanilla-inspired fragrance with a warm character.",
    },
    {
        "id": 14,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "icon": "💄",
        "description": "A stylish beauty collection for your daily routine.",
    },
]


# ============================================================
# LUXURY CSS
# ============================================================

CSS = "\n".join(
    [
        "<style>",
        "html, body, [class*='css'] {",
        "    font-family: Inter, Arial, sans-serif;",
        "}",
        "",
        ".stApp {",
        "    background: linear-gradient(135deg, #fbfaff 0%, #f5f0ff 48%, #ffffff 100%);",
        "}",
        "",
        "#MainMenu { visibility: hidden; }",
        "header { visibility: hidden; }",
        "footer { visibility: hidden; }",
        "",
        ".block-container {",
        "    max-width: 1250px;",
        "    padding-top: 2rem;",
        "    padding-bottom: 4rem;",
        "}",
        "",
        ".brand-title {",
        "    text-align: center;",
        "    font-size: 3.2rem;",
        "    font-weight: 900;",
        "    letter-spacing: 0.18em;",
        "    color: #241d35;",
        "    margin-bottom: 4px;",
        "}",
        "",
        ".brand-tagline {",
        "    text-align: center;",
        "    color: #8c819d;",
        "    font-size: 0.9rem;",
        "    letter-spacing: 0.14em;",
        "    margin-bottom: 28px;",
        "}",
        "",
        ".hero {",
        "    background: linear-gradient(135deg, #ffffff, #f0eaff);",
        "    border: 1px solid #e5dcf4;",
        "    border-radius: 28px;",
        "    padding: 42px 36px;",
        "    margin: 18px 0 30px 0;",
        "    box-shadow: 0 18px 50px rgba(80, 55, 110, 0.08);",
        "}",
        "",
        ".hero-label {",
        "    color: #806ca8;",
        "    font-size: 0.78rem;",
        "    font-weight: 800;",
        "    letter-spacing: 0.17em;",
        "    text-transform: uppercase;",
        "}",
        "",
        ".hero-title {",
        "    color: #241d30;",
        "    font-size: 2.7rem;",
        "    font-weight: 900;",
        "    line-height: 1.1;",
        "    margin: 12px 0;",
        "}",
        "",
        ".hero-text {",
        "    color: #746a80;",
        "    max-width: 680px;",
        "    line-height: 1.7;",
        "}",
        "",
        ".section-title {",
        "    color: #292132;",
        "    font-size: 1.7rem;",
        "    font-weight: 900;",
        "    margin: 24px 0 8px 0;",
        "}",
        "",
        ".section-subtitle {",
        "    color: #92869e;",
        "    margin-bottom: 20px;",
        "}",
        "",
        ".product-card {",
        "    background: #ffffff;",
        "    border: 1px solid #eae2f1;",
        "    border-radius: 22px;",
        "    padding: 18px;",
        "    margin-bottom: 12px;",
        "    min-height: 275px;",
        "    box-shadow: 0 10px 30px rgba(50, 35, 70, 0.06);",
        "}",
        "",
        ".product-icon {",
        "    height: 115px;",
        "    border-radius: 18px;",
        "    background: linear-gradient(135deg, #f7f3ff, #eee7ff);",
        "    display: flex;",
        "    justify-content: center;",
        "    align-items: center;",
        "    font-size: 3.6rem;",
        "    margin-bottom: 14px;",
        "}",
        "",
        ".product-category {",
        "    color: #988da5;",
        "    font-size: 0.72rem;",
        "    font-weight: 800;",
        "    text-transform: uppercase;",
        "    letter-spacing: 0.1em;",
        "}",
        "",
        ".product-name {",
        "    color: #292132;",
        "    font-size: 1.02rem;",
        "    font-weight: 850;",
        "    margin-top: 4px;",
        "}",
        "",
        ".product-price {",
        "    color: #684fa1;",
        "    font-size: 1.18rem;",
        "    font-weight: 900;",
        "    margin-top: 7px;",
        "}",
        "",
        ".info-card {",
        "    background: #ffffff;",
        "    border: 1px solid #e8e0ef;",
        "    border-radius: 24px;",
        "    padding: 28px;",
        "    box-shadow: 0 12px 35px rgba(50, 35, 70, 0.06);",
        "}",
        "",
        ".admin-card {",
        "    background: linear-gradient(135deg, #ffffff, #f3edff);",
        "    border: 1px solid #e2d7f2;",
        "    border-radius: 25px;",
        "    padding: 30px;",
        "    box-shadow: 0 15px 40px rgba(70, 50, 100, 0.08);",
        "}",
        "",
        "div.stButton > button {",
        "    min-height: 44px !important;",
        "    border-radius: 14px !important;",
        "    font-weight: 800 !important;",
        "    background: #f3efff !important;",
        "    color: #554477 !important;",
        "    border: 1px solid #ddd2f0 !important;",
        "    box-shadow: 0 5px 15px rgba(103, 77, 165, 0.07) !important;",
        "    transition: 0.2s ease !important;",
        "}",
        "",
        "div.stButton > button:hover {",
        "    background: #e8dfff !important;",
        "    color: #60469d !important;",
        "    border-color: #cdbdea !important;",
        "    transform: translateY(-2px);",
        "}",
        "",
        "div.stButton > button[kind='primary'] {",
        "    background: #ece4ff !important;",
        "    color: #58429a !important;",
        "    border-color: #d5c6f0 !important;",
        "}",
        "",
        ".stTextInput input, .stTextArea textarea {",
        "    border-radius: 13px !important;",
        "    border: 1px solid #ddd5e8 !important;",
        "    background: #ffffff !important;",
        "}",
        "",
        ".footer {",
        "    text-align: center;",
        "    color: #978ca4;",
        "    padding-top: 40px;",
        "    font-size: 0.85rem;",
        "}",
        "",
        "@media (max-width: 700px) {",
        "    .brand-title { font-size: 2rem; }",
        "    .hero { padding: 28px 20px; }",
        "    .hero-title { font-size: 2rem; }",
        "}",
        "</style>",
    ]
)

st.markdown(CSS, unsafe_allow_html=True)


# ============================================================
# FUNCTIONS
# ============================================================

def go_to(page):
    st.session_state.page = page
    st.rerun()


def add_to_cart(product_id):
    st.session_state.cart.append(product_id)
    st.toast("Added to cart ✦")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ♡")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="brand-title">LUXEMART</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="brand-tagline">Luxury • Style • Everyday Elegance</div>',
    unsafe_allow_html=True,
)


# ============================================================
# MAIN NAVIGATION
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:
    if st.button(
        "⌂  Shop",
        use_container_width=True,
        type="primary" if st.session_state.page == "Shop" else "secondary",
    ):
        go_to("Shop")

with c2:
    if st.button(
        f"♡  Favorites ({len(st.session_state.favorites)})",
        use_container_width=True,
        type="primary"
        if st.session_state.page == "Favorites"
        else "secondary",
    ):
        go_to("Favorites")

with c3:
    if st.button(
        f"🛒  Cart ({len(st.session_state.cart)})",
        use_container_width=True,
        type="primary" if st.session_state.page == "Cart" else "secondary",
    ):
        go_to("Cart")


st.markdown(
    "<hr style='border:0;border-top:1px solid #e5deeb;margin:25px 0;'>",
    unsafe_allow_html=True,
)


# ============================================================
# SECOND NAVIGATION
# ============================================================

c4, c5, c6 = st.columns(3)

with c4:
    if st.button(
        "✦ About",
        use_container_width=True,
        type="primary" if st.session_state.page == "About" else "secondary",
    ):
        go_to("About")

with c5:
    if st.button(
        "✉ Contact",
        use_container_width=True,
        type="primary" if st.session_state.page == "Contact" else "secondary",
    ):
        go_to("Contact")

with c6:
    if st.button(
        "♙ Admin",
        use_container_width=True,
        type="primary" if st.session_state.page == "Admin" else "secondary",
    ):
        go_to("Admin")


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-label">LUXEMART COLLECTION</div>
            <div class="hero-title">Elevate Your Everyday Style.</div>
            <div class="hero-text">
                Discover elegant clothes, beautiful perfumes, jewellery,
                fashion pieces, accessories and beauty essentials.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Explore Collection</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">Curated pieces for your luxury lifestyle.</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search",
        placeholder="Search clothes, perfume, jewellery...",
    )

    categories = [
        "All",
        "Clothes",
        "Fashion",
        "Jewellery",
        "Accessories",
        "Perfume",
        "Beauty",
    ]

    category = st.selectbox(
        "Category",
        categories,
    )

    filtered_products = PRODUCTS

    if search.strip():
        query = search.lower().strip()

        filtered_products = [
            product
            for product in filtered_products
            if query in product["name"].lower()
            or query in product["category"].lower()
            or query in product["description"].lower()
        ]

    if category != "All":
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    if not filtered_products:

        st.info("No products found. Try another search.")

    else:

        product_columns = st.columns(4)

        for index, product in enumerate(filtered_products):

            with product_columns[index % 4]:

                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="product-icon">
                            {product["icon"]}
                        </div>

                        <div class="product-category">
                            {product["category"]}
                        </div>

                        <div class="product-name">
                            {product["name"]}
                        </div>

                        <div class="product-price">
                            Rs. {product["price"]:,}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                b1
