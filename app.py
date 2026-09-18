import streamlit as st
from supabase import create_client
from datetime import datetime
import html

# =========================================================
# LuxeMart — Luxury Marketplace
# =========================================================

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🖤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LUXURY DESIGN
# =========================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700;800;900&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --black: #07080A;
    --dark: #0D0F13;
    --panel: #151820;
    --panel2: #1C2029;
    --gold: #D4AF37;
    --gold2: #F4D875;
    --white: #FFFFFF;
    --text: #F7F7F9;
    --muted: #C4C7CF;
    --border: #3A3E49;
    --green: #48D597;
}

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background: #07080A !important;
    color: #FFFFFF !important;
}

[data-testid="stHeader"] {
    background: #07080A !important;
}

[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    max-width: 1250px;
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
}

* {
    font-family: 'DM Sans', sans-serif;
}

h1,
h2,
h3 {
    font-family: 'Playfair Display', serif !important;
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

p,
span,
div,
label {
    color: #F7F7F9;
}

.luxe-logo {
    font-family: 'Playfair Display', serif !important;
    font-size: 3.4rem;
    line-height: 1;
    font-weight: 800;
    letter-spacing: -2px;
    color: #FFFFFF !important;
}

.luxe-logo span {
    color: #F4D875 !important;
}

.kicker {
    color: #F4D875 !important;
    font-size: 0.78rem;
    font-weight: 900;
    letter-spacing: 0.25em;
    margin-top: 8px;
    margin-bottom: 12px;
}

.gold-line {
    height: 2px;
    margin: 18px 0 25px 0;
    background: linear-gradient(
        90deg,
        #F4D875,
        #D4AF37,
        transparent
    );
}

/* HERO */

.hero {
    margin: 18px 0 28px 0;
    padding: 55px 45px;
    border-radius: 28px;
    border: 1px solid #3A3E49;
    background:
        radial-gradient(
            circle at 85% 15%,
            rgba(212,175,55,0.25),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #20242D,
            #0A0B0E
        );
    box-shadow:
        0 25px 70px rgba(0,0,0,0.55);
}

.hero h1 {
    font-size: clamp(3rem, 8vw, 6.5rem) !important;
    line-height: 0.95 !important;
    margin: 12px 0 25px 0 !important;
    color: #FFFFFF !important;
}

.hero p {
    color: #E4E5EA !important;
    font-size: 1.08rem;
    line-height: 1.8;
    max-width: 720px;
    font-weight: 600;
}

/* CARDS */

.card {
    background:
        linear-gradient(
            145deg,
            #1A1D25,
            #101216
        );
    border: 1px solid #393D47;
    border-radius: 22px;
    padding: 25px;
    margin-bottom: 18px;
    box-shadow:
        0 14px 35px rgba(0,0,0,0.30);
}

.card-title {
    color: #FFFFFF !important;
    font-size: 1.25rem;
    font-weight: 900;
    margin-top: 14px;
}

.card-text {
    color: #C9CCD4 !important;
    font-size: 0.95rem;
    font-weight: 600;
    margin-top: 6px;
}

.price {
    color: #F4D875 !important;
    font-size: 1.35rem;
    font-weight: 900;
    margin-top: 15px;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 50px;
    border: 1px solid #D4AF37;
    background: rgba(212,175,55,0.10);
    color: #F4D875 !important;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.08em;
}

/* STATS */

.stat {
    text-align: center;
    padding: 24px 15px;
    border: 1px solid #393D47;
    border-radius: 20px;
    background: #11141A;
    margin-bottom: 18px;
}

.stat-number {
    font-family: 'Playfair Display', serif !important;
    color: #F4D875 !important;
    font-size: 2.2rem;
    font-weight: 900;
}

.stat-label {
    color: #D2D4DA !important;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.10em;
}

/* BUTTONS */

.stButton > button {
    min-height: 48px !important;
    width: 100%;
    border-radius: 14px !important;
    border: 1px solid #555A66 !important;
    background: #1B1E26 !important;
    color: #FFFFFF !important;
    font-size: 0.88rem !important;
    font-weight: 900 !important;
    letter-spacing: 0.04em !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.22);
}

.stButton > button:hover {
    border-color: #F4D875 !important;
    color: #F4D875 !important;
    background: #242832 !important;
    transform: translateY(-1px);
}

.stButton > button[kind="primary"] {
    background:
        linear-gradient(
            135deg,
            #F4D875,
            #C49B28
        ) !important;
    color: #090909 !important;
    border: 1px solid #F4D875 !important;
    font-weight: 900 !important;
    text-shadow: none !important;
}

.stButton > button[kind="primary"]:hover {
    background:
        linear-gradient(
            135deg,
            #FFE994,
            #D4AF37
        ) !important;
    color: #000000 !important;
}

/* INPUTS */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #151820 !important;
    color: #FFFFFF !important;
    border: 1px solid #454A56 !important;
    border-radius: 13px !important;
    font-weight: 700 !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #AEB2BC !important;
}

.stTextInput label,
.stTextArea label,
.stNumberInput label,
.stSelectbox label {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* CHECKBOX */

.stCheckbox label {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* ALERTS */

[data-testid="stAlert"] {
    border-radius: 14px !important;
    font-weight: 700 !important;
}

/* DIVIDER */

hr {
    border-color: #353943 !important;
}

/* FOOTER */

.footer {
    margin-top: 65px;
    padding: 30px 10px;
    text-align: center;
    color: #AEB2BC !important;
    border-top: 1px solid #30343D;
    font-weight: 600;
}

.footer strong {
    color: #F4D875 !important;
}

/* MOBILE */

@media (max-width: 700px) {

    .block-container {
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
    }

    .luxe-logo {
        font-size: 2.6rem;
    }

    .hero {
        padding: 30px 22px;
        border-radius: 20px;
    }

    .hero h1 {
        font-size: 3.3rem !important;
    }

    .hero p {
        font-size: 0.98rem;
    }

    .card {
        padding: 20px;
    }

    .stButton > button {
        min-height: 50px !important;
        font-size: 0.82rem !important;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# SUPABASE
# =========================================================

try:
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]

    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

except Exception:
    st.error(
        "Supabase is not configured. "
        "Open Streamlit → Manage app → Settings → Secrets."
    )
    st.stop()

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# =========================================================
# HELPERS
# =========================================================

def safe_text(value):
    return html.escape(str(value if value is not None else ""))


def price(value):
    try:
        return f"Rs. {float(value):,.0f}"
    except Exception:
        return f"Rs. {value}"


def get_products():
    try:
        result = (
            supabase
            .table("products")
            .select("*")
            .execute()
        )
        return result.data or []
    except Exception:
        return []


def get_orders():
    try:
        result = (
            supabase
            .table("orders")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        return result.data or []
    except Exception:
        return []


def get_seller_requests():
    try:
        result = (
            supabase
            .table("seller_requests")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        return result.data or []
    except Exception:
        return []


def add_to_cart(product):
    st.session_state.cart.append(product)


def cart_total():
    total = 0

    for product in st.session_state.cart:
        try:
            total += float(product.get("price", 0))
        except Exception:
            pass

    return total


def remove_cart_item(index):
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)


# =========================================================
# DEMO PRODUCTS
# =========================================================

products = get_products()

if not products:
    products = [
        {
            "id": "demo1",
            "name": "Classic Linen Set",
            "category": "Clothes",
            "price": 8500,
        },
        {
            "id": "demo2",
            "name": "Signature Evening Dress",
            "category": "Clothes",
            "price": 12900,
        },
        {
            "id": "demo3",
            "name": "Minimal Ceramic Vase",
            "category": "Home",
            "price": 4200,
        },
        {
            "id": "demo4",
            "name": "Soft Luxe Cushion Set",
            "category": "Home",
            "price": 3800,
        },
    ]

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
<div class="luxe-logo">
    Luxe<span>Mart</span>
</div>

<div class="kicker">
    CURATED • ELEGANT • EVERYDAY
</div>
""",
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGATION
# =========================================================

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    if st.button(
        "✦ SHOP",
        type="primary"
        if st.session_state.page == "Shop"
        else "secondary",
    ):
        st.session_state.page = "Shop"
        st.rerun()

with nav2:
    if st.button(
        "COLLECTIONS",
        type="primary"
        if st.session_state.page == "Collections"
        else "secondary",
    ):
        st.session_state.page = "Collections"
        st.rerun()

with nav3:
    if st.button(
        f"🛍 CART ({len(st.session_state.cart)})",
        type="primary"
        if st.session_state.page == "Cart"
        else "secondary",
    ):
        st.session_state.page = "Cart"
        st.rerun()

with nav4:
    if st.button(
        "MORE",
        type="primary"
        if st.session_state.page in [
            "Sell With Us",
            "About",
            "Contact",
            "Admin",
        ]
        else "secondary",
    ):
        st.session_state.page = "More"
        st.rerun()

st.markdown(
    '<div class="gold-line"></div>',
    unsafe_allow_html=True,
)

# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
<div class="hero">

    <div class="kicker">
        LUXURY • SIMPLIFIED
    </div>

    <h1>
        Luxury finds<br>
        for your life.
    </h1>

    <p>
        Discover refined clothing and beautiful home products
        from independent sellers in a clean, premium shopping
        experience.
    </p>

</div>
""",
        unsafe_allow_html=True,
    )

    a, b, c = st.columns(3)

    with a:
        st.markdown(
            """
<div class="stat">
    <div class="stat-number">✦</div>
    <div class="stat-label">CURATED COLLECTION</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with b:
        st.markdown(
            f"""
<div class="stat">
    <div class="stat-number">{len(products)}</div>
    <div class="stat-label">PRODUCTS</div>
</div>
""",
            unsafe_allow_html=True,
        )

    with c:
        st.markdown(
            f"""
<div class="stat">
    <div class="stat-number">{len(st.session_state.cart)}</div>
    <div class="stat-label">CART ITEMS</div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("## Featured Finds")

    search = st.text_input(
        "Search products",
        placeholder="🔎 Search clothing, home products...",
    )

    if search:
        query = search.lower().strip()

        shown = [
            p
            for p in products
            if query in str(p.get("name", "")).lower()
            or query in str(p.get("category", "")).lower()
        ]
    else:
        shown = products

    if not shown:
        st.info("No products found.")

    cols = st.columns(2)

    for index, product in enumerate(shown):

        with cols[index % 2]:

            product_name = safe_text(
                product.get("name", "Product")
            )

            product_category = safe_text(
                product.get("category", "Collection")
            )

            product_id = product.get("id", index)

            st.markdown(
                f"""
<div class="card">

    <span class="badge">
        {product_category}
    </span>

    <div class="card-title">
        {product_name}
    </div>

    <div class="card-text">
        Curated by LuxeMart
    </div>

    <div class="price">
        {price(product.get("price", 0))}
    </div>

</div>
""",
                unsafe_allow_html=True,
            )

            if st.button(
                "＋ ADD TO CART",
                key=f"add_{index}_{product_id}",
                type="primary",
            ):
                add_to_cart(product)

                st.success(
                    f"{product.get('name', 'Product')} added to cart."
                )

                st.rerun()

# =========================================================
# COLLECTIONS
# =========================================================

elif st.session_state.page == "Collections":

    st.markdown(
        '<div class="kicker">EXPLORE</div>',
        unsafe_allow_html=True,
    )

    st.title("Collections")

    categories = sorted(
        set(
            str(p.get("category", "Other"))
            for p in products
        )
    )

    selected = st.selectbox(
        "Choose collection",
        ["All"] + categories,
    )

    if selected == "All":
        shown = products
    else:
        shown = [
            p
            for p in products
            if str(p.get("category", "")) == selected
        ]

    cols = st.columns(2)

    for index, product in enumerate(shown):

        with cols[index % 2]:

            st.markdown(
                f"""
<div class="card">

    <span class="badge">
        {safe_text(product.get("category", "Collection"))}
    </span>

    <div class="card-title">
        {safe_text(product.get("name", "Product"))}
    </div>

    <div class="price">
        {price(product.get("price", 0))}
    </div>

</div>
""",
                unsafe_allow_html=True,
            )

            if st.button(
                "＋ ADD TO CART",
                key=f"collection_{index}_{product.get('id', index)}",
                type="primary",
            ):
                add_to_cart(product)
                st.success("Added to cart.")
                st.rerun()

# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="kicker">YOUR SELECTION</div>',
        unsafe_allow_html=True,
    )

    st.title("Shopping Cart")

    if not st.session_state.cart:

        st.info(
            "Your cart is empty. Add something beautiful from Shop."
        )

        if st.button("✦ CONTINUE SHOPPING", type="primary"):
            st.session_state.page = "Shop"
            st.rerun()

    else:

        st.markdown(
            f"""
<div class="hero">

    <div class="kicker">
        YOUR CART
    </div>

    <h2>
        {len(st.session_state.cart)} item(s)
    </h2>

    <p>
        Review your selection below, then complete your
        delivery details for an easy checkout.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

        # Cart items

        for i, product in enumerate(
            st.session_state.cart
        ):

            st.markdown(
                f"""
<div class="card">

    <div class="card-title">
        {safe_text(product.get("name", "Product"))}
    </div>

    <div class="card-text">
        {safe_text(product.get("category", "Collection"))}
    </div>

    <div class="price">
        {price(product.get("price", 0))}
    </div>

</div>
""",
                unsafe_allow_html=True,
            )

            if st.button(
                "REMOVE",
                key=f"remove_{i}",
            ):
                remove_cart_item(i)
                st.rerun()

        st.markdown("---")

        total = cart_total()

        st.markdown(
            f"""
<div class="card">

    <div class="kicker">
        ORDER SUMMARY
    </div>

    <div style="
        font-size:1.5rem;
        font-weight:900;
        color:#FFFFFF;
    ">
        TOTAL
    </div>

    <div style="
        font-size:2.2rem;
        font-weight:900;
        color:#F4D875;
        margin-top:8px;
    ">
        {price(total)}
    </div>

</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown("## Easy Checkout")

        checkout_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
        )

        checkout_phone = st.text_input(
            "Phone / WhatsApp",
            placeholder="03XXXXXXXXX",
        )

        checkout_address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete delivery address",
            height=120,
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Cash on Delivery",
                "Bank Transfer",
            ],
        )

        st.markdown("")

        if st.button(
            "🛒 PLACE ORDER NOW",
            type="primary",
        ):

            if (
                not checkout_name.strip()
                or not checkout_phone.strip()
                or not checkout_address.strip()
            ):

                st.warning(
                    "Please complete your name, phone and delivery address."
                )

            else:

                order_success = True

                try:

                    for product in st.session_state.cart:

                        product_price = float(
                            product.get("price", 0)
                        )

                        supabase.table(
                            "orders"
                        ).insert(
                            {
                                "product_id": product.get("id"),
                                "product_name": product.get("name"),
                                "customer_name": checkout_name.strip(),
                                "phone": checkout_phone.strip(),
                                "address": checkout_address.strip(),
                                "quantity": 1,
                               
