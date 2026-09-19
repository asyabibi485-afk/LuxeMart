import streamlit as st
from supabase import create_client


# ============================================================
# LUXEMART
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

try:
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]
    ADMIN_EMAIL = st.secrets["admin"]["email"]

    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY,
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

if "product_page" not in st.session_state:
    st.session_state.product_page = 1

if "search" not in st.session_state:
    st.session_state.search = ""

if "category" not in st.session_state:
    st.session_state.category = "All"


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
        "image": "https://images.pexels.com/photos/13791265/pexels-photo-13791265.jpeg?cs=srgb&dl=pexels-rehman-yousaf-321165099-13791265.jpg&fm=jpg",
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
        return f"Rs. {float(amount):,.0f}"

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

    st.toast("Added to cart 🛒")


def toggle_favorite(product_id):

    if product_id in st.session_state.favorites:

        st.session_state.favorites.remove(product_id)

        st.toast("Removed from favorites")

    else:

        st.session_state.favorites.append(product_id)

        st.toast("Added to favorites ❤️")


def safe_image(url):

    try:

        st.image(
            url,
            use_container_width=True,
        )

    except Exception:

        st.info("Product image unavailable.")


def logout_admin():

    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.admin_logged_in = False
    st.session_state.page = "Shop"

    st.rerun()


# ============================================================
# MODERN DESIGN
# ============================================================

st.markdown(
    """
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #fff7fc 0%,
        #f5f0ff 50%,
        #eef7ff 100%
    );
}

.block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: #111111 !important;
    font-weight: 800 !important;
}

p, label, li {
    color: #111111 !important;
    font-weight: 600 !important;
}

.stButton > button {
    background: white !important;
    color: #111111 !important;
    border: 1px solid #d8c9eb !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    min-height: 42px !important;
}

.stButton > button:hover {
    background: #f4eaff !important;
    border-color: #a979d1 !important;
}

[data-testid="stTextInput"] input {
    background: white !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #d8c9eb !important;
    border-radius: 12px !important;
}

[data-testid="stTextArea"] textarea {
    background: white !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #d8c9eb !important;
    border-radius: 12px !important;
}

[data-baseweb="select"] > div {
    background: white !important;
    color: #000000 !important;
    border-radius: 12px !important;
}

[data-baseweb="select"] * {
    color: #000000 !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #f7edff,
        #eef7ff
    );
}

[data-testid="stMetricValue"] {
    color: #111111 !important;
}

.product-card {
    background: white;
    border-radius: 20px;
    padding: 12px;
    margin-bottom: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.title("LUXEMART")

    st.caption(
        "LUXURY • STYLE • ELEGANCE"
    )

    st.divider()

    st.subheader("Navigation")

    if st.button(
        "🏠 SHOP",
        use_container_width=True,
        key="nav_shop",
    ):
        go_to("Shop")

    if st.button(
        f"❤️ FAVORITES ({len(st.session_state.favorites)})",
        use_container_width=True,
        key="nav_favorites",
    ):
        go_to("Favorites")

    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        use_container_width=True,
        key="nav_cart",
    ):
        go_to("Cart")

    if st.button(
        "ℹ️ ABOUT",
        use_container_width=True,
        key="nav_about",
    ):
        go_to("About")

    if st.button(
        "📞 CONTACT",
        use_container_width=True,
        key="nav_contact",
    ):
        go_to("Contact")

    if st.button(
        "🔐 ADMIN",
        use_container_width=True,
        key="nav_admin",
    ):
        go_to("Admin")

    st.divider()

    st.subheader("Categories")

    for category in CATEGORIES:

        if st.button(
            category,
            use_container_width=True,
            key=f"side_category_{category}",
        ):

            st.session_state.category = category
            st.session_state.product_page = 1
            st.session_state.page = "Shop"

            st.rerun()


# ============================================================
# TOP HEADER
# ============================================================

top_left, top_middle, top_right = st.columns(
    [5, 2, 2]
)

with top_left:

    st.title("LUXEMART")

with top_right:

    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        use_container_width=True,
        key="top_cart_button",
    ):

        go_to("Cart")

st.divider()


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.header(
        "✨ Discover Your Luxury"
    )

    st.write(
        "Fashion, beauty, jewellery, perfumes "
        "and elegant lifestyle essentials."
    )

    hero1, hero2 = st.columns(
        [1.6, 1]
    )

    with hero1:

        st.info(
            "LUXEMART PREMIUM COLLECTION\n\n"
            "Discover elegant products for your "
            "modern lifestyle."
        )

    with hero2:

        safe_image(
            "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg"
        )

    st.divider()

    st.header(
        "✨ Explore Collection"
    )

    search_col, category_col, sort_col = st.columns(
        [2, 1, 1]
    )

    with search_col:

        search = st.text_input(
            "Search",
            value=st.session_state.search,
            placeholder="Search products...",
            key="search_products",
        )

        if search != st.session_state.search:

            st.session_state.search = search
            st.session_state.product_page = 1

    with category_col:

        category = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(
                st.session_state.category
            ),
            key="product_category",
        )

        if category != st.session_state.category:

            st.session_state.category = category
            st.session_state.product_page = 1

    with sort_col:

        sort_option = st.selectbox(
            "Sort",
            [
                "Featured",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A-Z",
            ],
            key="sort_products",
        )

    max_price = st.slider(
        "Maximum Price",
        min_value=1000,
        max_value=10000,
        value=10000,
        step=500,
    )

    # --------------------------------------------------------
    # FILTER PRODUCTS
    # --------------------------------------------------------

    filtered = []

    for product in PRODUCTS:

        if category != "All":

            if product["category"] != category:
                continue

        if search.strip():

            text = (
                product["name"]
                + " "
                + product["category"]
            ).lower()

            if search.lower() not in text:
                continue

        if product["price"] > max_price:
            continue

        filtered.append(product)

    # --------------------------------------------------------
    # SORT
    # --------------------------------------------------------

    if sort_option == "Price: Low to High":

        filtered.sort(
            key=lambda item: item["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered.sort(
            key=lambda item: item["price"],
            reverse=True,
        )

    elif sort_option == "Name: A-Z":

        filtered.sort(
            key=lambda item: item["name"]
        )

    # --------------------------------------------------------
    # PAGINATION
    # --------------------------------------------------------

    PRODUCTS_PER_PAGE = 4

    if not filtered:

        st.warning(
            "No products found."
        )

    else:

        total_pages = (
            len(filtered)
            + PRODUCTS_PER_PAGE
            - 1
        ) // PRODUCTS_PER_PAGE

        if st.session_state.product_page > total_pages:

            st.session_state.product_page = total_pages

        if st.session_state.product_page < 1:

            st.session_state.product_page = 1

        current_page = st.session_state.product_page

        start = (
            current_page - 1
        ) * PRODUCTS_PER_PAGE

        end = (
            start
            + PRODUCTS_PER_PAGE
        )

        current_products = filtered[
            start:end
        ]

        product_columns = st.columns(4)

        for index, product in enumerate(
            current_products
        ):

            with product_columns[index]:

                safe_image(
                    product["image"]
                )

                st.subheader(
                    product["name"]
                )

                st.caption(
                    product["category"]
                )

                st.write(
                    f"**{money(product['price'])}**"
                )

                if product["id"] in st.session_state.favorites:

                    favorite_label = "❤️ Favorite"

                else:

                    favorite_label = "♡ Favorite"

                if st.button(
                    favorite_label,
                    key=f"favorite_{product['id']}",
                    use_container_width=True,
                ):

                    toggle_favorite(
                        product["id"]
                    )

                    st.rerun()

                if st.button(
                    "🛒 ADD TO CART",
                    key=f"cart_{product['id']}",
                    use_container_width=True,
                ):

                    add_to_cart(
                        product["id"]
                    )

                    st.rerun()

        st.divider()

        # ----------------------------------------------------
        # PAGE NUMBER BUTTONS
        # ----------------------------------------------------

        st.subheader(
            "Explore Collection Pages"
        )

        page_columns = st.columns(
            total_pages
        )

        for page_number in range(
            1,
            total_pages + 1,
        ):

            with page_columns[page_number - 1]:

                if page_number == current_page:

                    label = (
                        f"📍 PAGE {page_number}"
                    )

                else:

                    label = (
                        f"PAGE {page_number}"
                    )

                if st.button(
                    label,
                    key=f"page_{page_number}",
                    use_container_width=True,
                ):

                    st.session_state.product_page = page_number

                    st.rerun()

        st.write("")

        previous_col, current_col, next_col = st.columns(
            [1, 2, 1]
        )

        with previous_col:

            if current_page > 1:

                if st.button(
                    "← PREVIOUS",
                    key="previous_page",
                    use_container_width=True,
                ):

                    st.session_state.product_page -= 1

                    st.rerun()

        with current_col:

            st.markdown(
                f"### Page {current_page} of {total_pages}"
            )

        with next_col:

            if current_page < total_pages:

                if st.button(
                    "NEXT →",
                    key="next_page",
                    use_container_width=True,
                ):

                    st.session_state.product_page += 1

                    st.rerun()


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.header(
        "❤️ My Favorites"
    )

    favorite_products = []

    for product_id in st.session_state.favorites:

        product = get_product(product_id)

        if product:
            favorite_products.append(product)

    if not favorite_products:

        st.info(
            "You have no favorite products yet."
        )

        if st.button(
            "🛍️ CONTINUE SHOPPING",
            use_container_width=True,
            key="favorite_shop",
        ):

            go_to("Shop")

    else:

        columns = st.columns(4)

        for index, product in enumerate(
            favorite_products
        ):

            with columns[index % 4]:

                safe_image(
                    product["image"]
                )

                st.subheader(
                    product["name"]
                )

                st.caption(
                    product["category"]
                )

                st.write(
                    f"**{money(product['price'])}**"
                )

                if st.button(
                    "🛒 ADD TO CART",
                    key=f"favorite_cart_{product['id']}",
                    use_container_width=True,
                ):

                    add_to_cart(
                        product["id"]
                    )

                    st.rerun()

                if st.button(
                    "REMOVE ❤️",
                    key=f"remove_favorite_{product['id']}",
                    use_container_width=True,
                ):

                    st.session_state.favorites.remove(
                        product["id"]
                    )

                    st.rerun()


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.header(
        "🛒 Shopping Cart"
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "🛍️ CONTINUE SHOPPING",
            use_container_width=True,
            key="empty_cart_shop",
        ):

            go_to("Shop")

    else:

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
                    key=f"remove_cart_{index}",
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

        st.divider()

        st.subheader(
            "Customer Information"
        )

        customer_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
            key="customer_name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX",
            key="customer_phone",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter complete delivery address",
            key="customer_address",
        )

        if st.button(
            "🎉 PLACE ORDER",
            use_container_width=True,
            key="place_order",
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
                            "Order was not created."
                        )

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

                    st.info(
                        f"Order ID: {order_id}"
                    )

                    st.balloons()

                except Exception as e:

                    st.error(
                        "Unable to place order."
                    )

                    st.code(
                        str(e)
                    )


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.header(
        "ℹ️ About LUXEMART"
    )

    st.subheader(
        "Luxury • Style • Elegance"
    )

    st.write(
        "LUXEMART is a modern luxury shopping experience "
        "for fashion, beauty, jewellery, perfumes and "
        "elegant lifestyle essentials."
    )

    st.divider()

    st.write(
        "✨ Fashion"
    )

    st.write(
        "💎 Jewellery"
    )

    st.write(
        "👜 Accessories"
    )

    st.write(
        "🌸 Perfumes"
    )

    st.write(
        "💄 Beauty"
    )

    st.write(
        "👗 Clothes"
    )


# ============================================================
# CONTACT
# ============================================================

elif st.session_state.page == "Contact":

    st.header(
        "📞 Contact LUXEMART"
    )

    st.write(
        "We are happy to hear from you."
    )

    st.divider()

    contact_col1, contact_col2 = st.columns(2)

    with contact_col1:

        st.subheader(
            "📞 Phone"
        )

        st.write(
            "03169707804"
        )

        st.subheader(
            "📧 Email"
        )

        st.write(
            "asyabibi485@gmail.com"
        )

    with contact_col2:

        st.subheader(
            "💬 Send a Message"
        )

        contact_name = st.text_input(
            "Your Name",
            key="contact_name",
        )

        contact_phone = st.text_input(
            "Your Phone",
            key="contact_phone",
        )

        contact_message = st.text_area(
            "Your Message",
            placeholder="Write your message here...",
            key="contact_message",
        )

        if st.button(
            "SEND MESSAGE",
            use_container_width=True,
            key="send_contact",
        ):

            if not contact_name.strip():

                st.error(
                    "Please enter your name."
                )

            elif not contact_message.strip():

                st.error(
                    "Please enter your message."
                )

            else:

                st.success(
                    "Thank you! Your message has been received."
                )

                st.info(
                    "For direct assistance: 03169707804"
                )

    st.divider()

    st.subheader(
        "LUXEMART"
    )

    st.write(
        "Luxury fashion, beauty, jewellery, "
        "perfumes and lifestyle essentials."
    )


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.header(
        "🔐 Admin Dashboard"
    )

    if not st.session_state.admin_logged_in:

        st.info(
            "Login using your configured Supabase admin account."
        )

        admin_email = st.text_input(
            "Admin Email",
            key="admin_email",
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            key="admin_password",
        )

        if st.button(
            "LOGIN",
            use_container_width=True,
            key="admin_login",
        ):

            try:

                result = (
                    supabase
                    .auth
                    .sign_in_with_password(
                        {
                            "email":
                                admin_email.strip(),

                            "password":
                                admin_password,
                        }
                    )
                )

                if result.user is None:

                    st.error(
                        "Login failed."
                    )

                else:

                    logged_email = (
                        result.user.email or ""
                    )

                    if (
                        logged_email.lower()
                        != ADMIN_EMAIL.lower()
                    ):

                        try:
                            supabase.auth.sign_out()
                        except Exception:
                            pass

                        st.error(
                            "This account is not authorized as admin."
                        )

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
            key="admin_logout",
        ):

            logout_admin()

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
                    desc=True,
                )
                .execute()
            )

            orders = response.data or []

            if not orders:

                st.info(
                    "No orders received yet."
                )

            else:

                st.metric(
                    "Total Orders",
                    len(orders),
                )

                st.divider()

                for order in orders:

                    order_id = order.get(
                        "id",
                        "N/A",
                    )

                    customer_name = order.get(
                        "customer_name",
                        "",
                    )

                    with st.expander(
                        f"🧾 Order #{order_id} — {customer_name}"
                    ):

                        st.write(
                            f"**Customer:** "
                            f"{customer_name}"
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

                        st.divider()

                        st.write(
                            "**Order Items:**"
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

                                    st.write(
                                        f"🛍️ "
                                        f"{item.get('product_name', '')} "
                                        f"x "
                                        f"{item.get('quantity', 1)} "
                                        f"— "
                                        f"{money(item.get('price', 0))}"
                                    )

                            else:

                                st.caption(
                                    "No items found."
                                )

                        except Exception as e:

                            st.error(
                                f"Unable to load order items: {e}"
                            )

        except Exception as e:

            st.error(
                "Unable to load customer orders."
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
