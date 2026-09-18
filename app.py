import streamlit as st
from supabase import create_client

# ============================================================
# LUXEMART
# Modern Luxury Shopping App
# Supabase Email + Password Admin Login
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SUPABASE CONNECTION
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
# LIGHT LUXURY DESIGN
# ============================================================

CSS = (
    "<style>"

    "@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');"

    "html,body,[class*='css']{"
    "font-family:'DM Sans',sans-serif;"
    "}"

    ".stApp{"
    "background:"
    "radial-gradient(circle at 5% 5%,rgba(118,87,255,.08),transparent 25%),"
    "radial-gradient(circle at 95% 10%,rgba(255,105,180,.08),transparent 25%),"
    "linear-gradient(135deg,#ffffff 0%,#faf8ff 50%,#fff8fc 100%);"
    "color:#18151e;"
    "}"

    ".block-container{"
    "max-width:1250px;"
    "padding-top:25px;"
    "padding-bottom:60px;"
    "}"

    "h1,h2,h3,h4{"
    "color:#18151e!important;"
    "font-weight:800!important;"
    "}"

    ".brand{"
    "font-family:'Playfair Display',serif;"
    "font-size:42px;"
    "font-weight:800;"
    "letter-spacing:-1px;"
    "background:linear-gradient(90deg,#7657ff,#e9579d);"
    "-webkit-background-clip:text;"
    "-webkit-text-fill-color:transparent;"
    "}"

    ".tagline{"
    "font-size:13px;"
    "font-weight:700;"
    "color:#625b6d;"
    "margin-top:-5px;"
    "}"

    /* --------------------------------------------------------
       LIGHT BUTTONS
       -------------------------------------------------------- */

    "div.stButton>button{"
    "border-radius:14px;"
    "font-weight:800;"
    "min-height:44px;"
    "background:#f3efff;"
    "color:#4b3f72;"
    "border:1px solid #ddd4f5;"
    "box-shadow:0 4px 12px rgba(118,87,255,.08);"
    "transition:all .2s ease;"
    "}"

    "div.stButton>button:hover{"
    "background:#e9e1ff;"
    "color:#7657ff;"
    "border-color:#cfc1f5;"
    "transform:translateY(-2px);"
    "}"

    "div.stButton>button[kind='primary']{"
    "background:#eee8ff;"
    "color:#5b46a8;"
    "border:1px solid #d7caf7;"
    "}"

    "div.stButton>button[kind='primary']:hover{"
    "background:#e4dcff;"
    "color:#4b3795;"
    "border-color:#c6b6ef;"
    "}"

    /* --------------------------------------------------------
       HERO
       -------------------------------------------------------- */

    ".hero{"
    "padding:55px 45px;"
    "border-radius:30px;"
    "margin:25px 0;"
    "background:linear-gradient(135deg,#eee8ff,#f9edff 48%,#fff0f7);"
    "border:1px solid #e8ddf7;"
    "box-shadow:0 25px 60px rgba(118,87,255,.12);"
    "}"

    ".hero h1{"
    "font-family:'Playfair Display',serif;"
    "font-size:50px;"
    "line-height:1.05;"
    "color:#241c32!important;"
    "margin:0 0 15px 0;"
    "}"

    ".hero p{"
    "font-size:17px;"
    "font-weight:600;"
    "color:#5b5365!important;"
    "max-width:650px;"
    "}"

    /* --------------------------------------------------------
       SECTIONS
       -------------------------------------------------------- */

    ".section-title{"
    "font-family:'Playfair Display',serif;"
    "font-size:32px;"
    "font-weight:800;"
    "color:#18151e;"
    "margin:32px 0 20px 0;"
    "}"

    /* --------------------------------------------------------
       PRODUCT CARDS
       -------------------------------------------------------- */

    ".product-card{"
    "background:rgba(255,255,255,.96);"
    "border:1px solid #eee8f5;"
    "border-radius:24px;"
    "padding:18px;"
    "margin-bottom:15px;"
    "box-shadow:0 12px 35px rgba(30,20,50,.06);"
    "transition:all .25s ease;"
    "}"

    ".product-card:hover{"
    "transform:translateY(-5px);"
    "box-shadow:0 20px 45px rgba(30,20,50,.11);"
    "border-color:#ded3f4;"
    "}"

    ".product-image{"
    "height:175px;"
    "border-radius:18px;"
    "background:linear-gradient(135deg,#f1ecff,#fff0f7);"
    "display:flex;"
    "align-items:center;"
    "justify-content:center;"
    "font-size:72px;"
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
    "color:#18151e;"
    "margin-top:5px;"
    "}"

    ".price{"
    "font-size:21px;"
    "font-weight:800;"
    "color:#18151e;"
    "margin-top:12px;"
    "}"

    /* --------------------------------------------------------
       CARDS
       -------------------------------------------------------- */

    ".info-card{"
    "background:white;"
    "border:1px solid #eee8f5;"
    "border-radius:24px;"
    "padding:30px;"
    "box-shadow:0 12px 35px rgba(30,20,50,.06);"
    "}"

    /* --------------------------------------------------------
       ADMIN
       -------------------------------------------------------- */

    ".admin-box{"
    "background:linear-gradient(135deg,#f2edff,#fff0f7);"
    "border:1px solid #e5d9f5;"
    "border-radius:25px;"
    "padding:30px;"
    "margin:25px 0;"
    "box-shadow:0 15px 40px rgba(118,87,255,.09);"
    "}"

    ".admin-box h2{"
    "color:#2a2138!important;"
    "font-weight:800;"
    "}"

    ".admin-box p{"
    "color:#62596d!important;"
    "font-weight:600;"
    "}"

    /* --------------------------------------------------------
       INPUTS
       -------------------------------------------------------- */

    .stTextInput input,
    .stTextArea textarea{
        border-radius:13px!important;
        border:1px solid #ddd5e8!important;
        background:white!important;
    }

    /* --------------------------------------------------------
       FOOTER
       -------------------------------------------------------- */

    ".footer{"
    "text-align:center;"
    "color:#716978;"
    "font-size:13px;"
    "padding-top:45px;"
    "}"

    /* --------------------------------------------------------
       MOBILE
       -------------------------------------------------------- */

    "@media(max-width:768px){"
    ".hero{"
    "padding:35px 25px;"
    "}"
    ".hero h1{"
    "font-size:36px;"
    "}"
    ".brand{"
    "font-size:34px;"
    "}"
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
        if supabase is not None:
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

    n1, n2, n3, n4, n5, n6 = st.columns(6)

    with n1:
        if st.button("⌂ Shop", use_container_width=True):
            go("Shop")

    with n2:
        if st.button(
            "♡ " + str(len(st.session_state.favorites)),
            use_container_width=True,
        ):
            go("Favorites")

    with n3:
        if st.button(
            "🛒 " + str(len(st.session_state.cart)),
            use_container_width=True,
        ):
            go("Cart")

    with n4:
        if st.button("✦ About", use_container_width=True):
            go("About")

    with n5:
        if st.button("☎ Contact", use_container_width=True):
            go("Contact")

    with n6:
        if st.button(
            "⚙ Admin",
            type="primary",
            use_container_width=True,
        ):
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
        "🔎 Search products",
        placeholder="Search handbags, jewellery, perfume...",
    )

    category = st.selectbox(
        "Category",
        ["All", "Fashion", "Jewellery", "Accessories", "Beauty"],
    )

    products = PRODUCTS.copy()

    if category != "All":
        products = [
            product
            for product in products
            if product["category"] == category
        ]

    if search:
        products = [
            product
            for product in products
            if search.lower() in product["name"].lower()
            or search.lower() in product["category"].lower()
        ]

    if not products:

        st.info("No products found.")

    else:

        columns = st.columns(4)

        for index, product in enumerate(products):

            with columns[index % 4]:

                favorite = (
                    product["id"]
                    in st.session_state.favorites
                )

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

                b1, b2 = st.columns(2)

                with b1:

                    if st.button(
                        "🛒 Add",
                        key="add_" + str(product["id"]),
                        use_container_width=True,
                    ):
                        add_cart(product)

                with b2:

                    if st.button(
                        "❤️" if favorite else "♡",
                        key="fav_" + str(product["id"]),
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
        product
        for product in PRODUCTS
        if product["id"] in st.session_state.favorites
    ]

    if not favorites:

        st.info("You haven't added any favorites yet.")

    else:

        columns = st.columns(4)

        for index, product in enumerate(favorites):

            with columns[index % 4]:

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
                    key="fav_cart_" + str(product["id"]),
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

        if st.button(
            "Continue Shopping",
            type="primary",
            use_container_width=True,
        ):
            go("Shop")

    else:

        total = 0

        for index, product in enumerate(
            st.session_state.cart
        ):

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

        st.markdown(
            "<div class='info-card'>"
            "<h2>Delivery Information</h2>"
            "</div>",
            unsafe_allow_html=True,
        )

        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        city = st.text_input("City")

        payment = st.selectbox(
            "Payment Method",
            [
                "Cash on Delivery",
                "Bank Transfer",
                "Other",
            ],
        )

        total = sum(
            product["price"]
            for product in st.session_state.cart
        )

        st.markdown(
            "### Total: Rs. "
            + f"{total:,}"
        )

        if st.button(
            "Place Order",
            type="primary",
            use_container_width=True,
        ):

            if not name or not phone or not address or not city:

                st.error(
                    "Please complete all delivery information."
                )

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

        if (
            not contact_name
            or not contact_email
            or not contact_message
        ):
            st.error("Please complete all fields.")
        else:
            st.success(
                "Message received. Thank you! 💜"
            )

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
            st.metric(
                "Products",
                len(PRODUCTS),
            )

        with c2:
            st.metric(
                "Cart Items",
                len(st.session_state.cart),
            )

        with c3:
            st.metric(
                "Favorites",
                len(st.session_state.favorites),
            )

        with c4:
            st.metric(
                "Store",
                "ONLINE",
            )

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
    # ADMIN LOGIN
    # --------------------------------------------------------

    else:

        st.markdown(
            "<div class='admin-box'>"
            "<h2>🔐 Admin Login</h2>"
            "<p>"
            "Sign in using the email and password "
            "configured in Supabase Authentication."
            "</p>"
            "</div>",
            unsafe_allow_html=True,
        )

        with st.form("admin_login"):

            email = st.text_input(
                "Admin Email",
                placeholder="Enter your Supabase email",
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your Supabase password",
            )

            login = st.form_submit_button(
                "🔐 Sign In",
                type="primary",
                use_container_width=True,
            )

        if login:

            if supabase is None:

                st.error(
                    "Supabase is not connected. "
                    "Check your Streamlit Secrets."
                )

            elif not email or not password:

                st.warning(
                    "Please enter your email and password."
                )

            else:

                try:

                    response = (
                        supabase.auth.sign_in_with_password(
                            {
                                "email": email.strip(),
                                "password": password,
                            }
                        )
                    )

                    if response.user is not None:

                        st.session_state.admin_user = response

                        st.success(
                            "Login successful! 🎉"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Login failed. "
                            "Please check your credentials."
                        )

                except Exception as error:

                    error_message = str(error)

                    if "Invalid login credentials" in error_message:

                        st.error(
                            "Invalid email or password."
                        )

                    elif "Email not confirmed" in error_message:

                        st.error(
                            "Please confirm your Supabase email first."
                        )

                    else:

                        st.error(
                            "Supabase login error: "
                            + error_message
                        )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    "<div class='footer'>"
    "✦ LUXEMART — Luxury • Style • Everyday Elegance ✦<br>"
    "© 2026 LUXEMART. All rights reserved."
    "</div>",
    unsafe_allow_html=True,
)
