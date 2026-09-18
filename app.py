import streamlit as st
from supabase import create_client, Client

# ============================================================
# LUXEMART — LUXURY TRENDY SHOP
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

    supabase: Client = create_client(
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

if "admin_user" not in st.session_state:
    st.session_state.admin_user = None


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
        "description": "Elegant premium handbag for a sophisticated look.",
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "icon": "🧣",
        "description": "Soft and stylish silk scarf for everyday elegance.",
    },
    {
        "id": 3,
        "name": "Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "icon": "📿",
        "description": "Classic pearl necklace with a graceful finish.",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "icon": "📿",
        "description": "Delicate bracelet designed for timeless style.",
    },
    {
        "id": 5,
        "name": "Gold Watch",
        "category": "Accessories",
        "price": 7999,
        "icon": "⌚",
        "description": "Luxury-inspired watch with a premium appearance.",
    },
    {
        "id": 6,
        "name": "Classic Sunglasses",
        "category": "Accessories",
        "price": 2999,
        "icon": "🕶️",
        "description": "Modern sunglasses with a stylish statement look.",
    },
    {
        "id": 7,
        "name": "Premium Makeup Set",
        "category": "Beauty",
        "price": 4499,
        "icon": "💄",
        "description": "Beautiful makeup essentials for your daily style.",
    },
    {
        "id": 8,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "icon": "👗",
        "description": "Elegant flowing luxury abaya.",
    },
    {
        "id": 9,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "icon": "👚",
        "description": "Premium lawn suit with a beautiful modern design.",
    },
    {
        "id": 10,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "icon": "👗",
        "description": "A sophisticated evening dress for special occasions.",
    },
    {
        "id": 11,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "icon": "👚",
        "description": "Comfortable and stylish casual kurti.",
    },
    {
        "id": 12,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "icon": "🌹",
        "description": "A romantic rose fragrance with an elegant finish.",
    },
    {
        "id": 13,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "icon": "✨",
        "description": "Rich oud-inspired fragrance with a luxurious character.",
    },
    {
        "id": 14,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "icon": "🌸",
        "description": "Sweet vanilla fragrance with a soft dreamy aroma.",
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def money(value):
    return f"Rs. {value:,}"


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
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap'
    );

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                rgba(225, 215, 255, 0.55),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #ffffff 0%,
                #faf8ff 45%,
                #f4f0ff 100%
            );
        color: #27232e;
        font-family: 'Poppins', sans-serif;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    h1,
    h2,
    h3 {
        font-family: 'Playfair Display', serif !important;
        color: #30283b !important;
    }

    .luxury-logo {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        font-weight: 700;
        letter-spacing: 3px;
        color: #30283b;
    }

    .luxury-subtitle {
        color: #8a7d98;
        font-size: 13px;
        letter-spacing: 2px;
    }

    .hero {
        padding: 45px 35px;
        border-radius: 28px;
        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.95),
                rgba(242,237,255,0.95)
            );
        border: 1px solid #e8def5;
        box-shadow: 0 20px 55px rgba(70, 52, 90, 0.10);
        margin: 25px 0;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 52px;
        line-height: 1.05;
        color: #30283b;
        margin-bottom: 12px;
    }

    .hero-text {
        color: #766b80;
        font-size: 16px;
        max-width: 650px;
        line-height: 1.8;
    }

    .product-card {
        padding: 12px;
        border-radius: 22px;
        background: rgba(255,255,255,0.80);
        border: 1px solid #ebe4f2;
        box-shadow: 0 12px 30px rgba(70,52,90,0.07);
        text-align: center;
        min-height: 155px;
        margin-bottom: 8px;
    }

    .product-image {
        height: 130px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 18px;
        background: linear-gradient(
            145deg,
            #faf8ff,
            #eee8fb
        );
        font-size: 65px;
    }

    .section-label {
        color: #9b8ca8;
        font-size: 12px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .footer-box {
        margin-top: 45px;
        padding: 28px;
        border-radius: 24px;
        background: #30283b;
        color: white;
        text-align: center;
    }

    .footer-title {
        font-family: 'Playfair Display', serif;
        font-size: 28px;
    }

    div.stButton > button {
        border-radius: 14px !important;
        border: 1px solid #ddd2ed !important;
        background: #f7f3ff !important;
        color: #4a3c58 !important;
        font-weight: 600 !important;
        min-height: 44px !important;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: #eee7fb !important;
        border-color: #cdbde4 !important;
        color: #30283b !important;
        transform: translateY(-1px);
    }

    .stTextInput input {
        border-radius: 14px !important;
        border: 1px solid #ded4e9 !important;
        background: white !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        border-radius: 14px !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

header_left, header_right = st.columns([2, 3])

with header_left:
    st.markdown(
        """
        <div class="luxury-logo">LUXEMART</div>
        <div class="luxury-subtitle">
            LUXURY • STYLE • ELEGANCE
        </div>
        """,
        unsafe_allow_html=True,
    )

with header_right:
    nav1, nav2, nav3, nav4, nav5 = st.columns(5)

    with nav1:
        if st.button("Shop", use_container_width=True):
            go_to("Shop")

    with nav2:
        if st.button("♡ Favorites", use_container_width=True):
            go_to("Favorites")

    with nav3:
        if st.button(
            f"🛍 Cart ({len(st.session_state.cart)})",
            use_container_width=True,
        ):
            go_to("Cart")

    with nav4:
        if st.button("About", use_container_width=True):
            go_to("About")

    with nav5:
        if st.button("Admin", use_container_width=True):
            go_to("Admin")


st.divider()


# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">

            <div class="section-label">
                PREMIUM COLLECTION
            </div>

            <div class="hero-title">
                Discover Your<br>
                Signature Style.
            </div>

            <div class="hero-text">
                Explore our carefully selected collection of fashion,
                jewellery, accessories, beauty products, clothes and
                luxury fragrances.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search products",
        placeholder="Search handbag, abaya, perfume, jewellery...",
    )

    categories = [
        "All",
        "Clothes",
        "Fashion",
        "Jewellery",
        "Accessories",
        "Perfume",
        "Beauty",
    ]

    selected_category = st.selectbox(
        "Category",
        categories,
    )

    filtered_products = PRODUCTS

    if selected_category != "All":
        filtered_products = [
            p
            for p in filtered_products
            if p["category"] == selected_category
        ]

    if search.strip():
        search_text = search.lower()

        filtered_products = [
            p
            for p in filtered_products
            if search_text in p["name"].lower()
            or search_text in p["category"].lower()
            or search_text in p["description"].lower()
        ]

    st.write("")

    if not filtered_products:
        st.info("No products found.")
    else:

        for start in range(0, len(filtered_products), 3):

            row = filtered_products[start:start + 3]

            columns = st.columns(3)

            for index, product in enumerate(row):

                with columns[index]:

                    # IMAGE ONLY IN HTML
                    # Product text is native Streamlit,
                    # preventing raw HTML from appearing.

                    st.markdown(
                        f"""
                        <div class="product-card">
                            <div class="product-image">
                                {product["icon"]}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f"<div class='section-label'>{product['category']}</div>",
                        unsafe_allow_html=True,
                    )

                    st.subheader(product["name"])

                    st.caption(product["description"])

                    st.markdown(
                        f"### {money(product['price'])}"
                    )

                    c1, c2 = st.columns(2)

                    with c1:

                        favorite_text = (
                            "♥ Saved"
                            if product["id"]
                            in st.session_state.favorites
                            else "♡ Favorite"
                        )

                        if st.button(
                            favorite_text,
                            key=f"favorite_{product['id']}",
                            use_container_width=True,
                        ):

                            if product["id"] in st.session_state.favorites:

                                st.session_state.favorites.remove(
                                    product["id"]
                                )

                            else:

                                st.session_state.favorites.append(
                                    product["id"]
                                )

                            st.rerun()

                    with c2:

                        if st.button(
                            "🛍 Add",
                            key=f"add_{product['id']}",
                            use_container_width=True,
                        ):

                            st.session_state.cart.append(
                                product["id"]
                            )

                            st.toast(
                                f"{product['name']} added to cart!"
                            )


# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.title("♡ Your Favorites")

    favorite_products = [
        get_product(product_id)
        for product_id in st.session_state.favorites
    ]

    favorite_products = [
        p for p in favorite_products if p
    ]

    if not favorite_products:

        st.info(
            "Your favorites are empty. Add products you love from the shop."
        )

        if st.button("← Continue Shopping"):
            go_to("Shop")

    else:

        for product in favorite_products:

            col1, col2, col3 = st.columns([1, 3, 1])

            with col1:
                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="product-image">
                            {product["icon"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:
                st.subheader(product["name"])
                st.caption(product["description"])
                st.write(money(product["price"]))

            with col3:

                if st.button(
                    "Remove",
                    key=f"remove_fav_{product['id']}",
                ):

                    st.session_state.favorites.remove(
                        product["id"]
                    )

                    st.rerun()

                if st.button(
                    "Add Cart",
                    key=f"favorite_cart_{product['id']}",
                ):

                    st.session_state.cart.append(
                        product["id"]
                    )

                    st.toast("Added to cart!")


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.title("🛍 Shopping Cart")

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button("← Continue Shopping"):
            go_to("Shop")

    else:

        for index, product_id in enumerate(
            st.session_state.cart
        ):

            product = get_product(product_id)

            if not product:
                continue

            col1, col2, col3 = st.columns(
                [1, 4, 1]
            )

            with col1:

                st.markdown(
                    f"""
                    <div class="product-card">
                        <div class="product-image">
                            {product["icon"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:

                st.subheader(product["name"])
                st.caption(product["category"])
                st.write(money(product["price"]))

            with col3:

                if st.button(
                    "Remove",
                    key=f"remove_cart_{index}",
                ):

                    st.session_state.cart.pop(index)

                    st.rerun()

        st.divider()

        st.subheader(
            f"Total: {money(cart_total())}"
        )

        st.write("")

        st.markdown("### Checkout")

        customer_name = st.text_input(
            "Customer Name",
            placeholder="Enter your name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter your complete delivery address",
        )

        checkout_col1, checkout_col2 = st.columns(2)

        with checkout_col1:

            if st.button(
                "← Continue Shopping",
                use_container_width=True,
            ):
                go_to("Shop")

        with checkout_col2:

            if st.button(
                "Place Order",
                use_container_width=True,
            ):

                if not customer_name.strip():
                    st.warning("Please enter your name.")

                elif not customer_phone.strip():
                    st.warning("Please enter your phone number.")

                elif not customer_address.strip():
                    st.warning("Please enter your delivery address.")

                else:

                    try:

                        order_data = {
                            "customer_name": customer_name.strip(),
                            "customer_phone": customer_phone.strip(),
                            "customer_address": customer_address.strip(),
                            "total_amount": cart_total(),
                        }

                        result = supabase.table(
                            "orders"
                        ).insert(
                            order_data
                        ).execute()

                        order_id = None

                        if result.data:
                            order_id = result.data[0].get("id")

                        if order_id:

                            for product_id in st.session_state.cart:

                                product = get_product(
                                    product_id
                                )

                                if product:

                                    item_data = {
                                        "order_id": order_id,
                                        "product_name": product["name"],
                                        "price": product["price"],
                                        "quantity": 1,
                                    }

                                    supabase.table(
                                        "order_items"
                                    ).insert(
                                        item_data
                                    ).execute()

                        st.session_state.cart = []

                        st.success(
                            "🎉 Your order has been placed successfully!"
                        )

                        st.balloons()

                    except Exception as e:

                        st.error(
                            "Order could not be placed."
                        )

                        st.code(str(e))


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.title("About LUXEMART")

    st.markdown(
        """
        ## ✦ Luxury Made Simple

        Welcome to **LUXEMART**, your destination for elegant fashion,
        beautiful accessories, jewellery, beauty products, clothes and
        premium fragrances.

        Our collection is designed around modern style, elegance and
        everyday luxury.

        ### Our Collections

        👗 Clothes  
        👜 Fashion  
        💎 Jewellery  
        ✨ Accessories  
        🌸 Perfume  
        💄 Beauty

        ### Contact

        📞 **03169707804**

        ✉️ **asyabibi485@gmail.com**
        """
    )


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.title("Admin Panel")

    if st.session_state.admin_user is None:

        st.info(
            "Sign in using your existing Supabase account."
        )

        admin_email = st.text_input(
            "Admin Email",
            value=ADMIN_EMAIL,
        )

        admin_password = st.text_input(
            "Password",
            type="password",
        )

        if st.button(
            "Sign In",
            use_container_width=True,
        ):

            if not admin_email.strip():
                st.warning("Enter your email.")

            elif not admin_password:
                st.warning("Enter your password.")

            elif admin_email.strip().lower() != ADMIN_EMAIL.lower():
                st.error(
                    "This account is not authorized as admin."
                )

            else:

                try:

                    auth_response = (
                        supabase.auth.sign_in_with_password(
                            {
                                "email": admin_email.strip(),
                                "password": admin_password,
                            }
                        )
                    )

                    st.session_state.admin_user = (
                        auth_response.user
                    )

                    st.success(
                        "Admin login successful."
                    )

                    st.rerun()

                except Exception as e:

                    st.error(
                        "Admin login failed."
                    )

                    st.code(str(e))

    else:

        st.success(
            f"Logged in as {st.session_state.admin_user.email}"
        )

        st.divider()

        st.subheader("LUXEMART Admin")

        st.write(
            "Admin authentication is connected to Supabase."
        )

        if st.button(
            "Sign Out",
            use_container_width=True,
        ):

            try:
                supabase.auth.sign_out()
            except Exception:
                pass

            st.session_state.admin_user = None

            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer-box">

        <div class="footer-title">
            LUXEMART
        </div>

        <p>
            Luxury • Style • Elegance
        </p>

        <p>
            📞 03169707804
            &nbsp;&nbsp; | &nbsp;&nbsp;
            ✉️ asyabibi485@gmail.com
        </p>

        <p>
            © 2026 LUXEMART. All rights reserved.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)








