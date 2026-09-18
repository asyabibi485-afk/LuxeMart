import streamlit as st

# =========================================================
# LUXEMART — CRAFTWORK-INSPIRED LUXURY STORE
# =========================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []


# =========================================================
# LUXURY / CRAFTWORK STYLE
# =========================================================

st.markdown(
    """
    <style>

    /* GLOBAL */
    .stApp {
        background: #f8f7f4;
        color: #151515;
    }

    .block-container {
        max-width: 1280px;
        padding: 1.2rem 28px 50px 28px;
    }

    h1, h2, h3, h4 {
        color: #151515 !important;
    }

    p, label {
        color: #666 !important;
    }

    /* TOP BAR */
    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #ffffff;
        border: 1px solid #e8e6e0;
        border-radius: 18px;
        padding: 14px 20px;
        margin-bottom: 18px;
        box-shadow: 0 4px 20px rgba(0,0,0,.025);
    }

    .brand {
        font-size: 23px;
        font-weight: 850;
        letter-spacing: 2px;
        color: #111;
    }

    .brand span {
        color: #a47b45;
    }

    .nav-note {
        font-size: 13px;
        color: #777;
    }

    /* HERO */
    .hero {
        position: relative;
        overflow: hidden;
        min-height: 390px;
        border-radius: 28px;
        background:
            radial-gradient(
                circle at 90% 15%,
                rgba(196,165,116,.20),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #e9e3d8 0%,
                #f7f5ef 55%,
                #eee9df 100%
            );
        border: 1px solid #e2ded5;
        padding: 60px 55px;
        margin-bottom: 32px;
    }

    .hero-small {
        display: inline-block;
        padding: 8px 13px;
        border-radius: 100px;
        background: #171717;
        color: #e4c58e;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
    }

    .hero-title {
        max-width: 700px;
        font-size: clamp(42px, 6vw, 76px);
        line-height: .95;
        letter-spacing: -4px;
        font-weight: 850;
        color: #111;
    }

    .hero-title span {
        color: #a47b45;
    }

    .hero-description {
        max-width: 570px;
        font-size: 17px;
        line-height: 1.7;
        color: #666;
        margin-top: 22px;
    }

    .hero-circle {
        position: absolute;
        right: -90px;
        bottom: -130px;
        width: 390px;
        height: 390px;
        border-radius: 50%;
        background: rgba(255,255,255,.42);
        border: 1px solid rgba(164,123,69,.15);
    }

    /* SECTION */
    .section-head {
        display: flex;
        justify-content: space-between;
        align-items: end;
        margin: 35px 0 18px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 850;
        letter-spacing: -1px;
        color: #151515;
    }

    .section-caption {
        color: #888;
        font-size: 13px;
    }

    /* SEARCH */
    div[data-testid="stTextInput"] input {
        border-radius: 14px !important;
        border: 1px solid #dedbd4 !important;
        background: white !important;
        color: #111 !important;
        padding: 13px 16px !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #a47b45 !important;
        box-shadow: 0 0 0 1px #a47b45 !important;
    }

    /* SELECT */
    div[data-testid="stSelectbox"] > div {
        border-radius: 14px !important;
    }

    /* PRODUCT CARD */
    .product-card {
        background: #ffffff;
        border: 1px solid #e8e5df;
        border-radius: 23px;
        padding: 12px;
        margin-bottom: 22px;
        transition: all .2s ease;
        box-shadow: 0 5px 25px rgba(0,0,0,.025);
    }

    .product-card:hover {
        transform: translateY(-3px);
        border-color: #c8a675;
        box-shadow: 0 12px 35px rgba(0,0,0,.07);
    }

    .product-name {
        font-size: 18px;
        font-weight: 800;
        color: #151515;
        margin-top: 14px;
    }

    .product-category {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #a47b45;
        font-weight: 800;
        margin-top: 5px;
    }

    .product-description {
        color: #777;
        font-size: 13px;
        line-height: 1.5;
        margin-top: 7px;
        min-height: 39px;
    }

    .product-price {
        font-size: 20px;
        font-weight: 850;
        color: #171717;
        margin: 12px 0 10px;
    }

    /* BUTTONS */
    .stButton > button {
        border-radius: 13px !important;
        border: 1px solid #dedbd4 !important;
        background: #ffffff !important;
        color: #151515 !important;
        font-weight: 750 !important;
        min-height: 44px !important;
        transition: all .18s ease !important;
    }

    .stButton > button:hover {
        background: #171717 !important;
        color: #ffffff !important;
        border-color: #171717 !important;
    }

    /* BENEFITS */
    .benefit {
        background: #ffffff;
        border: 1px solid #e7e3dc;
        border-radius: 20px;
        padding: 25px 20px;
        min-height: 145px;
        box-shadow: 0 4px 20px rgba(0,0,0,.025);
    }

    .benefit-icon {
        font-size: 25px;
        margin-bottom: 10px;
    }

    .benefit-title {
        font-size: 16px;
        font-weight: 800;
        color: #171717;
    }

    .benefit-text {
        font-size: 13px;
        line-height: 1.5;
        color: #777;
        margin-top: 7px;
    }

    /* PROMO */
    .promo {
        background: #171717;
        border-radius: 25px;
        padding: 30px;
        margin-top: 35px;
        color: white;
        text-align: center;
    }

    .promo-title {
        color: white;
        font-size: 25px;
        font-weight: 850;
    }

    .promo-text {
        color: #bdbdbd;
        font-size: 14px;
        margin-top: 7px;
    }

    /* FOOTER */
    .footer {
        border-top: 1px solid #ddd9d0;
        margin-top: 55px;
        padding: 30px 5px;
        display: flex;
        justify-content: space-between;
        color: #888;
        font-size: 13px;
    }

    .footer strong {
        color: #171717;
        letter-spacing: 1.5px;
    }

    .gold {
        color: #a47b45;
    }

    /* MOBILE */
    @media (max-width: 700px) {

        .block-container {
            padding-left: 12px;
            padding-right: 12px;
        }

        .topbar {
            padding: 13px 15px;
        }

        .brand {
            font-size: 19px;
        }

        .nav-note {
            display: none;
        }

        .hero {
            min-height: 340px;
            padding: 38px 25px;
            border-radius: 22px;
        }

        .hero-title {
            font-size: 43px;
            letter-spacing: -2.5px;
        }

        .hero-description {
            font-size: 15px;
        }

        .hero-circle {
            width: 230px;
            height: 230px;
            right: -100px;
            bottom: -80px;
        }

        .section-title {
            font-size: 25px;
        }

        .product-card {
            border-radius: 18px;
        }

        .footer {
            display: block;
            text-align: center;
            line-height: 2;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TOP BAR
# =========================================================

st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            LUXE<span>MART</span>
        </div>

        <div class="nav-note">
            Curated pieces for modern living
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

n1, n2, n3, n4 = st.columns(4)

with n1:
    if st.button("Shop", use_container_width=True):
        st.session_state.page = "Shop"
        st.rerun()

with n2:
    if st.button("Collections", use_container_width=True):
        st.session_state.page = "Collections"
        st.rerun()

with n3:
    if st.button(
        f"Cart  •  {len(st.session_state.cart)}",
        use_container_width=True
    ):
        st.session_state.page = "Cart"
        st.rerun()

with n4:
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-circle"></div>

            <div class="hero-small">
                NEW SEASON · 2026
            </div>

            <div class="hero-title">
                Things you'll<br>
                <span>love to live with.</span>
            </div>

            <div class="hero-description">
                Discover carefully selected clothes and home
                essentials designed to bring effortless style
                into everyday life.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # SEARCH
    st.markdown(
        """
        <div class="section-head">
            <div>
                <div class="section-title">
                    Explore
                </div>

                <div class="section-caption">
                    Find something made for you
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search products",
        placeholder="Search clothes, home products..."
    )

    c1, c2 = st.columns(2)

    with c1:
        category = st.selectbox(
            "Category",
            ["All", "Clothes", "Home"]
        )

    with c2:
        sort_by = st.selectbox(
            "Sort by",
            [
                "Newest",
                "Price: Low to High",
                "Price: High to Low"
            ]
        )

    # =====================================================
    # PRODUCTS
    # =====================================================

    products = get_products()

    # CATEGORY FILTER
    if category != "All":

        products = [
            p for p in products
            if str(
                p.get("category", "")
            ).lower() == category.lower()
        ]

    # SEARCH FILTER
    if search.strip():

        keyword = search.strip().lower()

        products = [
            p for p in products
            if keyword in str(
                p.get("name", "")
            ).lower()
            or keyword in str(
                p.get("description", "")
            ).lower()
            or keyword in str(
                p.get("category", "")
            ).lower()
        ]

    # SORT
    if sort_by == "Price: Low to High":

        products.sort(
            key=lambda x: float(
                x.get("price", 0) or 0
            )
        )

    elif sort_by == "Price: High to Low":

        products.sort(
            key=lambda x: float(
                x.get("price", 0) or 0
            ),
            reverse=True
        )

    # =====================================================
    # PRODUCT TITLE
    # =====================================================

    st.markdown(
        f"""
        <div class="section-head">

            <div>
                <div class="section-title">
                    Featured pieces
                </div>

                <div class="section-caption">
                    {len(products)} products available
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # PRODUCTS GRID
    # =====================================================

    if not products:

        st.info(
            "No products found. Try another search."
        )

    else:

        cols = st.columns(3)

        for i, product in enumerate(products):

            with cols[i % 3]:

                st.markdown(
                    '<div class="product-card">',
                    unsafe_allow_html=True
                )

                image = str(
                    product.get("image_url", "")
                ).strip()

                if image:

                    st.image(
                        image,
                        use_container_width=True
                    )

                else:

                    st.markdown(
                        """
                        <div style="
                            height:230px;
                            border-radius:17px;
                            background:#f1efe9;
                            display:flex;
                            align-items:center;
                            justify-content:center;
                            font-size:65px;
                        ">
                            ✦
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"""
                    <div class="product-category">
                        {product.get("category", "Collection")}
                    </div>

                    <div class="product-name">
                        {product.get("name", "Product")}
                    </div>

                    <div class="product-description">
                        {product.get("description", "")}
                    </div>

                    <div class="product-price">
                        {money(product.get("price", 0))}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    "Add to cart  +",
                    key=f"craft_add_{i}",
                    use_container_width=True
                ):

                    add_cart(product)

                    st.success(
                        "Added to your cart ✓"
                    )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )


    # =====================================================
    # BENEFITS
    # =====================================================

    st.markdown(
        """
        <div class="section-head">

            <div>
                <div class="section-title">
                    The LUXEMART way
                </div>

                <div class="section-caption">
                    Simple shopping, carefully selected
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    b1, b2, b3 = st.columns(3)

    with b1:

        st.markdown(
            """
            <div class="benefit">

                <div class="benefit-icon">
                    ✦
                </div>

                <div class="benefit-title">
                    Curated selection
                </div>

                <div class="benefit-text">
                    Carefully selected clothes and home
                    essentials for modern living.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with b2:

        st.markdown(
            """
            <div class="benefit">

                <div class="benefit-icon">
                    ⌁
                </div>

                <div class="benefit-title">
                    Easy shopping
                </div>

                <div class="benefit-text">
                    Search, explore and add your favourite
                    products to your cart in seconds.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with b3:

        st.markdown(
            """
            <div class="benefit">

                <div class="benefit-icon">
                    ♡
                </div>

                <div class="benefit-title">
                    Personal support
                </div>

                <div class="benefit-text">
                    We're here whenever you need help
                    with your order.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # PROMO
    # =====================================================

    st.markdown(
        """
        <div class="promo">

            <div class="promo-title">
                Made for your everyday.
            </div>

            <div class="promo-text">
                Clothes · Home · Essentials · Style
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.markdown(
        """
        <div class="section-head">

            <div>
                <div class="section-title">
                    Your cart
                </div>

                <div class="section-caption">
                    Review your selected pieces
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty. Start exploring our collection."
        )

        if st.button(
            "Continue shopping",
            use_container_width=True
        ):

            st.session_state.page = "Shop"
            st.rerun()

    else:

        # =================================================
        # EXISTING CART / CHECKOUT
        # =================================================
        #
        # Keep your existing working cart and Supabase
        # checkout code here.
        #
        # Do NOT replace your existing checkout function
        # if it is already successfully creating orders.
        #

        for i, item in enumerate(
            st.session_state.cart
        ):

            st.markdown(
                f"""
                <div class="benefit">

                    <div class="benefit-title">
                        {item.get("name", "Product")}
                    </div>

                    <div class="benefit-text">
                        {money(item.get("price", 0))}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <div class="promo">

                <div class="promo-title">
                    Ready to checkout?
                </div>

                <div class="promo-text">
                    Complete your order using your
                    existing checkout system.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# COLLECTIONS
# =========================================================

elif st.session_state.page == "Collections":

    st.markdown(
        """
        <div class="hero">

    
