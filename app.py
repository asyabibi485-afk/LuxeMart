import html
import re
import uuid
from urllib.parse import quote

import streamlit as st
from supabase import create_client

try:  # ask Supabase NOT to send the new row back (customers have no read access)
    from postgrest.types import ReturnMethod
    MINIMAL = ReturnMethod.minimal
except Exception:  # pragma: no cover
    MINIMAL = "minimal"

st.set_page_config(
    page_title="LuxeMart | Luxury Marketplace",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Business settings (edit these)
# -----------------------------
WHATSAPP_NUMBER = "923220956920"      # international format, no + or spaces
PHONE_DISPLAY = "03220956920"
EMAIL = "asyabibi485@gmail.com"
DELIVERY_FEE = 0                      # Rs. per order, 0 = free delivery

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');

:root{
  --ink:#241a16; --muted:#5e5148; --cream:#f7f2e9; --paper:#fffdf9;
  --line:#d3c6b2; --gold:#8a6840; --gold-dark:#6f5230;
}

html, body, .stApp, .stApp button, .stApp input, .stApp textarea {
  font-family:"DM Sans", sans-serif;
}
.stApp { background:var(--cream); color:var(--ink); font-weight:600; }
.block-container { max-width:1180px; padding:1rem 1.1rem 4rem; }
header[data-testid="stHeader"] { background:rgba(247,242,233,.92); }

/* ---------- Bold text everywhere ---------- */
.stApp p, .stApp li, .stApp label, .stApp summary,
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stWidgetLabel"] p {
  font-weight:700 !important; color:var(--ink);
}
.stApp [data-testid="stWidgetLabel"] p { font-size:1rem; }
.stApp [role="radiogroup"] label p { font-weight:800 !important; }
.stApp button[data-baseweb="tab"] p { font-weight:800 !important; }
.stApp input, .stApp textarea { font-weight:700 !important; font-size:16px !important; color:var(--ink) !important; }
.stApp input::placeholder, .stApp textarea::placeholder { color:#8a7d70 !important; font-weight:600 !important; opacity:1 !important; }

.brand { font-family:"Playfair Display",serif; font-size:clamp(2rem,5vw,3.1rem); font-weight:800; letter-spacing:-1.5px; line-height:1; color:var(--ink); }
.tagline { color:var(--muted); font-weight:800; letter-spacing:2px; font-size:.78rem; margin-top:.4rem; }
.kicker { color:var(--gold); letter-spacing:3px; font-size:.8rem; font-weight:800; text-transform:uppercase; }
.hero { padding:3rem 0 2rem; }
.hero h1 { font-family:"Playfair Display",serif; font-weight:800; font-size:clamp(3.2rem,9vw,7rem); line-height:.92; letter-spacing:-3px; margin:.8rem 0 1.3rem; color:var(--ink); }
.hero p { color:var(--muted) !important; font-size:1.15rem; line-height:1.7; max-width:650px; font-weight:700 !important; }
.hero-card { min-height:260px; border:1px solid var(--line); border-radius:18px;
  background: radial-gradient(circle at 30% 35%, rgba(255,255,255,.95), transparent 30%), linear-gradient(135deg,#e8dccb,#c8baa5 55%,#8e8475);
  display:flex; align-items:flex-end; padding:1.2rem; box-shadow:0 20px 55px rgba(57,45,29,.12); }
.hero-card span { background:rgba(255,253,249,.92); padding:.6rem .9rem; border-radius:999px; font-size:.78rem; letter-spacing:2px; font-weight:800; }
.section-title { font-family:"Playfair Display",serif; font-weight:800; font-size:2.2rem; margin:.4rem 0 1rem; color:var(--ink); }
.luxury-line { border-top:1px solid var(--line); margin:1rem 0 2rem; }
.product-img { height:220px; display:flex; align-items:center; justify-content:center; border-radius:12px;
  background:linear-gradient(135deg,#eee5d8,#cfc1ad); font-size:3rem; color:#7d6d58; }
.product-name { font-family:"Playfair Display",serif; font-size:1.4rem; font-weight:800; margin-top:.7rem; color:var(--ink); }
.product-desc { color:var(--muted) !important; min-height:40px; font-weight:700; }
.price { font-weight:800; font-size:1.15rem; color:var(--ink); }
.pill { display:inline-block; color:var(--gold); letter-spacing:1.5px; text-transform:uppercase; font-size:.7rem; font-weight:800; margin-top:.6rem; }
.info-card { background:var(--paper); border:1px solid var(--line); border-radius:16px; padding:1.4rem; height:100%; }
.info-card h3 { font-family:"Playfair Display",serif; font-weight:800; }
.footer { border-top:1px solid var(--line); margin-top:4rem; padding-top:1.5rem; color:var(--muted); font-size:.9rem; font-weight:700; }

/* cards (st.container(border=True)) */
.stApp [data-testid="stVerticalBlockBorderWrapper"] { background:var(--paper); border-radius:16px; border-color:var(--line); }

/* summary lines in cart */
.line-name { font-weight:800; font-size:1.05rem; color:var(--ink); }
.line-sub { color:var(--muted); font-weight:700; font-size:.92rem; }
.sum-row { display:flex; justify-content:space-between; font-weight:700; padding:.25rem 0; color:var(--ink); }
.sum-total { display:flex; justify-content:space-between; font-weight:800; font-size:1.3rem; padding:.7rem 0 .2rem; border-top:1.5px solid var(--line); margin-top:.4rem; color:var(--ink); }
.cod-note { background:#efe6d6; border-radius:12px; padding:.75rem 1rem; font-weight:800; color:var(--ink); margin:.4rem 0 1rem; }
.done-card { background:var(--paper); border:1.5px solid var(--gold); border-radius:18px; padding:1.6rem; }
.done-card h2 { font-family:"Playfair Display",serif; font-weight:800; margin:.2rem 0 .6rem; color:var(--ink); }

/* ---------- Fancy buttons ---------- */
.stApp button[data-testid^="stBaseButton"],
.stApp a[data-testid^="stBaseLinkButton"] {
  border-radius:999px; min-height:3rem; padding:.5rem 1.4rem;
  border:1px solid rgba(255,255,255,.14);
  background:linear-gradient(135deg,#2b201b 0%,#4d3a2d 100%);
  box-shadow:0 8px 20px rgba(36,26,22,.28), inset 0 1px 0 rgba(255,255,255,.14);
  letter-spacing:.4px; text-decoration:none;
  transition:transform .15s ease, box-shadow .15s ease, filter .15s ease;
}
.stApp button[data-testid^="stBaseButton"] *,
.stApp a[data-testid^="stBaseLinkButton"] * {
  color:#fffaf2 !important; font-weight:800 !important; text-decoration:none !important;
}
.stApp button[data-testid^="stBaseButton"]:hover,
.stApp a[data-testid^="stBaseLinkButton"]:hover {
  transform:translateY(-2px); filter:brightness(1.12);
  box-shadow:0 14px 28px rgba(36,26,22,.34), inset 0 1px 0 rgba(255,255,255,.2);
}
.stApp button[data-testid^="stBaseButton"]:active { transform:translateY(0); box-shadow:0 4px 10px rgba(36,26,22,.3); }
.stApp button[data-testid="stBaseButton-primary"],
.stApp button[data-testid="stBaseButton-primaryFormSubmit"],
.stApp button[kind="primary"], .stApp button[kind="primaryFormSubmit"],
.stApp a[data-testid="stBaseLinkButton-primary"] {
  background:linear-gradient(135deg,#c39a5c 0%,#8a6840 55%,#6f5230 100%);
  border:1px solid rgba(255,255,255,.28);
  box-shadow:0 10px 24px rgba(138,104,64,.45), inset 0 1px 0 rgba(255,255,255,.35);
}
.stApp button[data-testid^="stBaseButton"]:disabled { opacity:.55; }

/* keep small button rows on one line on phones (qty stepper, card buttons) */
[class*="st-key-row_"] [data-testid="stHorizontalBlock"] { flex-direction:row !important; flex-wrap:nowrap !important; gap:.5rem !important; align-items:center; }
[class*="st-key-row_"] [data-testid="stColumn"], [class*="st-key-row_"] [data-testid="column"] { min-width:0 !important; flex:1 1 0 !important; width:auto !important; }
[class*="st-key-qty_"] button { padding:0 !important; }
.qty-num { text-align:center; font-weight:800; font-size:1.2rem; color:var(--ink); }

/* ---------- Inputs ---------- */
.stApp [data-baseweb="input"], .stApp [data-baseweb="textarea"], .stApp [data-baseweb="select"] > div {
  background:var(--paper) !important; border-radius:12px !important; border:1.5px solid #cbbda8 !important;
}
.stApp [data-baseweb="input"]:focus-within, .stApp [data-baseweb="textarea"]:focus-within {
  border-color:var(--gold) !important; box-shadow:0 0 0 3px rgba(138,104,64,.18);
}
div[data-baseweb="tab-list"] { gap:1.2rem; border-bottom:1px solid var(--line); }
[data-testid="stMetric"] { background:var(--paper); border:1px solid var(--line); border-radius:14px; padding:.8rem 1rem; }
.stApp [data-testid="stMetricValue"] * { font-weight:800 !important; }

@media (max-width:700px) {
  .block-container { padding:.7rem .8rem 3rem; }
  .hero { padding:1.6rem 0 1rem; }
  .hero h1 { letter-spacing:-2px; font-size:3.4rem; }
  .hero p { font-size:1rem; }
  .hero-card { min-height:170px; }
  .product-img { height:190px; }
  .section-title { font-size:1.8rem; }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session state
# -----------------------------
NAV = ["Shop", "Collections", "Cart", "Sell With Us", "About", "Contact", "Admin"]
st.session_state.setdefault("cart", {})
st.session_state.setdefault("admin", None)
st.session_state.setdefault("admin_session", None)
st.session_state.setdefault("last_order", None)
st.session_state.setdefault("nav", "Shop")


# -----------------------------
# Supabase (one client per run; the admin login is restored each run)
# -----------------------------
def get_supabase():
    try:
        client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    except Exception:
        return None
    sess = st.session_state.admin_session
    if sess:
        try:
            res = client.auth.set_session(sess["access_token"], sess["refresh_token"])
            if res and res.session:
                st.session_state.admin_session = {
                    "access_token": res.session.access_token,
                    "refresh_token": res.session.refresh_token,
                }
                try:
                    client.postgrest.auth(res.session.access_token)
                except Exception:
                    pass
        except Exception:
            st.session_state.admin_session = None
            st.session_state.admin = None
    return client


supabase = get_supabase()

DEMO_PRODUCTS = [
    {"id": "demo1", "name": "Classic Linen Set", "description": "Breathable refined everyday wear.", "price": 8500, "category": "Clothes", "image_url": ""},
    {"id": "demo2", "name": "Signature Evening Dress", "description": "An elegant statement piece for special occasions.", "price": 12900, "category": "Clothes", "image_url": ""},
    {"id": "demo3", "name": "Minimal Ceramic Vase", "description": "A sculptural home accent with a quiet finish.", "price": 4200, "category": "Home", "image_url": ""},
    {"id": "demo4", "name": "Soft Luxe Cushion Set", "description": "Premium texture and everyday comfort.", "price": 3800, "category": "Home", "image_url": ""},
]


def esc(v):
    return html.escape(str(v if v is not None else ""))


def money(value):
    return f"Rs. {float(value):,.0f}"


def wa_number(phone):
    d = re.sub(r"\D", "", phone or "")
    if d.startswith("00"):
        d = d[2:]
    elif d.startswith("0"):
        d = "92" + d[1:]
    return d


def get_products(active_only=True):
    if not supabase:
        return DEMO_PRODUCTS
    try:
        q = supabase.table("products").select("*")
        if active_only:
            q = q.eq("active", True)
        return q.order("created_at", desc=True).execute().data or DEMO_PRODUCTS
    except Exception:
        return DEMO_PRODUCTS


# -----------------------------
# Cart actions (callbacks)
# -----------------------------
def go(page):
    st.session_state.nav = page


def add_to_cart(pid):
    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1
    st.session_state.last_order = None
    st.toast("Added to cart ✓")


def buy_now(pid):
    add_to_cart(pid)
    go("Cart")


def change_qty(pid, delta):
    q = st.session_state.cart.get(pid, 0) + delta
    if q <= 0:
        st.session_state.cart.pop(pid, None)
    else:
        st.session_state.cart[pid] = q


def remove_item(pid):
    st.session_state.cart.pop(pid, None)


def continue_shopping():
    st.session_state.last_order = None
    go("Shop")


def save_message(kind, name, contact, body):
    supabase.table("messages").insert(
        {"kind": kind, "name": name, "contact": contact, "message": body},
        returning=MINIMAL,
    ).execute()


# -----------------------------
# Header + navigation
# -----------------------------
cart_count = sum(st.session_state.cart.values())
top_left, top_right = st.columns([3, 2])
with top_left:
    st.markdown('<div class="brand">LuxeMart</div><div class="tagline">CURATED • ELEGANT • EVERYDAY</div>', unsafe_allow_html=True)
with top_right:
    st.button(f"🛍 Cart ({cart_count})", key="header_cart", on_click=go, args=("Cart",), use_container_width=True)

st.markdown('<div class="luxury-line"></div>', unsafe_allow_html=True)
page = st.radio("Navigation", NAV, horizontal=True, label_visibility="collapsed", key="nav")

# -----------------------------
# SHOP
# -----------------------------
if page == "Shop":
    st.markdown("""
    <section class="hero">
      <div class="kicker">Clothes &amp; home</div>
      <h1>Luxury finds<br>for your life.</h1>
      <p>Refined clothing and beautiful home products from independent sellers. Order in under a minute and pay when it arrives.</p>
    </section>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.15, .85])
    with left:
        st.button("View cart & checkout", type="primary", on_click=go, args=("Cart",), use_container_width=True, key="hero_cart")
    with right:
        st.markdown('<div class="hero-card"><span>LUXURY • CLOTHES • HOME</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="luxury-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Shop the collection</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([2, 1])
    with c1:
        search = st.text_input("Search", placeholder="Search products...", label_visibility="collapsed")
    with c2:
        category = st.selectbox("Category", ["All", "Clothes", "Home"], label_visibility="collapsed")

    products = [
        p for p in get_products()
        if (category == "All" or p.get("category") == category)
        and (not search or search.lower() in str(p.get("name", "")).lower() or search.lower() in str(p.get("description", "")).lower())
    ]

    if not products:
        st.info("No products found.")
    else:
        cols = st.columns(3)
        for i, p in enumerate(products):
            pid = str(p["id"])
            with cols[i % 3]:
                with st.container(border=True):
                    if p.get("image_url"):
                        st.image(p["image_url"], use_container_width=True)
                    else:
                        st.markdown('<div class="product-img">✦</div>', unsafe_allow_html=True)
                    st.markdown(
                        f'<div class="pill">{esc(p.get("category", "Collection"))}</div>'
                        f'<div class="product-name">{esc(p.get("name", "Product"))}</div>'
                        f'<div class="product-desc">{esc(p.get("description", ""))}</div>'
                        f'<div class="price">{money(p.get("price", 0))}</div>',
                        unsafe_allow_html=True,
                    )
                    with st.container(key=f"row_buy_{pid}"):
                        b1, b2 = st.columns(2)
                        b1.button("Add to cart", key=f"add_{pid}", on_click=add_to_cart, args=(pid,), use_container_width=True)
                        b2.button("Buy now", key=f"buy_{pid}", type="primary", on_click=buy_now, args=(pid,), use_container_width=True)

# -----------------------------
# CART + CHECKOUT (one page)
# -----------------------------
elif page == "Cart":
    st.markdown('<div class="section-title">Your bag</div>', unsafe_allow_html=True)

    order_done = st.session_state.last_order
    pmap = {str(p["id"]): p for p in get_products()}
    rows, subtotal = [], 0.0
    for pid, qty in list(st.session_state.cart.items()):
        if pid in pmap:
            p = pmap[pid]
            line = float(p["price"]) * qty
            subtotal += line
            rows.append((pid, p, qty, line))
        else:
            st.session_state.cart.pop(pid, None)

    if order_done and not rows:
        wa_text = (
            f"Hello LuxeMart, I placed order #{order_done['ref']}.\n"
            f"Name: {order_done['name']}\n"
            + "\n".join(f"- {q} x {n}" for n, q in order_done["items"])
            + f"\nTotal: {money(order_done['total'])} (cash on delivery)"
        )
        st.markdown(
            f'<div class="done-card"><div class="kicker">Order received</div>'
            f'<h2>Thank you, {esc(order_done["name"])}!</h2>'
            f'<p>Your order number is <b>#{esc(order_done["ref"])}</b>. We will call or WhatsApp you on '
            f'<b>{esc(order_done["phone"])}</b> to confirm delivery.</p>'
            f'<p>Total to pay on delivery: <b>{money(order_done["total"])}</b></p></div>',
            unsafe_allow_html=True,
        )
        st.write("")
        st.link_button("Send order on WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(wa_text)}", type="primary", use_container_width=True)
        st.button("Continue shopping", on_click=continue_shopping, use_container_width=True, key="done_continue")

    elif not rows:
        st.info("Your bag is empty.")
        st.button("Start shopping", type="primary", on_click=continue_shopping, use_container_width=True, key="empty_continue")

    else:
        for pid, p, qty, line in rows:
            with st.container(border=True):
                st.markdown(
                    f'<div class="line-name">{esc(p["name"])}</div>'
                    f'<div class="line-sub">{money(p["price"])} each · <b>{money(line)}</b></div>',
                    unsafe_allow_html=True,
                )
                with st.container(key=f"row_qty_{pid}"):
                    a, b, c, d = st.columns([1, 1, 1, 2])
                    a.button("−", key=f"minus_{pid}", on_click=change_qty, args=(pid, -1), use_container_width=True)
                    b.markdown(f'<div class="qty-num">{qty}</div>', unsafe_allow_html=True)
                    c.button("+", key=f"plus_{pid}", on_click=change_qty, args=(pid, 1), use_container_width=True)
                    d.button("Remove", key=f"rm_{pid}", on_click=remove_item, args=(pid,), use_container_width=True)

        total = subtotal + DELIVERY_FEE
        delivery_label = "Free" if DELIVERY_FEE == 0 else money(DELIVERY_FEE)
        st.markdown(
            f'<div class="sum-row"><span>Subtotal</span><span>{money(subtotal)}</span></div>'
            f'<div class="sum-row"><span>Delivery</span><span>{delivery_label}</span></div>'
            f'<div class="sum-total"><span>Total</span><span>{money(total)}</span></div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div class="section-title" style="margin-top:1.6rem;">Delivery details</div>', unsafe_allow_html=True)
        st.markdown('<div class="cod-note">💵 Pay cash when your order arrives. No card needed.</div>', unsafe_allow_html=True)

        with st.form("checkout"):
            name = st.text_input("Full name", placeholder="Your name", autocomplete="name")
            phone = st.text_input("Phone / WhatsApp", placeholder="03XX XXXXXXX", autocomplete="tel")
            address = st.text_area("Delivery address", placeholder="House, street, area, city", height=100)
            notes = st.text_input("Note for us (optional)", placeholder="Size, colour, delivery time...")
            submit = st.form_submit_button(f"Place order · {money(total)}", type="primary", use_container_width=True)

        if submit:
            digits = re.sub(r"\D", "", phone or "")
            if len(name.strip()) < 2:
                st.error("Please enter your name.")
            elif len(digits) < 10:
                st.error("Please enter a valid phone number (at least 10 digits).")
            elif len(
