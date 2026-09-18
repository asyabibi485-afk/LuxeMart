import streamlit as st
from supabase import create_client
from datetime import datetime, timezone

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🛍️",
    layout="wide"
)

# =========================================================
# SUPABASE
# =========================================================

try:
    supabase = create_client(
        st.secrets["supabase"]["url"],
        st.secrets["supabase"]["key"]
    )
except Exception as e:
    st.error("Supabase connection failed.")
    st.error(str(e))
    st.stop()


# =========================================================
# SESSION
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# =========================================================
# FUNCTIONS
# =========================================================

def money(value):
    try:
        return f"Rs {float(value):,.0f}"
    except Exception:
        return "Rs 0"


def get_products():
    try:
        result = (
            supabase
            .table("products")
            .select("*")
            .eq("active", True)
            .order("created_at", desc=True)
            .execute()
        )
        return result.data or []
    except Exception as e:
        st.error("Could not load products.")
        st.error(str(e))
        return []


def add_cart(product):
    st.session_state.cart.append(product)


def remove_cart(index):
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)


def get_cart_total():
    total = 0

    for item in st.session_state.cart:
        try:
            total += float(item.get("price", 0))
        except Exception:
            pass

    return total


# =========================================================
# LUXURY STYLE
# =========================================================

css = (
    "<style>"
    ".stApp{background:#080808;color:#f5f2eb;}"
    "h1,h2,h3{color:#f5f2eb!important;}"
    ".block-container{max-width:1250px;padding-top:1.5rem;}"
    ".brand{font-family:Georgia,serif;font-size:34px;"
    "font-weight:700;letter-spacing:3px;color:#f5f2eb;}"
    ".brand span{color:#d6b36a;}"
    ".tagline{color:#888;font-size:11px;letter-spacing:3px;"
    "text-transform:uppercase;}"
    ".hero{background:linear-gradient(120deg,#171717,#0d0d0d);"
    "border:1px solid #292929;border-radius:28px;"
    "padding:50px;margin:25px 0 30px;min-height:260px;}"
    ".hero-label{color:#d6b36a;font-size:12px;font-weight:700;"
    "letter-spacing:4px;text-transform:uppercase;}"
    ".hero-title{font-family:Georgia,serif;font-size:58px;"
    "line-height:1.05;color:#faf8f2;margin:15px 0;}"
    ".hero-text{max-width:600px;color:#999;font-size:16px;"
    "line-height:1.7;}"
    ".section-label{color:#d6b36a;font-size:11px;"
    "letter-spacing:3px;font-weight:700;}"
    ".section-title{font-family:Georgia,serif;color:#f5f2eb;"
    "font-size:34px;margin:5px 0 20px;}"
    ".card{background:#151515;border:1px solid #292929;"
    "border-radius:22px;padding:16px;margin-bottom:22px;}"
    ".product-name{font-family:Georgia,serif;color:#f5f2eb;"
    "font-size:22px;font-weight:600;margin-top:12px;}"
    ".product-description{color:#969696;line-height:1.5;"
    "min-height:48px;}"
    ".price{color:#d6b36a;font-size:22px;font-weight:700;"
    "margin:10px 0 15px;}"
    ".benefit{background:#111;border:1px solid #252525;"
    "border-radius:18px;padding:22px;text-align:center;"
    "min-height:110px;}"
    ".benefit-icon{font-size:25px;margin-bottom:8px;}"
    ".benefit-title{color:#f2eee6;font-weight:700;}"
    ".benefit-text{color:#858585;font-size:13px;margin-top:5px;}"
    ".promo{border:1px solid #3c3324;border-radius:22px;"
    "padding:30px;margin:35px 0;background:#14120e;}"
    ".promo-title{color:#d6b36a;font-family:Georgia,serif;"
    "font-size:28px;}"
    ".promo-text{color:#999;}"
    ".cart-box{background:#121212;border:1px solid #292929;"
    "border-radius:18px;padding:18px;margin-bottom:10px;}"
    ".cart-name{color:#f5f2eb;font-weight:700;}"
    ".cart-price{color:#d6b36a;font-weight:700;}"
    ".total-box{background:#17140f;border:1px solid #4c3e27;"
    "border-radius:18px;padding:25px;margin:20px 0;}"
    ".total-label{color:#999;font-size:13px;}"
    ".total-price{color:#d6b36a;font-family:Georgia,serif;"
    "font-size:34px;font-weight:700;}"
    ".footer{text-align:center;padding:40px 15px 20px;"
    "margin-top:55px;border-top:1px solid #252525;color:#777;"
    "line-height:1.8;}"
    ".footer-brand{font-family:Georgia,serif;font-size:24px;"
    "color:#d6b36a;}"
    ".stButton>button{width:100%;border-radius:12px;"
    "border:1px solid #383838;background:#151515;"
    "color:#f5f2eb;font-weight:600;min-height:43px;}"
    ".stButton>button:hover{border-color:#d6b36a;"
    "color:#d6b36a;background:#1b1812;}"
    ".stTextInput input{background:#121212!important;"
    "color:#f5f2eb!important;border-radius:12px!important;}"
    ".stTextArea textarea{background:#121212!important;"
    "color:#f5f2eb!important;border-radius:12px!important;}"
    "</style>"
)

st.markdown(css, unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    "<div class='brand'>LUXE<span>MART</span></div>"
    "<div class='tagline'>"
    "Curated luxury for everyday living"
    "</div>",
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# NAVIGATION
# =========================================================

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("🛍️ SHOP", key="nav_shop"):
        st.session_state.page = "Shop"
        st.rerun()

with c2:
    if st.button("✨ COLLECTIONS", key="nav_collections"):
        st.session_state.page = "Collections"
        st.rerun()

with c3:
    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        key="nav_cart"
    ):
        st.session_state.page = "Cart"
        st.rerun()

with c4:
    if st.button("📞 CONTACT", key="nav_contact"):
        st.session_state.page = "Contact"
        st.rerun()

with c5:
    if st.button("⚙️ ADMIN", key="nav_admin"):
        st.session_state.page = "Admin"
        st.rerun()

st.divider()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.markdown(
        "<div class='hero'>"
        "<div class='hero-label'>THE LUXE EDIT</div>"
        "<div class='hero-title'>"
        "Luxury finds<br>for your life."
        "</div>"
        "<div class='hero-text'>"
        "Discover elegant clothing and beautiful home products, "
        "carefully selected for a refined everyday experience."
        "</div>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='section-label'>EXPLORE</div>"
        "<div class='section-title'>Featured Collection</div>",
        unsafe_allow_html=True
    )

    search = st.text_input(
        "Search products",
        placeholder="Search your products..."
    )

    category = st.selectbox(
        "Category",
        ["All", "Clothes", "Home"]
    )

    products = get_products()

    if category != "All":
        products = [
            p for p in products
            if p.get("category") == category
        ]

    if search.strip():
        word = search.strip().lower()

        products = [
            p for p in products
            if word in str(
                p.get("name", "")
            ).lower()
            or word in str(
                p.get("description", "")
            ).lower()
        ]

    if not products:

        st.info("No products found.")

    else:

        cols = st.columns(3)

        for i, product in enumerate(products):

            with cols[i % 3]:

                st.markdown(
                    "<div class='card'>",
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
                        "<div style='height:220px;"
                        "display:flex;"
                        "align-items:center;"
                        "justify-content:center;"
                        "background:#0d0d0d;"
                        "border-radius:16px;"
                        "font-size:50px;'>"
                        "✦"
                        "</div>",
                        unsafe_allow_html=True
                    )

                st.markdown(
                    "<div class='product-name'>"
                    + str(product.get("name", "Product"))
                    + "</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    "<div class='product-description'>"
                    + str(product.get("description", ""))
                    + "</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    "<div class='price'>"
                    + money(product.get("price", 0))
                    + "</div>",
                    unsafe_allow_html=True
                )

                if st.button(
                    "ADD TO CART  +",
                    key=f"add_{i}"
                ):

                    add_cart(product)
                    st.success("Added to cart!")

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

    st.write("")

    b1, b2, b3 = st.columns(3)

    with b1:
        st.markdown(
            "<div class='benefit'>"
            "<div class='benefit-icon'>✦</div>"
            "<div class='benefit-title'>Curated Quality</div>"
            "<div class='benefit-text'>"
            "Products selected with care."
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

    with b2:
        st.markdown(
            "<div class='benefit'>"
            "<div class='benefit-icon'>◇</div>"
            "<div class='benefit-title'>Simple Shopping</div>"
            "<div class='benefit-text'>"
            "Easy browsing and checkout."
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

    with b3:
        st.markdown(
            "<div class='benefit'>"
            "<div class='benefit-icon'>♡</div>"
            "<div class='benefit-title'>Made For You</div>"
            "<div class='benefit-text'>"
            "Elegant products for everyday life."
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='promo'>"
        "<div class='promo-title'>"
        "Your style. Your space. Your Luxe."
        "</div>"
        "<div class='promo-text'>"
        "Explore the latest products and discover "
        "something made for your lifestyle."
        "</div>"
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# COLLECTIONS
# =========================================================

elif st.session_state.page == "Collections":

    st.markdown(
        "<div class='section-label'>CURATED</div>",
        unsafe_allow_html=True
    )

    st.header("✨ Collections")

    category = st.radio(
        "Choose collection",
        ["Clothes", "Home"],
        horizontal=True
    )

    products = get_products()

    products = [
        p for p in products
        if p.get("category") == category
    ]

    if not products:

        st.info(
            "No products in this collection."
        )

    else:

        cols = st.columns(3)

        for i, product in enumerate(products):

            with cols[i % 3]:

                st.markdown(
                    "<div class='card'>",
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

                st.markdown(
                    "<div class='product-name'>"
                    + str(product.get("name", "Product"))
                    + "</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    "<div class='product-description'>"
                    + str(product.get("description", ""))
                    + "</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    "<div class='price'>"
                    + money(product.get("price", 0))
                    + "</div>",
                    unsafe_allow_html=True
                )

                if st.button(
                    "ADD TO CART  +",
                    key=f"collection_{i}"
                ):

                    add_cart(product)
                    st.success("Added to cart!")

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.markdown(
        "<div class='section-label'>YOUR SELECTION</div>",
        unsafe_allow_html=True
    )

    st.header("🛒 Shopping Cart")

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button("← CONTINUE SHOPPING"):
            st.session_state.page = "Shop"
            st.rerun()

    else:

        for i, product in enumerate(
            st.session_state.cart
        ):

            c1, c2, c3 = st.columns([5, 2, 1])

            with c1:
                st.markdown(
                    "<div class='cart-box'>"
                    "<div class='cart-name'>"
                    + str(product.get("name", "Product"))
                    + "</div>"
                    "</div>",
                    unsafe_allow_html=True
                )

            with c2:
                st.markdown(
                    "<div class='cart-box'>"
                    "<div class='cart-price'>"
                    + money(product.get("price", 0))
                    + "</div>"
                    "</div>",
                    unsafe_allow_html=True
                )

            with c3:
                if st.button(
                    "✕",
                    key=f"remove_{i}"
                ):
                    remove_cart(i)
                    st.rerun()

        st.markdown(
            "<div class='total-box'>"
            "<div class='total-label'>ORDER TOTAL</div>"
            "<div class='total-price'>"
            + money(get_cart_total())
            + "</div>"
            "</div>",
            unsafe_allow_html=True
        )

        st.header("Checkout")

        name = st.text_input("Full Name")

        phone = st.text_input(
            "Phone / WhatsApp",
            placeholder="03220956920"
        )

        address = st.text_area(
            "Delivery Address"
        )

        notes = st.text_area(
            "Order Notes (optional)"
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Cash on Delivery",
                "Bank Transfer"
            ]
        )

        if st.button(
            "✨ PLACE ORDER",
            key="place_order"
        ):

            if not name.strip():

                st.error("Enter your name.")

            elif not phone.strip():

                st.error("Enter your phone number.")

            elif not address.strip():

                st.error("Enter your address.")

            else:

                try:

                    total = get_cart_total()

                    order = (
                        supabase
                        .table("orders")
                        .insert(
                            {
                                "customer_name":
                                    name.strip(),

                                "phone":
                                    phone.strip(),

                                "address":
                                    address.strip(),

                                "notes":
                                    notes.strip(),

                                "total":
                                    total,

                                "status":
                                    "pending",

                                "created_at":
                                    datetime.now(
                                        timezone.utc
                                    ).isoformat()
                            }
                        )
                        .execute()
                    )

                    if not order.data:

                        st.error(
                            "Order could not be created."
                        )
                        st.stop()

                    order_id = order.data[0]["id"]

                    for product in st.session_state.cart:

                        supabase.table(
                            "order_items"
                        ).insert(
                            {
                                "order_id":
                                    order_id,

                                "product_id":
                                    product.get("id"),

                                "product_name":
                                    product.get(
                                        "name",
                                        "Product"
                                    ),

                                "quantity":
                                    1,

                                "unit_price":
                                    float(
                                        product.get(
                                            "price",
                                            0
                                        )
                                    )
                            }
                        ).execute()

                    st.session_state.cart = []

                    st.success(
                        "🎉 Order placed successfully!"
                    )

                    st.write(
                        f"Order ID: `{order_id}`"
                    )

                    st.info(
                        f"Payment method selected: {payment}"
                    )

                    st.balloons()

                except Exception as e:

                    st.error("Order error:")
                    st.error(str(e))


# =========================================================
# CONTACT
# =========================================================

elif st.session_state.page == "Contact":

    st.markdown(
        "<div class='section-label'>GET IN TOUCH</div>",
        unsafe_allow_html=True
    )

    st.header("📞 Contact LuxeMart")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            "<div class='benefit'>"
            "<div class='benefit-icon'>☎</div>"
            "<div class='benefit-title'>"
            "Phone / WhatsApp"
            "</div>"
            "<div class='benefit-text'>"
            "03220956920"
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        st.link_button(
            "💬 WhatsApp",
            "https://wa.me/923220956920"
        )

    with c2:

        st.markdown(
            "<div class='benefit'>"
            "<div class='benefit-icon'>✉</div>"
            "<div class='benefit-title'>Email</div>"
            "<div class='benefit-text'>"
            "asyabibi485@gmail.com"
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        st.link_button(
            "✉️ Email Us",
            "mailto:asyabibi485@gmail.com"
        )


# =========================================================
# ADMIN
# =========================================================

elif st.session_state.page == "Admin":

    st.markdown(
        "<div class='section-label'>MANAGEMENT</div>",
        unsafe_allow_html=True
    )

    st.header("⚙️ Admin Dashboard")

    if not st.session_state.admin_logged_in:

        email = st.text_input("Admin Email")

        password = st.text_input(
            "Admin Password",
            type="password"
        )

        if st.button("🔐 LOGIN"):

            try:

                correct_email = (
                    st.secrets["admin"]["email"]
                )

                correct_password = (
                    st.secrets["admin"]["password"]
                )

                if (
                    email.strip() == correct_email
                    and password == correct_password
                ):

                    st.session_state.admin_logged_in = True

                    st.success(
                        "Login successful."
                    )

                    st.rerun()

                else:

                    st.error(
                        "Incorrect email or password."
                    )

            except Exception:

                st.error(
                    "Admin secrets are missing."
                )

    else:

        st.success("Admin logged in.")

        if st.button("🚪 LOGOUT"):

            st.session_state.admin_logged_in = False
            st.rerun()

        st.divider()

        st.header("📦 Products")

        try:

            products = (
                supabase
                .table("products")
                .select("*")
                .order(
                    "created_at",
                    desc=True
                )
                .execute()
            ).data or []

            if products:

                for product in products:

                    st.markdown(
                        "<div class='card'>",
                        unsafe_allow_html=True
                    )

                    st.write(
                        f"**{product.get('name', 'Product')}**"
                    )

                    st.write(
                        f"Category: "
                        f"{product.get('category', '')}"
                    )

                    st.write(
                        f"Price: "
                        f"{money(product.get('price', 0))}"
                    )

                    st.write(
                        f"Active: "
                        f"{product.get('active', True)}"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

            else:

                st.info("No products.")

        except Exception as e:

            st.error(str(e))

        st.divider()

        st.header("🧾 Customer Orders")

        try:

            orders = (
                supabase
                .table("orders")
                .select("*")
                .order(
                    "created_at",
                    desc=True
                )
                .execute()
            ).data or []

            if not orders:

                st.info("No orders yet.")

            else:

                for order in orders:

                    with st.expander(
                        f"Order: {order.get('id', '')}"
                    ):

                        st.write(
                            f"Customer: "
                            f"{order.get('customer_name', '')}"
                        )

                        st.write(
                            f"Phone: "
                            f"{order.get('phone', '')}"
                        )

                        st.write(
                            f"Address: "
                            f"{order.get('address', '')}"
                        )

                        st.write(
                            f"Total: "
                            f"{money(order.get('total', 0))}"
                        )

                        st.write(
                            f"Status: "
                            f"{order.get('status', 'pending')}"
                        )

                        st.write(
                            f"Created: "
                            f"{order.get('created_at', '')}"
                        )

        except Exception as e:

            st.error(str(e))


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    "<div class='footer'>"
    "<div class='footer-brand'>LUXEMART</div>"
    "Luxury shopping made simple.<br><br>"
    "03220956920 &nbsp; · &nbsp; "
    "asyabibi485@gmail.com<br>"
    "© 2026 LuxeMart. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)
