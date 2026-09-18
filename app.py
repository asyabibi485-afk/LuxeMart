import streamlit as st
from supabase import create_client

st.set_page_config(page_title="LuxeMart", page_icon="🛍️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap');
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
.brand{font-family:'Playfair Display',serif;font-size:2.6rem;font-weight:700}
.hero{padding:35px 0}.hero h1{font-family:'Playfair Display',serif;font-size:clamp(3rem,8vw,6rem);line-height:.95}
.price{font-weight:700;font-size:1.15rem}
</style>
""", unsafe_allow_html=True)

def sb():
    try:
        return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    except Exception:
        return None

supabase = sb()
if "cart" not in st.session_state: st.session_state.cart = {}
if "admin" not in st.session_state: st.session_state.admin = None

demo = [
 {"id":"demo1","name":"Classic Linen Set","description":"Breathable refined everyday wear.","price":8500,"category":"Clothes","image_url":""},
 {"id":"demo2","name":"Signature Evening Dress","description":"Elegant statement piece.","price":12900,"category":"Clothes","image_url":""},
 {"id":"demo3","name":"Minimal Ceramic Vase","description":"Modern decorative home accent.","price":4200,"category":"Home","image_url":""},
 {"id":"demo4","name":"Soft Luxe Cushion Set","description":"Premium finish and comfort.","price":3800,"category":"Home","image_url":""},
]

def products():
    if not supabase: return demo
    try:
        r=supabase.table("products").select("*").eq("active",True).order("created_at",desc=True).execute()
        return r.data or demo
    except Exception: return demo

def rs(v): return f"Rs. {float(v):,.0f}"

st.markdown('<div class="brand">LuxeMart</div>', unsafe_allow_html=True)
st.caption("Luxury clothes • Home products • Independent sellers")
page=st.radio("Menu",["Shop","Sell With Us","About","Contact","Admin"],horizontal=True,label_visibility="collapsed")
st.divider()

if page=="Shop":
    st.markdown('<div class="hero"><div>CURATED • ELEGANT • EVERYDAY</div><h1>Luxury finds<br>for your life.</h1><p>Discover refined clothing and beautiful home products from independent sellers.</p></div>',unsafe_allow_html=True)
    a,b=st.columns([2,1])
    with a: search=st.text_input("Search",placeholder="Search products...")
    with b: cat=st.selectbox("Category",["All","Clothes","Home"])
    ps=[p for p in products() if (cat=="All" or p.get("category")==cat) and (not search or search.lower() in str(p.get("name","")).lower())]
    cols=st.columns(3)
    for i,p in enumerate(ps):
        with cols[i%3]:
            if p.get("image_url"): st.image(p["image_url"],use_container_width=True)
            else: st.markdown('<div style="height:200px;background:linear-gradient(135deg,#eee5d6,#cfc3b0);border-radius:15px;display:flex;align-items:center;justify-content:center;font-size:45px">✦</div>',unsafe_allow_html=True)
            st.subheader(p.get("name","Product"))
            st.caption(p.get("description",""))
            st.markdown(f'<span class="price">{rs(p.get("price",0))}</span>',unsafe_allow_html=True)
            if st.button("Add to cart",key="add"+str(p["id"]),use_container_width=True):
                pid=str(p["id"]); st.session_state.cart[pid]=st.session_state.cart.get(pid,0)+1; st.success("Added.")
    st.divider(); st.subheader("Cart")
    pmap={str(p["id"]):p for p in products()}; total=0; rows=[]
    for pid,q in st.session_state.cart.items():
        if pid in pmap:
            p=pmap[pid]; line=float(p["price"])*q; total+=line; rows.append((pid,p,q,line))
    if not rows: st.info("Your cart is empty.")
    else:
        for pid,p,q,line in rows:
            st.write(f"**{p['name']}** × {q} — {rs(line)}")
        st.subheader(f"Total: {rs(total)}")
        with st.expander("Checkout"):
            name=st.text_input("Full name"); phone=st.text_input("Phone / WhatsApp"); address=st.text_area("Delivery address"); notes=st.text_area("Notes")
            if st.button("Place order",type="primary"):
                if not name or not phone or not address: st.error("Enter name, phone and address.")
                elif not supabase: st.error("Connect Supabase in Streamlit Secrets first.")
                else:
                    try:
                        o=supabase.table("orders").insert({"customer_name":name,"phone":phone,"address":address,"notes":notes,"total":total,"status":"pending"}).execute()
                        oid=o.data[0]["id"]
                        items=[{"order_id":oid,"product_id":None if pid.startswith("demo") else pid,"product_name":p["name"],"quantity":q,"unit_price":p["price"]} for pid,p,q,line in rows]
                        supabase.table("order_items").insert(items).execute()
                        st.session_state.cart={}; st.success(f"Order placed. Order ID: {oid}")
                    except Exception as e: st.error(str(e))

elif page=="Sell With Us":
    st.header("Sell With Us")
    st.write("Contact LuxeMart to list approved clothing and home products.")
    st.text_input("Name"); st.text_input("Phone / WhatsApp"); st.text_area("Product details")
    st.button("Send seller request")

elif page=="About":
    st.header("About LuxeMart")
    st.write("LuxeMart is a marketplace for refined clothing and home products. Customers can shop and place orders, while the admin can manage products and order status.")

elif page=="Contact":
    st.header("Contact")
    st.write("Add your business phone, WhatsApp and email here.")

else:
    st.header("Admin Dashboard")
    if not supabase:
        st.error("Supabase is not connected. Add SUPABASE_URL and SUPABASE_KEY in Streamlit Secrets.")
    elif not st.session_state.admin:
        email=st.text_input("Admin email"); password=st.text_input("Admin password",type="password")
        if st.button("Login",type="primary"):
            try:
                r=supabase.auth.sign_in_with_password({"email":email,"password":password})
                if r.user: st.session_state.admin=r.user; st.rerun()
                else: st.error("Login failed.")
            except Exception as e: st.error(f"Login failed: {e}")
    else:
        st.success("Admin logged in")
        if st.button("Logout"):
            supabase.auth.sign_out(); st.session_state.admin=None; st.rerun()
        t1,t2,t3=st.tabs(["Products","Orders","Add Product"])
        with t1:
            try:
                data=supabase.table("products").select("*").order("created_at",desc=True).execute().data or []
                for p in data:
                    x,y=st.columns([5,1]); x.write(f"**{p['name']}** — {p['category']} — {rs(p['price'])}")
                    if y.button("Delete",key="d"+str(p["id"])):
                        supabase.table("products").delete().eq("id",p["id"]).execute(); st.rerun()
            except Exception as e: st.error(str(e))
        with t2:
            try:
                orders=supabase.table("orders").select("*").order("created_at",desc=True).execute().data or []
                for o in orders:
                    with st.expander(f"{o['customer_name']} — {rs(o['total'])} — {o['status']}"):
                        st.write("Phone:",o["phone"]); st.write("Address:",o["address"]); st.write("Notes:",o.get("notes") or "-")
                        statuses=["pending","confirmed","shipped","delivered","cancelled"]
                        ns=st.selectbox("Status",statuses,index=statuses.index(o.get("status","pending")),key="s"+str(o["id"]))
                        if st.button("Update",key="u"+str(o["id"])):
                            supabase.table("orders").update({"status":ns}).eq("id",o["id"]).execute(); st.rerun()
            except Exception as e: st.error(str(e))
        with t3:
            n=st.text_input("Product name"); d=st.text_area("Description"); pr=st.number_input("Price (PKR)",min_value=0.0); c=st.selectbox("Category",["Clothes","Home"]); img=st.text_input("Image URL"); active=st.checkbox("Active",True)
            if st.button("Add product",type="primary"):
                try:
                    supabase.table("products").insert({"name":n,"description":d,"price":pr,"category":c,"image_url":img,"active":active}).execute(); st.success("Added."); st.rerun()
                except Exception as e: st.error(str(e))
