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

if "slider_index" not in st.session_state:
    st.session_state.slider_index = 0

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"


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
        "image": "https://images.pexels.com/photos/769749/pexels-photo-769749.jpeg",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "image": "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg",
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
        "image": "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
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
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
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
        "image": "https://images.pexels.com/photos/3059609/pexels-photo-3059609.jpeg",
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


# =========================================================
# HOME SLIDER
# =========================================================

SLIDES = [
    "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    "https://images.pexels.com/photos/904350/pexels-photo-904350.jpeg",
    "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
    "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
]


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    return None


def money(value):
    return f"Rs. {value:,.0f}"


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

    st.toast("Added to cart 🛍️")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


def show_product_image(image_url):
    try:
        st.image(
            image_url,
            use_container_width=True,
        )
    except Exception:
        st.info("Product image unavailable")


# =========================================================
# COMPLETE DESIGN
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       COLORFUL APP BACKGROUND
       PINK + PURPLE + BLUE
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(255, 105, 180, 0.38),
                transparent 28%
            ),
            radial-gradient(
                circle at 95% 10%,
                rgba(138, 43, 226, 0.40),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(30, 144, 255, 0.38),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #ffd6ec 0%,
                #ead7ff 45%,
                #cfe8ff 100%
            ) !important;

        color: #000000 !important;
    }


    /* =====================================================
       MAIN CONTENT
       ===================================================== */

    .main {
        background: transparent !important;
        color: #000000 !important;
    }

    [data-testid="stAppViewContainer"] {
        background: transparent !important;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #ffd6ec 0%,
                #ead7ff 50%,
                #d5eaff 100%
            ) !important;

        color: #000000 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }


    /* =====================================================
       BLACK TEXT
       ===================================================== */

    p,
    span,
    label,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #000000 !important;
    }


    /* =====================================================
       ALL TYPING INPUTS
       WHITE BACKGROUND
       BLACK FONT
       ===================================================== */

    input,
    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 9px !important;
        caret-color: #000000 !important;
    }

    input:focus,
    textarea:focus {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        box-shadow: 0 0 0 2px rgba(138, 43, 226, 0.25) !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #555555 !important;
        opacity: 1 !important;
    }


    /* =====================================================
       STREAMLIT TEXT INPUT
       ===================================================== */

    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border-radius: 9px !important;
    }

    div[data-baseweb="input"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }


    /* =====================================================
       CART CHECKOUT INPUTS
       ALWAYS WHITE
       ===================================================== */

    [data-testid="stTextInput"] {
        background: transparent !important;
    }

    [data-testid="stTextInput"] input {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
    }

    [data-testid="stTextArea"] {
        background: transparent !important;
    }

    [data-testid="stTextArea"] textarea {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
    }


    /* =====================================================
       SELECTBOX
       ===================================================== */

    div[data-baseweb="select"] {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 9px !important;
    }

    div[data-baseweb="select"] * {
        color: #000000 !important;
        background-color: #ffffff !important;
    }


    /* =====================================================
       DROPDOWN MENU
       ===================================================== */

    div[role="listbox"] {
        background: #ffffff !important;
        color: #000000 !important;
    }

    div[role="option"] {
        background: #ffffff !important;
        color: #000000 !important;
    }

    div[role="option"]:hover {
        background: #ead7ff !important;
        color: #000000 !important;
    }


    /* =====================================================
       BUTTONS
       WHITE + BLACK
       ===================================================== */

    .stButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 9px !important;
        font-weight: 700 !important;
        min-height: 42px !important;
    }

    .stButton > button:hover {
        background: #000000 !important;
        color: #ffffff !important;
        border-color: #000000 !important;
    }

    .stButton > button:active {
        background: #222222 !important;
        color: #ffffff !important;
    }


    /* =====================================================
       PRODUCT CARD
       ===================================================== */

    .product-card {
        background: rgba(255, 255, 255, 0.94) !important;
        border: 2px solid #000000;
        border-radius: 18px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.15);
        color: #000000 !important;
    }

    .product-card * {
        color: #000000 !important;
    }


    /* =====================================================
       EXPANDERS
       ===================================================== */

    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.90) !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
    }

    div[data-testid="stExpander"] * {
        color: #000000 !important;
    }


    /* =====================================================
       ALERTS
       ===================================================== */

    div[data-testid="stAlert"] {
        color: #000000 !important;
    }


    /* =====================================================
       SLIDER
       ===================================================== */

    div[data-testid="stSlider"] {
        color: #000000 !important;
    }

    div[data-testid="stSlider"] * {
        color: #000000 !important;
    }


    /* =====================================================
       CHECKBOX
       ===================================================== */

    div[data-testid="stCheckbox"] * {
        color: #000000 !important;
    }


    /* =====================================================
       TABLES
       ===================================================== */

    table {
        background: #ffffff !important;
        color: #000000 !important;
    }

    th,
    td {
        color: #000000 !important;
        background: #ffffff !important;
    }


    /* =====================================================
       METRICS
       ===================================================== */

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.90);
        border: 2px solid #000000;
        border-radius: 12px;
        padding: 12px;
    }

    [data-testid="stMetric"] * {
        color: #000000 !important;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {
        border-color: rgba(0, 0, 0, 0.35) !important;
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
        <h1 style="
            text-align:center;
            color:#000000;
            font-weight:900;
        ">
        🛍️ LUXEMART
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="
            text-align:center;
            color:#000000;
            font-weight:600;
        ">
        Premium Lifestyle Store
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    if st.button(
        "🏠 SHOP",
        use_container_width=True,
    ):
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

    st.markdown(
        "<h3>Categories</h3>",
        unsafe_allow_html=True,
    )

    for category in CATEGORIES:

        if st.button(
            category,
            key=f"sidebar_category_{category}",
            use_container_width=True,
        ):
            st.session_state.selected_category = category
            st.session_state.page = "Shop"
            st.rerun()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.title("🛍️ LUXEMART")
    st.subheader("Premium Collection")

    st.markdown(
        "Discover fashion, beauty, jewellery, perfumes and lifestyle essentials."
    )

    # -----------------------------------------------------
    # IMAGE SLIDER
    # -----------------------------------------------------

    st.markdown("### ✨ Featured Collection")

    slider_col1, slider_col2, slider_col3 = st.columns(
        [1, 8, 1]
    )

    with slider_col1:

        if st.button(
            "←",
            key="previous_slide",
            use_container_width=True,
        ):
            st.session_state.slider_index = (
                st.session_state.slider_index - 1
            ) % len(SLIDES)

            st.rerun()

    with slider_col2:

        st.image(
            SLIDES[st.session_state.slider_index],
            use_container_width=True,
        )

        st.markdown(
            f"""
            <div style="
                text-align:center;
                color:#000000;
                font-weight:700;
                margin-top:5px;
            ">
            {st.session_state.slider_index + 1}
            / {len(SLIDES)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with slider_col3:

        if st.button(
            "→",
            key="next_slide",
            use_container_width=True,
        ):
            st.session_state.slider_index = (
                st.session_state.slider_index + 1
            ) % len(SLIDES)

            st.rerun()

    st.divider()

    # -----------------------------------------------------
    # FILTERS
    # -----------------------------------------------------

    st.markdown("### 🔎 Find Products")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:

        search_text = st.text_input(
            "Search",
            placeholder="Type product name or category...",
            key="search_products",
        )

    with filter_col2:

        category_filter = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(
                st.session_state.selected_category
            ),
            key="category_filter",
        )

    filter_col3, filter_col4 = st.columns(2)

    with filter_col3:

        sort_filter = st.selectbox(
            "Sort By",
            [
                "Default",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A to Z",
            ],
            key="sort_filter",
        )

    with filter_col4:

        price_range = st.slider(
            "💰 Price Range",
            min_value=0,
            max_value=10000,
            value=(0, 10000),
            step=500,
            format="Rs. %d",
            key="price_filter",
        )

    # -----------------------------------------------------
    # FILTER LOGIC
    # -----------------------------------------------------

    filtered_products = PRODUCTS.copy()

    if search_text.strip():

        search_value = search_text.strip().lower()

        filtered_products = [
            product
            for product in filtered_products
            if (
                search_value in product["name"].lower()
                or search_value in product["category"].lower()
            )
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
        if minimum_price
        <= product["price"]
        <= maximum_price
  ]

    # -----------------------------------------------------
    # SORT
    # -----------------------------------------------------

    if sort_filter == "Price: Low to High":

        filtered_products.sort(
            key=lambda product: product["price"]
        )

    elif sort_filter == "Price: High to Low":

        filtered_products.sort(
            key=lambda product: product["price"],
            reverse=True,
        )

    elif sort_filter == "Name: A to Z":

        filtered_products.sort(
            key=lambda product: product["name"].lower()
        )

    st.markdown(
        f"""
        <p style="
            color:#000000;
            font-weight:700;
            font-size:17px;
        ">
        {len(filtered_products)} product(s) found
        </p>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # PRODUCT GRID
    # -----------------------------------------------------

    if not filtered_products:

        st.warning(
            "No products found. Try another search or filter."
        )

    else:

        columns = st.columns(4)

        for index, product in enumerate(filtered_products):

            with columns[index % 4]:

                st.markdown(
                    """
                    <div class="product-card">
                    """,
                    unsafe_allow_html=True,
                )

                show_product_image(
                    product["image"]
                )

                st.markdown(
                    f"""
                    <h3 style="
                        color:#000000;
                        margin-top:10px;
                    ">
                    {product["name"]}
                    </h3>

                    <p style="
                        color:#000000;
                        font-weight:600;
                    ">
                    {product["category"]}
                    </p>

                    <h3 style="
                        color:#000000;
                    ">
                    {money(product["price"])}
                    </h3>
                    """,
                    unsafe_allow_html=True,
                )

                favorite_icon = (
                    "❤️"
                    if product["id"]
                    in st.session_state.favorites
                    else "♡"
                )

                col_a, col_b = st.columns(2)

                with col_a:

                    if st.button(
                        favorite_icon,
                        key=f"favorite_{product['id']}",
                        use_container_width=True,
                    ):
                        toggle_favorite(
                            product["id"]
                        )
                        st.rerun()

                with col_b:

                    if st.button(
                        "ADD",
                        key=f"add_{product['id']}",
                        use_container_width=True,
                    ):
                        add_to_cart(
                            product["id"]
                        )
                        st.rerun()

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )


# =========================================================
# FAVORITES
# =========================================================

elif st.session_state.page == "Favorites":

    st.title("❤️ My Favorites")

    if not st.session_state.favorites:

        st.info(
            "You have not added any favorite products yet."
        )

    else:

        favorite_products = [
            get_product(product_id)
            for product_id
            in st.session_state.favorites
        ]

        favorite_products = [
            product
            for product in favorite_products
            if product is not None
        ]

        columns = st.columns(4)

        for index, product in enumerate(
            favorite_products
        ):

            with columns[index % 4]:

                st.markdown(
                    '<div class="product-card">',
                    unsafe_allow_html=True,
                )

                show_product_image(
                    product["image"]
                )

                st.markdown(
                    f"""
                    <h3>{product["name"]}</h3>
                    <p>{product["category"]}</p>
                    <h3>{money(product["price"])}</h3>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "🛒 ADD TO CART",
                    key=f"fav_cart_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(
                        product["id"]
                    )
                    st.rerun()

                if st.button(
                    "REMOVE ❤️",
                    key=f"remove_fav_{product['id']}",
                    use_container_width=True,
                ):
                    st.session_state.favorites.remove(
                        product["id"]
                    )
                    st.rerun()

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.title("🛒 Your Cart")

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button(
            "CONTINUE SHOPPING",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        st.markdown("### Selected Products")

        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            if product is None:
                continue

            col1, col2, col3 = st.columns(
                [5, 2, 1]
            )

            with col1:

                st.markdown(
                    f"""
                    <div style="
                        background:rgba(255,255,255,0.92);
                        padding:12px;
                        border:2px solid #000000;
                        border-radius:10px;
                    ">
                    <strong>
                    🛍️ {product["name"]}
                    </strong>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:

                st.markdown(
                    f"""
                    <div style="
                        background:#ffffff;
                        padding:12px;
                        border:2px solid #000000;
                        border-radius:10px;
                        text-align:center;
                        color:#000000;
                        font-weight:700;
                    ">
                    {money(product["price"])}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col3:

                if st.button(
                    "REMOVE",
                    key=f"remove_{index}",
                    use_container_width=True,
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

        st.divider()

        total = cart_total()

        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border:3px solid #000000;
                border-radius:14px;
                padding:18px;
                text-align:center;
                color:#000000;
            ">
                <h2 style="color:#000000;">
                    Total: {money(total)}
                </h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.subheader("📦 Checkout")

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Enter your full name",
            key="customer_name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number",
            key="customer_phone",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter complete delivery address",
            height=120,
            key="customer_address",
        )

        st.markdown(
            """
            <p style="
                color:#000000;
                font-size:14px;
                font-weight:600;
            ">
            Your information will be used for order delivery.
            </p>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "🛍️ PLACE ORDER",
            use_container_width=True,
        ):

            if not customer_name.strip():

                st.error(
                    "Please enter customer name."
                )

            elif not customer_phone.strip():

                st.error(
                    "Please enter phone number."
                )

            elif not customer_address.strip():

                st.error(
                    "Please enter delivery address."
                )

            else:

                try:

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

                        st.error(
                            "Order could not be created."
                        )

                    else:

                        order_id = (
                            order_response
                            .data[0]
                            .get("id")
                        )

                        for product_id in (
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

                        st.session_state.cart = []

                        st.success(
                            "🎉 Order placed successfully!"
                        )

                        st.balloons()

                except Exception as error:

                    st.error(
                        f"Order error: {error}"
                    )


# =========================================================
# ABOUT
# =========================================================

elif st.session_state.page == "About":

    st.title("ℹ️ About LUXEMART")

    st.markdown(
        """
        ## 🛍️ LUXEMART

        Welcome to LUXEMART — your premium online lifestyle
        shopping store.

        We offer carefully selected products across:

        - 👗 Clothes
        - 👜 Fashion
        - 💎 Jewellery
        - ⌚ Accessories
        - 🌹 Perfumes
        - 💄 Beauty

        ### 📞 Contact

        **Phone:** 03169707804

        **Email:** asyabibi485@gmail.com
        """
    )

    st.divider()

    st.markdown(
        """
        <div style="
            background:rgba(255,255,255,0.90);
            border:2px solid #000000;
            border-radius:15px;
            padding:20px;
            text-align:center;
        ">
            <h2 style="color:#000000;">
            Thank you for shopping with LUXEMART ❤️
            </h2>

            <p style="color:#000000;">
            Premium products. Elegant lifestyle.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# ADMIN
# =========================================================

elif st.session_state.page == "Admin":

    st.title("🔐 Admin Panel")

    if not st.session_state.admin_logged_in:

        st.subheader("Admin Login")

        admin_email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email",
            key="admin_email",
        )

        admin_password = st.text_input(
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

                response = (
                    supabase.auth.sign_in_with_password(
                        {
                            "email":
                                admin_email.strip(),

                            "password":
                                admin_password,
                        }
                    )
                )

                if response.user is None:

                    st.error(
                        "Invalid email or password."
                    )

                elif (
                    response.user.email.lower()
                    != ADMIN_EMAIL.lower()
                ):

                    st.error(
                        "This account is not authorized as admin."
                    )

                    try:
                        supabase.auth.sign_out()
                    except Exception:
                        pass

                else:

                    st.session_state.admin_logged_in = True

                    st.success(
                        "Admin login successful."
                    )

                    st.rerun()

            except Exception as error:

                st.error(
                    f"Login error: {error}"
                )

    else:

        st.success(
            "Admin logged in successfully."
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔄 REFRESH ORDERS",
                use_container_width=True,
            ):
                st.rerun()

        with col2:

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
            "📋 Client Requests Received"
        )

        try:

            orders_response = (
                supabase
                .table("orders")
                .select("*")
                .order(
                    "created_at",
                    desc=True,
                )
                .execute()
            )

            orders = orders_response.data or []

            if not orders:

                st.info(
                    "No customer orders received yet."
                )

            else:

                st.markdown(
                    f"""
                    <div style="
                        background:#ffffff;
                        border:2px solid #000000;
                        border-radius:12px;
                        padding:15px;
                        text-align:center;
                        margin-bottom:20px;
                    ">
                    <h2 style="color:#000000;">
                    {len(orders)} Order(s)
                    </h2>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                for order in orders:

                    order_id = order.get(
                        "id",
                        "N/A",
                    )

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

                    with st.expander(
                        f"🛍️ Order #{order_id} — {customer_name}"
                    ):

                        st.markdown(
                            f"""
                            <div style="
                                background:#ffffff;
                                border:2px solid #000000;
                                border-radius:10px;
                                padding:15px;
                                color:#000000;
                            ">

                            <p style="color:#000000;">
                            <strong>Customer:</strong>
                            {customer_name}
                            </p>

                            <p style="color:#000000;">
                            <strong>Phone:</strong>
                            {customer_phone}
                            </p>

                            <p style="color:#000000;">
                            <strong>Address:</strong>
                            {customer_address}
                            </p>

                            <p style="color:#000000;">
                            <strong>Total:</strong>
                            {money(total_amount)}
                            </p>

                            <p style="color:#000000;">
                            <strong>Date:</strong>
                            {created_at}
                            </p>

                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                        st.markdown(
                            "### 🛒 Ordered Products"
                        )

                        try:

                            items_response = (
                                supabase
                                .table("order_items")
                                .select("*")
                                .eq(
                                    "order_id",
                                    order_id,
                                )
                                .execute()
                            )
