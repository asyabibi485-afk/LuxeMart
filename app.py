                                "quantity": 1,
                                "total": product_price,
                                "status": "Pending",
                                "created_at": datetime.utcnow().isoformat(),
                            }
                        ).execute()

                except Exception as error:

                    order_success = False

                    st.error(
                        "Order could not be submitted. "
                        "Please check your Supabase orders table."
                    )

                if order_success:

                    st.session_state.cart = []

                    st.success(
                        "🎉 ORDER PLACED SUCCESSFULLY!"
                    )

                    st.info(
                        "Thank you for shopping with LuxeMart. "
                        "Your order has been received."
                    )

                    st.balloons()

# =========================================================
# MORE
# =========================================================

elif st.session_state.page == "More":

    st.markdown(
        '<div class="kicker">LUXEMART</div>',
        unsafe_allow_html=True,
    )

    st.title("More")

    st.markdown(
        """
<div class="hero">

    <div class="kicker">
        CUSTOMER MENU
    </div>

    <h2>
        Everything LuxeMart.
    </h2>

    <p>
        Contact us, learn about LuxeMart, or apply to sell
        your products on the marketplace.
    </p>

</div>
""",
        unsafe_allow_html=True,
    )

    more1, more2, more3 = st.columns(3)

    with more1:
        if st.button("🤝 SELL WITH US", type="primary"):
            st.session_state.page = "Sell With Us"
            st.rerun()

    with more2:
        if st.button("ABOUT LUXEMART"):
            st.session_state.page = "About"
            st.rerun()

    with more3:
        if st.button("📞 CONTACT US"):
            st.session_state.page = "Contact"
            st.rerun()

    st.markdown("")

    if st.button("🔐 ADMIN"):
        st.session_state.page = "Admin"
        st.rerun()

# =========================================================
# SELL WITH US
# =========================================================

elif st.session_state.page == "Sell With Us":

    st.markdown(
        '<div class="kicker">PARTNER WITH US</div>',
        unsafe_allow_html=True,
    )

    st.title("Sell With Us")

    st.markdown(
        """
<div class="hero">

    <div class="kicker">
        INDEPENDENT SELLERS
    </div>

    <h2>
        Bring your best products.
    </h2>

    <p>
        Submit your product information to LuxeMart.
        Approved sellers can showcase clothing and home products.
    </p>

</div>
""",
        unsafe_allow_html=True,
    )

    seller_name = st.text_input(
        "Your Name",
        placeholder="Enter your name",
    )

    seller_phone = st.text_input(
        "Phone / WhatsApp",
        placeholder="03XXXXXXXXX",
    )

    seller_details = st.text_area(
        "Product Details",
        placeholder="Tell us about your products...",
        height=180,
    )

    if st.button(
        "SEND SELLER REQUEST",
        type="primary",
    ):

        if (
            not seller_name.strip()
            or not seller_phone.strip()
            or not seller_details.strip()
        ):

            st.warning(
                "Please complete all fields."
            )

        else:

            try:

                supabase.table(
                    "seller_requests"
                ).insert(
                    {
                        "name": seller_name.strip(),
                        "phone": seller_phone.strip(),
                        "product_details": seller_details.strip(),
                        "status": "Pending",
                        "created_at": datetime.utcnow().isoformat(),
                    }
                ).execute()

                st.success(
                    "SELLER REQUEST SENT SUCCESSFULLY!"
                )

            except Exception:

                st.error(
                    "Could not send seller request. "
                    "Please check your seller_requests table."
                )

# =========================================================
# ABOUT
# =========================================================

elif st.session_state.page == "About":

    st.markdown(
        '<div class="kicker">OUR STORY</div>',
        unsafe_allow_html=True,
    )

    st.title("About LuxeMart")

    st.markdown(
        """
<div class="hero">

    <div class="kicker">
        CURATED • ELEGANT • EVERYDAY
    </div>

    <h2>
        Refined. Simple. Personal.
    </h2>

    <p>
        LuxeMart is a premium marketplace for carefully selected
        clothing and beautiful home products from independent sellers.
    </p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="card">

    <div class="card-title">
        OUR VISION
    </div>

    <div class="card-text">
        To create a beautiful and simple shopping experience
        where customers can discover products they love.
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

# =========================================================
# CONTACT
# =========================================================

elif st.session_state.page == "Contact":

    st.markdown(
        '<div class="kicker">GET IN TOUCH</div>',
        unsafe_allow_html=True,
    )

    st.title("Contact LuxeMart")

    st.markdown(
        """
<div class="card">

    <div class="card-title">
        CUSTOMER SUPPORT
    </div>

    <br>

    <div class="card-text">

        <strong style="color:#F4D875;">
            📱 PHONE / WHATSAPP
        </strong>

        <br>

        03220956920

        <br><br>

        <strong style="color:#F4D875;">
            ✉ EMAIL
        </strong>

        <br>

        asyabibi485@gmail.com

    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("## Send us a Message")

    contact_name = st.text_input(
        "Your Name",
        placeholder="Enter your name",
    )

    contact_message = st.text_area(
        "Your Message",
        placeholder="Write your message...",
        height=150,
    )

    if st.button(
        "SEND MESSAGE",
        type="primary",
    ):

        if (
            not contact_name.strip()
            or not contact_message.strip()
        ):

            st.warning(
                "Please enter your name and message."
            )

        else:

            st.success(
                "MESSAGE RECEIVED SUCCESSFULLY!"
            )

# =========================================================
# ADMIN
# =========================================================

elif st.session_state.page == "Admin":

    st.markdown(
        '<div class="kicker">PRIVATE AREA</div>',
        unsafe_allow_html=True,
    )

    st.title("LuxeMart Admin")

    if not st.session_state.admin_logged_in:

        admin_email = st.text_input(
            "Admin Email",
            placeholder="Enter admin email",
        )

        admin_password = st.text_input(
            "Admin Password",
            type="password",
            placeholder="Enter admin password",
        )

        if st.button(
            "LOGIN TO ADMIN",
            type="primary",
        ):

            try:

                correct_email = st.secrets["admin"]["email"]
                correct_password = st.secrets["admin"]["password"]

                if (
                    admin_email.strip() == correct_email
                    and admin_password == correct_password
                ):

                    st.session_state.admin_logged_in = True

                    st.success(
                        "ADMIN LOGIN SUCCESSFUL!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Incorrect admin email or password."
                    )

            except Exception:

                st.error(
                    "Admin credentials are not configured "
                    "in Streamlit Secrets."
                )

    else:

        st.success(
            "ADMIN PANEL ACTIVE"
        )

        if st.button(
            "LOG OUT",
            type="primary",
        ):

            st.session_state.admin_logged_in = False
            st.session_state.page = "Shop"
            st.rerun()

        st.markdown("---")

        orders = get_orders()
        sellers = get_seller_requests()

        x, y
