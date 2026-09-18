import streamlit as st

# ============================================================
# LUXEMART — MODERN TRENDY E-COMMERCE APP
# ============================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "category" not in st.session_state:
    st.session_state.category = "All"

if "search" not in st.session_state:
    st.session_state.search = ""


# ============================================================
# PRODUCT DATA
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Velvet Luxe Handbag",
        "category": "Fashion",
        "price": 3499,
        "emoji": "👜",
        "description": "Elegant everyday handbag with a premium luxury look.",
    },
    {
        "id": 2,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "emoji": "📿",
        "description": "Minimal pearl necklace designed for a timeless style.",
    },
    {
        "id": 3,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "emoji": "⌚",
        "description": "Modern gold-tone watch with an elegant premium finish.",
    },
    {
        "id": 4,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "emoji": "🕶️",
        "description": "Stylish sunglasses for a clean and confident look.",
    },
    {
        "id": 5,
        "name": "Luxury Perfume",
        "category": "Beauty",
        "price": 2999,
        "emoji": "🌸",
        "description": "A sophisticated fragrance with a soft lasting aroma.",
    },
    {
        "id": 6,
        "name": "Silk Evening Scarf",
        "category": "Fashion",
        "price": 1599,
        "emoji": "🧣",
        "description": "Soft statement scarf with an elegant evening aesthetic.",
    },
    {
        "id": 7,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "emoji": "💎",
        "description": "Delicate crystal bracelet for everyday glamour.",
    },
    {
        "id": 8,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "emoji": "💄",
        "description": "Beautiful makeup essentials packed into one stylish set.",
    },
]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap'
);

:root {
    --dark: #17131f;
    --purple: #7657ff;
    --pink: #ff4f9a;
    --text: #201b29;
    --muted: #81798b;
    --border: #eee8f4;
}

/* PAGE */

.stApp {
    background:
        radial-gradient(
            circle at 0% 0%,
            rgba(255, 79, 154, 0.13),
            transparent 25%
        ),
        radial-gradient(
            circle at 100% 5%,
            rgba(118, 87, 255, 0.15),
            transparent 27%
        ),
        linear-gradient(
            180deg,
            #fffaff 0%,
            #f8f7ff 50%,
            #ffffff 100%
        );
    color: var(--text);
}

.block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* REMOVE STREAMLIT MENU */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* HEADER */

.lux-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 17px 22px;
    margin-bottom: 18px;
    border-radius: 22px;
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(255,255,255,0.9);
    box-shadow: 0 12px 40px rgba(40,25,70,0.08);
    backdrop-filter: blur(18px);
}

.lux-logo {
    font-family: 'DM Sans', sans-serif;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -1.4px;
}

.lux-logo span {
    background: linear-gradient(
        135deg,
        #ff3f91,
        #7657ff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.live-dot {
    display: flex;
    align-items: center;
    gap: 7px;
    color: #716979;
    font-size: 12px;
    font-weight: 700;
}

.dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #38c982;
    box-shadow: 0 0 12px rgba(56,201,130,.7);
}

/* BUTTONS */

.stButton > button {
    min-height: 44px !important;
    border: 1px solid #eee8f4 !important;
    border-radius: 14px !important;
    background: rgba(255,255,255,0.92) !important;
    color: #282231 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 18px rgba(45,30,75,0.06);
    transition: all 0.22s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    border-color: transparent !important;
    color: white !important;
    background: linear-gradient(
        135deg,
        #ff3f91,
        #7657ff
    ) !important;
    box-shadow: 0 12px 30px rgba(118,87,255,0.24);
}

/* HERO */

.hero {
    position: relative;
    overflow: hidden;
    min-height: 390px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 55px 48px;
    margin: 10px 0 30px;
    border-radius: 32px;
    color: white;
    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(255,255,255,0.25),
            transparent 20%
        ),
        linear-gradient(
            135deg,
            #17131f,
            #332052 50%,
            #7657ff
        );
    box-shadow: 0 28px 70px rgba(69,45,125,0.22);
}

.hero:before {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    right: -80px;
    bottom: -120px;
    border-radius: 50%;
    background: rgba(255,79,154,0.34);
    filter: blur(15px);
}

.hero-label {
    position: relative;
    z-index: 2;
    width: fit-content;
    padding: 8px 13px;
    border-radius: 50px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

.hero h1 {
    position: relative;
    z-index: 2;
    max-width: 720px;
    margin: 18px 0 12px;
    font-family: 'Playfair Display', serif;
    font-size: clamp(42px, 7vw, 76px);
    line-height: 0.98;
    letter-spacing: -2.5px;
}

.hero p {
    position: relative;
    z-index: 2;
    max-width: 620px;
    margin: 0;
    color: rgba(255,255,255,0.78);
    font-size: 17px;
    line-height: 1.7;
}

/* SECTION */

.section {
    margin: 30px 0 18px;
}

.section h2 {
    margin: 0;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -0.8px;
}

.section p {
    margin: 6px 0 0;
    color: var(--muted);
}

/* PRODUCT */

.product-card {
    overflow: hidden;
    margin-bottom: 22px;
    border-radius: 25px;
    background: rgba(255,255,255,0.95);
    border: 1px solid var(--border);
    box-shadow: 0 12px 36px rgba(46,32,76,0.07);
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.product-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 22px 48px rgba(46,32,76,0.13);
}

.product-image {
    height: 190px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 72px;
    background:
        radial-gradient(
            circle at center,
            rgba(255,79,154,0.14),
            transparent 60%
        ),
        linear-gradient(
            135deg,
            #f7f1ff,
            #fff2f8
        );
}

.product-info {
    padding: 20px;
}

.product-category {
    color: #8b7e9e;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.product-name {
    margin-top: 7px;
    font-size: 19px;
    font-weight: 800;
    color: #241e2e;
}

.product-description {
    margin-top: 7px;
    min-height: 45px;
    color: #81798b;
    font-size: 13px;
    line-height: 1.55;
}

.price {
    margin-top: 13px;
    font-size: 21px;
    font-weight: 800;
    color: #7657ff;
}

.badge {
    display: inline-block;
    padding: 6px 10px;
    margin-bottom: 9px;
    border-radius: 50px;
    background: #fff0f7;
    color: #ff3f91;
    font-size: 10px;
    font-weight: 800;
}

/* SEARCH */

div[data-testid="stTextInput"] input {
    border-radius: 16px !important;
    border: 1px solid #eee8f4 !important;
    background: rgba(255,255,255,.92) !important;
    min-height: 48px !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* SELECTBOX */

div[data-baseweb="select"] > div {
    border-radius: 15px !important;
    border-color: #eee8f4 !important;
}

/* CART */

.cart-box {
    padding: 25px;
    border-radius: 25px;
    background: rgba(255,255,255,.92);
    border: 1px solid #eee8f4;
    box-shadow: 0 12px 35px rgba(46,32,76,.07);
}

.cart-total {
    padding: 18px 0;
    margin-top: 15px;
    border-top: 1px solid #eee8f4;
    font-size: 24px;
    font-weight: 800;
    color: #7657ff;
}

/* INFO CARDS */

.info-card {
    padding: 25px;
    min-height: 145px;
    border-radius: 24px;
    background: rgba(255,255,255,.88);
    border: 1px solid #eee8f4;
    box-shadow: 0 10px 30px rgba(46,32,76,.06);
}

.info-icon {
    font-size: 30px;
    margin-bottom: 8px;
}

.info-title {
    font-weight: 800;
    font-size: 17px;
}

.info-text {
    color: #81798b;
    font-size: 13px;
    line-height: 1.6;
}

/* FOOTER */

.lux-footer {
    margin-top: 50px;
    padding: 30px;
    text-align: center;
    border-radius: 25px;
    background: #17131f;
    color: rgba(255,255,255,.7);
}

.lux-footer strong {
    color: white;
}

/* MOBILE */

@media (max-width: 700px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        min-height: 330px;
        padding: 35px 25px;
        border-radius: 25px;
    }

    .hero h1 {
        font-size: 47px;
    }

    .hero p {
        font-size: 14px;
    }

    .lux-header {
        padding: 14px;
    }

    .lux-logo {
        font-size: 23px;
    }

    .product-image {
        height: 170px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"Rs. {value:,.0f}"


def add_to_cart(product):
    st.session_state.cart.append(product)
    st.toast(f"Added {product['name']} to cart ✦")


def remove_from_cart(index):
    if 0 <= index < len(st.session_state.cart):
        removed = st.session_state.cart.pop(index)
        st.toast(f"Removed {removed['name']}")


def toggle_favorite(product_id):
    if product_id in st.session_state.favorites:
        st.session_state.favorites.remove(product_id)
    else:
        st.session_state.favorites.append(product_id)


def go(page):
    st.session_state.page = page


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
<div class="lux-header">
    <div class="lux-logo">
        ✦ <span>LUXEMART</span>
    </div>

    <div class="live-dot">
        <span class="dot"></span>
        SHOPPING LIVE
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION
# ============================================================

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("⌂ Shop", use_container_width=True):
        go("Shop")

with nav2:
    if st.button("♡ Favorites", use_container_width=True):
        go("Favorites")

with nav3:
    if st.button(
        f"🛒 Cart ({len(st.session_state.cart)})",
        use_container_width=True,
    ):
        go("Cart")

with nav4:
    if st.button("✦ About", use_container_width=True):
        go("About")

with nav5:
    if st.button("☎ Contact", use_container_width=True):
        go("Contact")


# ============================================================
# SHOP PAGE
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
<div class="hero">

    <div class="hero-label">
        ✦ NEW SEASON COLLECTION
    </div>

    <h1>
        Style that<br>
        feels luxurious.
    </h1>

    <p>
        Discover carefully selected fashion, jewellery,
        accessories and beauty essentials designed to
        make everyday moments feel special.
    </p>

</div>
""",
        unsafe_allow_html=True,
    )

    # Search and category
    search_col, category_col = st.columns([2.2, 1])

    with search_col:
        search = st.text_input(
            "Search",
            placeholder="🔎  Search products...",
            label_visibility="collapsed",
        )
        st.session_state.search = search

    categories = ["All", "Fashion", "Jewellery", "Accessories", "Beauty"]

    with category_col:
        category = st.selectbox(
            "Category",
            categories,
            index=categories.index(st.session_state.category),
            label_visibility="collapsed",
        )
        st.session_state.category = category

    st.markdown(
        """
<div class="section">
    <h2>Featured collection</h2>
    <p>Explore our latest luxury-inspired pieces.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    filtered = PRODUCTS

    if category != "All":
        filtered = [
            p for p in filtered
            if p["category"] == category
        ]

    if search.strip():
        keyword = search.lower().strip()

        filtered = [
            p for p in filtered
            if keyword in p["name"].lower()
            or keyword in p["category"].lower()
            or keyword in p["description"].lower()
        ]

    if not filtered:
        st.info("No products found. Try another search.")

    cols = st.columns(4)

    for index, product in enumerate(filtered):

        with cols[index % 4]:

            is_favorite = product["id"] in st.session_state.favorites

            st.markdown(
                f"""
<div class="product-card">

    <div class="product-image">
        {product["emoji"]}
    </div>

    <div class="product-info">

        <div class="badge">
            NEW
        </div>

        <div class="product-category">
            {product["category"]}
        </div>

        <div class="product-name">
            {product["name"]}
        </div>

        <div class="product-description">
            {product["description"]}
        </div>

        <div class="price">
            {money(product["price"])}
        </div>

    </div>

</div>
""",
                unsafe_allow_html=True,
            )

            b1, b2 = st.columns(2)

            with b1:
                if st.button(
                    "♡" if not is_favorite else "♥",
                    key=f"fav_{product['id']}",
                    use_container_width=True,
                ):
                    toggle_favorite(product["id"])
                    st.rerun()

            with b2:
                if st.button(
                    "Add +",
                    key=f"cart_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(product)


# ============================================================
# FAVORITES PAGE
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        """
<div class="section">
    <h2>Your favorites ♡</h2>
    <p>Products you've saved for later.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    favorites = [
        p for p in PRODUCTS
        if p["id"] in st.session_state.favorites
    ]

    if not favorites:
        st.info("Your favorites list is empty.")

        if st.button("← Explore products"):
            go("Shop")
            st.rerun()

    else:

        cols = st.columns(4)

        for index, product in enumerate(favorites):

            with cols[index % 4]:

                st.markdown(
                    f"""
<div class="product-card">

    <div class="product-image">
        {product["emoji"]}
    </div>

    <div class="product-info">

        <div class="product-category">
            {product["category"]}
        </div>

        <div class="product-name">
            {product["name"]}
        </div>

        <div class="price">
            {money(product["price"])}
        </div>

    </div>

</div>
""",
                    unsafe_allow_html=True,
                )

                if st.button(
                    "🛒 Add to cart",
                    key=f"fav_cart_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(product)


# ============================================================
# CART PAGE
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        """
<div class="section">
    <h2>Your shopping bag 🛍️</h2>
    <p>Review your selected products before checkout.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button("← Continue shopping"):
            go("Shop")
            st.rerun()

    else:

        total = 0

        for i, product in enumerate(st.session_state.cart):

            price = product["price"]
            total += price

            c1, c2, c3 = st.columns([1, 4, 1])

            with c1:
                st.markdown(
                    f"""
<div style="
font-size:45px;
padding:10px;
text-align:center;
">
{product["emoji"]}
</div>
""",
                    unsafe_allow_html=True,
                )

            with c2:
                st.markdown(
                    f"""
**{product["name"]}**

{product["category"]}

**{money(price)}**
"""
                )

            with c3:
                if st.button(
                    "Remove",
                    key=f"remove_{i}",
                ):
                    remove_from_cart(i)
                    st.rerun()

        st.markdown(
            f"""
<div class="cart-box">

<div class="cart-total">
Total: {money(total)}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        st.markdown("### Checkout")

        name = st.text_input(
            "Full name",
            placeholder="Your name",
        )

        phone = st.text_input(
            "Phone number",
            placeholder="03XXXXXXXXX",
        )

        address = st.text_area(
            "Delivery address",
            placeholder="Enter your complete delivery address",
        )

        if st.button(
            "✨ Place Order",
            use_container_width=True,
        ):

            if not name or not phone or not address:
                st.warning(
                    "Please complete your name, phone number and address."
                )

            else:
                st.success(
                    f"Thank you {name}! Your order has been received."
                )

                st.session_state.cart = []


# ============================================================
# ABOUT PAGE
# ============================================================

elif st.session_state.page == "About":

    st.markdown(
        """
<div class="section">
    <h2>About LUXEMART ✦</h2>
    <p>A modern shopping experience built around style and simplicity.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    a, b, c = st.columns(3)

    with a:
        st.markdown(
            """
<div class="info-card">

<div class="info-icon">✦</div>

<div class="info-title">
Curated Style
</div>

<div class="info-text">
Discover carefully selected products
with a modern luxury-inspired aesthetic.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with b:
        st.markdown(
            """
<div class="info-card">

<div class="info-icon">♡</div>

<div class="info-title">
Simple Shopping
</div>

<div class="info-text">
Search, save favorites, add products
to your cart and checkout easily.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with c:
        st.markdown(
            """
<div class="info-card">

<div class="info-icon">⚡</div>

<div class="info-title">
Modern Experience
</div>

<div class="info-text">
A responsive interface designed for
both mobile and desktop shoppers.
</div>

</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# CONTACT PAGE
# ============================================================

elif st.session_state.page == "Contact":

    st.markdown(
        """
<div class="section">
    <h2>Let's connect ✦</h2>
    <p>We're here to help with your shopping experience.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            """
<div class="info-card">

<div class="info-icon">☎</div>

<div class="info-title">
Phone
</div>

<div class="info-text">
03220956920
</div>

</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        st.markdown(
            """
<div class="info-card">

<div class="info-icon">✉</div>

<div class="info-title">
Email
</div>

<div class="info-text">
asyabibi485@gmail.com
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with c2:

        st.markdown("### Send us a message")

        contact_name = st.text_input(
            "Name",
            key="contact_name",
        )

        contact_email = st.text_input(
            "Email",
            key="contact_email",
        )

        message = st.text_area(
            "Message",
            key="contact_message",
        )

        if st.button(
            "Send Message ✦",
            use_container_width=True,
        ):

            if not contact_name or not contact_email or not message:
                st.warning("Please complete all fields.")
            else:
                st.success(
                    "Your message has been received. Thank you!"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="lux-footer">

<strong>✦ LUXEMART</strong>

<br><br>

Modern style • Curated products • Easy shopping

<br><br>

© 2026 LUXEMART. All rights reserved.

</div>
""",
    unsafe_allow_html=True,
)
