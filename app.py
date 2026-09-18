import streamlit as st
from supabase import create_client
from datetime import datetime

# =========================================================
# LuxeMart — Dark & Bold Luxury Marketplace
# =========================================================

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🖤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LUXURY DARK DESIGN
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root {
    --black: #08090B;
    --panel: #111318;
    --panel2: #181A20;
    --gold: #D4AF37;
    --gold-light: #F2D77A;
    --white: #FFFFFF;
    --muted: #A8AAB2;
    --border: #30323A;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--black) !important;
    color: var(--white) !important;
}

[data-testid="stHeader"] {
    background: rgba(8,9,11,.95) !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
}

* {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: white !important;
}

.luxe-logo {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -2px;
    color: white;
}

.luxe-logo span {
    color: var(--gold);
}

.kicker {
    color: var(--gold-light);
    font-size: .78rem;
    font-weight: 800;
    letter-spacing: .28em;
    margin-bottom: 12px;
}

.hero {
    margin-top: 25px;
    padding: 55px 45px;
    border-radius: 28px;
    border: 1px solid var(--border);
    background:
        radial-gradient(circle at 85% 15%, rgba(212,175,55,.18), transparent 30%),
        linear-gradient(135deg,#17191F,#090A0D);
    box-shadow: 0 25px 80px rgba(0,0,0,.45);
}

.hero h1 {
    font-size: clamp(3rem,8vw,7rem) !important;
    line-height: .95;
    margin: 12px 0 25px;
}

.hero p {
    max-width: 720px;
    color: #C9CAD0;
    font-size: 1.1rem;
    line-height: 1.8;
}

.gold-line {
    height: 2px;
    margin: 25px 0;
    background: linear-gradient(
        90deg,
        var(--gold),
        transparent
    );
}

.card {
    background: linear-gradient(
        145deg,
        #191B21,
        #101115
    );
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 15px 35px rgba(0,0,0,.25);
}

.card:hover {
    border-color: var(--gold);
}

.product-name {
    color: white;
    font-size: 1.2rem;
    font-weight: 800;
}

.product-category {
    color: var(--muted);
    margin-top: 5px;
}

.price {
    color: var(--gold-light);
    font-size: 1.3rem;
    font-weight: 800;
    margin-top: 15px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 50px;
    border: 1px solid rgba(212,175,55,.5);
    color: var(--gold-light);
    font-size: .72rem;
    font-weight: 800;
    letter-spacing: .08em;
}

.stat {
    text-align: center;
    padding: 22px;
    border: 1px solid var(--border);
    border-radius: 18px;
    background: var(--panel);
}

.stat-number {
    font-family: 'Playfair Display', serif;
    color: var(--gold-light);
    font-size: 2rem;
    font-weight: 800;
}

.stat-label {
    color: var(--muted);
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: .08em;
}

/* Buttons */

.stButton > button {
    width: 100%;
    min-height: 46px;
    border-radius: 13px !important;
    border: 1px solid #41434B !important;
    background: #181A20 !important;
    color: white !important;
    font-weight: 800 !important;
}

.stButton > button:hover {
    border-color: var(--gold) !important;
    color: var(--gold-light) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        #D4AF37,
        #A98217
    ) !important;
    color: #090909 !important;
    border: none !important;
}

/* Inputs */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background: #15171C !important;
    color: white !important;
    border: 1px solid #353740 !important;
    border-radius: 12px !important;
}

label {
    color: #E8E8EC !important;
}

/* Tabs */

.stTabs [data-baseweb="tab"] {
    color: #A5A6AD !important;
    font-weight: 800 !important;
}

.stTabs [aria-selected="true"] {
    color: var(--gold-light) !important;
}

/* Footer */

.footer {
    margin-top: 60px;
    padding: 30px 10px;
    text-align: center;
    color: var(--muted);
    border-top: 1px solid var(--border);
}

@media(max-width:700px) {

    .block-container {
        padding-left: .8rem;
        padding-right: .8rem;
    }

    .hero {
        padding: 30px 22px;
        border-radius: 20px;
    }

    .hero h1 {
        font-size: 3.4rem !important;
    }

    .luxe-logo {
        font-size: 2.4rem;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SUPABASE CONNECTION
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
# DATABASE HELPERS
# =========================================================

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


def price(value):

    try:
        return f"Rs. {float(value):,.0f}"
    except:
        return f"Rs. {value}"


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="luxe-logo">
    Luxe<span>Mart</span>
</div>

<div class="kicker">
    CURATED • ELEGANT • EVERYDAY
</div>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

nav1, nav2, nav3 = st.columns(3)

with nav1:
    if st.button(
        "✦  SHOP",
        type="primary" if st.session_state.page == "Shop"
        else "secondary"
    ):
        st.session_state.page = "Shop"
        st.rerun()

with nav2:
    if st.button(
        "COLLECTIONS",
        type="primary" if st.session_state.page == "Collections"
        else "secondary"
    ):
        st.session_state.page = "Collections"
        st.rerun()

with nav3:
    if st.button(
        f"🛍 CART ({len(st.session_state.cart)})",
        type="primary"
    ):
        st.session_state.page = "Cart"
        st.rerun()


st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)


# =========================================================
# DATABASE PRODUCTS
# =========================================================

products = get_products()

# Demo products appear if database is empty.
if not products:

    products = [
        {
            "id": "demo1",
            "name": "Classic Linen Set",
            "category": "Clothes",
            "price": 8500
        },
        {
            "id": "demo2",
            "name": "Signature Evening Dress",
            "category": "Clothes",
            "price": 12900
        },
        {
            "id": "demo3",
            "name": "Minimal Ceramic Vase",
            "category": "Home",
            "price": 4200
        },
        {
            "id": "demo4",
            "name": "Soft Luxe Cushion Set",
            "category": "Home",
            "price": 3800
        }
    ]


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown("""
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
            from independent sellers in a clean,
            premium shopping experience.
        </p>

    </div>
    """, unsafe_allow_html=True)

    # Statistics

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="stat">
            <div class="stat-number">✦</div>
            <div class="stat-label">
                CURATED COLLECTION
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown(f"""
        <div class="stat">
            <div class="stat-number">
                {len(products)}
            </div>
            <div class="stat-label">
                PRODUCTS
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown(f"""
        <div class="stat">
            <div class="stat-number">
                {len(st.session_state.cart)}
            </div>
            <div class="stat-label">
                CART ITEMS
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Featured Finds")

    search = st.text_input(
        "Search",
        placeholder="Search clothing, home products..."
    )

    shown = products

    if search:

        q = search.lower()

        shown = [
            p for p in products
            if q in str(p.get("name", "")).lower()
            or q in str(p.get("category", "")).lower()
        ]

    cols = st.columns(2)

    for index, product in enumerate(shown):

        with cols[index % 2]:

            st.markdown(f"""
            <div class="card">

                <span class="badge">
                    {product.get("category", "Collection")}
                </span>

                <div class="product-name"
                     style="margin-top:15px">
                    {product.get("name", "Product")}
                </div>

                <div class="product-category">
                    Curated by LuxeMart
                </div>

                <div class="price">
                    {price(product.get("price", 0))}
                </div>

            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "ADD TO CART",
                key=f"add_{index}_{product.get('id')}",
                type="primary"
            ):

                st.session_state.cart.append(product)

                st.success(
                    f"{product.get('name')} added to cart."
                )

                st.rerun()


# =========================================================
# COLLECTIONS
# =========================================================

elif st.session_state.page == "Collections":

    st.markdown(
        '<div class="kicker">EXPLORE</div>',
        unsafe_allow_html=True
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
        ["All"] + categories
    )

    if selected == "All":
        shown = products
    else:
        shown = [
            p for p in products
            if str(p.get("category", "")) == selected
        ]

    for product in shown:

        st.markdown(f"""
        <div class="card">

            <span class="badge">
                {product.get("category", "Collection")}
            </span>

            <div class="product-name"
                 style="margin-top:15px">
                {product.get("name")}
            </div>

            <div class="price">
                {price(product.get("price", 0))}
            </div>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="kicker">YOUR SELECTION</div>',
        unsafe_allow_html=True
    )

    st.title("Shopping Cart")

    if not st.session_state.cart:

        st.info(
            "Your cart is empty. "
            "Add something beautiful from the Shop."
        )

    else:

        total = 0

        for i, product in enumerate(
            st.session_state.cart
        ):

            product_price = float(
                product.get("price", 0)
            )

            total += product_price

            st.markdown(f"""
            <div class="card">

                <div class="product-name">
                    {product.get("name")}
                </div>

                <div class="product-category">
                    {product.get("category")}
                </div>

                <div class="price">
                    {price(product_price)}
                </div>

            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            f"## Total: {price(total)}"
        )

        st.markdown("### Checkout")

        name = st.text_input("Your name")
        phone = st.text_input(
            "Phone / WhatsApp"
        )
        address = st.text_area(
            "Delivery address"
        )

        if st.button(
            "PLACE ORDER",
            type="primary"
        ):

            if not name or not phone or not address:

                st.warning(
                    "Please enter your name, "
                    "phone and address."
                )

            else:

                success = True

                try:

                    for product in st.session_state.cart:

                        supabase.table(
                            "orders"
                        ).insert({
                            "product_id":
                                product.get("id"),

                            "product_name":
                                product.get("name"),

                            "customer_name":
                                name,

                            "phone":
                                phone,

                            "address":
                                address,

                            "quantity":
                                1,

                            "total":
                                float(
                                    product.get(
                                        "price", 0
                                    )
                                ),

                            "status":
                                "Pending",

                            "created_at":
                                datetime.utcnow()
                                .isoformat()
                        }).execute()

                except Exception as e:

                    success = False

                    st.error(
                        "Order could not be submitted. "
                        "Check your Supabase orders table."
                    )

                if success:

                    st.session_state.cart = []

                    st.success(
                        "Your order has been submitted successfully!"
                    )

                    st.balloons()


# =========================================================
# SELL WITH US
# =========================================================

elif st.session_state.page == "Sell With Us":

    st.markdown(
        '<div class="kicker">PARTNER WITH US</div>',
        unsafe_allow_html=True
    )

    st.title("Sell With Us")

    st.markdown("""
    <div class="hero">

        <div class="kicker">
            INDEPENDENT SELLERS
        </div>

        <h2>
            Bring your best products.
        </h2>

        <p>
            Contact LuxeMart to list approved clothing
            and home products.
        </p>

    </div>
    """, unsafe_allow_html=True)

    seller_name = st.text_input("Name")

    seller_phone = st.text_input(
        "Phone / WhatsApp"
    )

    seller_details = st.text_area(
        "Product details",
        height=180
    )

    if st.button(
        "SEND SELLER REQUEST",
        type="primary"
    ):

        if not seller_name or not seller_phone or not seller_details:

            st.warning(
                "Please complete all fields."
            )

        else:

            try:

                supabase.table(
                    "seller_requests"
                ).insert({

                    "name":
                        seller_name,

                    "phone":
                        seller_phone,

                    "product_details":
                        seller_details,

                    "status":
                        "Pending",

                    "created_at":
                        datetime.utcnow()
                        .isoformat()

                }).execute()

                st.success(
                    "Seller request sent successfully!"
                )

            except Exception:

                st.error(
                    "Could not send seller request. "
                    "Check the seller_requests table."
                )


# =========================================================
# ABOUT
# =========================================================

elif st.session_state.page == "About":

    st.markdown(
        '<div class="kicker">OUR STORY</div>',
        unsafe_allow_html=True
    )

    st.title("About LuxeMart")

    st.markdown("""
    <div class="hero">

        <div class="kicker">
            CURATED • ELEGANT • EVERYDAY
        </div>

        <h2>
            Refined. Simple. Personal.
        </h2>

        <p>
            LuxeMart is a premium marketplace for
            carefully selected clothing and beautiful
            home products from independent sellers.
        </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CONTACT
# =========================================================

elif st.session_state.page == "Contact":

    st.markdown(
        '<div class="kicker">GET IN TOUCH</div>',
        unsafe_allow_html=True
    )

    st.title("Contact LuxeMart")

    st.markdown("""
    <div class="card">

        <div class="product-name">
            Customer Support
        </div>

        <br>

        <div style="color:#A8AAB2;font-size:1rem">

            <strong style="color:#F2D77A">
                Phone / WhatsApp
            </strong>
            <br>
            03220956920

            <br><br>

            <strong style="color:#F2D77A">
                Email
            </strong>
            <br>
            asyabibi485@gmail.com

     
