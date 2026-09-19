import streamlit as st
from supabase import create_client


# =========================================================
# LUXEMART - COMPLETE STREAMLIT APP
# =========================================================

st.set_page_config(
    page_title="LUXEMART",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# SUPABASE
# =========================================================

SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
ADMIN_EMAIL = st.secrets["admin"]["email"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "shop_category" not in st.session_state:
    st.session_state.shop_category = "All"

if "search" not in st.session_state:
    st.session_state.search = ""

if "product_page" not in st.session_state:
    st.session_state.product_page = 1


# =========================================================
# PRODUCTS
# =========================================================

PRODUCTS = [
    {
        "id": 1,
        "name": "Luxury Handbag",
        "category": "Fashion",
        "price": 5499,
        "image": "https://images.pexels.com/photos/1152077/pexels-photo-1152077.jpeg",
    },
    {
        "id": 2,
        "name": "Silk Scarf",
        "category": "Fashion",
        "price": 1999,
        "image": "https://images.pexels.com/photos/322207/pexels-photo-322207.jpeg",
    },
    {
        "id": 3,
        "name": "Elegant Pearl Necklace",
        "category": "Jewellery",
        "price": 3499,
        "image": "https://images.pexels.com/photos/1191531/pexels-photo-1191531.jpeg",
    },
    {
        "id": 4,
        "name": "Elegant Bracelet",
        "category": "Jewellery",
        "price": 2499,
        "image": "https://images.pexels.com/photos/1927259/pexels-photo-1927259.jpeg",
    },
    {
        "id": 5,
        "name": "Gold Watch",
        "category": "Accessories",
        "price": 7999,
        "image": "https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg",
    },
    {
        "id": 6,
        "name": "Classic Sunglasses",
        "category": "Accessories",
        "price": 2999,
        "image": "https://images.pexels.com/photos/46710/pexels-photo-46710.jpeg",
    },
    {
        "id": 7,
        "name": "Premium Makeup Set",
        "category": "Beauty",
        "price": 4499,
        "image": "https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg",
    },
    {
        "id": 8,
        "name": "Luxury Abaya",
        "category": "Clothes",
        "price": 4999,
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
    },
    {
        "id": 9,
        "name": "Premium Lawn Suit",
        "category": "Clothes",
        "price": 3999,
        "image": "https://images.pexels.com/photos/996329/pexels-photo-996329.jpeg",
    },
    {
        "id": 10,
        "name": "Elegant Evening Dress",
        "category": "Clothes",
        "price": 5999,
        "image": "https://images.pexels.com/photos/985635/pexels-photo-985635.jpeg",
    },
    {
        "id": 11,
        "name": "Classic Casual Kurti",
        "category": "Clothes",
        "price": 2499,
        "image": "https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg",
    },
    {
        "id": 12,
        "name": "Luxury Rose Perfume",
        "category": "Perfume",
        "price": 2999,
        "image": "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg",
    },
    {
        "id": 13,
        "name": "Royal Oud Perfume",
        "category": "Perfume",
        "price": 4499,
        "image": "https://images.pexels.com/photos/1961795/pexels-photo-1961795.jpeg",
    },
    {
        "id": 14,
        "name": "Vanilla Dream Perfume",
        "category": "Perfume",
        "price": 2799,
        "image": "https://images.pexels.com/photos/3059609/pexels-photo-3059609.jpeg",
    },
]


CATEGORIES = [
    "All",
    "Clothes",
    "Fashion",
    "Jewellery",
    "Accessories",
    "Perfume",
    "Beauty",
]


# =========================================================
# FUNCTIONS
# =========================================================

def get_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def money(amount):
    try:
        return f"Rs. {float(amount):,.0f}"
    except Exception:
        return "Rs. 0"


def cart_count():
    return len(st.session_state.cart)


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


def add_to_cart(product_id):
    st.session_state.cart.append(product_id)
    st.toast("Added to cart 🛒")


def toggle_favorite(product_id):

    if product_id in st.session_state.favorites:

        st.session_state.favorites.remove(product_id)
        st.toast("Removed from favorites")

    else:

        st.session_state.favorites.append(product_id)
        st.toast("Added to favorites ❤️")


def safe_image(column, image_url):

    try:

        column.image(
            image_url,
            use_container_width=True,
        )

    except Exception:

        column.info(
            "Product image unavailable"
        )


def logout_admin():

    try:
        supabase.auth.sign_out()
    except Exception:
        pass

    st.session_state.admin_logged_in = False
    st.session_state.page = "Shop"

    st.rerun()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("LUXEMART")

    st.caption(
        "Luxury • Style • Elegance"
    )

    st.divider()

    st.subheader("Navigation")

    if st.button(
        "🏠 Shop",
        key="sidebar_shop",
        use_container_width=True,
    ):
        go_to("Shop")

    if st.button(
        f"❤️ Favorites ({len(st.session_state.favorites)})",
        key="sidebar_favorites",
        use_container_width=True,
    ):
        go_to("Favorites")

    if st.button(
        f"🛒 Cart ({cart_count()})",
        key="sidebar_cart",
        use_container_width=True,
    ):
        go_to("Cart")

    if st.button(
        "ℹ️ About",
key="sidebar_about",
        use_container_width=True,
    ):
        go_to("About")

    if st.button(
        "🔐 Admin Dashboard",
        key="sidebar_admin",
        use_container_width=True,
    ):
        go_to("Admin")

    st.divider()

    st.subheader("Shop by Category")

    for category in CATEGORIES:

        if st.button(
            category,
            key=f"sidebar_category_{category}",
            use_container_width=True,
        ):

            st.session_state.shop_category = category
            st.session_state.product_page = 1
            st.session_state.page = "Shop"

            st.rerun()

    st.divider()

    st.caption(
        "Premium fashion & lifestyle"
    )


# =========================================================
# TOP HEADER
# =========================================================

header_left, header_middle, header_right = st.columns(
    [4, 4, 2]
)

with header_left:

    st.title("LUXEMART")

with header_middle:

    st.write("")

with header_right:

    if st.button(
        f"🛒 Cart ({cart_count()})",
        key="header_cart",
        use_container_width=True,
    ):

        go_to("Cart")


st.divider()


# =========================================================
# SHOP
# =========================================================

if st.session_state.page == "Shop":

    st.header(
        "✨ Discover Your Signature Style"
    )

    st.write(
        "Explore elegant fashion, jewellery, accessories, "
        "beauty products and fragrances."
    )

    hero_left, hero_right = st.columns(
        [1.5, 1]
    )

    with hero_left:

        st.info(
            "✨ NEW COLLECTION\n\n"
            "Discover elegant products selected "
            "for a modern luxury lifestyle."
        )

        st.success(
            "Easy browsing • Easy ordering • "
            "Secure order storage"
        )

    with hero_right:

        safe_image(
            hero_right,
            "https://images.pexels.com/photos/994523/pexels-photo-994523.jpeg",
        )

    st.divider()

    # =====================================================
    # EXPLORE COLLECTION
    # =====================================================

    st.header(
        "✨ Explore Collection"
    )

    search_col, category_col, sort_col = st.columns(
        [2, 1, 1]
    )

    with search_col:

        search = st.text_input(
            "Search products",
            value=st.session_state.search,
            placeholder="Handbag, perfume, necklace...",
            key="product_search",
        )

        if search != st.session_state.search:

            st.session_state.search = search
            st.session_state.product_page = 1

    with category_col:

        current_category_index = CATEGORIES.index(
            st.session_state.shop_category
        )

        selected_category = st.selectbox(
            "Category",
            CATEGORIES,
            index=current_category_index,
            key="product_category",
        )

        if (
            selected_category
            != st.session_state.shop_category
        ):

            st.session_state.shop_category = (
                selected_category
            )

            st.session_state.product_page = 1

    with sort_col:

        sort_option = st.selectbox(
            "Sort",
            [
                "Featured",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A-Z",
            ],
            key="product_sort",
        )

    max_price = st.slider(
        "Maximum price",
        min_value=1000,
        max_value=10000,
        value=10000,
        step=500,
        key="maximum_price",
    )

    # =====================================================
    # FILTER PRODUCTS
    # =====================================================

    filtered_products = []

    for product in PRODUCTS:

        if selected_category != "All":

            if product["category"] != selected_category:
                continue

        if search.strip():

            search_text = search.strip().lower()

            product_text = (
                product["name"]
                + " "
                + product["category"]
            ).lower()

            if search_text not in product_text:
                continue

        if product["price"] > max_price:
            continue

        filtered_products.append(product)

    # =====================================================
    # SORT PRODUCTS
    # =====================================================

    if sort_option == "Price: Low to High":

        filtered_products.sort(
            key=lambda product: product["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered_products.sort(
            key=lambda product: product["price"],
            reverse=True,
        )

    elif sort_option == "Name: A-Z":

        filtered_products.sort(
            key=lambda product: product["name"]
        )

    # =====================================================
    # PRODUCT COUNT
    # =====================================================

    st.caption(
        f"{len(filtered_products)} product(s) available"
    )

    # =====================================================
    # PAGINATION
    # =====================================================

    PRODUCTS_PER_PAGE = 4

    if not filtered_products:

        st.warning(
            "No products found. Try another search, "
            "category or price range."
        )

    else:

        total_pages = (
            len(filtered_products)
            + PRODUCTS_PER_PAGE
            - 1
        ) // PRODUCTS_PER_PAGE

        if st.session_state.product_page < 1:

            st.session_state.product_page = 1

        if st.session_state.product_page > total_pages:

            st.session_state.product_page = total_pages

        current_page = st.session_state.product_page

        start_index = (
            current_page - 1
        ) * PRODUCTS_PER_PAGE

        end_index = (
            start_index
            + PRODUCTS_PER_PAGE
        )

        page_products = filtered_products[
            start_index:end_index
        ]

        # =================================================
        # PRODUCT GRID
        # =================================================

        product_columns = st.columns(4)

        for index, product in enumerate(
            page_products
        ):

            column = product_columns[index]

            safe_image(
                column,
                product["image"],
            )

            column.subheader(
                product["name"]
            )

            column.caption(
                product["category"]
            )

            column.write(
                f"**{money(product['price'])}**"
            )

            if product["id"] in (
                st.session_state.favorites
            ):

                favorite_label = (
                    "❤️ Remove Favorite"
                )

            else:

                favorite_label = (
                    "♡ Add Favorite"
                )

            if column.button(
                favorite_label,
                key=f"favorite_product_{product['id']}",
                use_container_width=True,
            ):

                toggle_favorite(
                    product["id"]
                )

                st.rerun()

            if column.button(
                "🛒 Add to Cart",
                key=f"add_product_{product['id']}",
                use_container_width=True,
            ):

                add_to_cart(
                    product["id"]
                )

                st.rerun()

        st.divider()

        # =================================================
        # PREVIOUS / PAGE / NEXT
        # =================================================

        previous_col, page_col, next_col = st.columns(
            [1, 2, 1]
        )

        with previous_col:

            if current_page > 1:

                if st.button(
                    "← Previous",
                    key="previous_page",
                    use_container_width=True,
                ):

                    st.session_state.product_page -= 1
                    st.rerun()

            else:

                st.write("")

        with page_col:

            st.write(
                f"Page {current_page} of {total_pages}"
            )

            st.caption(
                f"Showing products "
                f"{start_index + 1}–"
                f"{min(end_index, len(filtered_products))}"
            )

        with next_col:

            if current_page < total_pages:

                if st.button(
                    "Next →",
                    key="next_page",
                    use_container_width=True,
                ):

                    st.session_state.product_page += 1
                    st.rerun()

            else:

                st.write("")


# =========================================================
# FAVORITES
# =========================================================

elif st.session_state.page == "Favorites":

    st.header(
        "❤️ Favorites"
    )

    st.write(
        "Your saved LUXEMART products."
    )

    favorite_products = []

    for product_id in st.session_state.favorites:

        product = get_product(product_id)

        if product:
            favorite_products.append(product)

    if not favorite_products:

        st.info(
            "You have no favorite products yet."
        )

        if st.button(
            "🛍️ Browse Products",
            key="favorites_browse",
            use_container_width=True,
        ):

            go_to("Shop")

    else:

        for start in range(
            0,
            len(favorite_products),
            4,
        ):

            row_products = favorite_products[
                start:start + 4
            ]

            columns = st.columns(4)

            for index, product in enumerate(
                row_products
            ):

                column = columns[index]

                safe_image(
                    column,
                    product["image"],
                )

                column.subheader(
                    product["name"]
                )

                column.caption(
                    product["category"]
                )

                column.write(
                    f"**{money(product['price'])}**"
                )

                if column.button(
                    "🛒 Add to Cart",
                    key=f"favorite_add_{product['id']}",
                    use_container_width=True,
                ):

                    add_to_cart(
                        product["id"]
                    )

                    st.rerun()

                if column.button(
                    "Remove ❤️",
                    key=f"favorite_remove_{product['id']}",
                    use_container_width=True,
                ):

                    st.session_state.favorites.remove(
                        product["id"]
                    )

                    st.rerun()


# =========================================================
# CART
# =========================================================

elif st.session_state.page == "Cart":

    st.header(
        "🛒 Shopping Cart"
    )

    st.write(
        "Review your products before placing your order."
    )

    if not st.session_state.cart:

        st.info(
            "Your cart is empty."
        )

        if st.button(
            "🛍️ Continue Shopping",
            key="continue_shopping",
            use_container_width=True,
        ):

            go_to("Shop")

    else:

        st.subheader(
            "Your Products"
        )

        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            if not product:
                continue

            col1, col2, col3 = st.columns(
                [5, 2, 1]
            )

            with col1:

                st.write(
                    f"🛍️ **{product['name']}**"
                )

                st.caption(
                    product["category"]
                )

            with col2:

                st.write(
                    f"**{money(product['price'])}**"
                )

            with col3:

                if st.button(
                    "Remove",
                    key=f"cart_remove_{index}",
                    use_container_width=True,
                ):

                    st.session_state.cart.pop(index)

                    st.rerun()

        st.divider()

        st.subheader(
            "Order Summary"
        )

        summary_left, summary_right = st.columns(2)

        with summary_left:

            st.metric(
                "Items",
                cart_count(),
            )

        with summary_right:

            st.metric(
                "Total",
                money(cart_total()),
            )

        st.divider()

        st.subheader(
            "Checkout"
        )

        customer_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
            key="checkout_name",
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX",
            key="checkout_phone",
        )

        customer_address = st.text_area(
            "Delivery Address",
            placeholder="Enter complete delivery address",
            key="checkout_address",
        )

        if st.button(
            "💳 Place Order",
            key="place_order",
            use_container_width=True,
        ):

            if not customer_name.strip():

                st.error(
                    "Please enter your name."
                )

            elif not customer_phone.strip():

                st.error(
                    "Please enter your phone number."
                )

            elif not customer_address.strip():

                st.error(
                    "Please enter your delivery address."
                )

            else:

                try:

                    total = cart_total()

                    order_data = {
                        "customer_name": customer_name.strip(),
                        "customer_phone": customer_phone.strip(),
                        "customer_address": customer_address.strip(),
                        "total_amount": total,
                    }

                    order_response = (
                        supabase
                        .table("orders")
                        .insert(order_data)
                        .execute()
                    )

                    if not order_response.data:

                        st.error(
                            "Order could not be created."
                        )

                    else:

                        order_id = (
                            order_response
                            .data[0]["id"]
                        )

                        for product_id in (
                            st.session_state.cart
                        ):

                            product = get_product(
                                product_id
                            )

                            if not product:
                                continue

                            item_data = {
                                "order_id": order_id,
                                "product_name": product["name"],
                                "price": product["price"],
                                "quantity": 1,
                            }

                            (
                                supabase
                                .table("order_items")
                                .insert(item_data)
                                .execute()
                            )

                        st.session_state.cart = []

                        st.success(
                            "🎉 Your order has been placed successfully!"
                        )

                        st.info(
                            f"Order ID: {order_id}"
                        )

                        st.balloons()

                except Exception as error:

                    st.error(
                        f"Order error: {error}"
                    )


# =========================================================
# ABOUT
# =========================================================

elif st.session_state.page == "About":

    st.header(
        "ℹ️ About LUXEMART"
    )

    st.subheader(
        "Luxury made simple."
    )

    st.write(
        "LUXEMART is a modern online shopping platform "
        "for fashion, jewellery, accessories, beauty "
        "products and fragrances."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📞 Contact"
        )

        st.write(
            "03169707804"
        )

    with col2:

        st.subheader(
            "📧 Email"
        )

        st.write(
            "asyabibi485@gmail.com"
        )

    st.divider()

    st.subheader(
        "Our Collection"
    )

    st.write(
        "✨ Clothes"
    )

    st.write(
        "💎 Jewellery"
    )

    st.write(
        "👜 Fashion"
    )

    st.write(
        "⌚ Accessories"
    )

    st.write(
        "🌸 Perfumes"
    )

    st.write(
        "💄 Beauty"
    )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

elif st.session_state.page == "Admin":

    st.header(
        "🔐 Admin Dashboard"
    )

    st.write(
        "Customer orders and requests."
    )

    if not st.session_state.admin_logged_in:

        st.info(
            "Authorized administrator login."
        )

        admin_email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email",
            key="admin_email",
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password",
            key="admin_password",
        )

        if st.button(
            "🔐 Login",
            key="admin_login",
            use_container_width=True,
        ):

            try:

                response = (
                    supabase
                    .auth
                    .sign_in_with_password(
                        {
                            "email": admin_email,
                            "password": admin_password,
                        }
                    )
                )

                if response.user:

                    logged_email = (
                        response.user.email or ""
                    )

                    if (
                        logged_email.lower()
                        == ADMIN_EMAIL.lower()
                    ):

                        st.session_state.admin_logged_in = True

                        st.success(
                            "Admin login successful."
                        )

                        st.rerun()

                    else:

                        try:
                            supabase.auth.sign_out()
                        except Exception:
                            pass

                        st.error(
                            "This account is not authorized as admin."
                        )

                else:

                    st.error(
                        "Login failed."
                    )

            except Exception as error:

                st.error(
                    f"Login error: {error}"
                )

    else:

        admin_left, admin_right = st.columns(
            [4, 1]
        )

        with admin_left:

            st.subheader(
                "📦 Customer Orders"
            )

        with admin_right:

            if st.button(
                "Logout",
                key="admin_logout",
                use_container_width=True,
            ):

                logout_admin()

        try:

            orders_response = (
                supabase
                .table("orders")
                .select("*")
                .order(
                    "created_at",
                    desc=True,
                )
                .execute()
            )

            orders = (
                orders_response.data
                or []
            )

            if not orders:

                st.info(
                    "No customer orders found."
                )

            else:

                st.metric(
                    "Total Orders",
                    len(orders),
                )

                st.divider()

                for order in orders:

                    order_id = order.get(
                        "id",
                        "N/A",
                    )

                    customer_name = order.get(
                        "customer_name",
                        "Customer",
                    )

                    with st.expander(
                        f"🧾 Order #{order_id} — {customer_name}"
                    ):

                        info1, info2 = st.columns(2)

                        with info1:

                            st.write(
                                f"**Customer:** "
                                f"{customer_name}"
                            )

                            st.write(
                                f"**Phone:** "
                                f"{order.get('customer_phone', '-')}"
                            )

                            st.write(
                                f"**Address:** "
                                f"{order.get('customer_address', '-')}"
                            )

                        with info2:

                            st.write(
                                f"**Total:** "
                                f"{money(order.get('total_amount', 0))}"
                            )

                            st.write(
                                f"**Date:** "
                                f"{order.get('created_at', '-')}"
                            )

                        st.divider()

                        st.subheader(
                            "🛍️ Order Items"
                        )

                        try:

                            items_response = (
                                supabase
                                .table("order_items")
                                .select("*")
                                .eq(
                                    "order_id",
                                    order_id,
                                )
                                .execute()
                            )

                            items = (
                                items_response.data
                                or []
                            )

                            if items:

                                for item in items:

                                    item_name = item.get(
                                        "product_name",
                                        "-",
                                    )

                                    item_price = item.get(
                                        "price",
                                        0,
                                    )

                                    quantity = item.get(
                                        "quantity",
                                        1,
                                    )

                                    st.write(
                                        f"🛍️ {item_name} — "
                                        f"{money(item_price)} × "
                                        f"{quantity}"
                                    )

                            else:

                                st.caption(
                                    "No order items found."
                                )

                        except Exception as item_error:

                            st.error(
                                "Could not load order items: "
                                + str(item_error)
                            )

        except Exception as error:

            st.error(
                "Could not load orders: "
                + str(error)
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "LUXEMART • Luxury • Fashion • Beauty • Lifestyle • © 2026"
)
