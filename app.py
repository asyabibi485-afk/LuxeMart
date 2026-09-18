import streamlit as st
from supabase import create_client

# ============================================================
# LUXEMART
# Supabase Email + Password Admin Login
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

@st.cache_resource
def get_supabase():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        return create_client(url, key)
    except Exception as error:
        st.error("Supabase connection error.")
        st.code(str(error))
        return None


supabase = get_supabase()

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None

# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Velvet Luxe Handbag",
        "category": "Fashion",
        "price": 3499,
        "emoji": "👜",
    },
    {
        "id": 2,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "emoji": "📿",
    },
    {
        "id": 3,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "emoji": "⌚",
    },
    {
        "id": 4,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "emoji": "🕶️",
    },
    {
        "id": 5,
        "name": "Luxury Perfume",
        "category": "Beauty",
        "price": 2999,
        "emoji": "🌸",
    },
    {
        "id": 6,
        "name": "Silk Evening Scarf",
        "category": "Fashion",
        "price": 1599,
        "emoji": "🧣",
    },
    {
        "id": 7,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "emoji": "💎",
    },
    {
        "id": 8,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "emoji": "💄",
    },
]

# ============================================================
# DESIGN
# ============================================================

CSS = (
    "<style>"
    "@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');"

    "html,body,[class*='css']{"
    "font-family:'DM Sans',sans-serif;"
    "}"

    ".stApp{"
    "background:linear-gradient(135deg,#faf9fc 0%,#f5f0ff 50%,#fff5fa 100%);"
    "color:#17131d;"
    "}"

    ".block-container{"
    "max-width:1250px;"
    "padding-top:25px;"
    "padding-bottom:50px;"
    "}"

    ".brand{"
    "font-family:'Playfair Display',serif;"
    "font-size:42px;"
    "font-weight:800;"
    "background:linear-gradient(90deg,#7657ff,#ff3f91);"
    "-webkit-background-clip:text;"
    "-webkit-text-fill-color:transparent;"
    "}"

    ".tagline{"
    "font-size:13px;"
    "font-weight:700;"
    "color:#51495b;"
    "}"

    ".hero{"
    "padding:55px 45px;"
    "border-radius:30px;"
    "background:linear-gradient(135deg,#7657ff,#a855f7,#ff3f91);"
    "box-shadow:0 25px 60px rgba(118,87,255,.22);"
    "margin:25px 0;"
    "}"

    ".hero h1{"
    "font-family:'Playfair Display',serif;"
    "font-size:48px;"
    "font-weight:800;"
    "color:white!important;"
    "margin:0 0 12px 0;"
    "}"

    ".hero p{"
    "color:white!important;"
    "font-size:17px;"
    "font-weight:600;"
    "max-width:650px;"
    "}"

    ".section-title{"
    "font-family:'Playfair Display',serif;"
    "font-size:32px;"
    "font-weight:800;"
    "color:#17131d;"
    "margin:30px 0 20px 0;"
    "}"

    ".product-card{"
    "background:white;"
    "border:1px solid #eee8f5;"
    "border-radius:24px;"
    "padding:18px;"
    "margin-bottom:15px;"
    "box-shadow:0 12px 35px rgba(30,20,50,.07);"
    "}"

    ".product-image{"
    "height:170px;"
    "border-radius:18px;"
    "background:linear-gradient(135deg,#f0ebff,#fff0f7);"
    "display:flex;"
    "align-items:center;"
    "justify-content:center;"
    "font-size:70px;"
    "margin-bottom:15px;"
    "}"

    ".product-category{"
    "font-size:11px;"
    "font-weight:800;"
    "color:#7657ff;"
    "text-transform:uppercase;"
    "letter-spacing:1px;"
    "}"

    ".product-name{"
    "font-size:18px;"
    "font-weight:800;"
    "color:#17131d;"
    "margin-top:5px;"
    "}"

    ".price{"
    "font-size:21px;"
    "font-weight:800;"
    "color:#17131d;"
    "margin-top:12px;"
    "}"

    ".info-card{"
    "background:white;"
    "border:1px solid #eee8f5;"
    "border-radius:24px;"
    "padding:30px;"
    "box-shadow:0 12px 35px rgba(30,20,50,.06);"
    "}"

    ".admin-box{"
    "background:linear-gradient(135deg,#17131d,#332a3b);"
    "border-radius:25px;"
    "padding:30px;"
    "margin:25px 0;"
    "}"

    ".admin-box h2{"
    "color:white!important;"
    "font-weight:800;"
    "}"

    ".admin-box p{"
    "color:#e7e0ee!important;"
    "font-weight:500;"
    "}"

    ".footer{"
    "text-align:center;"
    "color:#716978;"
    "font-size:13px;"
    "padding-top:40px;"
    "}"

    "div.stButton>button{"
    "border-radius:13px;"
    "font-weight:800;"
    "min-height:42px;"
    "}"

    "@media(max-width:768px){"
    ".hero{padding:35px 25px;}"
    ".hero h1{font-size:36px;}"
    ".brand{font-size:34px;}"
    "}"

    "</style>"
)

st.markdown(CSS, unsafe_allow_html=True)

# ============================================================
# FUNCTIONS
# ============================================================

def go(page):
    st.session_state.page = page
    st.rerun()


def add_cart(product):
    st.session_state.cart.append(product)
    st.toast(product["name"] + " added to cart 🛒")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
    else:
        st.session_state.favorites.append(product_id)


def admin_logout():
    try:
        if supabase:
            supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.admin_user = None
    st.session_state.page = "Shop"
    st.rerun()


# ============================================================
# HEADER
# ============================================================

left, right = st.columns([2, 4])

with left:
    st.markdown(
        "<div class='brand'>LUXEMART</div>"
        "<div class='tagline'>Luxury • Style • Everyday Elegance</div>",
        unsafe_allow_html=True,
    )

with right:
    nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(6)

    with nav1:
        if st.button("⌂ Shop", use_container_width=True):
            go("Shop")

    with nav2:
        if st.button(
            "♡ " + str(len(st.session_state.favorites)),
            use_container_width=True,
        ):
            go("Favorites")

    with nav3:
        if st.button(
            "🛒 " + str(len(st.session_state.cart)),
            use_container_width=True,
        ):
            go("Cart")

    with nav4:
        if st.button("✦ About", use_container_width=True):
            go("About")

    with nav5:
        if st.button("☎ Contact", use_container_width=True):
            go("Contact")

    with nav6:
        if st.button("⚙ Admin", type="primary", use_container_width=True):
            go("Admin")

st.divider()

# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        "<div class='hero'>"
        "<h1>Luxury that feels<br>uniquely yours.</h1>"
        "<p>"
        "Discover fashion, jewellery, beauty and accessories "
        "designed to add elegance to your everyday style."
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='section-title'>Explore Collection</div>",
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "🔎 Search",
        placeholder="Search products...",
    )

    category = st.selectbox(
        "Category",
        ["All", "Fashion", "Jewellery", "Accessories", "Beauty"],
    )

    products = PRODUCTS.copy()

    if category != "All":
        products = [
            p for p in products
            if p["category"] == category
        ]

    if search:
        products = [
            p for p in products
            if search.lower() in p["name"].lower()
            or search.lower() in p["category"].lower()
        ]

    if not products:
        st.info("No products found.")
    else:
        cols = st.columns(4)

        for index, product in enumerate(products):

            with cols[index % 4]:

                favorite = product["id"] in st.session_state.favorites

                st.markdown(
                    "<div class='product-card'>"
                    "<div class='product-image'>"
                    + product["emoji"]
                    + "</div>"
                    "<div class='product-category'>"
                    + product["category"]
                    + "</div>"
                    "<div class='product-name'>"
                    + product["name"]
                    + "</div>"
                    "<div class='price'>Rs. "
                    + f"{product['price']:,}"
                    + "</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

                a, b = st.columns(2)

                with a:
                    if st.button(
                        "🛒 Add",
                        key="add_" + str(product["id"]),
                        use_container_width=True,
                    ):
                        add_cart(product)

                with b:
                    if st.button(
                        "❤️" if favorite else "♡",
                        key="favorite_" + str(product["id"]),
                        use_container_width=True,
                    ):
                        toggle_favorite(product["id"])
                        st.rerun()

# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        "<div class='section-title'>Your Favorites ❤️</div>",
        unsafe_allow_html=True,
    )

    favorites = [
        p for p in PRODUCTS
        if p["id"] in st.session_state.favorites
    ]

    if not favorites:
        st.info("No favorite products yet.")
    else:
        cols = st.columns(4)

        for index, product in enumerate(favorites):

            with cols[index % 4]:

                st.markdown(
                    "<div class='product-card'>"
                    "<div class='product-image'>"
                    + product["emoji"]
                    + "</div>"
                    "<div class='product-category'>"
                    + product["category"]
                    + "</div>"
                    "<div class='product-name'>"
                    + product["name"]
                    + "</div>"
                    "<div class='price'>Rs. "
                    + f"{product['price']:,}"
                    + "</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

                if st.button(
                    "🛒 Add to Cart",
                    key="favorite_cart_" + str(product["id"]),
                    use_container_width=True,
                ):
                    add_cart(product)

# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        "<div class='section-title'>Shopping Cart 🛒</div>",
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your cart is empty.")

    else:

        total = 0

        for index, product in enumerate(st.session_state.cart):

            total += product["price"]

            c1, c2, c3 = st.columns([4, 2, 1])

            with c1:
                st.write(
                    product["emoji"]
                    + " **"
                    + product["name"]
                    + "**"
                )

            with c2:
                st.write(
                    "Rs. "
                    + f"{product['price']:,}"
                )

            with c3:
                if st.button(
                    "✕",
                    key="remove_" + str(index),
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

        st.divider()

        st.markdown(
            "<div class='info-card'>"
            "<h2>Order Total</h2>"
            "<h1>Rs. "
            + f"{total:,}"
            + "</h1>"
            "</div>",
            unsafe_allow_html=True,
        )

        if st.button(
            "Proceed to Checkout",
            type="primary",
            use_container_width=True,
        ):
            go("Checkout")

# ============================================================
# CHECKOUT
# ============================================================

elif st.session_state.page == "Checkout":

    st.markdown(
        "<div class='section-title'>Checkout</div>",
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your cart is empty.")

    else:

        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        city = st.text_input("City")

        payment = st.selectbox(
            "Payment Method",
            ["Cash on Delivery", "Bank Transfer", "Other"],
        )

        total = sum(
            p["price"]
            for p in st.session_state.cart
        )

        st.markdown("### Total: Rs. " + f"{total:,}")

        if st.button(
            "Place Order",
            type="primary",
            use_container_width=True,
        ):

            if not name or not phone or not address or not city:
                st.error("Please complete all delivery information.")
            else:
                st.success(
                    "Order submitted successfully! 🎉"
                )

                st.session_state.cart = []

# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.markdown(
        "<div class='section-title'>About LUXEMART ✦</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='info-card'>"
        "<h2>Welcome to LUXEMART</h2>"
        "<p>"
        "LUXEMART is a modern online shopping experience "
        "for fashion, jewellery, beauty and accessories."
        "</p>"
        "<h3>Our Style</h3>"
        "<p>"
        "Elegant design, modern trends and carefully selected "
        "products — all in one place."
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

# ============================================================
# CONTACT
# ============================================================

elif st.session_state.page == "Contact":

    st.markdown(
        "<div class='section-title'>Contact Us ☎</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='info-card'>"
        "<h2>Get in Touch</h2>"
        "<p>📞 <strong>03169707804</strong></p>"
        "<p>✉️ <strong>asyabibi485@gmail.com</strong></p>"
        "<p>"
        "We are happy to help with products, orders and questions."
        "</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.write("")

    contact_name = st.text_input("Your Name")
    contact_email = st.text_input("Your Email")
    contact_message = st.text_area("Your Message")

    if st.button(
        "Send Message",
        type="primary",
        use_container_width=True,
    ):

        if not contact_name or not contact_email or not contact_message:
            st.error("Please complete all fields.")
        else:
            st.success("Message received. Thank you! 💜")

# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    # --------------------------------------------------------
    # LOGGED IN
    # --------------------------------------------------------

    if st.session_state.admin_user is not None:

        user = st.session_state.admin_user.user

        if user is not None:
            email = user.email
        else:
            email = "Authenticated Admin"

        st.markdown(
            "<div class='admin-box'>"
            "<h2>⚙ LUXEMART Admin Dashboard</h2>"
            "<p>Logged in as: <strong>"
            + str(email)
            + "</strong></p>"
            "</div>",
            unsafe_allow_html=True,
        )

        if st.button(
            "🚪 Logout Admin",
            use_container_width=True,
        ):
            admin_logout()

        st.markdown(
            "<div class='section-title'>Dashboard</div>",
            unsafe_allow_html=True,
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Products", len(PRODUCTS))

        with c2:
            st.metric("Cart Items", len(st.session_state.cart))

        with c3:
            st.metric(
                "Favorites",
                len(st.session_state.favorites),
            )

        with c4:
            st.metric("Store", "ONLINE")

        st.markdown(
            "<div class='section-title'>Products</div>",
            unsafe_allow_html=True,
        )

        for product in PRODUCTS:

            p1, p2, p3 = st.columns([4, 2, 2])

            with p1:
                st.write(
                    product["emoji"]
                    + " **"
                    + product["name"]
                    + "**"
                )

            with p2:
                st.write(
                    "Rs. "
                    + f"{product['price']:,}"
                )

            with p3:
                st.write(product["category"])

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------

    else:

        st.markdown(
            "<div class='admin-box'>"
            "<h2>🔐 Admin Login</h2>"
            "<p>"
            "Use the email and password already configured "
            "in Supabase Authentication."
            "</p>"
            "</div>",
            unsafe_allow_html=True,
        )

        with st.form("supabase_admin_login"):

            email = st.text_input(
                "Email",
                placeholder="Your Supabase email",
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Your Supabase password",
            )

            submitted = st.form_submit_button(
                "🔐 Sign In",
                type="primary",
                use_container_width=True,
            )

        if submitted:

            if supabase is None:

                st.error(
                    "Supabase is not connected. "
                    "Check your Streamlit Secrets."
                )

        
