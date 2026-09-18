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
# PRODUCT DATA
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
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* ALL NORMAL TEXT */

.stApp p,
.stApp label,
.stApp li {
    color: #000000 !important;
    font-weight: 700 !important;
}

/* HEADINGS */

h1,
h2,
h3,
h4 {
    color: #000000 !important;
    font-weight: 700 !important;
}

/* BUTTONS */

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

/* TEXT INPUT */

div[data-testid="stTextInput"] input {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #d8c9eb !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}

/* TEXT AREA */

div[data-testid="stTextArea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #d8c9eb !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}

/* SELECT */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1px solid #d8c9eb !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] * {
    color: #000000 !important;
    font-weight: 700 !important;
}

/* HERO */

.hero-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero-text {
    font-size: 16px;
    font-weight: 700;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

left, right = st.columns([3, 7])

with left:

    st.title("LUXEMART")

    st.caption(
        "LUXURY • STYLE • ELEGANCE"
    )


with right:

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
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div style="
            padding:35px;
            border-radius:28px;
            background:#faf7ff;
            border:1px solid #e5dcef;
            margin-bottom:25px;
        ">

            <div class="hero-title">
                Discover Your Luxury
            </div>

            <div class="hero-text">
                Fashion, beauty, jewellery, perfumes
                and elegant lifestyle essentials.
            </div>

        </div>
        """,
        unsafe_allow_html=True
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

    columns = st.columns(3)

    for index, product in enumerate(filtered_products):

        with columns[index % 3]:

            # REAL PRODUCT IMAGE
            st.image(
                product["image"],
                use_container_width=True
            )

            # PRODUCT NAME
            st.subheader(
                product["name"]
            )

            # CATEGORY
            st.write(
                product["category"]
            )

            # PRICE
            st.markdown(
                f"**{money(product['price'])}**"
            )

            # BUTTONS
            button1, button2 = st.columns(2)

            with button1:

                if st.button(
                    "🛍️ ADD",
                    key=f"add_{product['id']}",
                    use_container_width=True
                ):

                    add_to_cart(
                        product["id"]
                    )

            with button2:

                if product["id"] in st.session_state.favorites:

                    favorite_text = "❤️"

                else:

                    favorite_text = "♡"

                if st.button(
                    favorite_text,
                    key=f"favorite_{product['id']}",
                    use_container_width=True
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
            "CONTINUE SHOPPING"
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
                    use_container_width=True
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
                    use_container_width=True
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
            "CONTINUE SHOPPING"
        ):

            go_to("Shop")

    else:

        for index, product_id in enumerate(
            st.session_state.cart
        ):

            product = get_product(
                product_id
            )

            if product:

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
                        key=f"remove_{index}"
                    ):

                        st.session_state.cart.pop(
                            index
                        )

                        st.rerun()

        st.divider()

        total = cart_total()

        st.subheader(
            f"Total: {money(total)}"
        )

        st.subheader(
            "Checkout"
        )

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
            placeholder="Enter your complete address"
        )

        if st.button(
            "PLACE ORDER",
            use_container_width=True
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

                    for product_id in (
                        st.session_state.cart
                    ):

                        product = get_product(
                            product_id
                        )

                        if product:

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
        "About LUXEMART"
    )

    st.write(
        "LUXEMART is a modern luxury shopping experience "
        "for fashion, beauty, jewellery, perfumes and "
        "lifestyle products."
    )

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

        st.write(
            "Login with your existing Supabase admin account."
        )

        email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        if st.button(
            "LOGIN",
            use_container_width=True
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
            use_container_width=True
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

            response = (
                supabase
                .table("orders")
                .select("*")
                .order(
                    "created_at",
                    desc=True
                )
                .execute()
            )

            orders = response.data or []

            if not orders:

                st.info(
                    "No orders received yet."
                )

            else:

                for order in orders:

                    st.markdown(
                        f"### Order #{order.get('id')}"
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
                        items_response.data
                        or []
                    )

                    if items:

                        st.write(
                            "Order Items:"
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

st.divider()

st.caption(
    "LUXEMART • Luxury • Style • Elegance"
)

st.caption(
    "📞 03169707804  |  📧 asyabibi485@gmail.com"
)
