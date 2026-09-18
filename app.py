import os
import streamlit as st
from supabase import create_client


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SUPABASE CONFIG
# ============================================================

SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
ADMIN_EMAIL = st.secrets["admin"]["email"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


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

if "slider_index" not in st.session_state:
    st.session_state.slider_index = 0

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"


# ============================================================
# PRODUCTS
# ============================================================

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
        "image": "https://images.pexels.com/photos/45982/pexels-photo-45982.jpeg",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "image": "https://images.pexels.com/photos/1458867/pexels-photo-1458867.jpeg",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "image": "https://images.pexels.com/photos/1927259/pexels-photo-1927259.jpeg",
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
        "image": "https://images.pexels.com/photos/3373746/pexels-photo-3373746.jpeg",
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
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
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
        "image": "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
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
        "image": "https://images.pexels.com/photos/1961792/pexels-photo-1961792.jpeg",
    },
    {
        "id": 14,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "image": "https://images.pexels.com/photos/1190829/pexels-photo-1190829.jpeg",
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


# ============================================================
# HOME SLIDER
# ============================================================

SLIDES = [
    "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    "https://images.pexels.com/photos/904350/pexels-photo-904350.jpeg",
    "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
    "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

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

        if product:
            total += product["price"]

    return total


def go_to(page):
    st.session_state.page = page
    st.rerun()


def add_to_cart(product_id):
    st.session_state.cart.append(product_id)
    st.toast("Added to cart 🛒")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


def show_product_image(image_path):
    if image_path.startswith("http"):
        st.image(image_path, use_container_width=True)
    elif os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.markdown(
            """
            <div style="
                height:250px;
                display:flex;
                align-items:center;
                justify-content:center;
                background:#f2edf8;
                border-radius:15px;
                font-size:60px;
            ">
            🛍️
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #ffffff;
        color: #111111;
    }

    section[data-testid="stSidebar"] {
        background: #f5effb;
        border-right: 1px solid #e5d9ef;
    }

    section[data-testid="stSidebar"] * {
        color: #111111 !important;
    }

    .luxury-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #111111;
        margin-bottom: 5px;
    }

    .luxury-subtitle {
        font-size: 15px;
        color: #777777;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 800;
        color: #111111;
        margin-top: 15px;
        margin-bottom: 20px;
    }

    .product-card {
        background: #ffffff;
        border: 1px solid #eee5f5;
        border-radius: 18px;
        padding: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 18px rgba(80, 40, 100, 0.07);
    }

    .product-name {
        font-size: 18px;
        font-weight: 800;
        color: #111111;
        margin-top: 10px;
    }

    .product-category {
        font-size: 13px;
        color: #888888;
    }

    .product-price {
        font-size: 19px;
        font-weight: 900;
        color: #111111;
        margin-top: 5px;
    }

    .slider-box {
        border-radius: 22px;
        overflow: hidden;
        margin-bottom: 25px;
    }

    .cart-total {
        background: #f5effb;
        border-radius: 15px;
        padding: 20px;
        font-size: 24px;
        font-weight: 900;
        margin-top: 20px;
    }

    .admin-box {
        background: #f8f4fb;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #eadff1;
        margin-bottom: 15px;
    }

    div.stButton > button {
        border-radius: 10px;
        border: 1px solid #cdb5dd;
        background: #eee4f6;
        color: #111111;
        font-weight: 700;
    }

    div.stButton > button:hover {
        background: #dcc8ea;
        border-color: #b795cb;
    }

    input, textarea {
        border-radius: 10px !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size:30px;
            font-weight:900;
            letter-spacing:3px;
            margin-bottom:5px;
        ">
        LUXEMART
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("Premium Lifestyle Store")

    st.divider()

    if st.button("🛍️ SHOP", use_container_width=True):
        go_to("Shop")

    if st.button(
        f"❤️ FAVORITES ({len(st.session_state.favorites)})",
        use_container_width=True,
    ):
        go_to("Favorites")

    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        use_container_width=True,
    ):
        go_to("Cart")

    if st.button("ℹ️ ABOUT", use_container_width=True):
        go_to("About")

    if st.button("🔐 ADMIN", use_container_width=True):
        go_to("Admin")

    st.divider()

    st.markdown("### CATEGORIES")

    for category in CATEGORIES:

        if st.button(
            category,
            key=f"category_{category}",
            use_container_width=True,
        ):
            st.session_state.selected_category = category
            st.session_state.page = "Shop"
            st.rerun()


# ============================================================
# SHOP PAGE
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        '<div class="luxury-title">LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="luxury-subtitle">Premium fashion, beauty, jewellery and lifestyle essentials.</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # SLIDER
    # --------------------------------------------------------

    st.markdown('<div class="slider-box">', unsafe_allow_html=True)

    st.image(
        SLIDES[st.session_state.slider_index],
        use_container_width=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    slider_col1, slider_col2, slider_col3 = st.columns(
        [1, 2, 1]
    )

    with slider_col1:

        if st.button(
            "← PREVIOUS",
            use_container_width=True,
        ):
            st.session_state.slider_index = (
                st.session_state.slider_index - 1
            ) % len(SLIDES)

            st.rerun()

    with slider_col2:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:10px;
                font-weight:700;
            ">
            {st.session_state.slider_index + 1} / {len(SLIDES)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with slider_col3:

        if st.button(
            "NEXT →",
            use_container_width=True,
        ):
            st.session_state.slider_index = (
                st.session_state.slider_index + 1
            ) % len(SLIDES)

            st.rerun()

    st.divider()

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    selected_category = st.session_state.selected_category

    if selected_category == "All":
        filtered_products = PRODUCTS
    else:
        filtered_products = [
            product
            for product in PRODUCTS
            if product["category"] == selected_category
        ]

    st.markdown(
        f'<div class="section-title">{selected_category} COLLECTION</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # PRODUCTS
    # --------------------------------------------------------

    if not filtered_products:

        st.info("No products found.")

    else:

        for start in range(0, len(filtered_products), 4):

            row_products = filtered_products[start:start + 4]

            columns = st.columns(4)

            for column, product in zip(columns, row_products):

                with column:

                    st.markdown(
                        '<div class="product-card">',
                        unsafe_allow_html=True,
                    )

                    show_product_image(product["image"])

                    st.markdown(
                        f'<div class="product-name">{product["name"]}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-category">{product["category"]}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-price">{money(product["price"])}</div>',
                        unsafe_allow_html=True,
                    )

                    button_col1, button_col2 = st.columns(2)

                    with button_col1:

                        if st.button(
                            "🛒 ADD",
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

                    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# FAVORITES PAGE
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="section-title">❤️ MY FAVORITES</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.favorites:

        st.info("You have not added any products to favorites yet.")

        if st.button("CONTINUE SHOPPING"):
            go_to("Shop")

    else:

        favorite_products = [
            get_product(product_id)
            for product_id in st.session_state.favorites
        ]

        favorite_products = [
            product
            for product in favorite_products
            if product is not None
        ]

        for start in range(0, len(favorite_products), 4):

            row_products = favorite_products[start:start + 4]

            columns = st.columns(4)

            for column, product in zip(columns, row_products):

                with column:

                    st.markdown(
                        '<div class="product-card">',
                        unsafe_allow_html=True,
                    )

                    show_product_image(product["image"])

                    st.markdown(
                        f'<div class="product-name">{product["name"]}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-price">{money(product["price"])}</div>',
                        unsafe_allow_html=True,
                    )

                    if st.button(
                        "🛒 ADD TO CART",
                        key=f"favorite_add_{product['id']}",
                        use_container_width=True,
                    ):
                        add_to_cart(product["id"])

                    if st.button(
                        "REMOVE ❤️",
                        key=f"favorite_remove_{product['id']}",
                        use_container_width=True,
                    ):
                        st.session_state.favorites.remove(product["id"])
                        st.rerun()

                    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# CART PAGE
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="section-title">🛒 SHOPPING CART</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button("START SHOPPING"):
            go_to("Shop")

    else:

        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            if product is None:
                continue

            col1, col2, col3 = st.columns([5, 2, 1])

            with col1:

                st.write(
                    f"🛍️ **{product['name']}**"
                )

                st.caption(
                    product["category"]
                )

            with col2:

                st.write(
                    money(product["price"])
                )

            with col3:

                if st.button(
                    "REMOVE",
                    key=f"remove_{index}",
                    use_container_width=True,
                ):

                    st.session_state.cart.pop(index)
                    st.rerun()

        total = cart_total()

        st.markdown(
            f"""
            <div class="cart-total">
                TOTAL: {money(total)}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.markdown("### CUSTOMER INFORMATION")

        customer_name = st.text_input(
            "Full Name",
            key="customer_name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            key="customer_phone",
        )

        customer_address = st.text_area(
            "Delivery Address",
            key="customer_address",
            height=120,
        )

        checkout_col1, checkout_col2 = st.columns(2)

        with checkout_col1:

            if st.button(
                "PLACE ORDER",
                use_container_width=True,
            ):

                if not customer_name.strip():

                    st.error("Please enter your name.")

                elif not customer_phone.strip():

                    st.error("Please enter your phone number.")

                elif not customer_address.strip():

                    st.error("Please enter your delivery address.")

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

                            st.error(
                                "Order could not be created."
                            )

                        else:

                            order_id = order_response.data[0]["id"]

                            for product_id in st.session_state.cart:

                                product = get_product(product_id)

                                if product:

                                    item_data = {
                                        "order_id": order_id,
                                        "product_name": product["name"],
                                        "price": product["price"],
                                        "quantity": 1,
                                    }

                                    supabase \
                                        .table("order_items") \
                                        .insert(item_data) \
                                        .execute()

                            st.session_state.cart = []

                            st.success(
                                "🎉 Your order has been placed successfully!"
                            )

                            st.balloons()

                    except Exception as error:

                        st.error(
                            f"Order error: {error}"
                        )

        with checkout_col2:

            if st.button(
                "CONTINUE SHOPPING",
                use_container_width=True,
            ):
                go_to("Shop")


# ============================================================
# ABOUT PAGE
# ============================================================

elif st.session_state.page == "About":

    st.markdown(
        '<div class="section-title">ℹ️ ABOUT LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ### Welcome to LUXEMART 🛍️

        LUXEMART is a premium online lifestyle store offering
        fashion, clothes, jewellery, accessories, beauty products
        and perfumes.

        Our goal is to provide customers with an elegant,
        simple and convenient shopping experience.

        ### Contact

        📞 **Phone:** 03169707804

        📧 **Email:** asyabibi485@gmail.com

        ### Categories

        - 👗 Clothes
        - 👜 Fashion
        - 💎 Jewellery
        - ⌚ Accessories
        - 🌸 Perfumes
        - 💄 Beauty

        Thank you for shopping with LUXEMART.
        """,
    )


# ============================================================
# ADMIN PAGE
# ============================================================

elif st.session_state.page == "Admin":

    st.markdown(
        '<div class="section-title">🔐 ADMIN PANEL</div>',
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # ALREADY LOGGED IN
    # --------------------------------------------------------

    if st.session_state.admin_logged_in:

        st.success("Admin logged in.")

        if st.button(
            "LOGOUT",
            use_container_width=True,
        ):

            try:
                supabase.auth.sign_out()
            except Exception:
                pass

            st.session_state.admin_logged_in = False
            st.rerun()

        st.divider()

        st.markdown(
            '<div class="section-title">CLIENT REQUESTS RECEIVED</div>',
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

                st.info("No customer orders found.")

            else:

                for order in orders:

                    st.markdown(
                        '<div class="admin-box">',
                        unsafe_allow_html=True,
                    )

                    order_id = order.get("id", "")

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
                        f"### 🧾 Order #{order_id}"
                    )

                    st.write(
                        f"**Customer:** {customer_name}"
                    )

                    st.write(
                        f"**Phone:** {customer_phone}"
                    )

                    st.write(
                        f"**Address:** {customer_address}"
                    )

                    st.write(
                        f"**Total:** {money(total_amount)}"
                    )

                    st.write(
                        f"**Date:** {created_at}"
                    )

                    st.markdown("#### ORDER ITEMS")

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

                            for item in items:

                                product_name = item.get(
                                    "product_name",
                                    "Unknown Product",
                                )

                                price = item.get(
                                    "price",
                                    0,
                                )

                                quantity = item.get(
                                    "quantity",
                                    1,
                                )

                                st.write(
                                    f"• {product_name} — "
                                    f"{money(price)} × {quantity}"
                                )

                        else:

                            st.caption(
                                "No order items found."
                            )

                    except Exception as item_error:

                        st.warning(
                            f"Could not load order items: {item_error}"
                        )

                    st.markdown("</div>", unsafe_allow_html=True)

        except Exception as error:

            st.error(
                f"Could not load customer orders: {error}"
            )

    # --------------------------------------------------------
    # ADMIN LOGIN
    # --------------------------------------------------------

    else:

        st.info(
            "Please login with the administrator account."
        )

        admin_email = st.text_input(
            "Admin Email"
        )

        admin_password = st.text_input(
            "Password",
            type="password",
        )

        if st.button(
            "LOGIN",
            use_container_width=True,
        ):

            if not admin_email.strip():

                st.error(
                    "Please enter admin email."
                )

            elif not admin_password:

                st.error(
                    "Please enter password."
                )

            elif admin_email.strip().lower() != ADMIN_EMAIL.strip().lower():

                st.error(
                    "This email is not authorized as admin."
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

                    if auth_response.user:

                        st.session_state.admin_logged_in = True

                        st.success(
                            "Login successful."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Login failed."
                        )

                except Exception as error:

                    st.error(
                        f"Login error: {error}"
                    )

