import streamlit as st
from supabase import create_client

# ============================================================
# LUXEMART - COMPLETE STREAMLIT APP
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SUPABASE CONFIGURATION
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
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "icon": "🧣",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "icon": "📿",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "icon": "📿",
    },
    {
        "id": 5,
        "name": "Gold Watch",
        "category": "Accessories",
        "price": 7999,
        "icon": "⌚",
    },
    {
        "id": 6,
        "name": "Classic Sunglasses",
        "category": "Accessories",
        "price": 2999,
        "icon": "🕶️",
    },
    {
        "id": 7,
        "name": "Premium Makeup Set",
        "category": "Beauty",
        "price": 4499,
        "icon": "💄",
    },
    {
        "id": 8,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
    },
    {
        "id": 9,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
    },
    {
        "id": 10,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
    },
    {
        "id": 11,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
    },
    {
        "id": 12,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
    },
    {
        "id": 13,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
    },
    {
        "id": 14,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
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
# FUNCTIONS
# ============================================================

def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def money(amount):
    return f"Rs. {int(amount):,}"


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
    st.toast("Product added to cart 🛍️")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")
    else:
        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@500;600;700&display=swap'
);

/* MAIN APP */

.stApp {
    background: #ffffff !important;
}

.block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* NORMAL TEXT */

.stApp p,
.stApp label,
.stApp li {
    color: #000000 !important;
    font-family: "Poppins", sans-serif !important;
    font-weight: 700 !important;
}

/* HEADINGS */

h1,
h2,
h3,
h4 {
    color: #000000 !important;
    font-family: "Playfair Display", serif !important;
    font-weight: 700 !important;
}

/* BRAND */

.brand {
    color: #000000 !important;
    font-family: "Playfair Display", serif;
    font-size: 36px;
    font-weight: 700;
    letter-spacing: 4px;
}

.tagline {
    color: #000000 !important;
    font-family: "Poppins", sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

/* HERO */

.hero-box {
    margin: 25px 0;
    padding: 42px;
    border-radius: 30px;
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #faf7ff 50%,
        #f0eafa 100%
    );
    border: 1px solid #e5dcef;
    box-shadow: 0 15px 45px rgba(50, 40, 65, 0.08);
}

.hero-title {
    color: #000000 !important;
    font-family: "Playfair Display", serif;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero-text {
    color: #000000 !important;
    font-family: "Poppins", sans-serif;
    font-size: 16px;
    font-weight: 700;
}

/* PRODUCT CARD */

.product-card {
    padding: 15px;
    border-radius: 22px;
    background: #ffffff !important;
    border: 1px solid #e5dcef;
    box-shadow: 0 10px 28px rgba(50, 40, 65, 0.08);
    margin-bottom: 12px;
}

.product-image {
    height: 155px;
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
    margin-bottom: 15px;
}

.product-name {
    color: #000000 !important;
font-family: "Playfair Display", serif;
    font-size: 22px;
    font-weight: 700;
    margin: 0;
}

.product-category {
    color: #000000 !important;
    font-family: "Poppins", sans-serif;
    font-size: 13px;
    font-weight: 700;
    margin-top: 5px;
}

.product-price {
    color: #000000 !important;
    font-family: "Poppins", sans-serif;
    font-size: 18px;
    font-weight: 700;
    margin-top: 10px;
}

/* BUTTONS */

div.stButton > button {
    background: #f5efff !important;
    color: #000000 !important;
    border: 1px solid #d8cae8 !important;
    border-radius: 14px !important;
    font-family: "Poppins", sans-serif !important;
    font-weight: 700 !important;
    min-height: 44px !important;
}

div.stButton > button:hover {
    background: #e9def7 !important;
    color: #000000 !important;
    border-color: #b99bd3 !important;
}

/* TEXT INPUT */

div[data-testid="stTextInput"] input {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #d8cae8 !important;
    border-radius: 12px !important;
    font-family: "Poppins", sans-serif !important;
    font-weight: 700 !important;
}

/* TEXT AREA */

div[data-testid="stTextArea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #d8cae8 !important;
    border-radius: 12px !important;
    font-family: "Poppins", sans-serif !important;
    font-weight: 700 !important;
}

/* SELECT */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1px solid #d8cae8 !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] * {
    color: #000000 !important;
    font-weight: 700 !important;
}

div[role="option"] {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 700 !important;
}

div[role="option"]:hover {
    background-color: #f5efff !important;
}

/* NUMBER INPUT */

div[data-testid="stNumberInput"] input {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    font-weight: 700 !important;
}

/* PLACEHOLDER */

input::placeholder,
textarea::placeholder {
    color: #777777 !important;
    -webkit-text-fill-color: #777777 !important;
    opacity: 1 !important;
    font-weight: 600 !important;
}

/* FOOTER */

.footer-box {
    margin-top: 50px;
    padding: 35px;
    border-radius: 25px;
    background: #30283b;
    text-align: center;
}

.footer-title {
    color: #ffffff !important;
    font-family: "Playfair Display", serif;
    font-size: 28px;
    font-weight: 700;
}

.footer-text {
    color: #ffffff !important;
    font-family: "Poppins", sans-serif;
    font-size: 14px;
    font-weight: 700;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

header_left, header_right = st.columns(
    [3, 7]
)

with header_left:

    st.markdown(
        """
        <div class="brand">LUXEMART</div>
        <div class="tagline">
            LUXURY • STYLE • ELEGANCE
        </div>
        """,
        unsafe_allow_html=True,
    )


with header_right:

    nav1, nav2, nav3, nav4, nav5 = st.columns(5)

    with nav1:
        if st.button(
            "SHOP",
            use_container_width=True
        ):
            go_to("Shop")

    with nav2:
        if st.button(
            "❤️ FAVORITES",
            use_container_width=True
        ):
            go_to("Favorites")

    with nav3:
        if st.button(
            f"🛒 CART ({len(st.session_state.cart)})",
            use_container_width=True
        ):
            go_to("Cart")

    with nav4:
        if st.button(
            "ABOUT",
            use_container_width=True
        ):
            go_to("About")

    with nav5:
        if st.button(
            "ADMIN",
            use_container_width=True
        ):
            go_to("Admin")


st.divider()


# ============================================================
# SHOP PAGE
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero-box">

            <div class="hero-title">
                Discover Your Luxury
            </div>

            <div class="hero-text">
                Explore our beautiful collection of fashion,
                beauty, jewellery, perfumes and lifestyle essentials.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search Products",
        placeholder="Type product name..."
    )

    category = st.selectbox(
        "Choose Category",
        CATEGORIES
    )

    filtered_products = PRODUCTS.copy()

    if search.strip():

        filtered_products = [
            product
            for product in filtered_products
            if search.lower() in product["name"].lower()
        ]

    if category != "All":

        filtered_products = [
            product
            for product in filtered_products
            if product["category"] == category
        ]

    st.markdown(
        f"## {len(filtered_products)} Products"
    )

    if not filtered_products:

        st.info("No products found.")

    product_columns = st.columns(3)

    for index, product in enumerate(filtered_products):

        with product_columns[index % 3]:

            # ------------------------------------------------
            # PRODUCT HTML
            # ------------------------------------------------

            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-image">
                        {product["icon"]}
                    </div>

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

            button1, button2 = st.columns(2)

            with button1:

                if st.button(
                    "🛍️ ADD",
                    key=f"add_product_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(product["id"])

            with button2:

                if product["id"] in st.session_state.favorites:
                    favorite_text = "❤️"
                else:
                    favorite_text = "♡"

                if st.button(
                    favorite_text,
                    key=f"favorite_product_{product['id']}",
                    use_container_width=True,
                ):
                    toggle_favorite(product["id"])
                    st.rerun()


# ============================================================
# FAVORITES PAGE
# ============================================================

elif st.session_state.page == "Favorites":

    st.title("❤️ My Favorites")

    favorite_products = [
        product
        for product in PRODUCTS
        if product["id"] in st.session_state.favorites
    ]

    if not favorite_products:

        st.info(
            "You have not added any favorites yet."
        )

        if st.button("CONTINUE SHOPPING"):
            go_to("Shop")

    else:

        favorite_columns = st.columns(3)

        for index, product in enumerate(favorite_products):

            with favorite_columns[index % 3]:

                st.markdown(
                    f"""
                    <div class="product-card">

                        <div class="product-image">
                            {product["icon"]}
                        </div>

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

                if st.button(
                    "🛍️ ADD TO CART",
                    key=f"favorite_cart_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(product["id"])


# ============================================================
# CART PAGE
# ============================================================

elif st.session_state.page == "Cart":

    st.title("🛒 Shopping Cart")

    if not st.session_state.cart:

        st.info("Your shopping cart is empty.")

        if st.button("CONTINUE SHOPPING"):
            go_to("Shop")

    else:

        for index, product_id in enumerate(
            st.session_state.cart
        ):

            product = get_product(product_id)

            if product:

                cart_col1, cart_col2, cart_col3 = st.columns(
                    [5, 2, 1]
                )

                with cart_col1:

                    st.markdown(
                        f"**{product['icon']} {product['name']}**"
                    )

                with cart_col2:

                    st.markdown(
                        f"**{money(product['price'])}**"
                    )

                with cart_col3:

                    if st.button(
                        "✕",
                        key=f"remove_cart_{index}",
                    ):

                        st.session_state.cart.pop(index)
                        st.rerun()

        st.divider()

        total = cart_total()

        st.markdown(
            f"## Total: {money(total)}"
        )

        st.markdown("## Checkout")

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Enter your full name"
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number"
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete delivery address"
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

                        raise Exception(
                            "Supabase did not return the new order."
                        )

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

                except Exception as e:

                    st.error(
                        "Unable to place the order."
                    )

                    st.code(
                        str(e)
                    )


# ============================================================
# ABOUT PAGE
# ============================================================

elif st.session_state.page == "About":

    st.title("About LUXEMART")

    st.markdown(
        """
        <div class="hero-box">

            <div class="hero-title">
                Luxury Made Simple
            </div>

            <div class="hero-text">
                LUXEMART is a modern online shopping experience
                created for fashion, beauty, jewellery and lifestyle
                lovers.
                <br><br>
                Browse our collection, save your favourites,
                add products to your cart and place your order
                directly through the app.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Contact Us")

    st.write("📞 03169707804")
    st.write("📧 asyabibi485@gmail.com")


# ============================================================
# ADMIN PAGE
# ============================================================

elif st.session_state.page == "Admin":

    st.title("🔐 Admin Panel")

    if not st.session_state.admin_logged_in:

        st.write(
            "Sign in using your existing Supabase admin account."
        )

        admin_email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email"
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        if st.button(
            "LOGIN",
            use_container_width=True,
        ):

            try:

                login_result = (
                    supabase.auth.sign_in_with_password(
                        {
                            "email": admin_email.strip(),
                            "password": admin_password,
                        }
                    )
                )

                if login_result.user is None:

                    st.error(
                        "Login failed."
                    )

                elif (
                    admin_email.strip().lower()
                    != ADMIN_EMAIL.lower()
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
            "📦 Customer Orders"
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

                st.info(
                    "No orders received yet."
                )

            else:

                for order in orders:

                    st.markdown(
                        f"""
                        <div class="product-card">

                            <div class="product-name">
                                Order #{order.get("id")}
                            </div>

                            <div class="product-category">
                                Customer:
                                {order.get("customer_name", "")}
                            </div>

                            <div class="product-category">
                                Phone:
                                {order.get("customer_phone", "")}
                            </div>

                            <div class="product-category">
                                Address:
                                {order.get("customer_address", "")}
                            </div>

                            <div class="product-price">
                                Total:
                                {money(order.get("total_amount", 0))}
                            </div>

                            <div class="product-category">
                                Date:
                                {order.get("created_at", "")}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    items_response = (
                        supabase
                        .table("order_items")
                        .select("*")
                        .eq(
                            "order_id",
                            order["id"]
                        )
                        .execute()
                    )

                    items = (
                        items_response.data or []
                    )

                    if items:

                        st.markdown(
                            "### Order Items"
                        )

                        for item in items:

                            st.write(
                                f"• "
                                f"{item.get('product_name', '')} "
                                f"× {item.get('quantity', 1)} "
                                f"— "
                                f"{money(item.get('price', 0))}"
                            )

                    st.divider()

        except Exception as e:

            st.error(
                "Unable to load orders."
            )

            st.code(
                str(e)
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer-box">

        <div class="footer-title">
            LUXEMART
        </div>

        <div class="footer-text">
            Luxury • Style • Elegance
        </div>

        <br>

        <div class="footer-text">
            📞 03169707804
            &nbsp;&nbsp; | &nbsp;&nbsp;
            📧 asyabibi485@gmail.com
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)









