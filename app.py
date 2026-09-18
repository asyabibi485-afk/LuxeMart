import streamlit as st

st.set_page_config(
    page_title="LUXEMART",
    page_icon="✦",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []


# -----------------------------
# SIMPLE LUXURY STYLE
# -----------------------------

st.markdown(
    """
<style>
.stApp {
    background-color: #f7f5f0;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 3px;
}

.gold {
    color: #a47b45;
}

.hero-box {
    background-color: #ebe5da;
    padding: 45px;
    border-radius: 25px;
    margin: 20px 0;
}

.hero-title {
    font-size: 55px;
    font-weight: 800;
    line-height: 1.0;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #e5e0d7;
    margin-bottom: 15px;
}

.price {
    font-size: 22px;
    font-weight: 800;
}

.small-text {
    color: #777;
}
</style>
""",
    unsafe_allow_html=True
)


# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="main-title">LUXE<span class="gold">MART</span></div>',
    unsafe_allow_html=True
)

st.caption("Curated pieces for modern living")


# -----------------------------
# NAVIGATION
# -----------------------------

a, b, c, d = st.columns(4)

with a:
    if st.button("Shop", use_container_width=True):
        st.session_state.page = "Shop"
        st.rerun()

with b:
    if st.button("Collections", use_container_width=True):
        st.session_state.page = "Collections"
        st.rerun()

with c:
    if st.button(
        "Cart (" + str(len(st.session_state.cart)) + ")",
        use_container_width=True
    ):
        st.session_state.page = "Cart"
        st.rerun()

with d:
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown(
        """
<div class="hero-box">
    <div class="small-text">NEW SEASON · 2026</div>
    <div class="hero-title">
        Things you'll<br>
        <span class="gold">love to live with.</span>
    </div>
    <p>
        Discover carefully selected clothes and home
        essentials for everyday living.
    </p>
</div>
""",
        unsafe_allow_html=True
    )

    st.subheader("Explore")

    search = st.text_input(
        "Search",
        placeholder="Search products..."
    )

    category = st.selectbox(
        "Category",
        ["All", "Clothes", "Home"]
    )

    # -----------------------------------------------------
    # USE EXISTING BACKEND IF AVAILABLE
    # -----------------------------------------------------

    products = []

    if "get_products" in globals():

        try:
            products = get_products()
        except Exception as e:
            st.error("Could not load products.")
            st.code(str(e))

    if products is None:
        products = []

    # -----------------------------------------------------
    # FILTER
    # -----------------------------------------------------

    if category != "All":

        products = [
            p for p in products
            if str(p.get("category", "")).lower()
            == category.lower()
        ]

    if search.strip():

        word = search.lower().strip()

        products = [
            p for p in products
            if word in str(
                p.get("name", "")
            ).lower()
            or word in str(
                p.get("description", "")
            ).lower()
            or word in str(
                p.get("category", "")
            ).lower()
        ]

    st.subheader("Featured Pieces")

    if not products:

        st.info(
            "No products available yet."
        )

    else:

        columns = st.columns(3)

        for index, product in enumerate(products):

            with columns[index % 3]:

                st.markdown(
                    '<div class="card">',
                    unsafe_allow_html=True
                )

                image = str(
                    product.get("image_url", "")
                ).strip()

                if image:

                    try:
                        st.image(
                            image,
                            use_container_width=True
                        )
                    except Exception:
                        st.write("✦")

                else:

                    st.markdown(
                        "<div style='font-size:60px;text-align:center;'>✦</div>",
                        unsafe_allow_html=True
                    )

                name = str(
                    product.get(
                        "name",
                        "Product"
                    )
                )

                description = str(
                    product.get(
                        "description",
                        ""
                    )
                )

                price = product.get(
                    "price",
                    0
                )

                st.markdown(
                    "<h3>" + name + "</h3>",
                    unsafe_allow_html=True
                )

                st.write(description)

                st.markdown(
                    '<div class="price">' +
                    str(price) +
                    "</div>",
                    unsafe_allow_html=True
                )

                if st.button(
                    "Add to Cart +",
                    key="add_" + str(index),
                    use_container_width=True
                ):

                    if "add_cart" in globals():

                        try:
                            add_cart(product)
                        except Exception:
                            st.session_state.cart.append(
                                product
                            )

                    else:

                        st.session_state.cart.append(
                            product
                        )

                    st.success(
                        "Added to cart ✓"
                    )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )


# =========================================================
# COLLECTIONS
# =========================================================

elif st.session_state.page == "Collections":

    st.markdown(
        """
<div class="hero-box">
    <div class="small-text">LUXEMART COLLECTIONS</div>
    <div class="hero-title">
        Curated for<br>
        <span class="gold">your lifestyle.</span>
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    x, y, z = st.columns(3)

    with x:
        st.markdown(
            """
<div class="card">
<h2>Clothes</h2>
<p>Modern fashion for everyday style.</p>
</div>
""",
            unsafe_allow_html=True
        )

    with y:
        st.markdown(
            """
<div class="card">
<h2>Home</h2>
<p>Beautiful essentials for your space.</p>
</div>
""",
            unsafe_allow_html=True
        )

    with z:
        st.markdown(
            """
<div class="card">
<h2>Essentials</h2>
<p>Useful products for everyday living.</p>
</div>
""",
            unsafe_allow_html=True
        )


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.title("Your Cart")

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "Continue Shopping",
            use_container_width=True
        ):

            st.session_state.page = "Shop"
            st.rerun()

    else:

        total = 0

        for item in st.session_state.cart:

            name = str(
                item.get(
                    "name",
                    "Product"
                )
            )

            price = float(
                item.get(
                    "price",
                    0
                ) or 0
            )

            total += price

            st.markdown(
                '<div class="card">' +
                "<h
