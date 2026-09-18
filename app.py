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
# SUPABASE
# =========================================================
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
ADMIN_EMAIL = st.secrets["admin"]["email"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# =========================================================
# SESSION STATE
# =========================================================
defaults = {
    "page": "Shop",
    "cart": [],
    "favorites": [],
    "admin_logged_in": False,
    "slider_index": 0,
    "selected_category": "All",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


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
# FUNCTIONS
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

        if product:
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
        st.toast("Already in cart")


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
    st.session_state.page = "Shop"
    st.rerun()


# =========================================================
# MODERN CSS
# =========================================================
st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap'
    );

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 196, 218, 0.55),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 5%,
                rgba(190, 190, 255, 0.45),
                transparent 28%
            ),
            radial-gradient(
                circle at 80% 85%,
                rgba(174, 224, 255, 0.40),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #fff4f8 0%,
                #f7f3ff 50%,
                #f1f9ff 100%
            );

        color: #111111;
        font-family: 'DM Sans', sans-serif;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #fff0f6 0%,
                #f3efff 50%,
                #edf9ff 100%
            );

        border-right: 1px solid rgba(255,255,255,0.9);
    }

    .brand {
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        font-family: 'Playfair Display', serif;
        font-size: 30px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #17121b;
        padding: 8px 0 2px 0;
    }

    .brand-small {
        text-align: center;
        color: #7a707d;
        font-size: 11px;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    .main-brand {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 48px;
        font-weight: 700;
        letter-spacing: 5px;
        color: #17121b;
        margin-top: 5px;
        margin-bottom: 2px;
    }

    .main-tagline {
        text-align: center;
        color: #766d78;
        font-size: 12px;
        letter-spacing: 3px;
        margin-bottom: 25px;
    }

    .hero-box {
        background: rgba(255,255,255,0.70);
        border: 1px solid rgba(255,255,255,0.95);
        border-radius: 28px;
        padding: 10px;
        box-shadow: 0 18px 55px rgba(70,50,90,0.10);
        margin-bottom: 22px;
    }

    .section-heading {
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        font-weight: 600;
        color: #17121b;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .product-box {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 12px;
        margin-bottom: 8px;
        box-shadow: 0 10px 32px rgba(70,50,90,0.08);
    }

    .product-title {
        font-size: 17px;
        font-weight: 700;
        color: #18131b;
        margin-top: 8px;
    }

    .product-category {
        color: #887e8c;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-top: 2px;
    }

    .product-price {
        color: #17121b;
        font-size: 18px;
        font-weight: 700;
        margin-top: 5px;
    }

    .info-box {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 10px 32px rgba(70,50,90,0.07);
        margin-bottom: 18px;
    }

    .total-box {
        background: #17131a;
        color: white;
        border-radius: 20px;
        padding: 22px;
        margin: 15px 0 22px 0;
    }

    .total-small {
        color: #d5cdd8;
        font-size: 12px;
        letter-spacing: 1px;
    }

    .total-large {
        font-size: 28px;
        font-weight: 700;
        margin-top: 4px;
    }

    .admin-box {
        background: rgba(255,255,255,0.84);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 10px 32px rgba(70,50,90,0.07);
        margin-bottom: 18px;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stNumberInput"] input {
        background: #ffffff !important;
        color: #111111 !important;
        border: 1px solid #e4dce8 !important;
        border-radius: 13px !important;
    }

    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #b996c8 !important;
        box-shadow: 0 0 0 3px rgba(185,150,200,0.15) !important;
    }

    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        color: #111111 !important;
        border-radius: 13px !important;
    }

    .stButton > button {
        border-radius: 13px !important;
        min-height: 42px !important;
        font-weight: 600 !important;
        border: 1px solid #e5dce8 !important;
        background: #ffffff !important;
        color: #18131b !important;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(70,50,90,0.12);
        border-color: #c5a8d0 !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255,255,255,0.60) !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: #ffffff !important;
    }

    img {
        border-radius: 16px;
    }

    @media (max-width: 768px) {
        .main-brand {
            font-size: 34px;
            letter-spacing: 3px;
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
        '<div class="brand">🛍️ LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="brand-small">PREMIUM LIFESTYLE STORE</div>',
        unsafe_allow_html=True,
    )

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

    if st.button("✨  About", use_container_width=True):
        go_to("About")

    st.markdown("---")

    st.markdown("### Collections")

    for category in CATEGORIES:

        if st.button(
            category,
            key=f"category_{category}",
            use_container_width=True,
        ):
            st.session_state.selected_category = category
            st.session_state.page = "Shop"
            st.rerun()

    st.markdown("---")

    st.caption("Elegant • Modern • Premium")


# =========================================================
# SHOP PAGE
# =========================================================
if st.session_state.page == "Shop":

    st.markdown(
        '<div class="main-brand">🛍️ LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-tagline">PREMIUM LIFESTYLE STORE</div>',
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # HERO IMAGE
    # -----------------------------------------------------
    current_slide = SLIDES[st.session_state.slider_index]

    st.markdown('<div class="hero-box">', unsafe_allow_html=True)

    st.image(
        current_slide,
        use_container_width=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)

    previous_col, count_col, next_col = st.columns(
        [1, 2, 1]
    )

    with previous_col:

        if st.button(
            "‹ Previous",
            use_container_width=True,
        ):
            st.session_state.slider_index = (
                st.session_state.slider_index - 1
            ) % len(SLIDES)

            st.rerun()

    with count_col:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding-top:10px;
                color:#766d78;
                font-size:13px;
                font-weight:600;
            ">
                {st.session_state.slider_index + 1}
                / {len(SLIDES)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with next_col:

        if st.button(
            "Next ›",
            use_container_width=True,
        ):
            st.session_state.slider_index = (
                st.session_state.slider_index + 1
            ) % len(SLIDES)

            st.rerun()

    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-heading">Discover Your Collection</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col, sort_col = st.columns(
        [2.2, 1.2, 1.2]
    )

    with search_col:

        search_text = st.text_input(
            "Search",
            placeholder="Search handbags, perfumes, jewellery...",
            label_visibility="collapsed",
        )

    with category_col:

        category_filter = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(
                st.session_state.selected_category
            ),
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
        1000,
        10000,
        (1000, 10000),
        500,
    )

    # -----------------------------------------------------
    # FILTER PRODUCTS
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

    filtered_products = [
        product
        for product in filtered_products
        if price_range[0]
        <= product["price"]
        <= price_range[1]
    ]

    if sort_filter == "Price: Low to High":

        filtered_products.sort(
            key=lambda item: item["price"]
        )

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
    # CATEGORY BUTTONS
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-heading">Shop by Category</div>',
        unsafe_allow_html=True,
    )

    category_columns = st.columns(len(CATEGORIES))

    for index, category in enumerate(CATEGORIES):

        with category_columns[index]:

            if st.button(
                category,
                key=f"shop_category_{category}",
                use_container_width=True,
            ):
                st.session_state.selected_category = category
                st.rerun()

    st.caption(
        f"{len(filtered_products)} products available"
    )

    # -----------------------------------------------------
    # PRODUCTS
    # -----------------------------------------------------
    if not filtered_products:

        st.markdown(
            """
            <div class="info-box" style="text-align:center;">
                <h3>No products found</h3>
                <p>Try another search or category.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        for start in range(
            0,
            len(filtered_products),
            4,
        ):

            product_row = filtered_products[
                start:start + 4
            ]

            columns = st.columns(4)

            for column, product in zip(
                columns,
                product_row,
            ):

                with column:

                    # Product image is rendered by Streamlit.
                    # No raw HTML is used here.
                    st.image(
                        product["image"],
                        use_container_width=True,
                    )

                    st.markdown(
                        '<div class="product-box">',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<div class="product-title">{product["name"]}</div>',
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

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True,
                    )

                    add_col, fav_col = st.columns(2)

                    with add_col:
if st.button(
                            "🛒 Add",
                            key=f"add_product_{product['id']}",
                            use_container_width=True,
                        ):
                            add_to_cart(product["id"])

                    with fav_col:

                        if (
                            product["id"]
                            in st.session_state.favorites
                        ):
                            favorite_icon = "❤️"
                        else:
                            favorite_icon = "♡"

                        if st.button(
                            favorite_icon,
                            key=f"favorite_product_{product['id']}",
                            use_container_width=True,
                        ):
                            toggle_favorite(
                                product["id"]
                            )
                            st.rerun()


# =========================================================
# FAVORITES
# =========================================================
elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="main-brand">❤️ FAVORITES</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-tagline">YOUR SAVED LUXEMART COLLECTION</div>',
        unsafe_allow_html=True,
    )

    favorite_products = []

    for product_id in st.session_state.favorites:

        product = get_product(product_id)

        if product:
            favorite_products.append(product)

    if not favorite_products:

        st.markdown(
            """
            <div class="info-box" style="text-align:center;">
                <h3>♡ No favorites yet</h3>
                <p>
                    Tap the heart button on products
                    you love.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Explore LUXEMART",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        for start in range(
            0,
            len(favorite_products),
            4,
        ):

            row = favorite_products[
                start:start + 4
            ]

            columns = st.columns(4)

            for column, product in zip(
                columns,
                row,
            ):

                with column:

                    st.image(
                        product["image"],
                        use_container_width=True,
                    )

                    st.markdown(
                        f'<div class="product-title">{product["name"]}</div>',
                        unsafe_allow_html=True,
                    )

                    st.caption(
                        product["category"]
                    )

                    st.markdown(
                        f"**{money(product['price'])}**"
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
        '<div class="main-brand">🛒 CART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-tagline">YOUR LUXEMART ORDER</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.markdown(
            """
            <div class="info-box" style="text-align:center;">
                <h3>Your cart is empty</h3>
                <p>
                    Add something beautiful to your cart.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "Continue Shopping",
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
                [1.2, 4, 1]
            )

            with col1:

                st.image(
                    product["image"],
                    use_container_width=True,
                )

            with col2:

                st.markdown(
                    f"### {product['name']}"
                )

                st.caption(
                    product["category"]
                )

                st.write(
                    money(product["price"])
                )

            with col3:

                if st.button(
                    "Remove",
                    key=f"cart_remove_{index}",
                    use_container_width=True,
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

            st.divider()

        total = cart_total()

        st.markdown(
            f"""
            <div class="total-box">

                <div class="total-small">
                    ORDER TOTAL
                </div>

                <div class="total-large">
                    {money(total)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-heading">Delivery Details</div>',
            unsafe_allow_html=True,
        )

        customer_name = st.text_input(
            "Full Name",
            placeholder="Your full name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Complete delivery address",
        )

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
                    "Please complete all delivery details."
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

                        st.error(
                            "Order could not be created."
                        )

                    else:

                        order_id = (
                            order_response
                            .data[0]["id"]
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
                            "🎉 Order placed successfully!"
                        )

                        st.balloons()

                        st.rerun()

                except Exception as error:

                    st.error(
                        f"Order error: {error}"
                    )


# =========================================================
# ABOUT
# =========================================================
elif st.session_state.page == "About":

    st.markdown(
        '<div class="main-brand">LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-tagline">ABOUT OUR STORE</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
            <div class="info-box">

                <h3>✨ Our Story</h3>

                <p>
                    LUXEMART is a modern lifestyle shopping
                    experience bringing fashion, jewellery,
                    beauty, accessories and fragrances together.
                </p>

                <p>
                    Our focus is a simple, elegant and enjoyable
                    shopping experience.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:

        st.markdown(
            """
            <div class="info-box">

                <h3>💎 Why LUXEMART?</h3>

                <p>✨ Elegant products</p>
                <p>🛍️ Simple shopping</p>
                <p>❤️ Favorites</p>
                <p>🚚 Easy checkout</p>
                <p>💎 Premium interface</p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="info-box">

            <h3>📞 Contact</h3>

            <p>
                <strong>Phone:</strong> 03169707804
            </p>

            <p>
                <strong>Email:</strong> asyabibi485@gmail.com
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
        '<div class="main-brand">🔐 ADMIN</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-tagline">LUXEMART MANAGEMENT</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.admin_logged_in:

        st.markdown(
            """
            <div class="admin-box">

                <h3>Administrator Login</h3>

                <p>
                    Authorized administrator access only.
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

        admin_email = st.text_input(
            "Admin Email",
            placeholder="Admin email",
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            placeholder="Password",
        )

        if st.button(
            "Sign In",
            use_container_width=True,
        ):

            if (
                not admin_email.strip()
                or not admin_password
            ):

                st.error(
                    "Enter email and password."
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

                    if (
                        user
                        and user.email
                        and user.email.lower()
                        == ADMIN_EMAIL.lower()
                    ):

                        st.session_state.admin_logged_in = True

                        st.success(
                            "Admin login successful."
                        )

                        st.rerun()

                    else:

                        try:
                            supabase.auth.sign_out()
                        except Exception:
                            pass

                        st.error(
                            "This account is not authorized."
                        )

                except Exception as error:

                    st.error(
                        f"Login error: {error}"
                    )

    else:

        if st.button(
            "Logout",
            use_container_width=True,
        ):
            logout_admin()

        st.markdown(
            '<div class="section-heading">Client Requests Received</div>',
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
                    "No customer orders yet."
                )

            else:

                for number, order in enumerate(
                    orders,
                    1,
                ):

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
                        <div class="admin-box">

                            <h3>
                                Order #{number}
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
                            .eq(
                                "order_id",
                                order_id,
                            )
                            .execute()
                        )

                        items = (
                            items_response.data
                            or []
                        )

                        if items:

                            with st.expander(
                                "View ordered products"
                            ):

                                for item in items:

                                    item_name = item.get(
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
                                        f"🛍️ {item_name} "
                                        f"— {money(float(item_price))} "
                                        f"× {quantity}"
                                    )

                    except Exception as error:

                        st.warning(
                            f"Order items error: {error}"
                        )

        except Exception as error:

            st.error(
                f"Unable to load orders: {error}"
            )


# =========================================================
# FOOTER ADMIN BUTTON
# =========================================================
st.markdown("---")

footer_left, footer_center, footer_right = st.columns(
    [1, 2, 1]
)

with footer_center:

    if st.button(
        "🔐 Admin Login",
        use_container_width=True,
    ):
        st.session_state.page = "Admin"
        st.rerun()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#817783;
        font-size:12px;
        padding:12px;
    ">
        LUXEMART • Elegant • Modern • Premium
    </div>
    """,
    unsafe_allow_html=True,
)
