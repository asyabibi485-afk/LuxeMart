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

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "page": "Shop",
    "cart": [],
    "favorites": [],
    "admin_logged_in": False,
    "shop_category": "All",
    "search": "",
    "order_success": False,
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
        "image": "https://images.pexels.com/photos/1152077/pexels-photo-1152077.jpeg",
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "image": "https://images.pexels.com/photos/322207/pexels-photo-322207.jpeg",
    },
    {
        "id": 3,
        "name": "Elegant Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "image": "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg",
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
        "image": "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
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
        "image": "https://images.pexels.com/photos/996329/pexels-photo-996329.jpeg",
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
        "image": "https://images.pexels.com/photos/1961795/pexels-photo-1961795.jpeg",
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

        if product:
            total += product["price"]

    return total


def cart_count():
    return len(st.session_state.cart)


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


def safe_image(column, image_url):
    try:
        column.image(
            image_url,
            use_container_width=True,
        )
    except Exception:
        column.markdown(
            """
            <div class="image-fallback">
                🛍️
                <br>
                <span>Image unavailable</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def logout_admin():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.admin_logged_in = False
    st.session_state.page = "Shop"
    st.rerun()


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(255, 210, 225, 0.55),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(220, 205, 255, 0.45),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #fff8fb 0%,
                #f8f4ff 50%,
                #f5f9ff 100%
            );
    }

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #fff0f6 0%,
                #f5efff 50%,
                #eef5ff 100%
            );
        border-right: 1px solid rgba(120,80,150,0.12);
    }

    .luxury-title {
        font-size: 44px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #17131c;
        margin-bottom: 0;
    }

    .luxury-subtitle {
        color: #706879;
        font-size: 15px;
        margin-top: -5px;
        margin-bottom: 20px;
    }

    .hero-box {
        padding: 38px;
        border-radius: 28px;
        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.96),
                rgba(255,239,247,0.94)
            );
        border: 1px solid rgba(100,70,100,0.08);
        box-shadow: 0 15px 40px rgba(50,30,70,0.08);
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 38px;
        font-weight: 900;
        color: #17131c;
    }

    .hero-text {
        font-size: 17px;
        color: #665f6d;
        line-height: 1.7;
    }

    .product-card {
        background: rgba(255,255,255,0.94);
        border: 1px solid rgba(70,50,80,0.08);
        border-radius: 22px;
        padding: 14px;
        margin-bottom: 15px;
        box-shadow: 0 10px 30px rgba(40,30,60,0.07);
    }

    .product-name {
        color: #17131c;
        font-size: 18px;
        font-weight: 800;
    }

    .product-category {
        color: #8a7f8d;
        font-size: 13px;
        margin-top: 3px;
    }

    .product-price {
        color: #9c3c69;
        font-size: 20px;
        font-weight: 900;
        margin-top: 8px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 900;
        color: #17131c;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .info-card {
        padding: 25px;
        border-radius: 22px;
        background: rgba(255,255,255,0.92);
        border: 1px solid rgba(80,50,100,0.08);
        box-shadow: 0 10px 30px rgba(40,30,60,0.06);
        margin-bottom: 18px;
    }

    .info-title {
        font-size: 20px;
        font-weight: 800;
        color: #17131c;
    }

    .info-text {
        color: #68616d;
        line-height: 1.7;
    }

    .image-fallback {
        height: 250px;
        border-radius: 18px;
        background:
            linear-gradient(
                135deg,
                #f7eaf0,
                #eee8fa
            );
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 34px;
        color: #8c7182;
    }

    .image-fallback span {
        font-size: 13px;
    }

    .top-brand {
        font-size: 36px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #17131c;
    }

    .footer {
        text-align: center;
        color: #77707d;
        padding: 35px 10px 15px 10px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="top-brand">
            LUXEMART
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🧭 Navigation")

    if st.button(
        "🏠 Shop",
        key="nav_shop",
        use_container_width=True,
    ):
        go_to("Shop")

    if st.button(
        f"❤️ Favorites ({len(st.session_state.favorites)})",
        key="nav_favorites",
        use_container_width=True,
    ):
        go_to("Favorites")

    if st.button(
        "ℹ️ About",
        key="nav_about",
        use_container_width=True,
    ):
        go_to("About")

    # ADMIN IS NOW IN NAVIGATION
    if st.button(
        "🔐 Admin Dashboard",
        key="nav_admin",
        use_container_width=True,
    ):
        go_to("Admin")

    st.markdown("---")

    st.markdown("### 🛍️ Categories")

    for category in CATEGORIES:

        if st.button(
            category,
            key=f"category_{category}",
            use_container_width=True,
        ):
            st.session_state.shop_category = category
            st.session_state.page = "Shop"
            st.rerun()

    st.markdown("---")

    st.caption("Luxury • Fashion • Beauty • Lifestyle")


# =========================================================
# TOP BAR
# =========================================================

top_left, top_middle, top_cart = st.columns(
    [5, 2, 1.5]
)

with top_left:

    st.markdown(
        """
        <div class="top-brand">
            LUXEMART
        </div>
        """,
        unsafe_allow_html=True,
    )

with top_middle:

    if st.session_state.page != "Shop":

        if st.button(
            "← Continue Shopping",
            key="top_shop",
            use_container_width=True,
        ):
            go_to("Shop")


with top_cart:

    # CART SEPARATELY AT TOP RIGHT
    if st.button(
        f"🛒 Cart ({cart_count()})",
        key="top_cart_button",
        use_container_width=True,
    ):
        go_to("Cart")


st.markdown("---")


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown(
        '<div class="luxury-subtitle">'
        'Luxury • Style • Elegance • Everyday Essentials'
        '</div>',
        unsafe_allow_html=True,
    )

    hero_left, hero_right = st.columns(
        [1.35, 1]
    )

    with hero_left:

        st.markdown(
            """
            <div class="hero-box">

                <div class="hero-title">
                    Discover Your<br>
                    Signature Style ✨
                </div>

                <div class="hero-text">
                    Explore elegant fashion, jewellery,
                    accessories, beauty products and fragrances
                    selected for a modern luxury lifestyle.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with hero_right:

        safe_image(
            hero_right,
            "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
        )

    st.markdown(
        '<div class="section-title">'
        '✨ Explore Collection'
        '</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col, sort_col = st.columns(
        [2, 1, 1]
    )

    with search_col:

        search = st.text_input(
            "Search Products",
            value=st.session_state.search,
            placeholder="Search handbag, perfume, necklace...",
        )

        st.session_state.search = search

    with category_col:

        selected_category = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(
                st.session_state.shop_category
            ),
        )

        st.session_state.shop_category = selected_category

    with sort_col:

        sort_option = st.selectbox(
            "Sort",
            [
                "Featured",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A-Z",
            ],
        )

    max_price = st.slider(
        "Maximum Price",
        min_value=1000,
        max_value=10000,
        value=10000,
        step=500,
    )

    # Filter
    filtered_products = []

    for product in PRODUCTS:

        if selected_category != "All":

            if product["category"] != selected_category:
                continue

        if search.strip():

            search_text = search.strip().lower()

            product_text = (
                product["name"]
                + " "
                + product["category"]
            ).lower()

            if search_text not in product_text:
                continue

        if product["price"] > max_price:
            continue

        filtered_products.append(product)

    # Sort
    if sort_option == "Price: Low to High":

        filtered_products.sort(
            key=lambda x: x["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered_products.sort(
            key=lambda x: x["price"],
            reverse=True,
        )

    elif sort_option == "Name: A-Z":

        filtered_products.sort(
            key=lambda x: x["name"]
        )

    st.caption(
        f"{len(filtered_products)} product(s) available"
    )

    if not filtered_products:

        st.info(
            "No products found. Try another category or search."
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

            for index, product in enumerate(
                row_products
            ):

                column = columns[index]

                safe_image(
                    column,
                    product["image"],
                )

                column.markdown(
                    f"""
                    <div class="product-card">

                        <div class="product-name">
                            {product["name"]}
                        </div>

                        <div class="product-category">
                            {product["category"]}
                        </div>

                        <div class="product-price">
                            {money(product["price"])}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                favorite_icon = (
                    "❤️"
                    if product["id"]
                    in st.session_state.favorites
                    else "♡"
                )

                if column.button(
                    f"{favorite_icon} Favorite",
                    key=f"favorite_{product['id']}",
                    use_container_width=True,
                ):

                    toggle_favorite(
                        product["id"]
                    )

                    st.rerun()

                if column.button(
                    "🛒 Add to Cart",
                    key=f"add_{product['id']}",
                    use_container_width=True,
                ):

                    add_to_cart(
                        product["id"]
                    )

                    st.rerun()


# =========================================================
# FAVORITES
# =========================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="luxury-title">'
        'Favorites ❤️'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="luxury-subtitle">'
        'Your saved luxury products'
        '</div>',
        unsafe_allow_html=True,
    )

    favorite_products = []

    for product_id in st.session_state.favorites:

        product = get_product(product_id)

        if product:
            favorite_products.append(product)

    if not favorite_products:

        st.info(
            "You have not added any favorites yet."
        )

        if st.button(
            "🛍️ Browse Products",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        for start in range(
            0,
            len(favorite_products),
            4,
        ):

            row_products = favorite_products[
                start:start + 4
            ]

            columns = st.columns(4)

            for index, product in enumerate(
                row_products
            ):

                column = columns[index]

                safe_image(
                    column,
                    product["image"],
                )

                column.markdown(
                    f"""
                    <div class="product-card">

                        <div class="product-name">
                            {product["name"]}
                        </div>

                        <div class="product-category">
                            {product["category"]}
                        </div>

                        <div class="product-price">
                            {money(product["price"])}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if column.button(
                    "🛒 Add to Cart",
                    key=f"fav_add_{product['id']}",
                    use_container_width=True,
                ):

                    add_to_cart(
                        product["id"]
                    )

                    st.rerun()

                if column.button(
                    "Remove ❤️",
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
        '<div class="luxury-title">'
        'Shopping Cart 🛒'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="luxury-subtitle">'
        'Review your selected products'
        '</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "🛍️ Continue Shopping",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        st.markdown(
            '<div class="section-title">'
            'Your Products'
            '</div>',
            unsafe_allow_html=True,
        )

        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            if not product:
                continue

            col1, col2, col3 = st.columns(
                [5, 2, 1]
            )

            with col1:

                st.markdown(
                    f"""
                    <div class="info-card">

                        <div class="info-title">
                            🛍️ {product["name"]}
                        </div>

                        <div class="info-text">
                            {product["category"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:

                st.markdown(
                    f"""
                    <div style="
                        padding:25px 5px;
                        font-size:20px;
                        font-weight:800;
                        color:#9c3c69;
                    ">
                        {money(product["price"])}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col3:

                if st.button(
                    "Remove",
                    key=f"remove_{index}",
                    use_container_width=True,
                ):

                    st.session_state.cart.pop(index)
                    st.rerun()

        st.markdown("---")

        total = cart_total()

        st.markdown(
            f"""
            <div class="info-card">

                <div class="info-title">
                    Order Summary
                </div>

                <div class="product-price">
                    Total: {money(total)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">'
            'Checkout'
            '</div>',
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
            placeholder="Enter complete delivery address",
        )

        if st.button(
            "💳 Place Order",
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

                            if not product:
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
                        st.session_state.order_success = True

                        st.success(
                            "🎉 Your order has been placed successfully!"
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

    st.markdown(
        '<div class="luxury-title">'
        'About LUXEMART'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="luxury-subtitle">'
        'Luxury made simple'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">

            <div class="info-title">
                ✨ Welcome to LUXEMART
            </div>

            <div class="info-text">

                LUXEMART is a modern online shopping platform
                for elegant fashion, jewellery, accessories,
                beauty products and fragrances.

                <br><br>

                Our goal is to provide a simple, stylish and
                convenient shopping experience.

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="info-card">

                <div class="info-title">
                    📞 Contact
                </div>

                <div class="info-text">
                    03169707804
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="info-card">

                <div class="info-title">
                    📧 Email
                </div>

                <div class="info-text">
                    asyabibi485@gmail.com
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# ADMIN
# =========================================================

elif st.session_state.page == "Admin":

    st.markdown(
        '<div class="luxury-title">'
        'Admin Dashboard 🔐'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="luxury-subtitle">'
        'Customer orders and requests'
        '</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.admin_logged_in:

        st.markdown(
            """
            <div class="info-card">

                <div class="info-title">
                    🔐 Administrator Login
                </div>

                <div class="info-text">
                    Authorized administrators only.
                </div>

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
            "🔐 Login",
            use_container_width=True,
        ):

            try:

                response = (
                    supabase
                    .auth
                    .sign_in_with_password(
                        {
                            "email": admin_email,
                            "password": admin_password,
                        }
                    )
                )

                if response.user:

                    logged_email = (
                        response.user.email or ""
                    )

                    if (
                        logged_email.lower()
                        == ADMIN_EMAIL.lower()
                    ):

                        st.session_state.admin_logged_in = True

                        st.success(
                            "Admin login successful."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "This account is not authorized as admin."
                        )

                else:

                    st.error(
                        "Login failed."
                    )

            except Exception as error:

                st.error(
                    f"Login error: {error}"
                )

    else:

        admin_top1, admin_top2 = st.columns(
            [5, 1]
        )

        with admin_top1:

            st.markdown(
                '<div class="section-title">'
                '📦 Client Requests Received'
                '</div>',
                unsafe_allow_html=True,
            )

        with admin_top2:

            if st.button(
                "Logout",
                use_container_width=True,
            ):

                logout_admin()

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

                    order_id = order.get(
                        "id",
                        "N/A",
                    )

                    customer_name = order.get(
                        "customer_name",
                        "Customer",
                    )

                    with st.expander(
                        f"🧾 Order #{order_id} — "
                        f"{customer_name}"
                    ):

                        info1, info2 = st.columns(2)

                        with info1:

                            st.write(
                                f"**Customer:** "
                                f"{customer_name}"
                            )

                            st.write(
                                f"**Phone:** "
                                f"{order.get('customer_phone', '-')}"
                            )

                            st.write(
                                f"**Address:** "
                                f"{order.get('customer_address', '-')}"
                            )

                        with info2:

                            st.write(
                                f"**Total:** "
                                f"{money(order.get('total_amount', 0))}"
                            )

                            st.write(
                                f"**Date:** "
                                f"{order.get('created_at', '-')}"
                            )

                        st.markdown(
                            "### 🛍️ Order Items"
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

                                for item in items:

                                    item_name = item.get(
                                        "product_name",
                                        "-",
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
                                        f"• {item_name} — "
                                        f"{money(item_price)} "
                                        f"× {quantity}"
                                    )

                            else:

                                st.caption(
                                    "No order items found."
                                )

                        except Exception as item_error:

                            st.error(
                                f"Could not load items: "
                                f"{item_error}"
                            )

        except Exception as error:

            st.error(
                f"Could not load orders: {error}"
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    "---"
)

st.markdown(
    """
    <div class="footer">

        <b>LUXEMART</b>

        <br>

        Luxury • Fashion • Beauty • Lifestyle

        <br><br>

        © 2026 LUXEMART. All rights reserved.

    </div>
    """,
    unsafe_allow_html=True,
)

