import streamlit as st
from supabase import create_client


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="LUXEMART",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# SUPABASE CONFIG
# =========================================================
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
ADMIN_EMAIL = st.secrets["admin"]["email"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

if "slider_index" not in st.session_state:
    st.session_state.slider_index = 0


# =========================================================
# PRODUCTS
# =========================================================
PRODUCTS = [
    {
        "id": 1,
        "name": "Luxury Handbag",
        "category": "Fashion",
        "price": 5499,
        "image": "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "image": "https://images.pexels.com/photos/904350/pexels-photo-904350.jpeg",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "image": "https://images.pexels.com/photos/1454171/pexels-photo-1454171.jpeg",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "image": "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg",
    },
    {
        "id": 5,
        "name": "Gold Watch",
        "category": "Accessories",
        "price": 7999,
        "image": "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
    },
    {
        "id": 6,
        "name": "Classic Sunglasses",
        "category": "Accessories",
        "price": 2999,
        "image": "https://images.pexels.com/photos/46710/pexels-photo-46710.jpeg",
    },
    {
        "id": 7,
        "name": "Premium Makeup Set",
        "category": "Beauty",
        "price": 4499,
        "image": "https://images.pexels.com/photos/2533266/pexels-photo-2533266.jpeg",
    },
    {
        "id": 8,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "image": "images/luxury_abaya.jpg",
    },
    {
        "id": 9,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "image": "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    },
    {
        "id": 10,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
    },
    {
        "id": 11,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "image": "https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg",
    },
    {
        "id": 12,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "image": "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
    },
    {
        "id": 13,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "image": "https://images.pexels.com/photos/1190829/pexels-photo-1190829.jpeg",
    },
    {
        "id": 14,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "image": "https://images.pexels.com/photos/1961795/pexels-photo-1961795.jpeg",
    },
]


CATEGORIES = [
    "All",
    "Clothes",
    "Fashion",
    "Jewellery",
    "Accessories",
    "Perfume",
    "Beauty",
]


SLIDES = [
    "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    "https://images.pexels.com/photos/904350/pexels-photo-904350.jpeg",
    "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
    "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
]


# =========================================================
# HELPERS
# =========================================================
def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def money(amount):
    return f"Rs. {amount:,.0f}"


def cart_total():
    total = 0

    for product_id in st.session_state.cart:
        product = get_product(product_id)

        if product is not None:
            total += product["price"]

    return total


def go_to(page):
    st.session_state.page = page
    st.rerun()


def add_to_cart(product_id):
    if product_id not in st.session_state.cart:
        st.session_state.cart.append(product_id)
        st.toast("Added to cart 🛒")
    else:
        st.toast("Already in your cart")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


def logout_admin():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.admin_logged_in = False
    go_to("Shop")


# =========================================================
# TRENDY LUXURY CSS
# =========================================================
st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');


/* =====================================================
   GLOBAL
===================================================== */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 196, 218, 0.55), transparent 28%),
        radial-gradient(circle at 90% 5%, rgba(190, 190, 255, 0.45), transparent 28%),
        radial-gradient(circle at 80% 85%, rgba(174, 224, 255, 0.38), transparent 30%),
        linear-gradient(135deg, #fff4f8 0%, #f7f3ff 48%, #f1f9ff 100%);
    color: #111111;
    font-family: 'DM Sans', sans-serif;
}


/* =====================================================
   REMOVE STREAMLIT TOP SPACE
===================================================== */

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1450px;
}


/* =====================================================
   SIDEBAR
===================================================== */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(255, 236, 245, 0.98),
            rgba(240, 236, 255, 0.98),
            rgba(235, 248, 255, 0.98)
        );
    border-right: 1px solid rgba(255,255,255,0.9);
}


[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.2rem;
}


.luxemart-logo {
    white-space: nowrap;
    overflow: hidden;
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #17121c;
    text-align: center;
    margin-bottom: 4px;
}


.luxemart-subtitle {
    text-align: center;
    color: #77717c;
    font-size: 12px;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 25px;
}


/* =====================================================
   SIDEBAR BUTTONS
===================================================== */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.95);
    background: rgba(255,255,255,0.62);
    color: #161219;
    font-weight: 600;
    transition: all 0.25s ease;
}


[data-testid="stSidebar"] .stButton > button:hover {
    background: white;
    transform: translateX(3px);
    box-shadow: 0 8px 25px rgba(100,80,120,0.10);
}


/* =====================================================
   MAIN TITLES
===================================================== */

h1, h2, h3 {
    color: #151018 !important;
}


.luxury-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 5vw, 58px);
    line-height: 1.05;
    font-weight: 700;
    color: #17121b;
    margin-bottom: 8px;
}


.luxury-subtitle {
    color: #69616d;
    font-size: 16px;
    margin-bottom: 20px;
}


.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    font-weight: 600;
    margin: 25px 0 15px 0;
}


/* =====================================================
   WHITE TYPING AREAS
===================================================== */

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stNumberInput"] input {
    background: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #e5dfe8 !important;
    border-radius: 13px !important;
    box-shadow: 0 5px 20px rgba(70,50,90,0.05) !important;
}


div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border: 1px solid #c9a4d8 !important;
    box-shadow: 0 0 0 3px rgba(201,164,216,0.15) !important;
}


div[data-testid="stTextInput"] label,
div[data-testid="stTextArea"] label {
    color: #27212b !important;
    font-weight: 600 !important;
}


/* =====================================================
   SELECTBOX / SLIDER
===================================================== */

div[data-baseweb="select"] > div {
    background: white !important;
    border-radius: 13px !important;
    border: 1px solid #e5dfe8 !important;
}


[data-testid="stSlider"] {
    padding-top: 10px;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {
    border-radius: 13px;
    min-height: 42px;
    font-weight: 600;
    border: 1px solid rgba(220,210,225,0.9);
    background: white;
    color: #17131a;
    transition: all 0.25s ease;
}


.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(75,55,90,0.12);
    border-color: #cbb2d8;
}


.primary-button .stButton > button {
    background: #17131a;
    color: white;
}


/* =====================================================
   HERO
===================================================== */

.hero-wrapper {
    background: rgba(255,255,255,0.50);
    border: 1px solid rgba(255,255,255,0.9);
    border-radius: 28px;
    padding: 12px;
    box-shadow: 0 20px 60px rgba(80,60,100,0.10);
    backdrop-filter: blur(18px);
    margin-bottom: 25px;
}


.hero-image {
    width: 100%;
    height: 370px;
    object-fit: cover;
    border-radius: 21px;
    display: block;
}


/* =====================================================
   CATEGORY CHIPS
===================================================== */

.category-title {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    margin-bottom: 12px;
}


.category-chip {
    background: rgba(255,255,255,0.70);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 50px;
    padding: 9px 15px;
    text-align: center;
    font-size: 13px;
    font-weight: 600;
    color: #302936;
    box-shadow: 0 6px 20px rgba(80,60,100,0.05);
}


/* =====================================================
   PRODUCT CARDS
===================================================== */

.product-card {
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 22px;
    padding: 10px;
    margin-bottom: 18px;
    box-shadow: 0 12px 35px rgba(70,50,90,0.08);
    backdrop-filter: blur(12px);
    transition: all 0.25s ease;
}


.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 45px rgba(70,50,90,0.14);
}


.product-card img {
    width: 100%;
    height: 235px;
    object-fit: cover;
    border-radius: 17px;
}


.product-name {
    color: #19141c;
    font-size: 17px;
    font-weight: 700;
    margin-top: 11px;
}


.product-category {
    color: #887e8c;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 3px;
}


.product-price {
    color: #17121a;
    font-size: 18px;
    font-weight: 700;
    margin-top: 6px;
}


/* =====================================================
   INFO CARDS
===================================================== */

.info-card {
    background: rgba(255,255,255,0.78);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 12px 35px rgba(70,50,90,0.07);
    margin-bottom: 20px;
}


.info-card h3 {
    font-family: 'Playfair Display', serif;
    margin-top: 0;
}


/* =====================================================
   CART
===================================================== */

.cart-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 10px 30px rgba(70,50,90,0.07);
}


.total-card {
    background: #17131a;
    color: white;
    border-radius: 20px;
    padding: 22px;
    margin-top: 18px;
    box-shadow: 0 15px 35px rgba(30,20,40,0.18);
}


.total-card .total-label {
    color: #d8d0dc;
    font-size: 13px;
}


.total-card .total-value {
    font-size: 28px;
    font-weight: 700;
    margin-top: 3px;
}


/* =====================================================
   ADMIN
===================================================== */

.admin-card {
    background: rgba(255,255,255,0.86);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.95);
    box-shadow: 0 12px 35px rgba(70,50,90,0.08);
    margin-bottom: 18px;
}


/* =====================================================
   EXPANDERS
===================================================== */

[data-testid="stExpander"] {
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(255,255,255,0.9);
    border-radius: 16px;
}


/* =====================================================
   DIVIDERS
===================================================== */

hr {
    border: none;
    height: 1px;
    background: rgba(100,80,110,0.10);
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .hero-image {
        height: 250px;
    }

    .product-card img {
        height: 200px;
    }

    .luxury-title {
        font-size: 38px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown(
        """
        <div class="luxemart-logo">🛍️ LUXEMART</div>
        <div class="luxemart-subtitle">Premium Lifestyle Store</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Explore")

    if st.button("🏠  Shop", use_container_width=True):
        go_to("Shop")

    if st.button(
        f"❤️  Favorites ({len(st.session_state.favorites)})",
        use_container_width=True,
    ):
        go_to("Favorites")

    if st.button(
        f"🛒  Cart ({len(st.session_state.cart)})",
        use_container_width=True,
    ):
        go_to("Cart")

    if st.button("✨  About LUXEMART", use_container_width=True):
        go_to("About")

    st.markdown("---")

    st.markdown("### Collections")

    for category in CATEGORIES:
        if st.button(
            f"• {category}",
            key=f"sidebar_category_{category}",
            use_container_width=True,
        ):
            st.session_state.selected_category = category
            st.session_state.page = "Shop"
            st.rerun()

    st.markdown("---")

    st.caption("LUXEMART")
    st.caption("Elegant • Modern • Premium")


# =========================================================
# SHOP
# =========================================================
if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="luxury-title">
            Discover Your Style
        </div>

        <div class="luxury-subtitle">
            Curated fashion, beauty, jewellery and lifestyle essentials
            for a beautifully elevated everyday.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # HERO
    # -----------------------------------------------------
    slide = SLIDES[st.session_state.slider_index]

    st.markdown(
        f"""
        <div class="hero-wrapper">
            <img class="hero-image" src="{slide}">
        </div>
        """,
        unsafe_allow_html=True,
    )

    hero_col1, hero_col2, hero_col3 = st.columns([1, 2, 1])

    with hero_col1:
        if st.button("‹ Previous", use_container_width=True):
            st.session_state.slider_index = (
                st.session_state.slider_index - 1
            ) % len(SLIDES)
            st.rerun()

    with hero_col2:
        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding-top:9px;
                color:#746b78;
                font-size:13px;
                font-weight:600;
            ">
                {st.session_state.slider_index + 1}
                / {len(SLIDES)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with hero_col3:
        if st.button("Next ›", use_container_width=True):
            st.session_state.slider_index = (
                st.session_state.slider_index + 1
            ) % len(SLIDES)
            st.rerun()

    # -----------------------------------------------------
    # SEARCH & FILTERS
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">Find Your Favorites</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col, sort_col = st.columns([2.3, 1.2, 1.2])

    with search_col:
        search_text = st.text_input(
            "Search",
            placeholder="Search products...",
            label_visibility="collapsed",
        )

    with category_col:
        category_filter = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(st.session_state.selected_category),
            label_visibility="collapsed",
        )

    with sort_col:
        sort_filter = st.selectbox(
            "Sort",
            [
                "Featured",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A to Z",
            ],
            label_visibility="collapsed",
        )

    price_range = st.slider(
        "Price Range",
        min_value=1000,
        max_value=10000,
        value=(1000, 10000),
        step=500,
    )

    # -----------------------------------------------------
    # FILTER
    # -----------------------------------------------------
    filtered_products = PRODUCTS.copy()

    if search_text.strip():
        search_value = search_text.strip().lower()

        filtered_products = [
            product
            for product in filtered_products
            if search_value in
product["name"].lower()
            or search_value in product["category"].lower()
        ]

    if category_filter != "All":
        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category_filter
        ]

    minimum_price = price_range[0]
    maximum_price = price_range[1]

    filtered_products = [
        product
        for product in filtered_products
        if minimum_price <= product["price"] <= maximum_price
    ]

    if sort_filter == "Price: Low to High":
        filtered_products.sort(key=lambda item: item["price"])

    elif sort_filter == "Price: High to Low":
        filtered_products.sort(
            key=lambda item: item["price"],
            reverse=True,
        )

    elif sort_filter == "Name: A to Z":
        filtered_products.sort(
            key=lambda item: item["name"].lower()
        )

    # -----------------------------------------------------
    # CATEGORY CHIPS
    # -----------------------------------------------------
    st.markdown(
        '<div class="category-title">Shop by Collection</div>',
        unsafe_allow_html=True,
    )

    chip_columns = st.columns(len(CATEGORIES))

    for index, category in enumerate(CATEGORIES):
        with chip_columns[index]:

            if st.button(
                category,
                key=f"chip_{category}",
                use_container_width=True,
            ):
                st.session_state.selected_category = category
                st.rerun()

    # -----------------------------------------------------
    # PRODUCT COUNT
    # -----------------------------------------------------
    st.markdown(
        f"""
        <div style="
            color:#7c727f;
            font-size:13px;
            margin:18px 0 12px 0;
        ">
            Showing {len(filtered_products)} products
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # PRODUCTS
    # -----------------------------------------------------
    if not filtered_products:

        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <h3>No products found</h3>
                <p>Try another search or category.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        for start in range(0, len(filtered_products), 4):

            row_products = filtered_products[start:start + 4]

            columns = st.columns(4)

            for column, product in zip(columns, row_products):

                with column:

                    st.markdown(
                        f"""
                        <div class="product-card">

                            <img src="{product['image']}">

                            <div class="product-name">
                                {product['name']}
                            </div>

                            <div class="product-category">
                                {product['category']}
                            </div>

                            <div class="product-price">
                                {money(product['price'])}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    button_col1, button_col2 = st.columns(2)

                    with button_col1:

                        if st.button(
                            "🛒 Add",
                            key=f"add_{product['id']}",
                            use_container_width=True,
                        ):
                            add_to_cart(product["id"])

                    with button_col2:

                        favorite_icon = (
                            "❤️"
                            if product["id"]
                            in st.session_state.favorites
                            else "♡"
                        )

                        if st.button(
                            favorite_icon,
                            key=f"fav_{product['id']}",
                            use_container_width=True,
                        ):
                            toggle_favorite(product["id"])
                            st.rerun()


# =========================================================
# FAVORITES
# =========================================================
elif st.session_state.page == "Favorites":

    st.markdown(
        """
        <div class="luxury-title">
            Your Favorites
        </div>

        <div class="luxury-subtitle">
            Your personally selected LUXEMART pieces.
        </div>
        """,
        unsafe_allow_html=True,
    )

    favorite_products = [
        get_product(product_id)
        for product_id in st.session_state.favorites
    ]

    favorite_products = [
        product
        for product in favorite_products
        if product is not None
    ]

    if not favorite_products:

        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <h3>♡ Your favorites are empty</h3>
                <p>
                    Tap the heart icon on products you love
                    to save them here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Explore Collection", use_container_width=True):
            go_to("Shop")

    else:

        for start in range(0, len(favorite_products), 4):

            row_products = favorite_products[start:start + 4]

            columns = st.columns(4)

            for column, product in zip(columns, row_products):

                with column:

                    st.markdown(
                        f"""
                        <div class="product-card">

                            <img src="{product['image']}">

                            <div class="product-name">
                                {product['name']}
                            </div>

                            <div class="product-category">
                                {product['category']}
                            </div>

                            <div class="product-price">
                                {money(product['price'])}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    c1, c2 = st.columns(2)

                    with c1:
                        if st.button(
                            "🛒 Add",
                            key=f"fav_add_{product['id']}",
                            use_container_width=True,
                        ):
                            add_to_cart(product["id"])

                    with c2:
                        if st.button(
                            "Remove",
                            key=f"fav_remove_{product['id']}",
                            use_container_width=True,
                        ):
                            st.session_state.favorites.remove(
                                product["id"]
                            )
                            st.rerun()


# =========================================================
# CART
# =========================================================
elif st.session_state.page == "Cart":

    st.markdown(
        """
        <div class="luxury-title">
            Shopping Cart
        </div>

        <div class="luxury-subtitle">
            Review your selected items before checkout.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <h3>🛒 Your cart is empty</h3>
                <p>Discover something beautiful from our collection.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Continue Shopping", use_container_width=True):
            go_to("Shop")

    else:

        # -------------------------------------------------
        # CART ITEMS
        # -------------------------------------------------
        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            if product is None:
                continue

            col1, col2, col3 = st.columns([5, 2, 1])

            with col1:

                st.markdown(
                    f"""
                    <div class="cart-card">
                        <strong>🛍️ {product['name']}</strong>
                        <br>
                        <span style="color:#8a808e;font-size:13px;">
                            {product['category']}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:

                st.markdown(
                    f"""
                    <div style="
                        padding:18px 0;
                        font-weight:700;
                    ">
                        {money(product['price'])}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col3:

                if st.button(
                    "×",
                    key=f"remove_cart_{index}",
                    use_container_width=True,
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

        # -------------------------------------------------
        # TOTAL
        # -------------------------------------------------
        total = cart_total()

        st.markdown(
            f"""
            <div class="total-card">

                <div class="total-label">
                    ORDER TOTAL
                </div>

                <div class="total-value">
                    {money(total)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">Checkout Details</div>',
            unsafe_allow_html=True,
        )

        customer_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete delivery address",
        )

        checkout_col1, checkout_col2 = st.columns(2)

        with checkout_col1:

            if st.button(
                "🛍️ Place Order",
                use_container_width=True,
            ):

                if (
                    not customer_name.strip()
                    or not customer_phone.strip()
                    or not customer_address.strip()
                ):

                    st.error(
                        "Please complete all checkout fields."
                    )

                else:

                    try:

                        order_data = {
                            "customer_name": customer_name.strip(),
                            "customer_phone": customer_phone.strip(),
                            "customer_address": customer_address.strip(),
                            "total_amount": total,
                        }

                        order_response = (
                            supabase
                            .table("orders")
                            .insert(order_data)
                            .execute()
                        )

                        if not order_response.data:
                            st.error("Unable to create order.")
                        else:

                            order_id = order_response.data[0]["id"]

                            for product_id in st.session_state.cart:

                                product = get_product(product_id)

                                if product is None:
                                    continue

                                item_data = {
                                    "order_id": order_id,
                                    "product_name": product["name"],
                                    "price": product["price"],
                                    "quantity": 1,
                                }

                                supabase.table(
                                    "order_items"
                                ).insert(item_data).execute()

                            st.session_state.cart = []

                            st.success(
                                "🎉 Your order has been placed successfully!"
                            )

                            st.balloons()

                            st.rerun()

                    except Exception as error:
                        st.error(
                            f"Order error: {error}"
                        )

        with checkout_col2:

            if st.button(
                "← Continue Shopping",
                use_container_width=True,
            ):
                go_to("Shop")


# =========================================================
# ABOUT
# =========================================================
elif st.session_state.page == "About":

    st.markdown(
        """
        <div class="luxury-title">
            About LUXEMART
        </div>

        <div class="luxury-subtitle">
            A modern destination for elegant lifestyle essentials.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.4, 1])

    with col1:

        st.markdown(
            """
            <div class="info-card">

                <h3>Our Story</h3>

                <p>
                    LUXEMART is designed as a modern premium shopping
                    experience where fashion, beauty, jewellery,
                    accessories and fragrances come together in one
                    elegant destination.
                </p>

                <p>
                    Our goal is to make discovering beautiful products
                    simple, stylish and enjoyable.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="info-card">

                <h3>Why LUXEMART?</h3>

                <p>✨ Elegant collections</p>
                <p>🛍️ Easy shopping</p>
                <p>❤️ Personal favorites</p>
                <p>🚚 Simple checkout</p>
                <p>💎 Premium experience</p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="info-card">

            <h3>Contact</h3>

            <p>
                📞 <strong>03169707804</strong>
            </p>

            <p>
                ✉️ <strong>asyabibi485@gmail.com</strong>
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# ADMIN
# =========================================================
elif st.session_state.page == "Admin":

    st.markdown(
        """
        <div class="luxury-title">
            Admin Dashboard
        </div>

        <div class="luxury-subtitle">
            Manage customer orders securely.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # LOGIN
    # -----------------------------------------------------
    if not st.session_state.admin_logged_in:

        st.markdown(
            """
            <div class="admin-card">
                <h3>🔐 Administrator Login</h3>
                <p>
                    Sign in with your authorized administrator account.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        admin_email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email",
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password",
        )

        if st.button(
            "Sign In",
            use_container_width=True,
        ):

            if not admin_email.strip() or not admin_password:

                st.error(
                    "Please enter email and password."
                )

            else:

                try:

                    auth_response = (
                        supabase.auth.sign_in_with_password(
                            {
                                "email": admin_email.strip(),
                                "password": admin_password,
                            }
                        )
                    )

                    user = auth_response.user

                    if user is None:

                        st.error(
                            "Login failed."
                        )

                    elif (
                        user.email
                        and user.email.lower()
                        == ADMIN_EMAIL.lower()
                    ):

                        st.session_state.admin_logged_in = True

                        st.success(
                            "Admin login successful."
                        )

                        st.rerun()

                    else:

                        supabase.auth.sign_out()

                        st.error(
                            "This account is not authorized as admin."
                        )

                except Exception as error:

                    st.error(
                        f"Login error: {error}"
                    )

    # -----------------------------------------------------
    # ADMIN DASHBOARD
    # -----------------------------------------------------
    else:

        top_col1, top_col2 = st.columns([4, 1])

        with top_col1:
            st.success("Admin authenticated successfully.")

        with top_col2:

            if st.button(
                "Logout",
                use_container_width=True,
            ):
                logout_admin()

        st.markdown(
            '<div class="section-title">Client Requests Received</div>',
            unsafe_allow_html=True,
        )

        try:

            orders_response = (
                supabase
                .table("orders")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            orders = orders_response.data or []

            if not orders:

                st.markdown(
                    """
                    <div class="info-card" style="text-align:center;">
                        <h3>No orders yet</h3>
                        <p>
                            Customer orders will appear here.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:

                for order_number, order in enumerate(orders, 1):

                    order_id = order.get("id")

                    customer_name = order.get(
                        "customer_name",
                        "N/A",
                    )

                    customer_phone = order.get(
                        "customer_phone",
                        "N/A",
                    )

                    customer_address = order.get(
                        "customer_address",
                        "N/A",
                    )

                    total_amount = order.get(
                        "total_amount",
                        0,
                    )

                    created_at = order.get(
                        "created_at",
                        "N/A",
                    )

                    st.markdown(
                        f"""
                        <div class="admin-card">

                            <h3>
                                Order #{order_number}
                            </h3>

                            <p>
                                <strong>Customer:</strong>
                                {customer_name}
                            </p>

                            <p>
                                <strong>Phone:</strong>
                                {customer_phone}
                            </p>

                            <p>
                                <strong>Address:</strong>
                                {customer_address}
                            </p>

                            <p>
                                <strong>Total:</strong>
                                {money(float(total_amount))}
                            </p>

                            <p>
                                <strong>Date:</strong>
                                {created_at}
                            </p>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    try:

                        items_response = (
                            supabase
                            .table("order_items")
                            .select("*")
                            .eq("order_id", order_id)
                            .execute()
                        )

                        items = items_response.data or []

                        if items:

                            with st.expander(
                                "View Ordered Products"
                            ):

                                for item in items:

                                    product_name = item.get(
                                        "product_name",
                                        "Product",
                                    )

                                    item_price = item.get(
                                        "price",
                                        0,
                                    )

                                    quantity = item.get(
                                        "quantity",
                                        1,
                                    )

                                    st.write(
                                        f"🛍️ {product_name} "
                                        f"— {money(float(item_price))} "
                                        f"× {quantity}"
                                    )

                    except Exception as item_error:

                        st.warning(
                            f"Unable to load order items: {item_error}"
                        )

        except Exception as error:

            st.error(
                f"Unable to load orders: {error}"
            )


# =========================================================
# ADMIN ACCESS BUTTON
# =========================================================
# Hidden from the normal navigation but accessible through
# the small footer button.
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])

with footer_col2:

    if st.button(
        "🔐 Admin",
        use_container_width=True,
    ):
        st.session_state.page = "Admin"
        st.rerun()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#827886;
        font-size:12px;
        padding:15px;
    ">
        © LUXEMART • Premium Lifestyle Store
    </div>
    """,
    unsafe_allow_html=True,
)
            
