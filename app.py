import streamlit as st
from supabase import create_client

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# SUPABASE
# ============================================================

try:
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]
    ADMIN_EMAIL = st.secrets["admin"]["email"]

    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

except Exception as e:
    st.error("Supabase configuration could not be loaded.")
    st.code(str(e))
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
        "image": "https://images.pexels.com/photos/1152077/pexels-photo-1152077.jpeg",
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "image": "https://images.pexels.com/photos/959314/pexels-photo-959314.jpeg",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "image": "https://images.pexels.com/photos/1616096/pexels-photo-1616096.jpeg",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "image": "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
    },
    {
        "id": 5,
        "name": "Gold Watch",
        "category": "Accessories",
        "price": 7999,
        "image": "https://images.pexels.com/photos/277390/pexels-photo-277390.jpeg",
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
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
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


# ============================================================
# SLIDER
# ============================================================

SLIDES = [
    {
        "title": "Discover Your Luxury",
        "text": "Fashion, beauty, jewellery, perfumes and elegant lifestyle essentials.",
        "image": "https://images.pexels.com/photos/1152077/pexels-photo-1152077.jpeg",
    },
    {
        "title": "Elegant Fashion",
        "text": "Discover beautiful fashion pieces designed for your style.",
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
    },
    {
        "title": "Luxury Accessories",
        "text": "Complete your look with premium watches and accessories.",
        "image": "https://images.pexels.com/photos/277390/pexels-photo-277390.jpeg",
    },
    {
        "title": "Beauty & Perfume",
        "text": "Explore elegant beauty products and luxury fragrances.",
        "image": "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
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
    try:
        return f"Rs. {int(amount):,}"
    except Exception:
        return "Rs. 0"


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
    st.toast("Added to cart 🛍️")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


# ============================================================
# DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #ffffff;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .stApp p,
    .stApp label,
    .stApp li {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    h1,
    h2,
    h3,
    h4 {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #faf7ff;
        border-right: 1px solid #e5dcef;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p {
        color: #000000 !important;
    }

    div.stButton > button {
        background-color: #f3ecff !important;
        color: #000000 !important;
        border: 1px solid #d8c9eb !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        min-height: 44px !important;
    }

    div.stButton > button:hover {
        background-color: #e6d9f7 !important;
        color: #000000 !important;
        border-color: #b99bd3 !important;
    }

    div[data-testid="stTextInput"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #d8c9eb !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: 1px solid #d8c9eb !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid #d8c9eb !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    .slider-box {
        padding: 30px;
        border-radius: 25px;
        background-color: #faf7ff;
        border: 1px solid #e5dcef;
        min-height: 220px;
    }

    .slider-title {
        font-size: 36px;
        font-weight: 800;
        color: #000000;
        margin-bottom: 12px;
    }

    .slider-text {
        font-size: 16px;
        font-weight: 600;
        color: #000000;
        line-height: 1.6;
    }

    .slider-small {
        margin-top: 20px;
        font-size: 13px;
        font-weight: 700;
        color: #6c5a7b;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 0 20px 0;
        ">
            <div style="
                font-size:30px;
                font-weight:800;
                color:#000000;
            ">
                ✦ LUXEMART
            </div>

            <div style="
                font-size:12px;
                font-weight:700;
                color:#6c5a7b;
            ">
                LUXURY • STYLE • ELEGANCE
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.subheader("Navigation")

    if st.button(
        "🏠 SHOP",
        use_container_width=True,
    ):
        go_to("Shop")

    if st.button(
        "❤️ FAVORITES",
        use_container_width=True,
    ):
        go_to("Favorites")

    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        use_container_width=True,
    ):
        go_to("Cart")

    if st.button(
        "ℹ️ ABOUT",
        use_container_width=True,
    ):
        go_to("About")

    if st.button(
        "🔐 ADMIN",
        use_container_width=True,
    ):
        go_to("Admin")

    st.divider()

    st.subheader("Categories")
for category in CATEGORIES[1:]:

        if st.button(
            category,
            key=f"category_{category}",
            use_container_width=True,
        ):

            st.session_state.selected_category = category
            st.session_state.page = "Shop"
            st.rerun()


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.title("LUXEMART")

    st.caption(
        "Discover luxury fashion, beauty, jewellery, accessories and perfumes."
    )

    # --------------------------------------------------------
    # SLIDER
    # --------------------------------------------------------

    slide = SLIDES[
        st.session_state.slider_index
    ]

    left_slider, right_slider = st.columns(
        [1.3, 1]
    )

    with left_slider:

        st.markdown(
            f"""
            <div class="slider-box">

                <div class="slider-title">
                    {slide["title"]}
                </div>

                <div class="slider-text">
                    {slide["text"]}
                </div>

                <div class="slider-small">
                    LUXEMART • PREMIUM COLLECTION
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_slider:

        st.image(
            slide["image"],
            use_container_width=True,
        )

    previous_col, counter_col, next_col = st.columns(
        [1, 2, 1]
    )

    with previous_col:

        if st.button(
            "❮ PREVIOUS",
            key="previous_slide",
            use_container_width=True,
        ):

            st.session_state.slider_index = (
                st.session_state.slider_index - 1
            ) % len(SLIDES)

            st.rerun()

    with counter_col:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:10px;
                font-weight:700;
                color:#000000;
            ">
                Slide {st.session_state.slider_index + 1}
                / {len(SLIDES)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with next_col:

        if st.button(
            "NEXT ❯",
            key="next_slide",
            use_container_width=True,
        ):

            st.session_state.slider_index = (
                st.session_state.slider_index + 1
            ) % len(SLIDES)

            st.rerun()

    st.divider()

    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    search = st.text_input(
        "🔎 Search Products",
        placeholder="Type product name...",
    )

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    category = st.selectbox(
        "Choose Category",
        CATEGORIES,
        index=CATEGORIES.index(
            st.session_state.selected_category
        ),
    )

    st.session_state.selected_category = category

    # --------------------------------------------------------
    # FILTER
    # --------------------------------------------------------

    filtered_products = PRODUCTS.copy()

    if search.strip():

        filtered_products = [
            product
            for product in filtered_products
            if search.lower()
            in product["name"].lower()
        ]

    if category != "All":

        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    st.subheader(
        f"{len(filtered_products)} Products"
    )

    # --------------------------------------------------------
    # PRODUCT GRID
    # --------------------------------------------------------

    if not filtered_products:

        st.info("No products found.")

    else:

        columns = st.columns(3)

        for index, product in enumerate(
            filtered_products
        ):

            with columns[index % 3]:

                st.image(
                    product["image"],
                    use_container_width=True,
                )

                st.subheader(
                    product["name"]
                )

                st.write(
                    product["category"]
                )

                st.markdown(
                    f"**{money(product['price'])}**"
                )

                add_col, fav_col = st.columns(2)

                with add_col:

                    if st.button(
                        "🛍️ ADD",
                        key=f"add_{product['id']}",
                        use_container_width=True,
                    ):

                        add_to_cart(
                            product["id"]
                        )

                with fav_col:

                    if product["id"] in st.session_state.favorites:
                        favorite_text = "❤️"
                    else:
                        favorite_text = "♡"

                    if st.button(
                        favorite_text,
                        key=f"favorite_{product['id']}",
                        use_container_width=True,
                    ):

                        toggle_favorite(
                            product["id"]
                        )

                        st.rerun()


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.title("❤️ My Favorites")

    favorite_products = [
        product
        for product in PRODUCTS
        if product["id"]
        in st.session_state.favorites
    ]

    if not favorite_products:

        st.info(
            "No favorite products yet."
        )

        if st.button(
            "CONTINUE SHOPPING",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        columns = st.columns(3)

        for index, product in enumerate(
            favorite_products
        ):

            with columns[index % 3]:

                st.image(
                    product["image"],
                    use_container_width=True,
                )

                st.subheader(
                    product["name"]
                )

                st.write(
                    product["category"]
                )

                st.markdown(
                    f"**{money(product['price'])}**"
                )

                if st.button(
                    "🛍️ ADD TO CART",
                    key=f"fav_add_{product['id']}",
                    use_container_width=True,
                ):

                    add_to_cart(
                        product["id"]
                    )


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.title("🛒 Shopping Cart")

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "CONTINUE SHOPPING",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        # ----------------------------------------------------
        # CART ITEMS
        # ----------------------------------------------------

        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            # IMPORTANT:
            # Skip invalid product IDs.
            if product is None:
                continue

            col1, col2, col3 = st.columns(
                [5, 2, 1]
            )

            with col1:

                st.write(
                    f"🛍️ {product['name']}"
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

        # ----------------------------------------------------
        # TOTAL
        # ----------------------------------------------------

        st.divider()

        total = cart_total()

        st.subheader(
            f"Total: {money(total)}"
        )

        # ----------------------------------------------------
        # CHECKOUT
        # ----------------------------------------------------

        st.subheader(
            "Checkout"
        )

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Enter your full name",
            key="checkout_name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number",
            key="checkout_phone",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete address",
            key="checkout_address",
        )

        if st.button(
            "PLACE ORDER",
            use_container_width=True,
        ):

            if not customer_name.strip():

                st.error(
                    "Please enter your name."
                )

            elif not customer_phone.strip():

                st.error(
                    "Please enter your phone number."
                )

            elif not customer_address.strip():

                st.error(
                    "Please enter your delivery address."
                )

            else:

                try:

                    # ----------------------------------------
                    # CREATE ORDER
                    # ----------------------------------------

                    order_data = {
                        "customer_name":
                            customer_name.strip(),

                        "customer_phone":
                            customer_phone.strip(),

                        "customer_address":
                            customer_address.strip(),

                        "total_amount":
                            total,
                    }

                    order_response = (
                        supabase
                        .table("orders")
                        .insert(order_data)
                        .execute()
                    )

                    if not order_response.data:

                        raise Exception(
                            "Supabase did not return the new order."
                        )

                    order_id = (
                        order_response
                        .data[0]["id"]
                    )

                    # ----------------------------------------
                    # CREATE ORDER ITEMS
                    # ----------------------------------------

                    for product_id in list(
                        st.session_state.cart
                    ):

                        product = get_product(
                            product_id
                        )

                        if product is None:
                            continue

                        item_data = {
                            "order_id":
                                order_id,

                            "product_name":
                                product["name"],

                            "price":
                                product["price"],

                            "quantity":
                                1,
                        }

                        (
                            supabase
                            .table("order_items")
                            .insert(item_data)
                            .execute()
                        )

                    # ----------------------------------------
                    # CLEAR CART
                    # ----------------------------------------

                    st.session_state.cart = []

                    st.success(
                        "🎉 Order placed successfully!"
                    )

                    st.balloons()

                except Exception as e:

                    st.error(
                        "Unable to place the order."
                    )

                    st.code(
                        str(e)
                    )


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.title(
        "ℹ️ About LUXEMART"
    )

    st.write(
        "LUXEMART is a modern luxury shopping experience "
        "for fashion, beauty, jewellery, perfumes and "
        "lifestyle products."
    )

    st.divider()

    st.subheader(
        "Contact"
    )

    st.write(
        "📞 03169707804"
    )

    st.write(
        "📧 asyabibi485@gmail.com"
    )


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.title(
        "🔐 Admin Panel"
    )

    if not st.session_state.admin_logged_in:

        st.info(
            "Login with your existing Supabase admin account."
        )

        email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email",
            key="admin_email",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password",
            key="admin_password",
        )

        if st.button(
            "LOGIN",
            use_container_width=True,
        ):

            try:

                result = (
                    supabase.auth
                    .sign_in_with_password(
                        {
                            "email":
                                email.strip(),

                            "password":
                                password,
                        }
                    )
                )

                if result.user is None:

                    st.error(
                        "Login failed."
                    )

                elif (
                    email.strip().lower()
                    != ADMIN_EMAIL.strip().lower()
                ):

                    st.error(
                        "This account is not the configured admin account."
                    )

                    supabase.auth.sign_out()

                else:

                    st.session_state.admin_logged_in = True

                    st.success(
                        "Admin login successful."
                    )

                    st.rerun()

            except Exception as e:

                st.error(
                    "Login failed."
                )

                st.code(
                    str(e)
                )

    else:

        st.success(
            f"Logged in as {ADMIN_EMAIL}"
        )

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

        st.subheader(
            "📦 Client Requests Received"
        )

        try:

            response = (
                supabase
                .table("orders")
                .select("*")
                .order(
                    "created_at",
                    desc=True,
                )
                .execute()
            )

            orders = response.data or []

            if not orders:

                st.info(
                    "No client requests received yet."
                )

            else:

                st.success(
                    f"✅ {len(orders)} client request(s) received."
                )

                for order in orders:

                    st.markdown(
                        f"### 🧾 Order #{order.get('id')}"
                    )

                    st.write(
                        f"**Customer:** "
                        f"{order.get('customer_name', '')}"
                    )

                    st.write(
                        f"**Phone:** "
                        f"{order.get('customer_phone', '')}"
                    )

                    st.write(
                        f"**Address:** "
                        f"{order.get('customer_address', '')}"
                    )

                    st.write(
                        f"**Total:** "
                        f"{money(order.get('total_amount', 0))}"
                    )

                    st.write(
                        f"**Date:** "
                        f"{order.get('created_at', '')}"
                    )

                    try:

                        items_response = (
                            supabase
                            .table("order_items")
                            .select("*")
                            .eq(
                                "order_id",
                                order["id"],
                            )
                            .execute()
                        )

                        items = (
                            items_response.data
                            or []
                        )

                        if items:

                            st.write(
                                "**Order Items:**"
                            )

                            for item in items:

                                st.write(
                                    f"• "
                                    f"{item.get('product_name', '')} "
                                    f"x "
                                    f"{item.get('quantity', 1)} "
                                    f"- "
                                    f"{money(item.get('price', 0))}"
                                )

                    except Exception as item_error:

                        st.warning(
                            "Could not load items for this order."
                        )

                        st.code(
                            str(item_error)
                        )

                    st.divider()

        except Exception as e:

            st.error(
                "Unable to load client requests."
            )

            st.code(
                str(e)
            )






