
import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="LuxeMart | Luxury Marketplace",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Luxury responsive UI
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
  --ink:#171717;
  --muted:#6d685f;
  --cream:#f7f2e9;
  --paper:#fffdf9;
  --line:#ddd4c7;
  --gold:#9a7a4f;
  --soft:#ece3d5;
}

html, body, [class*="css"] {
  font-family:"DM Sans", sans-serif;
}
.stApp {
  background:var(--cream);
  color:var(--ink);
}
.block-container {
  max-width:1180px;
  padding:1rem 1.25rem 4rem;
}
header[data-testid="stHeader"] {
  background:rgba(247,242,233,.92);
}
.brand {
  font-family:"Playfair Display",serif;
  font-size:clamp(2rem,5vw,3.1rem);
  font-weight:700;
  letter-spacing:-1.5px;
  line-height:1;
}
.kicker {
  color:var(--gold);
  letter-spacing:4px;
  font-size:.78rem;
  font-weight:700;
  text-transform:uppercase;
}
.hero {
  padding:4.2rem 0 3rem;
}
.hero h1 {
  font-family:"Playfair Display",serif;
  font-size:clamp(3.7rem,9vw,7.6rem);
  line-height:.9;
  letter-spacing:-4px;
  margin:.9rem 0 1.5rem;
}
.hero p {
  color:var(--muted);
  font-size:1.18rem;
  line-height:1.8;
  max-width:650px;
}
.hero-card {
  min-height:310px;
  border:1px solid var(--line);
  border-radius:3px;
  background:
    radial-gradient(circle at 30% 35%, rgba(255,255,255,.95), transparent 30%),
    linear-gradient(135deg,#e8dccb,#c8baa5 55%,#8e8475);
  display:flex;
  align-items:flex-end;
  padding:1.4rem;
  box-shadow:0 20px 55px rgba(57,45,29,.10);
}
.hero-card span {
  background:rgba(255,253,249,.88);
  padding:.65rem .85rem;
  font-size:.78rem;
  letter-spacing:2px;
  font-weight:700;
}
.section-title {
  font-family:"Playfair Display",serif;
  font-size:2.4rem;
  margin:.4rem 0 1.2rem;
}
.luxury-line {
  border-top:1px solid var(--line);
  margin:1rem 0 2.5rem;
}
.product {
  background:var(--paper);
  border:1px solid var(--line);
  border-radius:2px;
  padding:.75rem .75rem 1rem;
  height:100%;
  box-shadow:0 12px 30px rgba(57,45,29,.06);
}
.product-img {
  height:240px;
  display:flex;
  align-items:center;
  justify-content:center;
  background:linear-gradient(135deg,#eee5d8,#cfc1ad);
  font-size:3rem;
  color:#7d6d58;
}
.product-name {
  font-family:"Playfair Display",serif;
  font-size:1.35rem;
  font-weight:600;
  margin-top:.9rem;
}
.product-desc { color:var(--muted); min-height:42px; }
.price { font-weight:700; font-size:1.05rem; }
.pill {
  display:inline-block;
  color:var(--gold);
  letter-spacing:1.5px;
  text-transform:uppercase;
  font-size:.68rem;
  font-weight:700;
}
.info-card {
  background:var(--paper);
  border:1px solid var(--line);
  padding:1.4rem;
  height:100%;
}
.info-card h3 {
  font-family:"Playfair Display",serif;
}
.footer {
  border-top:1px solid var(--line);
  margin-top:4rem;
  padding-top:1.5rem;
  color:var(--muted);
  font-size:.85rem;
}
div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
  border-radius:2px;
  min-height:2.7rem;
  border:1px solid #1b1b1b;
  background:#171717;
  color:white;
  font-weight:700;
}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
  background:#3a352f;
  border-color:#3a352f;
  color:white;
}
div[data-baseweb="tab-list"] {
  gap:1.5rem;
  border-bottom:1px solid var(--line);
}
button[data-baseweb="tab"] {
  background:transparent;
}
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
  background:var(--paper);
  border-color:var(--line);
}
[data-testid="stMetric"] {
  background:var(--paper);
  border:1px solid var(--line);
  padding:1rem;
}
@media (max-width:700px) {
  .block-container {padding:0.7rem .9rem 3rem;}
  .hero {padding:2.4rem 0 1.7rem;}
  .hero h1 {letter-spacing:-2.5px;font-size:3.7rem;}
  .hero p {font-size:1rem;}
  .hero-card {min-height:220px;margin-top:1rem;}
  .product-img {height:185px;}
}

/* Strong text contrast fix for Streamlit */
.stApp, .stApp * {
  color: #171717;
}
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp [data-testid="stMarkdownContainer"] strong,
.stApp [data-testid="stMarkdownContainer"] span {
  color: #171717 !important;
}
.stApp [data-testid="stWidgetLabel"] p,
.stApp [data-testid="stWidgetLabel"] span,
.stApp label,
.stApp label p {
  color: #171717 !important;
}
.stApp [role="radiogroup"] label,
.stApp [role="radiogroup"] label p,
.stApp [role="radiogroup"] label span {
  color: #171717 !important;
  opacity: 1 !important;
}
.stApp button,
.stApp button p,
.stApp button span {
  color: #171717 !important;
}
.stApp div.stButton > button,
.stApp div[data-testid="stFormSubmitButton"] > button {
  color: #ffffff !important;
}
.stApp input,
.stApp textarea,
.stApp select,
.stApp [data-baseweb="select"] *,
.stApp [data-baseweb="input"] * {
  color: #171717 !important;
}
.stApp input::placeholder,
.stApp textarea::placeholder {
  color: #777066 !important;
  opacity: 1 !important;
}
.stApp [data-testid="stMetricLabel"],
.stApp [data-testid="stMetricValue"],
.stApp [data-testid="stMetricDelta"] {
  color: #171717 !important;
}
.stApp [data-baseweb="tab-list"] button,
.stApp [data-baseweb="tab-list"] button p {
  color: #171717 !important;
  opacity: 1 !important;
}
.stApp [data-testid="stExpander"] summary,
.stApp [data-testid="stExpander"] summary * {
  color: #171717 !important;
}
.stApp [data-testid="stAlert"] p {
  color: inherit !important;
}


a { color:#171717 !important; font-weight:600; text-decoration:underline; }

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Supabase
# -----------------------------
def get_supabase():
    try:
        return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    except Exception:
        return None

supabase = get_supabase()

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "admin" not in st.session_state:
    st.session_state.admin = None

DEMO_PRODUCTS = [
    {"id":"demo1","name":"Classic Linen Set","description":"Breathable refined everyday wear.","price":8500,"category":"Clothes","image_url":""},
    {"id":"demo2","name":"Signature Evening Dress","description":"An elegant statement piece for special occasions.","price":12900,"category":"Clothes","image_url":""},
    {"id":"demo3","name":"Minimal Ceramic Vase","description":"A sculptural home accent with a quiet finish.","price":4200,"category":"Home","image_url":""},
    {"id":"demo4","name":"Soft Luxe Cushion Set","description":"Premium texture and everyday comfort.","price":3800,"category":"Home","image_url":""},
]

def money(value):
    return f"Rs. {float(value):,.0f}"

def get_products(active_only=True):
    if not supabase:
        return DEMO_PRODUCTS
    try:
        q = supabase.table("products").select("*")
        if active_only:
            q = q.eq("active", True)
        result = q.order("created_at", desc=True).execute()
        return result.data or DEMO_PRODUCTS
    except Exception:
        return DEMO_PRODUCTS

def product_image(p):
    if p.get("image_url"):
        return p["image_url"]
    return None

# -----------------------------
# Header
# -----------------------------
top_left, top_right = st.columns([5,1])
with top_left:
    st.markdown('<div class="brand" style="color:#171717 !important;">LuxeMart</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#7b7368;margin-top:.35rem;">CURATED • ELEGANT • EVERYDAY</div>', unsafe_allow_html=True)
with top_right:
    st.metric("Cart", sum(st.session_state.cart.values()))

st.markdown('<div class="luxury-line"></div>', unsafe_allow_html=True)

page = st.radio(
    "Navigation",
    ["Shop", "Collections", "Sell With Us", "About", "Contact", "Admin"],
    horizontal=True,
    label_visibility="collapsed",
)

# -----------------------------
# SHOP
# -----------------------------
if page == "Shop":
    st.markdown("""
    <section class="hero">
      <div class="kicker">CURATED • ELEGANT • EVERYDAY</div>
      <h1>Luxury finds<br>for your life.</h1>
      <p>Discover refined clothing and beautiful home products from independent sellers — presented in a clean, premium shopping experience.</p>
    </section>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.15, .85])
    with left:
        if st.button("Shop Collection", use_container_width=True):
            st.session_state.shop_jump = True
    with right:
        st.markdown('<div class="hero-card"><span>LUXURY • CLOTHES • HOME</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="luxury-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Shop the collection</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([2,1])
    with c1:
        search = st.text_input("Search", placeholder="Search products...", label_visibility="collapsed")
    with c2:
        category = st.selectbox("Category", ["All", "Clothes", "Home"], label_visibility="collapsed")

    all_products = get_products()
    products = [
        p for p in all_products
        if (category == "All" or p.get("category") == category)
        and (not search or search.lower() in str(p.get("name","")).lower() or search.lower() in str(p.get("description","")).lower())
    ]

    if not products:
        st.info("No products found.")
    else:
        cols = st.columns(3)
        for i, p in enumerate(products):
            with cols[i % 3]:
                st.markdown('<div class="product">', unsafe_allow_html=True)
                img = product_image(p)
                if img:
                    st.image(img, use_container_width=True)
                else:
                    st.markdown('<div class="product-img">✦</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="pill">{p.get("category","Collection")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-name">{p.get("name","Product")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-desc">{p.get("description","")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="price">{money(p.get("price",0))}</div>', unsafe_allow_html=True)
                if st.button("Add to cart", key=f"add_{p['id']}", use_container_width=True):
                    pid = str(p["id"])
                    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1
                    st.success("Added to cart")
                st.markdown('</div>', unsafe_allow_html=True)

    # Cart
    st.markdown('<div class="luxury-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Your cart</div>', unsafe_allow_html=True)
    pmap = {str(p["id"]): p for p in all_products}
    rows, total = [], 0
    for pid, qty in list(st.session_state.cart.items()):
        if pid in pmap:
            p = pmap[pid]
            line = float(p["price"]) * qty
            total += line
            rows.append((pid, p, qty, line))

    if not rows:
        st.info("Your cart is empty.")
    else:
        for pid, p, qty, line in rows:
            a, b, c = st.columns([4,1,2])
            with a:
                st.write(f"**{p['name']}**")
            with b:
                st.write(f"× {qty}")
            with c:
                st.write(money(line))
        st.markdown(f"### Total: {money(total)}")

        with st.expander("Checkout — delivery details"):
            with st.form("checkout"):
                name = st.text_input("Full name")
                phone = st.text_input("Phone / WhatsApp")
                address = st.text_area("Delivery address")
                notes = st.text_area("Order notes", placeholder="Optional")
                submit = st.form_submit_button("Place order", use_container_width=True)

            if submit:
                if not name or not phone or not address:
                    st.error("Please enter your name, phone and delivery address.")
                elif not supabase:
                    st.error("Supabase is not connected. Add the Streamlit Secrets first.")
                else:
                    try:
                        order = supabase.table("orders").insert({
                            "customer_name": name,
                            "phone": phone,
                            "address": address,
                            "notes": notes,
                            "total": total,
                            "status": "pending",
                        }).execute()
                        order_id = order.data[0]["id"]
                        items = [
                            {
                                "order_id": order_id,
                                "product_id": None if str(pid).startswith("demo") else pid,
                                "product_name": p["name"],
                                "quantity": qty,
                                "unit_price": p["price"],
                            }
                            for pid, p, qty, line in rows
                        ]
                        supabase.table("order_items").insert(items).execute()
                        st.session_state.cart = {}
                        st.success(f"Order placed successfully. Order ID: {order_id}")
                    except Exception as e:
                        st.error(f"Order could not be placed: {e}")

# -----------------------------
# COLLECTIONS
# -----------------------------
elif page == "Collections":
    st.markdown('<div class="kicker">SHOP BY MOOD</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Collections</div>', unsafe_allow_html=True)
    a, b = st.columns(2)
    with a:
        st.markdown("""
        <div class="info-card">
          <div class="kicker">01 • CLOTHES</div>
          <h3>Quiet luxury, made wearable.</h3>
          <p>Refined everyday pieces, occasion wear and timeless essentials.</p>
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown("""
        <div class="info-card">
          <div class="kicker">02 • HOME</div>
          <h3>Beautiful details for your space.</h3>
          <p>Minimal accents, soft textures and considered home products.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<div class="luxury-line"></div>', unsafe_allow_html=True)
    st.write("Use the Shop tab to browse current products and add them to your cart.")

# -----------------------------
# SELL
# -----------------------------
elif page == "Sell With Us":
    st.markdown('<div class="kicker">FOR INDEPENDENT SELLERS</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Sell With Us</div>', unsafe_allow_html=True)
    st.write("Contact LuxeMart to list approved clothing and home products.")
    with st.form("seller_request"):
        name = st.text_input("Name")
        phone = st.text_input("Phone / WhatsApp")
        details = st.text_area("Product details", placeholder="Tell us what you want to sell.")
        send = st.form_submit_button("Send seller request")
    if send:
        if not name or not phone or not details:
            st.error("Please complete all fields.")
        else:
            st.success("Thank you. Your seller request has been prepared for review.")

# -----------------------------
# ABOUT
# -----------------------------
elif page == "About":
    st.markdown('<div class="kicker">OUR STORY</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">About LuxeMart</div>', unsafe_allow_html=True)
    a, b = st.columns([1.2, .8])
    with a:
        st.write("LuxeMart is a marketplace for refined clothing and home products. Customers can discover products, add them to a cart and place delivery orders. Independent sellers can showcase approved products, while the admin manages products and order status.")
    with b:
        st.markdown("""
        <div class="info-card">
          <div class="kicker">THE LUXEMART STANDARD</div>
          <h3>Simple. Elegant. Useful.</h3>
          <p>We keep the experience focused on beautiful products and easy ordering.</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# CONTACT
# -----------------------------
elif page == "Contact":
    st.markdown('<div class="kicker">GET IN TOUCH</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Contact LuxeMart</div>', unsafe_allow_html=True)
    a, b = st.columns(2)
    with a:
        st.markdown("""
        <div class="info-card">
          <h3>Customer support</h3>
          <p>For orders, product questions and seller enquiries, contact your LuxeMart business team.</p>
          <p><strong>Phone / WhatsApp:</strong> <a href="tel:+923220956920">03220956920</a></p>
          <p><strong>Email:</strong> <a href="mailto:asyabibi485@gmail.com">asyabibi485@gmail.com</a></p>
        </div>
        """, unsafe_allow_html=True)
    with b:
        with st.form("contact_form"):
            n = st.text_input("Your name")
            e = st.text_input("Email or phone")
            m = st.text_area("Message")
            send = st.form_submit_button("Send message", use_container_width=True)
        if send:
            st.success("Thank you. Your message is ready for your business contact workflow.")

# -----------------------------
# ADMIN
# -----------------------------
else:
    st.markdown('<div class="kicker">PRIVATE AREA</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Admin Dashboard</div>', unsafe_allow_html=True)

    if not supabase:
        st.error("Supabase is not connected. Add SUPABASE_URL and SUPABASE_KEY in Streamlit Cloud → Settings → Secrets.")
    elif not st.session_state.admin:
        st.info("Sign in with the Supabase Auth email and password you created for LuxeMart.")
        with st.form("admin_login"):
            email = st.text_input("Admin email")
            password = st.text_input("Admin password", type="password")
            login = st.form_submit_button("Login", use_container_width=True)
        if login:
            try:
                result = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if result.user:
                    st.session_state.admin = result.user
                    st.rerun()
                else:
                    st.error("Login failed.")
            except Exception as e:
                st.error(f"Login failed: {e}")
    else:
        st.success("Admin logged in")
        if st.button("Logout"):
            try:
                supabase.auth.sign_out()
            except Exception:
                pass
            st.session_state.admin = None
            st.rerun()

        tab_products, tab_orders, tab_add = st.tabs(["Products", "Orders", "Add Product"])

        with tab_products:
            try:
                data = supabase.table("products").select("*").order("created_at", desc=True).execute().data or []
                if not data:
                    st.info("No products yet.")
                for p in data:
                    a, b = st.columns([5,1])
                    with a:
                        st.write(f"**{p['name']}** — {p['category']} — {money(p['price'])}")
                    with b:
                        if st.button("Delete", key=f"delete_{p['id']}"):
                            supabase.table("products").delete().eq("id", p["id"]).execute()
                            st.rerun()
            except Exception as e:
                st.error(str(e))

        with tab_orders:
            try:
                orders = supabase.table("orders").select("*").order("created_at", desc=True).execute().data or []
                if not orders:
                    st.info("No customer orders yet.")
                statuses = ["pending", "confirmed", "shipped", "delivered", "cancelled"]
                for o in orders:
                    with st.expander(f"{o['customer_name']} — {money(o['total'])} — {o['status']}"):
                        st.write("**Phone:**", o["phone"])
                        st.write("**Address:**", o["address"])
                        st.write("**Notes:**", o.get("notes") or "-")
                        current = o.get("status","pending")
                        ns = st.selectbox(
                            "Order status",
                            statuses,
                            index=statuses.index(current) if current in statuses else 0,
                            key=f"status_{o['id']}",
                        )
                        if st.button("Update status", key=f"update_{o['id']}"):
                            supabase.table("orders").update({"status": ns}).eq("id", o["id"]).execute()
                            st.success("Order status updated.")
                            st.rerun()
            except Exception as e:
                st.error(str(e))

        with tab_add:
            with st.form("add_product"):
                name = st.text_input("Product name")
                desc = st.text_area("Description")
                price = st.number_input("Price (PKR)", min_value=0.0, step=100.0)
                category = st.selectbox("Category", ["Clothes","Home"])
                image_url = st.text_input("Image URL", placeholder="Optional")
                active = st.checkbox("Active", value=True)
                add = st.form_submit_button("Add product", use_container_width=True)
            if add:
                if not name:
                    st.error("Product name is required.")
                else:
                    try:
                        supabase.table("products").insert({
                            "name": name,
                            "description": desc,
                            "price": price,
                            "category": category,
                            "image_url": image_url,
                            "active": active,
                        }).execute()
                        st.success("Product added.")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))

st.markdown("""
<div class="footer">
  <strong>LuxeMart</strong> · Luxury clothes & home marketplace · Built for simple shopping and selling.
</div>
""", unsafe_allow_html=True)
