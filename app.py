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
# SLIDER
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

        st.image(
            image_path,
            use_container_width=True,
        )

    elif os.path.exists(image_path):

        st.image(
            image_path,
            use_container_width=True,
        )

    else:

        st.markdown(
            """
            <div class="image-placeholder">
                🛍️
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# WHITE + BLACK DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background: #ffffff !important;
        color: #000000 !important;
    }

    html,
    body,
    [class*="css"],
    p,
    span,
    label,
    div {
        color: #000000;
    }


    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #dddddd;
    }

    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }


    /* -------------------------------------------------------
       HEADINGS
    ------------------------------------------------------- */

    .luxury-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #000000 !important;
        margin-bottom: 5px;
    }

    .luxury-subtitle {
        font-size: 15px;
        color: #000000 !important;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 900;
        color: #000000 !important;
        margin-top: 15px;
        margin-bottom: 20px;
    }


    /* -------------------------------------------------------
       SEARCH / FILTER AREA
       ------------------------------------------------------- */

    .filter-title {
        font-size: 20px;
        font-weight: 900;
        color: #000000 !important;
        margin-bottom: 12px;
    }

    .filter-box {
        background: #ffffff;
        border: 1px solid #d9d9d9;
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 25px;
    }


    /* -------------------------------------------------------
       PRODUCT CARDS
    ------------------------------------------------------- */

    .product-card {
        background: #ffffff !important;
        border: 1px solid #dddddd;
        border-radius: 18px;
        padding: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    }

    .product-name {
        font-size: 18px;
        font-weight: 900;
        color: #000000 !important;
        margin-top: 10px;
    }

    .product-category {
        font-size: 13px;
        color: #000000 !important;
        opacity: 0.65;
    }

    .product-price {
        font-size: 19px;
        font-weight: 900;
        color: #000000 !important;
        margin-top: 5px;
    }


    /* -------------------------------------------------------
       IMAGE PLACEHOLDER
    ------------------------------------------------------- */

    .image-placeholder {
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 15px;
        font-size: 60px;
        color: #000000 !important;
    }


    /* -------------------------------------------------------
       SLIDER
    ------------------------------------------------------- */

    .slider-box {
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid #dddddd;
        margin-bottom: 20px;
        background: #ffffff;
    }


    /* -------------------------------------------------------
       CART
    ------------------------------------------------------- */

    .cart-total {
        background: #ffffff;
        border: 2px solid #000000;
        border-radius: 15px;
        padding: 20px;
        font-size: 24px;
        font-weight: 900;
        color: #000000 !important;
        margin-top: 20px;
    }


    /* -------------------------------------------------------
       ADMIN
    ------------------------------------------------------- */

    .admin-box {
        background: #ffffff;
        color: #000000 !important;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }


    /* -------------------------------------------------------
       BUTTONS
    ------------------------------------------------------- */

    div.stButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 10px;
        font-weight: 800;
    }

    div.stButton > button:hover {
        background: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #000000 !important;
    }


    /* -------------------------------------------------------
       TEXT INPUTS
    ------------------------------------------------------- */

    div[data-baseweb="input"] {
        background: #ffffff !important;
        border: 1px solid #000000 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] input {
        background: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    div[data-baseweb="input"] input::placeholder {
        color: #555555 !important;
        -webkit-text-fill-color: #555555 !important;
    }


    /* -------------------------------------------------------
       TEXT AREA
    ------------------------------------------------------- */

    div[data-baseweb="textarea"] {
        background: #ffffff !important;
        border: 1px solid #000000 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="textarea"] textarea {
        background: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    div[data-baseweb="textarea"] textarea::placeholder {
        color: #555555 !important;
        -webkit-text-fill-color: #555555 !important;
    }


    /* -------------------------------------------------------
       SELECTBOX
    ------------------------------------------------------- */

    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] span {
        color: #000000 !important;
    }


    /* -------------------------------------------------------
       SLIDER
    ------------------------------------------------------- */

    div[data-testid="stSlider"] {
        color: #000000 !important;
    }


    /* -------------------------------------------------------
       CHECKBOX
    ------------------------------------------------------- */

    div[data-testid="stCheckbox"] label {
        color: #000000 !important;
    }


    /* -------------------------------------------------------
       ALERTS
    ------------------------------------------------------- */

    div[data-testid="stAlert"] {
        color: #000000 !important;
        background: #ffffff !important;
        border: 1px solid #dddddd;
    }


    /* -------------------------------------------------------
       DIVIDERS
    ------------------------------------------------------- */

    hr {
        border-color: #dddddd !important;
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
            color:#000000;
            margin-bottom:5px;
        ">
        LUXEMART
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            color:#000000;
            font-size:13px;
            margin-bottom:15px;
        ">
        Premium Lifestyle Store
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    if st.button(
        "🛍️ SHOP",
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
        """
        <div style="
            font-size:18px;
            font-weight:900;
            color:#000000;
            margin-bottom:10px;
        ">
        CATEGORIES
        </div>
        """,
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


# ============================================================
# SHOP PAGE
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        '<div class="luxury-title">LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="luxury-subtitle">
        Premium fashion, beauty, jewellery and lifestyle essentials.
        </div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # FILTERS
    # ========================================================

    st.markdown(
        """
        <div class="filter-box">
        <div class="filter-title">
        🔎 FIND YOUR PRODUCT
        </div>
        """,
        unsafe_allow_html=True,
    )

    filter_col1, filter_col2, filter_col3 = st.columns(
        [2, 1, 1]
    )

    with filter_col1:

        search_text = st.text_input(
            "Search products",
            placeholder="Search handbag, abaya, perfume...",
            key="product_search",
        )

    with filter_col2:

        filter_category = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(
                st.session_state.selected_category
            ),
            key="filter_category",
        )

    with filter_col3:

        sort_option = st.selectbox(
            "Sort By",
            [
                "Default",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A to Z",
            ],
            key="sort_products",
        )

    st.markdown(
        """
        <div style="
            margin-top:10px;
            margin-bottom:5px;
            font-weight:800;
            color:#000000;
        ">
        💰 Price Range
        </div>
        """,
        unsafe_allow_html=True,
    )

    price_range = st.slider(
        "Price Range",
        min_value=0,
        max_value=10000,
        value=(0, 10000),
        step=500,
        format="Rs. %d",
        key="price_range",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


    # ========================================================
    # FILTER PRODUCTS
    # ========================================================

    filtered_products = PRODUCTS.copy()

    # Search
    if search_text.strip():

        search_value = search_text.strip().lower()

        filtered_products = [
            product
            for product in filtered_products
            if search_value in product["name"].lower()
            or search_value in product["category"].lower()
        ]


    # Category
    if filter_category != "All":

        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == filter_category
        ]


    # Price
    minimum_price = price_range[0]
    maximum_price = price_range[1]

    filtered_products = [
        product
        for product in filtered_products
        if minimum_price
        <= product["price"]
        <= maximum_price
    ]


    # Sorting
    if sort_option == "Price: Low to High":

        filtered_products.sort(
            key=lambda product: product["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered_products.sort(
            key=lambda product: product["price"],
            reverse=True,
        )

    elif sort_option == "Name: A to Z":

        filtered_products.sort(
            key=lambda product: product["name"].lower()
        )


    # ========================================================
    # RESULT COUNT
    # ========================================================

    st.markdown(
        f"""
        <div style="
            color:#000000;
            font-weight:800;
            margin-bottom:15px;
        ">
        Showing {len(filtered_products)} product(s)
        </div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # IMAGE SLIDER
    # ========================================================

    if not search_text.strip() and filter_category == "All":

        st.markdown(
            '<div class="slider-box">',
            unsafe_allow_html=True,
        )

        st.image(
            SLIDES[st.session_state.slider_index],
            use_container_width=True,
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

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
                    font-weight:800;
                    color:#000000;
                ">
                {st.session_state.slider_index + 1}
                /
                {len(SLIDES)}
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


    # ========================================================
    # COLLECTION TITLE
    # ========================================================

    if filter_category == "All":

        collection_name = "ALL COLLECTION"

    else:

        collection_name = (
            f"{filter_category.upper()} COLLECTION"
        )

    st.markdown(
        f"""
        <div class="section-title">
        {collection_name}
        </div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # PRODUCTS
    # ========================================================

    if not filtered_products:

        st.warning(
            "No products match your filters."
        )

        if st.button(
            "CLEAR FILTERS",
            use_container_width=True,
        ):

            st.session_state.product_search = ""
            st.session_state.filter_category = "All"
            st.session_state.sort_products = "Default"
            st.session_state.price_range = (
                0,
                10000,
            )

            st.rerun()

    else:

        for start in range(
            0,
            len(filtered_products),
            4,
        ):

            row_products = filtered_products[
                start:start + 4
            ]

            columns = st.columns(4)

            for column, product in zip(
                columns,
                row_products,
            ):

                with column:

                    st.markdown(
                        '<div class="product-card">',
                        unsafe_allow_html=True,
                    )

                    show_product_image(
                        product["image"]
                    )

                    st.markdown(
                        f"""
                        <div class="product-name">
                        {product["name"]}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f"""
                        <div class="product-category">
                        {product["category"]}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f"""
                        <div class="product-price">
                        {money(product["price"])}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    button_col1, button_col2 = st.columns(
                        2
                    )

                    with button_col1:

                        if st.button(
                            "🛒 ADD",
                            key=f"add_{product['id']}",
                            use_container_width=True,
                        ):

                            add_to_cart(
                                product["id"]
                            )

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

                            toggle_favorite(
                                product["id"]
                            )

                            st.rerun()

                 
