import streamlit as st
from supabase import create_client


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="🛍️",
    layout="wide",
)


# =========================================================
# SUPABASE CONFIG
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

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "slide" not in st.session_state:
    st.session_state.slide = 0

if "shop_category" not in st.session_state:
    st.session_state.shop_category = "All"


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
# CSS
# =========================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap'
    );

    .stApp {
        background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255,190,215,0.55),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(195,190,255,0.50),
            transparent 28%
        ),
        radial-gradient(
            circle at 80% 90%,
            rgba(175,225,255,0.45),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #fff5f9,
            #f7f3ff,
            #f0faff
        );

        font-family: 'DM Sans', sans-serif;
        color: #111111;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background:
        linear-gradient(
            180deg,
            #fff0f6,
            #f2efff,
            #eefaff
        );
    }

    .logo {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #17121b;
        padding: 8px;
    }

    .subtitle {
        text-align: center;
        color: #77707c;
        font-size: 11px;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    .main-logo {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 44px;
        font-weight: 700;
        letter-spacing: 4px;
        color: #17121b;
    }

    .main-subtitle {
        text-align: center;
        color: #77707c;
        font-size: 11px;
        letter-spacing: 3px;
        margin-bottom: 25px;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        font-weight: 700;
        color: #18131b;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .product-box {
        background: rgba(255,255,255,0.88);
        border-radius: 18px;
        padding: 12px;
        margin-bottom: 8px;
        box-shadow: 0 8px 25px rgba(70,50,90,0.07);
    }

    .product-name {
        color: #18131b;
        font-size: 17px;
        font-weight: 700;
    }

    .product-category {
        color: #8b808f;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .product-price {
        color: #17121b;
        font-size: 18px;
        font-weight: 700;
        margin-top: 4px;
    }

    .info-box {
        background: rgba(255,255,255,0.88);
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 10px 30px rgba(70,50,90,0.08);
        margin-bottom: 18px;
    }

    .total-box {
        background: #17131a;
        color: white;
        border-radius: 20px;
        padding: 22px;
        margin: 20px 0;
    }

    .total-small {
        color: #d6cdd9;
        font-size: 12px;
        letter-spacing: 1px;
    }

    .total-big {
        font-size: 28px;
        font-weight: 700;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        background: white !important;
        color: #111111 !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] > div {
        background: white !important;
        border-radius: 12px !important;
    }

    .stButton > button {
        background: white !important;
        color: #18131b !important;
        border: 1px solid #e2d9e7 !important;
        border-radius: 12px !important;
        min-height: 42px !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px rgba(70,50,90,0.12);
    }

    img {
        border-radius: 17px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)
# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    '<div class="logo">🛍️ LUXEMART</div>',
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    '<div class="subtitle">PREMIUM LIFESTYLE STORE</div>',
    unsafe_allow_html=True,
)

if st.sidebar.button(
    "🏠 Shop",
    use_container_width=True,
):
    go_to("Shop")


if st.sidebar.button(
    f"❤️ Favorites ({len(st.session_state.favorites)})",
    use_container_width=True,
):
    go_to("Favorites")


if st.sidebar.button(
    f"🛒 Cart ({len(st.session_state.cart)})",
    use_container_width=True,
):
    go_to("Cart")


if st.sidebar.button(
    "✨ About",
    use_container_width=True,
):
    go_to("About")


st.sidebar.markdown("---")

st.sidebar.markdown("### Collections")

for category in CATEGORIES:

    if st.sidebar.button(
        category,
        key=f"category_{category}",
        use_container_width=True,
    ):
        st.session_state.shop_category = category
        st.session_state.page = "Shop"
        st.rerun()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown(
        '<div class="main-logo">🛍️ LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-subtitle">PREMIUM LIFESTYLE STORE</div>',
        unsafe_allow_html=True,
    )

    st.image(
        SLIDES[st.session_state.slide],
        use_container_width=True,
    )

    previous_col, number_col, next_col = st.columns(
        [1, 2, 1]
    )

    previous_clicked = previous_col.button(
        "‹ Previous",
        use_container_width=True,
    )

    number_col.markdown(
        f"""
        <div style="
        text-align:center;
        padding:10px;
        color:#77707c;
        font-weight:600;
        ">
        {st.session_state.slide + 1}
        / {len(SLIDES)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    next_clicked = next_col.button(
        "Next ›",
        use_container_width=True,
    )

    if previous_clicked:
        st.session_state.slide = (
            st.session_state.slide - 1
        ) % len(SLIDES)

        st.rerun()

    if next_clicked:
        st.session_state.slide = (
            st.session_state.slide + 1
        ) % len(SLIDES)

        st.rerun()

    st.markdown(
        '<div class="section-title">Discover Your Collection</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search",
        placeholder="Search products...",
        label_visibility="collapsed",
    )

    selected_category = st.session_state.shop_category

    category = st.selectbox(
        "Category",
        CATEGORIES,
        index=CATEGORIES.index(selected_category),
    )

    st.session_state.shop_category = category

    sort_option = st.selectbox(
        "Sort Products",
        [
            "Featured",
            "Price: Low to High",
            "Price: High to Low",
            "Name: A to Z",
        ],
    )

    minimum_price, maximum_price = st.slider(
        "Price Range",
        1000,
        10000,
        (1000, 10000),
        500,
    )

    filtered_products = PRODUCTS.copy()

    if search.strip():

        search_value = search.strip().lower()

        filtered_products = [
            product
            for product in filtered_products
            if (
                search_value in product["name"].lower()
                or search_value in product["category"].lower()
            )
        ]

    if category != "All":

        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    filtered_products = [
        product
        for product in filtered_products
        if minimum_price
        <= product["price"]
        <= maximum_price
    ]

    if sort_option == "Price: Low to High":

        filtered_products.sort(
            key=lambda x: x["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered_products.sort(
            key=lambda x: x["price"],
            reverse=True,
        )

    elif sort_option == "Name: A to Z":

        filtered_products.sort(
            key=lambda x: x["name"].lower()
        )

    st.caption(
        f"{len(filtered_products)} products available"
    )

    for start in range(
        0,
        len(filtered_products),
        4,
    ):

        row = filtered_products[
            start:start + 4
        ]

        columns = st.columns(4)

        for index, product in enumerate(row):

            column = columns[index]

            column.image(
                product["image"],
                use_container_width=True,
            )

            column.markdown(
                '<div class="product-box">',
                unsafe_allow_html=True,
            )

            column.markdown(
                f'<div class="product-name">{product["name"]}</div>',
                unsafe_allow_html=True,
            )

            column.markdown(
                f'<div class="product-category">{product["category"]}</div>',
                unsafe_allow_html=True,
            )

            column.markdown(
                f'<div class="product-price">{money(product["price"])}</div>',
                unsafe_allow_html=True,
            )

            column.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

            add_clicked = column.button(
                "🛒 Add to Cart",
                key=f"add_{product['id']}",
                use_container_width=True,
            )

            if add_clicked:
                add_to_cart(product["id"])

            if product["id"] in st.session_state.favorites:
                favorite_label = "❤️ Remove Favorite"
            else:
                favorite_label = "♡ Add Favorite"

            favorite_clicked = column.button(
                favorite_label,
                key=f"fav_{product['id']}",
                use_container_width=True,
            )

            if favorite_clicked:
                toggle_favorite(product["id"])
                st.rerun()


# =========================================================
# FAVORITES
# =========================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="main-logo">❤️ FAVORITES</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-subtitle">YOUR SAVED COLLECTION</div>',
        unsafe_allow_html=True,
    )

    favorite_products = []

    for product_id in st.session_state.favorites:

        product = get_product(product_id)

        if product is not None:
            favorite_products.append(product)

    if not favorite_products:

        st.info(
            "Your favorites list is empty."
        )

        if st.button(
            "Explore Products",
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

            for index, product in enumerate(row):

                column = columns[index]

                column.image(
                    product["image"],
                    use_container_width=True,
                )

                column.markdown(
                    f"### {product['name']}"
                )

                column.caption(
                    product["category"]
                )

                column.write(
                    f"**{money(product['price'])}**"
                )

                add_clicked = column.button(
                    "🛒 Add to Cart",
                    key=f"favorite_add_{product['id']}",
                    use_container_width=True,
                )

                if add_clicked:
                    add_to_cart(product["id"])

                remove_clicked = column.button(
                    "Remove Favorite",
                    key=f"favorite_remove_{product['id']}",
                    use_container_width=True,
                )

                if remove_clicked:

                    st.session_state.favorites.remove(
                        product["id"]
                    )

                    st.rerun()


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="main-logo">🛒 CART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-subtitle">YOUR LUXEMART ORDER</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "Continue Shopping",
            use_container_width=True,
        ):
            go_to("Shop")

    else:

        cart_items = list(
            st.session_state.cart
        )

        for index, product_id in enumerate(cart_items):

            product = get_product(product_id)

            if product is None:
                continue

            image_col, info_col, action_col = st.columns(
                [1, 4, 1]
            )

            image_col.image(
                product["image"],
                use_container_width=True,
            )

            info_col.markdown(
                f"### {product['name']}"
            )

            info_col.caption(
                product["category"]
            )

            info_col.write(
                f"**{money(product['price'])}**"
            )

            remove_clicked = action_col.button(
                "Remove",
                key=f"cart_remove_{index}",
                use_container_width=True,
            )

            if remove_clicked:

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

            <div class="total-big">
            {money(total)}
            </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">Delivery Details</div>',
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

        place_order = st.button(
            "🛍️ Place Order",
            use_container_width=True,
        )

        if place_order:

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
                    "Please enter your address."
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
                            "Order was not created."
                        )

                    else:

                        order_id = (
                            order_response.data[0]["id"]
                        )

                        for product_id in cart_items:

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
        '<div class="main-logo">LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-subtitle">ABOUT OUR STORE</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    left.markdown(
        """
        <div class="info-box">

        <h3>✨ Our Story</h3>

        <p>
        LUXEMART is a modern lifestyle store offering
        fashion, beauty, jewellery, accessories,
        clothing and fragrances in one elegant
        shopping experience.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    right.markdown(
        """
        <div class="info-box">

        <h3>💎 Why LUXEMART?</h3>

        <p>✨ Elegant collections</p>
        <p>🛍️ Easy shopping</p>
        <p>❤️ Favorites</p>
        <p>🚚 Simple checkout</p>
        <p>💎 Premium experience</p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-box">

        <h3>📞 Contact</h3>

        <p>
        Phone: <strong>03169707804</strong>
        </p>

        <p>
        Email: <strong>asyabibi485@gmail.com</strong>
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
        '<div class="main-logo">🔐 ADMIN</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="main-subtitle">LUXEMART MANAGEMENT</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.admin_logged_in:

        st.info(
            "Administrator login"
        )

        email = st.text_input(
            "Admin Email"
        )

        password = st.text_input(
            "Password",
            type="password",
        )

        login_clicked = st.button(
            "Login",
            use_container_width=True,
        )

        if login_clicked:

            if not email.strip():

                st.error(
                    "Please enter admin email."
                )

            elif not password:

                st.error(
                    "Please enter password."
                )

            else:

                try:

                    login_response = (
                        supabase
                        .auth
                        .sign_in_with_password(
                            {
                                "email": email.strip(),
                                "password": password,
                            }
                        )
                    )

                    user = login_response.user

                    if (
                        user
                        and user.email
                        and user.email.lower()
                        == ADMIN_EMAIL.lower()
                    ):

                        st.session_state.admin_logged_in = True
                        st.success(
                            "Login successful."
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
            '<div class="section-title">Client Requests Received</div>',
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
                    "No orders received yet."
                )

            else:

                for order_number, order in enumerate(
                    orders,
                    start=1,
                ):

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
                        <div class="info-box">

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

                    order_id = order.get("id")

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
                            items_response.data or []
                        )

                        if items:

                            with st.expander(
                                "🛍️ View Products"
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
                                        f"🛍️ {item_name} — "
                                        f"{money(float(item_price))} × "
                                        f"{quantity}"
                                    )

                    except Exception as item_error:

                        st.warning(
                            f"Order items error: {item_error}"
                        )

        except Exception as error:

            st.error(
                f"Could not load orders: {error}"
            )


# =========================================================
# ADMIN LOGIN BUTTON
# =========================================================

st.markdown("---")

if st.button(
    "🔐 Admin Login",
    use_container_width=True,
):
    go_to("Admin")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#817783;
        font-size:12px;
        padding:20px;
    ">

    🛍️ LUXEMART
    <br>
    Elegant • Modern • Premium

    </div>
    """,
    unsafe_allow_html=True,
)
                   

