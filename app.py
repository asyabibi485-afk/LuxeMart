import streamlit as st
from supabase import create_client, Client

# ============================================================
# LUXEMART — MODERN LUXURY E-COMMERCE
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

@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)


try:
    supabase = get_supabase()
    supabase_connected = True
except Exception as e:
    supabase = None
    supabase_connected = False
    supabase_error = str(e)


# ============================================================
# SETTINGS
# ============================================================

ADMIN_EMAIL = st.secrets["admin"]["email"]

CONTACT_PHONE = "03169707804"
CONTACT_EMAIL = "asyabibi485@gmail.com"


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
        "description": "Soft and elegant scarf designed for a sophisticated style.",
    },
    {
        "id": 3,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
        "description": "Elegant flowing abaya with a timeless luxury appearance.",
    },
    {
        "id": 4,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
        "description": "Premium lawn suit perfect for stylish everyday wear.",
    },
    {
        "id": 5,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
        "description": "Graceful evening dress for special occasions.",
    },
    {
        "id": 6,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
        "description": "Comfortable and fashionable casual kurti.",
    },
    {
        "id": 7,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "icon": "📿",
        "description": "Classic pearl-inspired necklace with an elegant finish.",
    },
    {
        "id": 8,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "icon": "💎",
        "description": "Beautiful crystal bracelet for a refined look.",
    },
    {
        "id": 9,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "icon": "⌚",
        "description": "Classic gold-style watch with a premium appearance.",
    },
    {
        "id": 10,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "icon": "🕶️",
        "description": "Modern sunglasses designed to complete your look.",
    },
    {
        "id": 11,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
        "description": "Romantic rose fragrance with a luxurious character.",
    },
    {
        "id": 12,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
        "description": "Rich oud-inspired fragrance with a royal feel.",
    },
    {
        "id": 13,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
        "description": "Smooth vanilla fragrance with a warm and sweet character.",
    },
    {
        "id": 14,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "icon": "💄",
        "description": "Stylish makeup collection for your beauty routine.",
    },
]


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

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None

if "search" not in st.session_state:
    st.session_state.search = ""


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"Rs. {value:,.0f}"


def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def add_to_cart(product_id):
    st.session_state.cart.append(product_id)


def remove_from_cart(index):
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
    else:
        st.session_state.favorites.append(product_id)


def cart_total():
    total = 0

    for product_id in st.session_state.cart:
        product = get_product(product_id)

        if product:
            total += product["price"]

    return total


def show_message(message, kind="success"):
    if kind == "success":
        st.success(message)
    elif kind == "error":
        st.error(message)
    else:
        st.info(message)


# ============================================================
# CSS
# ============================================================

css = [
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 5%, rgba(224, 213, 255, 0.45), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(245, 225, 242, 0.50), transparent 30%),
            #fbfaff;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.3rem;
        padding-bottom: 3rem;
    }

    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 2.1rem;
        font-weight: 700;
        letter-spacing: 3px;
        color: #292235;
        margin-bottom: 0;
    }

    .tagline {
        color: #81788f;
        font-size: 0.78rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero {
        padding: 55px 45px;
        border-radius: 30px;
        background:
            linear-gradient(135deg, rgba(255,255,255,0.95), rgba(244,239,255,0.95));
        border: 1px solid rgba(255,255,255,0.9);
        box-shadow: 0 20px 60px rgba(75, 58, 100, 0.10);
        margin: 20px 0 35px 0;
    }

    .hero-small {
        color: #8d8298;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 0.75rem;
        font-weight: 700;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        color: #28202f;
        font-size: clamp(2.4rem, 6vw, 5rem);
        line-height: 1;
        margin: 12px 0;
        font-weight: 700;
    }

    .hero-text {
        color: #716878;
        max-width: 620px;
        font-size: 1rem;
        line-height: 1.8;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        color: #302637;
        font-size: 2rem;
        font-weight: 600;
        margin: 25px 0 5px 0;
    }

    .product-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid #eee8f5;
        border-radius: 23px;
        padding: 22px;
        min-height: 330px;
        box-shadow: 0 12px 35px rgba(70, 50, 90, 0.07);
        transition: 0.25s ease;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 42px rgba(70, 50, 90, 0.13);
    }

    .product-icon {
        height: 135px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #f8f4ff, #fff7fb);
        border-radius: 18px;
        font-size: 4.4rem;
        margin-bottom: 17px;
    }

    .product-category {
        color: #a18eae;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    .product-name {
        color: #302637;
        font-family: 'Playfair Display', serif;
        font-size: 1.18rem;
        font-weight: 600;
        margin-top: 5px;
    }

    .product-price {
        color: #6d587c;
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 7px;
    }

    .product-description {
        color: #918895;
        font-size: 0.82rem;
        line-height: 1.5;
        min-height: 50px;
    }

    .info-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid #eee8f5;
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 12px 35px rgba(70,50,90,0.07);
    }

    .footer {
        text-align: center;
        color: #9990a2;
        padding: 35px 10px 10px 10px;
        font-size: 0.8rem;
    }

    div.stButton > button {
        border-radius: 13px;
        border: 1px solid #e4dced;
        background: linear-gradient(135deg, #ffffff, #f5f0ff);
        color: #4b3b57;
        font-weight: 600;
        min-height: 42px;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        border-color: #cdbbe0;
        background: #eee7ff;
        color: #382c43;
    }

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 13px !important;
        border-color: #e4dced !important;
        background: #ffffff !important;
    }

    .cart-total {
        background: linear-gradient(135deg, #f5efff, #fff7fb);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #e8def0;
    }

    .cart-total-label {
        color: #8d8298;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .cart-total-price {
        color: #34283d;
        font-family: 'Playfair Display', serif;
        font-size: 2.3rem;
        font-weight: 700;
        margin-top: 5px;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 35px 22px;
        }

        .product-card {
            min-height: auto;
        }
    }
    </style>
    """
]

st.markdown("\n".join(css), unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

top_left, top_right = st.columns([2.3, 3])

with top_left:
    st.markdown(
        '<div class="brand">LUXEMART</div>'
        '<div class="tagline">Luxury • Beauty • Fashion</div>',
        unsafe_allow_html=True,
    )

with top_right:
    nav1, nav2, nav3, nav4 = st.columns(4)

    with nav1:
        if st.button("Shop", use_container_width=True):
            st.session_state.page = "Shop"
            st.rerun()

    with nav2:
        if st.button(
            f"♡ Favorites ({len(st.session_state.favorites)})",
            use_container_width=True,
        ):
            st.session_state.page = "Favorites"
            st.rerun()

    with nav3:
        if st.button(
            f"Bag ({len(st.session_state.cart)})",
            use_container_width=True,
        ):
            st.session_state.page = "Cart"
            st.rerun()

    with nav4:
        if st.button("Admin", use_container_width=True):
            st.session_state.page = "Admin"
            st.rerun()


st.divider()


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-small">New Collection 2026</div>
            <div class="hero-title">Luxury made<br>beautifully simple.</div>
            <div class="hero-text">
                Discover curated fashion, clothes, jewellery, accessories,
                perfume and beauty essentials — all in one elegant place.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Explore the collection</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col = st.columns([2, 1])

    with search_col:
        search = st.text_input(
            "Search",
            value=st.session_state.search,
            placeholder="Search products...",
            label_visibility="collapsed",
        )
        st.session_state.search = search

    with category_col:
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
            index=categories.index(st.session_state.category),
            label_visibility="collapsed",
        )

        st.session_state.category = category

    filtered_products = PRODUCTS

    if category != "All":
        filtered_products = [
            p for p in filtered_products
            if p["category"] == category
        ]

    if search.strip():
        search_lower = search.lower()

        filtered_products = [
            p for p in filtered_products
            if search_lower in p["name"].lower()
            or search_lower in p["category"].lower()
            or search_lower in p["description"].lower()
        ]

    st.write("")

    if not filtered_products:
        st.info("No products found. Try another search.")
    else:

        for start in range(0, len(filtered_products), 4):

            row_products = filtered_products[start:start + 4]

            cols = st.columns(4)

            for col, product in zip(cols, row_products):

                with col:

                    favorite_symbol = (
                        "♥"
                        if product["id"] in st.session_state.favorites
                        else "♡"
                    )

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

                            <div class="product-description">
                                {product["description"]}
                            </div>

                            <div class="product-price">
                                {money(product["price"])}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    b1, b2 = st.columns(2)

                    with b1:
                        if st.button(
                            "Add to Bag",
                            key=f"cart_{product['id']}",
                            use_container_width=True,
                        ):
                            add_to_cart(product["id"])
                            st.success("Added!")

                    with b2:
                        if st.button(
                            favorite_symbol,
                            key=f"fav_{product['id']}",
                            use_container_width=True,
                        ):
                            toggle_favorite(product["id"])
                            st.rerun()


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="section-title">Your Favorites</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.favorites:
        st.info("Your favorites are empty.")

        if st.button("Browse Collection"):
            st.session_state.page = "Shop"
            st.rerun()

    else:

        favorite_products = [
            get_product(pid)
            for pid in st.session_state.favorites
        ]

        favorite_products = [
            p for p in favorite_products
            if p is not None
        ]

        for start in range(0, len(favorite_products), 4):

            row_products = favorite_products[start:start + 4]

            cols = st.columns(4)

            for col, product in zip(cols, row_products):

                with col:

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
                                {money(product["price"])}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    if st.button(
                        "Remove Favorite",
                        key=f"remove_fav_{product['id']}",
                        use_container_width=True,
                    ):
                        st.session_state.favorites.remove(product["id"])
                        st.rerun()


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="section-title">Your Shopping Bag</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:
        st.info("Your shopping bag is empty.")

        if st.button("Continue Shopping"):
            st.session_state.page = "Shop"
            st.rerun()

    else:

        for index, product_id in enumerate(st.session_state.cart):

            product = get_product(product_id)

            if not product:
                continue

            c1, c2, c3, c4 = st.columns([0.8, 3, 1.2, 1])

            with c1:
                st.markdown(
                    f"<div style='font-size:2rem'>{product['icon']}</div>",
                    unsafe_allow_html=True,
                )

            with c2:
                st.markdown(f"**{product['name']}**")
                st.caption(product["category"])

            with c3:
                st.markdown(f"**{money(product['price'])}**")

            with c4:
                if st.button(
                    "Remove",
import streamlit as st
from supabase import create_client, Client

# ============================================================
# LUXEMART — MODERN LUXURY E-COMMERCE
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

@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)


try:
    supabase = get_supabase()
    supabase_connected = True
except Exception as e:
    supabase = None
    supabase_connected = False
    supabase_error = str(e)


# ============================================================
# SETTINGS
# ============================================================

ADMIN_EMAIL = st.secrets["admin"]["email"]

CONTACT_PHONE = "03169707804"
CONTACT_EMAIL = "asyabibi485@gmail.com"


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
        "description": "Soft and elegant scarf designed for a sophisticated style.",
    },
    {
        "id": 3,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
        "description": "Elegant flowing abaya with a timeless luxury appearance.",
    },
    {
        "id": 4,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
        "description": "Premium lawn suit perfect for stylish everyday wear.",
    },
    {
        "id": 5,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
        "description": "Graceful evening dress for special occasions.",
    },
    {
        "id": 6,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
        "description": "Comfortable and fashionable casual kurti.",
    },
    {
        "id": 7,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "icon": "📿",
        "description": "Classic pearl-inspired necklace with an elegant finish.",
    },
    {
        "id": 8,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "icon": "💎",
        "description": "Beautiful crystal bracelet for a refined look.",
    },
    {
        "id": 9,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "icon": "⌚",
        "description": "Classic gold-style watch with a premium appearance.",
    },
    {
        "id": 10,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "icon": "🕶️",
        "description": "Modern sunglasses designed to complete your look.",
    },
    {
        "id": 11,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
        "description": "Romantic rose fragrance with a luxurious character.",
    },
    {
        "id": 12,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
        "description": "Rich oud-inspired fragrance with a royal feel.",
    },
    {
        "id": 13,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
        "description": "Smooth vanilla fragrance with a warm and sweet character.",
    },
    {
        "id": 14,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "icon": "💄",
        "description": "Stylish makeup collection for your beauty routine.",
    },
]


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

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None

if "search" not in st.session_state:
    st.session_state.search = ""


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"Rs. {value:,.0f}"


def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def add_to_cart(product_id):
    st.session_state.cart.append(product_id)


def remove_from_cart(index):
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
    else:
        st.session_state.favorites.append(product_id)


def cart_total():
    total = 0

    for product_id in st.session_state.cart:
        product = get_product(product_id)

        if product:
            total += product["price"]

    return total


def show_message(message, kind="success"):
    if kind == "success":
        st.success(message)
    elif kind == "error":
        st.error(message)
    else:
        st.info(message)


# ============================================================
# CSS
# ============================================================

css = [
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 5%, rgba(224, 213, 255, 0.45), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(245, 225, 242, 0.50), transparent 30%),
            #fbfaff;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.3rem;
        padding-bottom: 3rem;
    }

    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 2.1rem;
        font-weight: 700;
        letter-spacing: 3px;
        color: #292235;
        margin-bottom: 0;
    }

    .tagline {
        color: #81788f;
        font-size: 0.78rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero {
        padding: 55px 45px;
        border-radius: 30px;
        background:
            linear-gradient(135deg, rgba(255,255,255,0.95), rgba(244,239,255,0.95));
        border: 1px solid rgba(255,255,255,0.9);
        box-shadow: 0 20px 60px rgba(75, 58, 100, 0.10);
        margin: 20px 0 35px 0;
    }

    .hero-small {
        color: #8d8298;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 0.75rem;
        font-weight: 700;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        color: #28202f;
        font-size: clamp(2.4rem, 6vw, 5rem);
        line-height: 1;
        margin: 12px 0;
        font-weight: 700;
    }

    .hero-text {
        color: #716878;
        max-width: 620px;
        font-size: 1rem;
        line-height: 1.8;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        color: #302637;
        font-size: 2rem;
        font-weight: 600;
        margin: 25px 0 5px 0;
    }

    .product-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid #eee8f5;
        border-radius: 23px;
        padding: 22px;
        min-height: 330px;
        box-shadow: 0 12px 35px rgba(70, 50, 90, 0.07);
        transition: 0.25s ease;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 42px rgba(70, 50, 90, 0.13);
    }

    .product-icon {
        height: 135px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #f8f4ff, #fff7fb);
        border-radius: 18px;
        font-size: 4.4rem;
        margin-bottom: 17px;
    }

    .product-category {
        color: #a18eae;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    .product-name {
        color: #302637;
        font-family: 'Playfair Display', serif;
        font-size: 1.18rem;
        font-weight: 600;
        margin-top: 5px;
    }

    .product-price {
        color: #6d587c;
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 7px;
    }

    .product-description {
        color: #918895;
        font-size: 0.82rem;
        line-height: 1.5;
        min-height: 50px;
    }

    .info-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid #eee8f5;
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 12px 35px rgba(70,50,90,0.07);
    }

    .footer {
        text-align: center;
        color: #9990a2;
        padding: 35px 10px 10px 10px;
        font-size: 0.8rem;
    }

    div.stButton > button {
        border-radius: 13px;
        border: 1px solid #e4dced;
        background: linear-gradient(135deg, #ffffff, #f5f0ff);
        color: #4b3b57;
        font-weight: 600;
        min-height: 42px;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        border-color: #cdbbe0;
        background: #eee7ff;
        color: #382c43;
    }

    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 13px !important;
        border-color: #e4dced !important;
        background: #ffffff !important;
    }

    .cart-total {
        background: linear-gradient(135deg, #f5efff, #fff7fb);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
        border: 1px solid #e8def0;
    }

    .cart-total-label {
        color: #8d8298;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .cart-total-price {
        color: #34283d;
        font-family: 'Playfair Display', serif;
        font-size: 2.3rem;
        font-weight: 700;
        margin-top: 5px;
    }

    @media (max-width: 700px) {
        .hero {
            padding: 35px 22px;
        }

        .product-card {
            min-height: auto;
        }
    }
    </style>
    """
]

st.markdown("\n".join(css), unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

top_left, top_right = st.columns([2.3, 3])

with top_left:
    st.markdown(
        '<div class="brand">LUXEMART</div>'
        '<div class="tagline">Luxury • Beauty • Fashion</div>',
        unsafe_allow_html=True,
    )

with top_right:
    nav1, nav2, nav3, nav4 = st.columns(4)

    with nav1:
        if st.button("Shop", use_container_width=True):
            st.session_state.page = "Shop"
            st.rerun()

    with nav2:
        if st.button(
            f"♡ Favorites ({len(st.session_state.favorites)})",
            use_container_width=True,
        ):
            st.session_state.page = "Favorites"
            st.rerun()

    with nav3:
        if st.button(
            f"Bag ({len(st.session_state.cart)})",
            use_container_width=True,
        ):
            st.session_state.page = "Cart"
            st.rerun()

    with nav4:
        if st.button("Admin", use_container_width=True):
            st.session_state.page = "Admin"
            st.rerun()


st.divider()


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-small">New Collection 2026</div>
            <div class="hero-title">Luxury made<br>beautifully simple.</div>
            <div class="hero-text">
                Discover curated fashion, clothes, jewellery, accessories,
                perfume and beauty essentials — all in one elegant place.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Explore the collection</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col = st.columns([2, 1])

    with search_col:
        search = st.text_input(
            "Search",
            value=st.session_state.search,
            placeholder="Search products...",
            label_visibility="collapsed",
        )
        st.session_state.search = search

    with category_col:
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
            index=categories.index(st.session_state.category),
            label_visibility="collapsed",
        )

        st.session_state.category = category

    filtered_products = PRODUCTS

    if category != "All":
        filtered_products = [
            p for p in filtered_products
            if p["category"] == category
        ]

    if search.strip():
        search_lower = search.lower()

        filtered_products = [
            p for p in filtered_products
            if search_lower in p["name"].lower()
            or search_lower in p["category"].lower()
            or search_lower in p["description"].lower()
        ]

    st.write("")

    if not filtered_products:
        st.info("No products found. Try another search.")
    else:

        for start in range(0, len(filtered_products), 4):

            row_products = filtered_products[start:start + 4]

            cols = st.columns(4)

            for col, product in zip(cols, row_products):

                with col:

                    favorite_symbol = (
                        "♥"
                        if product["id"] in st.session_state.favorites
                        else "♡"
                    )

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

                            <div class="product-description">
                                {product["description"]}
                            </div>

                            <div class="product-price">
                                {money(product["price"])}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    b1, b2 = st.columns(2)

                    with b1:
                        if st.button(
                            "Add to Bag",
                            key=f"cart_{product['id']}",
                            use_container_width=True,
                        ):
                            add_to_cart(product["id"])
                            st.success("Added!")

                    with b2:
                        if st.button(
                            favorite_symbol,
                            key=f"fav_{product['id']}",
                            use_container_width=True,
                        ):
                            toggle_favorite(product["id"])
                            st.rerun()


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="section-title">Your Favorites</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.favorites:
        st.info("Your favorites are empty.")

        if st.button("Browse Collection"):
            st.session_state.page = "Shop"
            st.rerun()

    else:

        favorite_products = [
            get_product(pid)
            for pid in st.session_state.favorites
        ]

        favorite_products = [
            p for p in favorite_products
            if p is not None
        ]

        for start in range(0, len(favorite_products), 4):

            row_products = favorite_products[start:start + 4]

            cols = st.columns(4)

            for col, product in zip(cols, row_products):

                with col:

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
                                {money(product["price"])}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    if st.button(
                        "Remove Favorite",
                        key=f"remove_fav_{product['id']}",
                        use_container_width=True,
                    ):
                        st.session_state.favorites.remove(product["id"])
                        st.rerun()


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="section-title">Your Shopping Bag</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:
        st.info("Your shopping bag is empty.")

        if st.button("Continue Shopping"):
            st.session_state.page = "Shop"
            st.rerun()

    else:

        for index, product_id in enumerate(st.session_state.cart):

            product = get_product(product_id)

            if not product:
                continue

            c1, c2, c3, c4 = st.columns([0.8, 3, 1.2, 1])

            with c1:
                st.markdown(
                    f"<div style='font-size:2rem'>{product['icon']}</div>",
                    unsafe_allow_html=True,
                )

            with c2:
                st.markdown(f"**{product['name']}**")
                st.caption(product["category"])

            with c3:
                st.markdown(f"**{money(product['price'])}**")

            with c4:
                if st.button(
                    "Remove",
                    key=f"remove_cart_{index}",
                    use_container_width=True,
                ):
                    remove_from_cart(index)
                    st.rerun()

            st.divider()

        total = cart_total()

        st.markdown(
            f"""
            <div class="cart-total">
                <div class="cart-total-label">Order Total</div>
                <div class="cart-total-price">{money(total)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        st.markdown("### Checkout")

        name = st.text_input(
            "Customer Name",
            placeholder="Enter your name",
        )

        email = st.text_input(
            "Email",
            placeholder="Enter your email",
        )

        phone = st.text_input(
            "Phone",
            value=CONTACT_PHONE,
        )

        address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete delivery address",
        )

        if st.button(
            "Place Order",
            type="primary",
            use_container_width=True,
        ):

            if not name.strip():
                st.error("Please enter your name.")

            elif not email.strip():
                st.error("Please enter your email.")

            elif not phone.strip():
                st.error("Please enter your phone number.")

            elif not address.strip():
                st.error("Please enter your delivery address.")

            elif not supabase_connected:
                st.error(
                    "Supabase connection failed. Please check your Streamlit Secrets."
                )

            else:

                order_items = []

                for product_id in st.session_state.cart:

                    product = get_product(product_id)

                    if product:
                        order_items.append(
                            {
                                "id": product["id"],
                                "name": product["name"],
                                "category": product["category"],
                                "price": product["price"],
                            }
                        )

                order_data = {
                    "customer_name": name.strip(),
                    "customer_email": email.strip(),
                    "phone": phone.strip(),
                    "address": address.strip(),
                    "items": order_items,
                    "total": total,
                    "status": "Pending",
                }

                try:

                    result = (
                        supabase
                        .table("orders")
                        .insert(order_data)
                        .execute()
                    )

                    if result.data:

                        st.success(
                            "🎉 Order placed successfully! "
                            "Thank you for shopping with LUXEMART."
                        )

                        st.session_state.cart = []

                        st.balloons()

                    else:
                        st.error("Order could not be created.")

                except Exception as e:

                    st.error(
                        "Order error. Please check your Supabase orders "
                        "table and Row Level Security policy."
                    )

                    st.code(str(e))


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.markdown(
        '<div class="section-title">Admin Dashboard</div>',
        unsafe_allow_html=True,
    )

    if st.session_state.admin_user:

        user_email = st.session_state.admin_user.get(
            "email",
            ADMIN_EMAIL,
        )

        st.markdown(
            f"""
            <div class="info-card">
                <h3>Welcome to LUXEMART Admin</h3>
                <p>
                    Logged in as <b>{user_email}</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        if st.button(
            "Logout",
            use_container_width=True,
        ):

            try:
                supabase.auth.sign_out()
            except Exception:
                pass

            st.session_state.admin_user = None
            st.rerun()

        st.write("")

        st.markdown("### Store Overview")

        a1, a2, a3 = st.columns(3)

        with a1:
            st.metric(
                "Products",
                len(PRODUCTS),
            )

        with a2:
            st.metric(
                "Categories",
                6,
            )

        with a3:
            st.metric(
                "Cart Items",
                len(st.session_state.cart),
            )

        st.info(
            "Admin authentication is handled through Supabase Auth. "
            "The configured admin email is used to restrict dashboard access."
        )

    else:

        st.markdown(
            """
            <div class="info-card">
                <h3>Secure Admin Login</h3>
                <p>
                    Sign in using your Supabase Auth account.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        login_email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email",
        )

        login_password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password",
        )

        if st.button(
            "Login to Admin",
            use_container_width=True,
        ):

            if not login_email.strip():
                st.error("Please enter your email.")

            elif not login_password:
                st.error("Please enter your password.")

            elif login_email.strip().lower() != ADMIN_EMAIL.lower():
                st.error("This email is not authorized for admin access.")

            elif not supabase_connected:
                st.error(
                    "Supabase connection failed. Check your Streamlit Secrets."
                )

            else:

                try:

                    response = supabase.auth.sign_in_with_password(
                        {
                            "email": login_email.strip(),
                            "password": login_password,
                        }
                    )

                    if response.user:

                        st.session_state.admin_user = {
                            "id": response.user.id,
                            "email": response.user.email,
                        }

                        st.success("Login successful.")
                        st.rerun()

                    else:
                        st.error("Login failed.")

                except Exception as e:

                    st.error(
                        "Login failed. Check your Supabase Auth email "
                        "and password."
                    )

                    st.code(str(e))


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.markdown(
        '<div class="section-title">About LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
            <h2>LUXEMART</h2>

            <p>
                Welcome to LUXEMART — a modern destination for fashion,
                clothes, jewellery, accessories, perfume and beauty.
            </p>

            <p>
                Our goal is to make online shopping feel elegant,
                simple and enjoyable.
            </p>

            <p>
                Discover carefully selected products and enjoy a beautiful
                shopping experience from anywhere.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CONTACT
# ============================================================

elif st.session_state.page == "Contact":

    st.markdown(
        '<div class="section-title">Contact LUXEMART</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"""
            <div class="info-card">
                <h3>📞 Phone</h3>
                <p>{CONTACT_PHONE}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="info-card">
                <h3>✉️ Email</h3>
                <p>{CONTACT_EMAIL}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# FOOTER NAVIGATION
# ============================================================

st.write("")
st.divider()

f1, f2, f3, f4 = st.columns(4)

with f1:
    if st.button("Shop", key="footer_shop", use_container_width=True):
        st.session_state.page = "Shop"
        st.rerun()

with f2:
    if st.button("About", key="footer_about", use_container_width=True):
        st.session_state.page = "About"
        st.rerun()

with f3:
    if st.button("Contact", key="footer_contact", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()

with f4:
    if st.button("Admin", key="footer_admin", use_container_width=True):
        st.session_state.page = "Admin"
        st.rerun()

st.markdown(
    f"""
    <div class="footer">
        © 2026 LUXEMART · Luxury • Beauty • Fashion<br>
        {CONTACT_PHONE} · {CONTACT_EMAIL}
    </div>
    """,
    unsafe_allow_html=True,
)




















        
