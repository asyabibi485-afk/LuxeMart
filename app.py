import streamlit as st
from supabase import create_client, Client

# ============================================================
# LUXEMART — MODERN LUXURY STREAMLIT SHOP
# Supabase Email/Password Admin Authentication
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def init_supabase():
    try:
        supabase_url = st.secrets["SUPABASE_URL"]
        supabase_key = st.secrets["SUPABASE_ANON_KEY"]

        return create_client(
            supabase_url,
            supabase_key
        )
    except Exception as e:
        st.error("Supabase connection is not configured correctly.")
        st.code(str(e))
        return None


supabase: Client = init_supabase()


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
        "emoji": "👜",
        "description": "Elegant premium handbag for a sophisticated look.",
    },
    {
        "id": 2,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "emoji": "📿",
        "description": "Classic pearl-inspired jewellery for every occasion.",
    },
    {
        "id": 3,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "emoji": "⌚",
        "description": "Luxury-inspired classic watch design.",
    },
    {
        "id": 4,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "emoji": "🕶️",
        "description": "Stylish sunglasses with a premium modern look.",
    },
    {
        "id": 5,
        "name": "Luxury Perfume",
        "category": "Beauty",
        "price": 2999,
        "emoji": "🌸",
        "description": "A beautiful fragrance for an elegant everyday style.",
    },
    {
        "id": 6,
        "name": "Silk Evening Scarf",
        "category": "Fashion",
        "price": 1599,
        "emoji": "🧣",
        "description": "Soft and elegant scarf for evening outfits.",
    },
    {
        "id": 7,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "emoji": "💎",
        "description": "Sparkling bracelet designed for a glamorous finish.",
    },
    {
        "id": 8,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "emoji": "💄",
        "description": "Complete beauty set for a polished look.",
    },
]


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(124, 88, 255, 0.10), transparent 28%),
            radial-gradient(circle at 90% 15%, rgba(255, 63, 145, 0.09), transparent 25%),
            #faf9fc;
        color: #15121b;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #15121b !important;
        font-weight: 800 !important;
    }

    p, label, span, div {
        color: #24202b;
    }

    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #7657ff, #ff3f91);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }

    .tagline {
        color: #51495b !important;
        font-weight: 600;
        font-size: 14px;
        margin-top: -8px;
    }

    .hero {
        margin-top: 25px;
        padding: 55px 45px;
        border-radius: 30px;
        background:
            radial-gradient(circle at 90% 20%, rgba(255,255,255,.30), transparent 25%),
            linear-gradient(135deg, #7657ff, #a855f7 48%, #ff3f91);
        box-shadow: 0 25px 60px rgba(118,87,255,.20);
        color: white;
    }

    .hero h1 {
        color: white !important;
        font-family: 'Playfair Display', serif;
        font-size: 50px;
        line-height: 1.05;
        margin-bottom: 12px;
    }

    .hero p {
        color: rgba(255,255,255,.94) !important;
        font-size: 17px;
        font-weight: 500;
        max-width: 620px;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        font-weight: 800;
        margin-top: 38px;
        margin-bottom: 18px;
        color: #15121b;
    }

    .product-card {
        background: rgba(255,255,255,.95);
        border: 1px solid #eeeaf5;
        border-radius: 24px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 12px 35px rgba(30,20,50,.07);
        transition: all .25s ease;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 45px rgba(30,20,50,.13);
    }

    .product-image {
        height: 180px;
        border-radius: 18px;
        background: linear-gradient(135deg, #f0ebff, #fff0f7);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 75px;
        margin-bottom: 17px;
    }

    .product-name {
        font-size: 19px;
        font-weight: 800;
        color: #15121b;
        margin-bottom: 4px;
    }

    .product-category {
        font-size: 12px;
        color: #7657ff;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .product-description {
        color: #5b5464;
        font-size: 13px;
        min-height: 40px;
        margin-top: 7px;
    }

    .price {
        font-size: 22px;
        font-weight: 800;
        color: #15121b;
        margin-top: 12px;
    }

    .info-card {
        background: white;
        border-radius: 24px;
        padding: 28px;
        border: 1px solid #eeeaf5;
        box-shadow: 0 12px 35px rgba(30,20,50,.06);
        margin-bottom: 20px;
    }

    .admin-box {
        background: linear-gradient(135deg, #15121b, #292331);
        border-radius: 25px;
        padding: 30px;
        color: white;
        margin-bottom: 25px;
    }

    .admin-box h2 {
        color: white !important;
    }

    .admin-box p {
        color: #ddd7e7 !important;
    }

    .success-box {
        padding: 18px;
        border-radius: 15px;
        background: #ecfff5;
        border: 1px solid #b7efd1;
        color: #12663c;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #716978 !important;
        padding: 35px 10px 10px;
        font-size: 13px;
    }

    div.stButton > button {
        border-radius: 13px;
        border: 1px solid #e7e1ef;
        background: white;
        color: #15121b;
        font-weight: 700;
        min-height: 43px;
        transition: .2s;
    }

    div.stButton > button:hover {
        border-color: #7657ff;
        color: #7657ff;
        transform: translateY(-1px);
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #7657ff, #ff3f91);
        color: white;
        border: none;
    }

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px;
    }

    @media (max-width: 768px) {
        .hero {
            padding: 35px 25px;
        }

        .hero h1 {
            font-size: 36px;
        }

        .brand {
            font-size: 34px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def go_to(page):
    st.session_state.page = page
    st.rerun()


def add_to_cart(product):
    st.session_state.cart.append(product)
    st.toast(f"{product['name']} added to cart 🛒")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


def logout_admin():
    st.session_state.admin_user = None
    go_to("Shop")


# ============================================================
# HEADER
# ============================================================

header_left, header_right = st.columns([2, 3])

with header_left:
    st.markdown(
        """
        <div class="brand">LUXEMART</div>
        <div class="tagline">Luxury • Style • Everyday Elegance</div>
        """,
        unsafe_allow_html=True,
    )

with header_right:
    nav = st.columns(6)

    with nav[0]:
        if st.button("⌂ Shop", use_container_width=True):
            go_to("Shop")

    with nav[1]:
        if st.button(
            f"♡ {len(st.session_state.favorites)}",
            use_container_width=True,
        ):
            go_to("Favorites")

    with nav[2]:
        if st.button(
            f"🛒 {len(st.session_state.cart)}",
            use_container_width=True,
        ):
            go_to("Cart")

    with nav[3]:
        if st.button("✦ About", use_container_width=True):
            go_to("About")

    with nav[4]:
        if st.button("☎ Contact", use_container_width=True):
            go_to("Contact")

    with nav[5]:
        if st.button("⚙ Admin", type="primary", use_container_width=True):
            go_to("Admin")


st.divider()


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">
            <h1>Luxury that feels<br>uniquely yours.</h1>
            <p>
                Discover carefully selected fashion, jewellery,
                beauty and accessories designed to add elegance
                to your everyday style.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Explore Collection</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "🔎 Search products",
        placeholder="Search handbags, jewellery, perfume...",
    )

    categories = ["All", "Fashion", "Jewellery", "Accessories", "Beauty"]

    selected_category = st.selectbox(
        "Category",
        categories,
    )

    filtered_products = PRODUCTS

    if selected_category != "All":
        filtered_products = [
            p for p in filtered_products
            if p["category"] == selected_category
        ]

    if search:
        filtered_products = [
            p for p in filtered_products
            if search.lower() in p["name"].lower()
            or search.lower() in p["category"].lower()
        ]

    if not filtered_products:
        st.info("No products found.")
    else:
        columns = st.columns(4)

        for index, product in enumerate(filtered_products):

            with columns[index % 4]:

                is_favorite = product["id"] in st.session_state.favorites

                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="product-image">
                            {product["emoji"]}
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

                        <div class="price">
                            Rs. {product["price"]:,}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                b1, b2 = st.columns(2)

                with b1:
                    if st.button(
                        "🛒 Add",
                        key=f"cart_{product['id']}",
                        use_container_width=True,
                    ):
                        add_to_cart(product)

                with b2:
                    if st.button(
                        "❤️" if is_favorite else "♡",
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
        '<div class="section-title">Your Favorites ❤️</div>',
        unsafe_allow_html=True,
    )

    favorite_products = [
        p for p in PRODUCTS
        if p["id"] in st.session_state.favorites
    ]

    if not favorite_products:
        st.info("You haven't added any favorites yet.")
    else:
        columns = st.columns(4)

        for index, product in enumerate(favorite_products):

            with columns[index % 4]:

                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="product-image">
                            {product["emoji"]}
                        </div>

                        <div class="product-category">
                            {product["category"]}
                        </div>

                        <div class="product-name">
                            {product["name"]}
                        </div>

                        <div class="price">
                            Rs. {product["price"]:,}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "🛒 Add to Cart",
                    key=f"fav_cart_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(product)


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="section-title">Shopping Cart 🛒</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button("Continue Shopping", type="primary"):
            go_to("Shop")

    else:

        total = 0

        for index, product in enumerate(st.session_state.cart):

            total += product["price"]

            col1, col2, col3 = st.columns([4, 2, 1])

            with col1:
                st.markdown(
                    f"**{product['emoji']} {product['name']}**"
                )

            with col2:
                st.write(f"Rs. {product['price']:,}")

            with col3:
                if st.button(
                    "✕",
                    key=f"remove_{index}",
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

        st.divider()

        st.markdown(
            f"""
            <div class="info-card">
                <h2>Order Total</h2>
                <h1>Rs. {total:,}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Proceed to Checkout",
            type="primary",
            use_container_width=True,
        ):
            go_to("Checkout")


# ============================================================
# CHECKOUT
# ============================================================

elif st.session_state.page == "Checkout":

    st.markdown(
        '<div class="section-title">Checkout</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your cart is empty.")

    else:

        st.markdown(
            """
            <div class="info-card">
                <h2>Delivery Information</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        city = st.text_input("City")

        payment = st.selectbox(
            "Payment Method",
            [
                "Cash on Delivery",
                "Bank Transfer",
                "Other",
            ],
        )

        total = sum(
            product["price"]
            for product in st.session_state.cart
        )

        st.markdown(f"### Total: Rs. {total:,}")

        if st.button(
            "Place Order",
            type="primary",
            use_container_width=True,
        ):

            if not name or not phone or not address or not city:
                st.error("Please complete all delivery information.")

            else:

                st.success(
                    "Order submitted successfully! 🎉"
                )

                st.session_state.cart = []

                st.markdown(
                    """
                    <div class="success-box">
                        Thank you for shopping with LUXEMART.
                        We will contact you shortly to confirm your order.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.markdown(
        '<div class="section-title">About LUXEMART ✦</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">

        <h2>Welcome to LUXEMART</h2>

        <p>
        LUXEMART is a modern online shopping experience created
        around fashion, beauty, jewellery and elegant accessories.
        </p>

        <p>
        Our goal is to make luxury-inspired shopping simple,
        beautiful and enjoyable.
        </p>

        <h3>Our Style</h3>

        <p>
        Elegant design, modern trends and carefully selected
        products — all in one place.
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
        '<div class="section-title">Contact Us ☎</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <d
