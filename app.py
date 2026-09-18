import streamlit as st
from supabase import create_client

# ============================================================
# LUXEMART
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
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]
    ADMIN_EMAIL = st.secrets["admin"]["email"]

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

except Exception:
    st.error("Supabase configuration could not be loaded.")
    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Luxury Handbag",
        "category": "Fashion",
        "price": 5499,
        "icon": "👜",
        "description": "Elegant premium handbag for a sophisticated look.",
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "icon": "🧣",
        "description": "Soft and stylish silk scarf for everyday elegance.",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "icon": "📿",
        "description": "Classic pearl necklace with a graceful finish.",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "icon": "📿",
        "description": "Delicate bracelet designed for timeless style.",
    },
    {
        "id": 5,
        "name": "Gold Watch",
        "category": "Accessories",
        "price": 7999,
        "icon": "⌚",
        "description": "Luxury-inspired watch with a premium appearance.",
    },
    {
        "id": 6,
        "name": "Classic Sunglasses",
        "category": "Accessories",
        "price": 2999,
        "icon": "🕶️",
        "description": "Modern sunglasses with a stylish statement look.",
    },
    {
        "id": 7,
        "name": "Premium Makeup Set",
        "category": "Beauty",
        "price": 4499,
        "icon": "💄",
        "description": "Beautiful makeup essentials for your daily style.",
    },
    {
        "id": 8,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
        "description": "Elegant flowing luxury abaya.",
    },
    {
        "id": 9,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
        "description": "Premium lawn suit with a beautiful modern design.",
    },
    {
        "id": 10,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
        "description": "A sophisticated evening dress for special occasions.",
    },
    {
        "id": 11,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
        "description": "Comfortable and stylish casual kurti.",
    },
    {
        "id": 12,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
        "description": "A romantic rose fragrance with an elegant finish.",
    },
    {
        "id": 13,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
        "description": "Rich oud-inspired fragrance with a luxurious character.",
    },
    {
        "id": 14,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
        "description": "Sweet vanilla fragrance with a soft dreamy aroma.",
    },
]


# ============================================================
# FUNCTIONS
# ============================================================

def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def money(amount):
    return f"Rs. {amount:,}"


def cart_total():
    total = 0

    for product_id in st.session_state.cart:
        product = get_product(product_id)

        if product is not None:
            total += product["price"]

    return total


def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()


# ============================================================
# CSS
# ============================================================
st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@500;600;700&display=swap'
    );

    /* =========================
       MAIN APP BACKGROUND
       ========================= */

    .stApp {
        background: #ffffff !important;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    /* =========================
       NORMAL TEXT
       ========================= */

    .stApp p,
    .stApp span,
    .stApp label,
    .stApp li {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* =========================
       HEADINGS
       ========================= */

    h1,
    h2,
    h3,
    h4 {
        color: #000000 !important;
        font-family: "Playfair Display", serif !important;
        font-weight: 700 !important;
    }

    /* =========================
       BRAND
       ========================= */

    .brand {
        font-family: "Playfair Display", serif;
        font-size: 36px;
        font-weight: 700;
        letter-spacing: 4px;
        color: #000000 !important;
    }

    .tagline {
        color: #000000 !important;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
    }

    /* =========================
       HERO
       ========================= */

    .hero-box {
        padding: 38px;
        margin: 25px 0;
        border-radius: 28px;
        background: linear-gradient(
            135deg,
            #ffffff,
            #f1ebfb
        );
        border: 1px solid #e5dcef;
        box-shadow: 0 15px 45px rgba(50, 40, 65, 0.08);
    }

    /* =========================
       PRODUCT CARD
       ========================= */

    .product-card {
        padding: 10px;
        border-radius: 22px;
        background: rgba(255, 255, 255, 0.90);
        border: 1px solid #e8dfef;
        box-shadow: 0 10px 28px rgba(50, 40, 65, 0.07);
        margin-bottom: 10px;
    }

    .product-image {
        height: 145px;
        border-radius: 20px;
        background: linear-gradient(
            145deg,
            #ffffff,
            #eee7f8
        );
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 65px;
    }

    /* =========================
       BUTTONS
       ========================= */

    div.stButton > button {
        background: #f5efff !important;
        color: #000000 !important;
        border: 1px solid #d8cae8 !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        min-height: 44px !important;
    }

    div.stButton > button:hover {
        background: #e9def7 !important;
        color: #000000 !important;
        border-color: #cbb8e2 !important;
    }

    /* =========================
       TEXT INPUT
       WHITE BACKGROUND
       BLACK TEXT
       ========================= */

    input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #d8cae8 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    input:focus {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border-color: #b99bd8 !important;
        box-shadow: 0 0 0 1px #b99bd8 !important;
    }

    /* =========================
       TEXTAREA
       ========================= */

    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #d8cae8 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    textarea:focus {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border-color: #b99bd8 !important;
        box-shadow: 0 0 0 1px #b99bd8 !important;
    }

    /* =========================
       PLACEHOLDER TEXT
       ========================= */

    input::placeholder,
    textarea::placeholder {
        color: #777777 !important;
        -webkit-text-fill-color: #777777 !important;
        opacity: 1 !important;
    }

    /* =========================
       SELECT BOX
       ========================= */

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid #d8cae8 !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* =========================
       SELECT MENU
       ========================= */

    div[role="listbox"] {
        background-color: #ffffff !important;
    }

    div[role="option"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    div[role="option"]:hover {
        background-color: #f5efff !important;
        color: #000000 !important;
    }

    /* =========================
       NUMBER INPUT
       ========================= */

    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* =========================
       CHECKBOX
       ========================= */

    div[data-testid="stCheckbox"] label {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;
        padding: 30px;
        margin-top: 45px;
        border-radius: 25px;
        background: #30283b;
    }

    .footer h2,
    .footer p {
        color: #ffffff !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)
        
                                            


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.title("♡ Your Favorites")

    if not st.session_state.favorites:

        st.info("Your favorites are empty.")

        if st.button("← Continue Shopping"):
            navigate("Shop")

    else:

        for product_id in st.session_state.favorites:

            product = get_product(product_id)

            if product is None:
                continue

            left, middle, right = st.columns([1, 4, 1])

            with left:
                st.markdown(
                    f"""
                    <div class="product-image">
                        {product["icon"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with middle:
                st.subheader(product["name"])
                st.write(product["description"])
                st.markdown(
                    f"**{money(product['price'])}**"
                )

            with right:

                if st.button(
                    "Remove",
                    key=f"remove_favorite_{product['id']}",
                ):

                    st.session_state.favorites.remove(
                        product["id"]
                    )

                    st.rerun()

                if st.button(
                    "Add Cart",
                    key=f"favorite_cart_{product['id']}",
                ):

                    st.session_state.cart.append(
                        product["id"]
                    )

                    st.toast("Added to cart!")


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.title("🛍 Shopping Cart")

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button("← Continue Shopping"):
            navigate("Shop")

    else:

        for index, product_id in enumerate(
            st.session_state.cart
        ):

            product = get_product(product_id)

            if product is None:
                continue

            left, middle, right = st.columns([1, 4, 1])

            with left:
                st.markdown(
                    f"""
                    <div class="product-image">
                        {product["icon"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with middle:
                st.subheader(product["name"])
                st.write(product["category"])
                st.markdown(
                    f"**{money(product['price'])}**"
                )

            with right:

                if st.button(
                    "Remove",
                    key=f"remove_cart_{index}",
                ):

                    st.session_state.cart.pop(index)
                    st.rerun()

        st.divider()

        st.subheader(
            f"Total: {money(cart_total())}"
        )

        st.markdown("## Checkout")

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Enter your name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete address",
        )

        if st.button(
            "Place Order",
            use_container_width=True,
        ):

            if not customer_name.strip():

                st.warning("Please enter your name.")

            elif not customer_phone.strip():

                st.warning("Please enter your phone number.")

            elif not customer_address.strip():

                st.warning("Please enter your delivery address.")

            else:

                try:

                    order_data = {
                        "customer_name": customer_name.strip(),
                        "customer_phone": customer_phone.strip(),
                        "customer_address": customer_address.strip(),
                        "total_amount": cart_total(),
                    }

                    response = (
                        supabase
                        .table("orders")
                        .insert(order_data)
                        .execute()
                    )

                    order_id = None

                    if response.data:
                        order_id = response.data[0].get("id")

                    if order_id is not None:

                        for product_id in st.session_state.cart:

                            product = get_product(product_id)

                            if product is not None:

                                item_data = {
                                    "order_id": order_id,
                                    "product_name": product["name"],
                                    "price": product["price"],
                                    "quantity": 1,
                                }

                                (
                                    supabase
                                    .table("order_items")
                                    .insert(item_data)
                                    .execute()
                                )

                    st.session_state.cart = []

                    st.success(
                        "🎉 Your order has been placed successfully!"
                    )

                    st.balloons()

                except Exception:

                    st.error(
                        "Unable to place the order. "
                        "Please check your Supabase table column names."
                    )


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.title("About LUXEMART")

    st.write(
        "Welcome to LUXEMART, your destination for elegant "
        "fashion, jewellery, accessories, clothes, beauty "
        "products and luxury fragrances."
    )

    st.subheader("Our Collections")

    st.write("👗 Clothes")
    st.write("👜 Fashion")
    st.write("💎 Jewellery")
    st.write("✨ Accessories")
    st.write("🌸 Perfume")
    st.write("💄 Beauty")

    st.subheader("Contact")

    st.write("📞 03169707804")
    st.write("✉️ asyabibi485@gmail.com")


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.title("Admin Panel")

    if not st.session_state.admin_logged_in:

        st.write(
            "Sign in with your existing Supabase account."
        )

        email = st.text_input(
            "Admin Email",
            value=ADMIN_EMAIL,
        )

        password = st.text_input(
            "Password",
            type="password",
        )

        if st.button(
            "Sign In",
            use_container_width=True,
        ):

            if not email.strip():

                st.warning("Please enter your email.")

            elif not password:

                st.warning("Please enter your password.")

            elif email.strip().lower() != ADMIN_EMAIL.lower():

                st.error(
                    "This email is not authorized for admin access."
                )

            else:

                try:

                    supabase.auth.sign_in_with_password(
                        {
                            "email": email.strip(),
                            "password": password,
                        }
                    )

                    st.session_state.admin_logged_in = True

                    st.success(
                        "Admin login successful."
                    )

                    st.rerun()

                except Exception:

                    st.error(
                        "Admin login failed. "
                        "Please check your Supabase account."
                    )

    else:

        st.success("Admin account is logged in.")

        st.subheader("LUXEMART Administration")

        st.write(
            f"Admin: {ADMIN_EMAIL}"
        )

        if st.button(
            "Sign Out",
            use_container_width=True,
        ):

            try:
                supabase.auth.sign_out()
            except Exception:
                pass

            st.session_state.admin_logged_in = False

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <h2>LUXEMART</h2>
        <p>Luxury • Style • Elegance</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("📞 03169707804")
st.write("✉️ asyabibi485@gmail.com")

st.caption(
    "© 2026 LUXEMART. All rights reserved."
)
