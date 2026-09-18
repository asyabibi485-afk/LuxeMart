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
# SUPABASE
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


SLIDES = [
    "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
    "https://images.pexels.com/photos/904350/pexels-photo-904350.jpeg",
    "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
    "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
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
        return

    if os.path.exists(image_path):
        st.image(
            image_path,
            use_container_width=True,
        )
        return

    st.markdown(
        """
        <div class="image-placeholder">
            🛍️
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #ffffff !important;
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #dddddd;
    }

    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }

    p, span, label, div {
        color: #000000;
    }

    .luxury-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #000000 !important;
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

    .filter-box {
        background: #ffffff !important;
        border: 1px solid #cccccc;
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 25px;
    }

    .filter-title {
        font-size: 20px;
        font-weight: 900;
        color: #000000 !important;
        margin-bottom: 12px;
    }

    .product-card {
        background: #ffffff !important;
        border: 1px solid #dddddd;
        border-radius: 18px;
        padding: 12px;
        margin-bottom: 20px;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.06);
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

    .image-placeholder {
        height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 15px;
        font-size: 60px;
    }

    .slider-box {
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid #dddddd;
        margin-bottom: 20px;
        background: #ffffff;
    }

    .cart-total {
        background: #ffffff !important;
        border: 2px solid #000000;
        border-radius: 15px;
        padding: 20px;
        font-size: 24px;
        font-weight: 900;
        color: #000000 !important;
        margin-top: 20px;
    }

    .admin-box {
        background: #ffffff !important;
        color: #000000 !important;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
    }

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
    }

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

    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] span {
        color: #000000 !important;
    }

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
        ">
        LUXEMART
        </div>

        <div style="
            font-size:13px;
            color:#000000;
            margin-bottom:15px;
        ">
        Premium Lifestyle Store
        </div>
        """,
        unsafe_allow_html=True,
    )

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
            key=f"sidebar_{category}",
            use_container_width=True,
        ):
            st.session_state.selected_category = category
            st.session_state.page = "Shop"
            st.rerun()


# ============================================================
# SHOP
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

    # --------------------------------------------------------
    # FILTER
    # --------------------------------------------------------

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
            "Search",
            placeholder="Search product...",
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

    price_range = st.slider(
        "💰 Price Range",
        min_value=0,
        max_value=10000,
        value=(0, 10000),
        step=500,
        format="Rs. %d",
        key="price_filter",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # APPLY FILTERS
    # --------------------------------------------------------

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

    st.write(
        f"**{len(filtered_products)} product(s) found**"
    )

    # --------------------------------------------------------
    # SLIDER
    # --------------------------------------------------------

    if not search_text.strip() and category_filter == "All":

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

        slide_col1, slide_col2, slide_col3 = st.columns(
            [1, 2, 1]
        )

        with slide_col1:

            if st.button(
                "← PREVIOUS",
                use_container_width=True,
            ):

                st.session_state.slider_index = (
                    st.session_state.slider_index - 1
                ) % len(SLIDES)

                st.rerun()

        with slide_col2:

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    padding:10px;
                    font-weight:800;
                    color:#000000;
                ">
                {st.session_state.slider_index + 1}
                / {len(SLIDES)}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with slide_col3:

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
    # PRODUCTS
    # --------------------------------------------------------

    if not filtered_products:

        st.warning(
            "No products found with the selected filters."
        )

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

                        if product["id"] in st.session_state.favorites:
                            favorite_icon = "❤️"
                        else:
                            favorite_icon = "♡"

                        if st.button(
                            favorite_icon,
                            key=f"favorite_{product['id']}",
                            use_container_width=True,
                        ):

                            toggle_favorite(
                                product["id"]
                            )

                            st.rerun()

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True,
                    )


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="section-title">❤️ MY FAVORITES</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.favorites:

        st.info(
            "Your favorites list is empty."
        )

        if st.button(
            "CONTINUE SHOPPING",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        favorite_products = []

        for product_id in st.session_state.favorites:

            product = get_product(product_id)

            if product is not None:
                favorite_products.append(product)

        for start in range(
            0,
            len(favorite_products),
            4,
        ):

            row_products = favorite_products[
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
                        <div class="product-price">
                        {money(product["price"])}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    if st.button(
                        "🛒 ADD TO CART",
                        key=f"fav_add_{product['id']}",
                        use_container_width=True,
                    ):
                        add_to_cart(
                            product["id"]
                        )

                    if st.button(
                        "REMOVE ❤️",
                        key=f"fav_remove_{product['id']}",
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


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="section-title">🛒 SHOPPING CART</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "START SHOPPING",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

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

                    st.session_state.cart.pop(
                        index
                    )

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

        st.markdown(
            '<div class="section-title">CUSTOMER INFORMATION</div>',
            unsafe_allow_html=True,
        )

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
            height=120,
            key="customer_address",
        )

        checkout_col1, checkout_col2 = st.columns(2)

        with checkout_col1:

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

                        if order_response.data:

                            order_id = (
                                order_response.data[0]["id"]
                            )

                            for product_id in (
                                st.session_state.cart
                            ):

                                product = get_product(
                                    product_id
                                )

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

                        else:

                            st.error(
                                "Order could not be created."
                            )

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
# ABOUT
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

        Our goal is to provide customers with a simple,
        elegant and convenient shopping experience.

        ### Contact

        📞 **Phone:** 03169707804

        📧 **Email:** asyabibi485@gmail.com

        ### Categories

        👗 Clothes

        👜 Fashion

        💎 Jewellery

        ⌚ Accessories

        🌸 Perfumes

        💄 Beauty
        """
    )


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.markdown(
        '<div class="section-title">🔐 ADMIN PANEL</div>',
        unsafe_allow_html=True,
    )

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
                .order(
                    "created_at",
                    desc=True,
                )
                .execute()
            )

            orders = orders_response.data or []

            if not orders:

                st.info(
                    "No customer orders found."
                )

            else:

                for order in orders:

                    st.markdown(
                        '<div class="admin-box">',
                        unsafe_allow_html=True,
                    )

                    order_id = order.get(
                        "id",
                        "",
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

                    st.markdown(
                        "#### ORDER ITEMS"
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

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True,
                    )

        except Exception as error:

            st.error(
                f"Could not load customer orders: {error}"
            )

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

            elif (
                admin_email.strip().lower()
                != ADMIN_EMAIL.strip().lower()
            ):

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
