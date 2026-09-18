import streamlit as st
from supabase import create_client
from datetime import datetime, timezone

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# SUPABASE
# -----------------------------

try:
    supabase = create_client(
        st.secrets["supabase"]["url"],
        st.secrets["supabase"]["key"]
    )
except Exception as e:
    st.error("Supabase connection failed.")
    st.error(str(e))
    st.stop()


# -----------------------------
# SESSION
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# -----------------------------
# FUNCTIONS
# -----------------------------

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


# -----------------------------
# STYLE
# -----------------------------

st.markdown(
    "<style>"
    ".stApp{background:#0b0b0b;color:white;}"
    "h1,h2,h3{color:white!important;}"
    ".card{background:#171717;border:1px solid #333;"
    "border-radius:18px;padding:20px;margin-bottom:20px;}"
    ".price{color:#d6b36a;font-size:24px;font-weight:700;}"
    ".gold{color:#d6b36a;}"
    ".footer{text-align:center;padding:30px;color:#888;"
    "border-top:1px solid #333;margin-top:40px;}"
    "</style>",
    unsafe_allow_html=True
)


# -----------------------------
# HEADER
# -----------------------------

st.title("LuxeMart")

st.caption("LUXURY • CLOTHES • HOME")


# -----------------------------
# NAVIGATION
# -----------------------------

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("🛍️ Shop"):
        st.session_state.page = "Shop"
        st.rerun()

with c2:
    if st.button("✨ Collections"):
        st.session_state.page = "Collections"
        st.rerun()

with c3:
    if st.button(
        f"🛒 Cart ({len(st.session_state.cart)})"
    ):
        st.session_state.page = "Cart"
        st.rerun()

with c4:
    if st.button("📞 Contact"):
        st.session_state.page = "Contact"
        st.rerun()

with c5:
    if st.button("⚙️ Admin"):
        st.session_state.page = "Admin"
        st.rerun()


st.divider()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.header("Luxury finds for your life.")

    st.write(
        "Discover elegant clothing and beautiful home products."
    )

    search = st.text_input(
        "🔎 Search products",
        placeholder="Search..."
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
            if word in str(p.get("name", "")).lower()
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
                    st.write("🛍️")

                st.subheader(
                    product.get(
                        "name",
                        "Product"
                    )
                )

                st.write(
                    product.get(
                        "description",
                        ""
                    )
                )

                st.markdown(
                    f"<div class='price'>"
                    f"{money(product.get('price', 0))}"
                    f"</div>",
                    unsafe_allow_html=True
                )

                if st.button(
                    "Add to Cart",
                    key=f"add_{i}"
                ):
                    add_cart(product)
                    st.success("Added to cart!")

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )


# =========================================================
# COLLECTIONS
# =========================================================

elif st.session_state.page == "Collections":

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
        st.info("No products in this collection.")

    for i, product in enumerate(products):

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.subheader(
            product.get("name", "Product")
        )

        st.write(
            product.get("description", "")
        )

        st.markdown(
            f"<div class='price'>"
            f"{money(product.get('price', 0))}"
            f"</div>",
            unsafe_allow_html=True
        )

        if st.button(
            "Add to Cart",
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

    st.header("🛒 Your Cart")

    if not st.session_state.cart:

        st.info("Your cart is empty.")

    else:

        for i, product in enumerate(
            st.session_state.cart
        ):

            c1, c2, c3 = st.columns(
                [5, 2, 1]
            )

            with c1:
                st.write(
                    f"**{product.get('name', 'Product')}**"
                )

            with c2:
                st.write(
                    money(product.get("price", 0))
                )

            with c3:

                if st.button(
                    "✕",
                    key=f"remove_{i}"
                ):
                    remove_cart(i)
                    st.rerun()

        st.divider()

        st.subheader(
            f"Total: {money(get_cart_total())}"
        )

        st.header("Checkout")

        name = st.text_input(
            "Full Name"
        )

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
                                "customer_name": name.strip(),
                                "phone": phone.strip(),
                                "address": address.strip(),
                                "notes": notes.strip(),
                                "total": total,
                                "status": "pending",
                                "created_at": datetime.now(
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
                                "order_id": order_id,
                                "product_id": product.get("id"),
                                "product_name": product.get(
                                    "name",
                                    "Product"
                                ),
                                "quantity": 1,
                                "unit_price": float(
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

                    st.error(
                        "Order error:"
                    )

                    st.error(str(e))


# =========================================================
# CONTACT
# =========================================================

elif st.session_state.page == "Contact":

    st.header("📞 Contact LuxeMart")

    st.subheader("📱 Phone / WhatsApp")

    st.write("032209
