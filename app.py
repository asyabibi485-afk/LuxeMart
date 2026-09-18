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
# SUPABASE CONNECTION
# ============================================================

try:
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]
    ADMIN_EMAIL = st.secrets["admin"]["email"]

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    supabase_ok = True

except Exception as e:
    supabase = None
    ADMIN_EMAIL = ""
    supabase_ok = False
    supabase_error = str(e)

# ============================================================
# CONTACT
# ============================================================

PHONE = "03169707804"
EMAIL = "asyabibi485@gmail.com"

# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Velvet Luxe Handbag",
        "category": "Fashion",
        "price": 3499,
        "icon": "👜",
        "description": "Elegant premium handbag.",
    },
    {
        "id": 2,
        "name": "Silk Evening Scarf",
        "category": "Fashion",
        "price": 1599,
        "icon": "🧣",
        "description": "Soft and elegant evening scarf.",
    },
    {
        "id": 3,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
        "description": "Elegant flowing luxury abaya.",
    },
    {
        "id": 4,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
        "description": "Premium stylish lawn suit.",
    },
    {
        "id": 5,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
        "description": "Beautiful dress for special occasions.",
    },
    {
        "id": 6,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
        "description": "Comfortable fashionable kurti.",
    },
    {
        "id": 7,
        "name": "Signature Pearl Necklace",
        "category": "Jewellery",
        "price": 2199,
        "icon": "📿",
        "description": "Classic elegant pearl necklace.",
    },
    {
        "id": 8,
        "name": "Crystal Bracelet",
        "category": "Jewellery",
        "price": 1299,
        "icon": "💎",
        "description": "Beautiful crystal bracelet.",
    },
    {
        "id": 9,
        "name": "Classic Gold Watch",
        "category": "Accessories",
        "price": 4999,
        "icon": "⌚",
        "description": "Classic premium-style watch.",
    },
    {
        "id": 10,
        "name": "Premium Sunglasses",
        "category": "Accessories",
        "price": 1899,
        "icon": "🕶️",
        "description": "Modern stylish sunglasses.",
    },
    {
        "id": 11,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
        "description": "Elegant romantic rose fragrance.",
    },
    {
        "id": 12,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
        "description": "Rich royal oud fragrance.",
    },
    {
        "id": 13,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
        "description": "Warm sweet vanilla fragrance.",
    },
    {
        "id": 14,
        "name": "Luxury Makeup Set",
        "category": "Beauty",
        "price": 2699,
        "icon": "💄",
        "description": "Beautiful makeup collection.",
    },
]

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
# FUNCTIONS
# ============================================================

def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def price(value):
    return f"Rs. {value:,.0f}"


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


# ============================================================
# DESIGN
# ============================================================

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap'
    );

    .stApp {
        background:
        radial-gradient(
            circle at 10% 5%,
            rgba(226, 215, 255, 0.55),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(255, 225, 244, 0.50),
            transparent 30%
        ),
        #fcfbff;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
    }

    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: 4px;
        color: #30263a;
    }

    .tagline {
        color: #8d8298;
        font-size: 0.72rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero {
        margin-top: 25px;
        margin-bottom: 35px;
        padding: 55px 40px;
        border-radius: 30px;
        background: linear-gradient(
            135deg,
            #ffffff,
            #f5efff
        );
        border: 1px solid #eee6f5;
        box-shadow: 0 20px 60px rgba(70, 50, 90, 0.10);
    }

    .hero-label {
        color: #9a8ca6;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        color: #2d2435;
        font-size: 4rem;
        line-height: 1.05;
        margin-top: 12px;
    }

    .hero-text {
        color: #766c7e;
        max-width: 650px;
        line-height: 1.8;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        color: #302638;
        font-size: 2rem;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .card {
        background: rgba(255,255,255,0.95);
        border: 1px solid #eee7f4;
        border-radius: 22px;
        padding: 18px;
        margin-bottom: 12px;
        box-shadow: 0 10px 30px rgba(70,50,90,0.07);
    }

    .product-image {
        height: 145px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            #f8f4ff,
            #fff6fb
        );
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4.3rem;
        margin-bottom: 15px;
    }

    .category {
        color: #a18fae;
        font-size: 0.70rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .product-name {
        font-family: 'Playfair Display', serif;
        color: #302638;
        font-size: 1.15rem;
        font-weight: 600;
        margin-top: 5px;
    }

    .description {
        color: #908797;
        font-size: 0.82rem;
        min-height: 42px;
        margin-top: 5px;
    }

    .product-price {
        color: #695476;
        font-weight: 700;
        margin-top: 8px;
        margin-bottom: 12px;
    }

    .info-box {
        background: white;
        border: 1px solid #eee7f4;
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 10px 35px rgba(70,50,90,0.07);
    }

    .total-box {
        background: linear-gradient(
            135deg,
            #f4edff,
            #fff5fb
        );
        border: 1px solid #e9def3;
        border-radius: 22px;
        padding: 25px;
        text-align: center;
        margin: 20px 0;
    }

    .total-title {
        color: #8d8198;
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .total-price {
        color: #302538;
        font-family: 'Playfair Display', serif;
        font-size: 2.3rem;
        font-weight: 700;
    }

    div.stButton > button {
        background: linear-gradient(
            135deg,
            #ffffff,
            #f3edff
        );
        color: #493b54;
        border: 1px solid #e3d9ec;
        border-radius: 13px;
        font-weight: 600;
        min-height: 42px;
    }

    div.stButton > button:hover {
        background: #ebe2ff;
        border-color: #cdbce0;
        color: #34283d;
    }

    .footer {
        text-align: center;
        color: #9a91a2;
        padding: 35px 10px;
        font-size: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HEADER
# ============================================================

left, right = st.columns([2, 5])

with left:
    st.markdown(
        """
        <div class="brand">LUXEMART</div>
        <div class="tagline">Luxury • Beauty • Fashion</div>
        """,
        unsafe_allow_html=True,
    )

with right:
    n1, n2, n3, n4, n5 = st.columns(5)

    with n1:
        if st.button("Shop", use_container_width=True):
            go_to("Shop")

    with n2:
        if st.button("♡ Favorites", use_container_width=True):
            go_to("Favorites")

    with n3:
        if st.button(
            f"Bag ({len(st.session_state.cart)})",
            use_container_width=True,
        ):
            go_to("Cart")

    with n4:
        if st.button("About", use_container_width=True):
            go_to("About")

    with n5:
        if st.button("Admin", use_container_width=True):
            go_to("Admin")

st.divider()

# ============================================================
# SHOP PAGE
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-label">New Collection</div>
            <div class="hero-title">
                Luxury made<br>
                beautifully simple.
            </div>
            <div class="hero-text">
                Discover fashion, clothes, jewellery, accessories,
                perfume and beauty essentials in one elegant store.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Explore Collection</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col = st.columns([2, 1])

    with search_col:
        search = st.text_input(
            "Search products",
            placeholder="Search products...",
        )

    with category_col:
        category = st.selectbox(
            "Category",
            [
                "All",
                "Clothes",
                "Fashion",
                "Jewellery",
                "Accessories",
                "Perfume",
                "Beauty",
            ],
        )

    filtered = PRODUCTS

    if category != "All":
        filtered = [
            p for p in filtered
            if p["category"] == category
        ]

    if search:
        search_text = search.lower()

        filtered = [
            p for p in filtered
            if search_text in p["name"].lower()
            or search_text in p["category"].lower()
        ]

    if not filtered:
        st.info("No products found.")

    for start in range(0, len(filtered), 4):

        row = filtered[start:start + 4]
        cols = st.columns(4)

        for col, product in zip(cols, row):

            with col:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="product-image">
                            {product["icon"]}
                        </div>

                        <div class="category">
                            {product["category"]}
                        </div>

                        <div class="product-name">
                            {product["name"]}
                        </div>

                        <div class="description">
                            {product["description"]}
                        </div>

                        <div class="product-price">
                            {price(product["price"])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                c1, c2 = st.columns(2)

                with c1:
                    if st.button(
                        "Add",
                        key=f"add_{product['id']}",
                        use_container_width=True,
                    ):
                        st.session_state.cart.append(product["id"])
                        st.toast("Added to bag!")

                with c2:
                    favorite = product["id"] in st.session_state.favorites

                    button_text = "♥" if favorite else "♡"

                    if st.button(
                        button_text,
                        key=f"favorite_{product['id']}",
                        use_container_width=True,
                    ):

                        if favorite:
                            st.session_state.favorites.remove(
                                product["id"]
                            )
                        else:
                            st.session_state.favorites.append(
                                product["id"]
                            )

                        st.rerun()

# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.markdown(
        '<div class="section-title">Your Favorites</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.favorites:

        st.info("You have no favorite products yet.")

        if st.button("Browse Products"):
            go_to("Shop")

    else:

        favorite_products = []

        for product_id in st.session_state.favorites:
            product = get_product(product_id)

            if product:
                favorite_products.append(product)

        cols = st.columns(4)

        for col, product in zip(cols, favorite_products):

            with col:

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="product-image">
                            {product["icon"]}
                        </div>

                        <div class="category">
                            {product["category"]}
                        </div>

                        <div class="product-name">
                            {product["name"]}
                        </div>

                        <div class="product-price">
                            {price(product["price"])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "Remove",
                    key=f"remove_{product['id']}",
                    use_container_width=True,
                ):
                    st.session_state.favorites.remove(
                        product["id"]
                    )
                    st.rerun()

# ============================================================
# CART PAGE
# ============================================================

elif st.session_state.page == "Cart":

    st.markdown(
        '<div class="section-title">Shopping Bag</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.cart:

        st.info("Your shopping bag is empty.")

        if st.button("Continue Shopping"):
            go_to("Shop")

    else:

        for index, product_id in enumerate(
            st.session_state.cart
        ):

            product = get_product(product_id)

            if not product:
                continue

            c1, c2, c3, c4 = st.columns(
                [0.7, 3, 1.2, 1]
            )

            with c1:
                st.write(product["icon"])

            with c2:
                st.write(f"**{product['name']}**")
                st.caption(product["category"])

            with c3:
                st.write(
                    f"**{price(product['price'])}**"
                )

            with c4:
                if st.button(
                    "Remove",
                    key=f"cart_remove_{index}",
                    use_container_width=True,
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

        total = cart_total()

        st.markdown(
            f"""
            <div class="total-box">
                <div class="total-title">
                    Order Total
                </div>
                <div class="total-price">
                    {price(total)}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Checkout")

        customer_name = st.text_input(
            "Customer Name"
        )

        customer_email = st.text_input(
            "Email"
        )

        customer_phone = st.text_input(
            "Phone",
            value=PHONE,
        )

        customer_address = st.text_area(
            "Delivery Address"
        )

        if st.button(
            "Place Order",
            type="primary",
            use_container_width=True,
        ):

            if not customer_name.strip():
                st.error("Please enter your name.")

            elif not customer_email.strip():
                st.error("Please enter your email.")

            elif not customer_phone.strip():
                st.error("Please enter your phone.")

            elif not customer_address.strip():
                st.error("Please enter your address.")

            elif not supabase_ok:
                st.error(
                    "Supabase connection failed. "
                    "Check Streamlit Secrets."
                )

            else:

                items = []

                for product_id in st.session_state.cart:

                    product = get_product(product_id)

                    if product:
                        items.append(
                            {
                                "id": product["id"],
                                "name": product["name"],
                                "category": product["category"],
                                "price": product["price"],
                            }
                        )

                order = {
                    "customer_name": customer_name.strip(),
                    "customer_email": customer_email.strip(),
                    "phone": customer_phone.strip(),
                    "address": customer_address.strip(),
                    "items": items,
                    "total": total,
                    "status": "Pending",
                }

                
