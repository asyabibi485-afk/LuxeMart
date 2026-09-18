import streamlit as st
from supabase import create_client, Client

# 1. Initialize Supabase Connection
# (Make sure these are added securely to your GitHub Secrets / Streamlit Secrets)
URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(URL, KEY)

# 2. Inject Trending Minimalist CSS Styles
st.markdown("""
    <style>
    /* Card design for clothing items */
    .cloth-card {
        background-color: #F8F9FA;
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        text-align: center;
    }
    .cloth-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 16px;
        font-weight: 600;
        color: #111111;
        margin-top: 8px;
    }
    .cloth-price {
        color: #555555;
        font-weight: 500;
        font-size: 14px;
    }
    /* Rounded retail buttons */
    div.stButton > button:first-child {
        background-color: #000000;
        color: #ffffff;
        border-radius: 20px;
        border: none;
        padding: 6px 18px;
        font-size: 13px;
        font-weight: 600;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #222222;
    }
    </style>
""", unsafe_allowed_html=True)

st.title("🛍️ Modern Collection")

# 3. Fetch Data from Supabase
try:
    response = supabase.table("clothing_products").select("*").execute()
    products = response.data
except Exception as e:
    st.error(f"Error connecting to database: {e}")
    products = []

# 4. Display Items in a 3-Column Modern Grid
if products:
    # Create 3 columns for a balanced look
    cols = st.columns(3)
    
    for i, item in enumerate(products):
        # Cycle through columns (0, 1, 2)
        with cols[i % 3]:
            # Create a visual container wrapper
            with st.container():
                # Display Product Image
                if item.get("image_url"):
                    st.image(item["image_url"], use_container_width=True)
                else:
                    st.image("https://placeholder.com", use_container_width=True)
                
                # Title and Price with custom styled markdown
                st.markdown(f'<div class="cloth-title">{item["title"]}</div>', unsafe_allowed_html=True)
                st.markdown(f'<div class="cloth-price">PKR {item["price"]:,}</div>', unsafe_allowed_html=True)
                
                # Interactive CTA Button
                if st.button("View Details", key=f"btn_{item['id']}"):
                    st.toast(f"Opening details for {item['title']}...")
else:
    st.info("No clothing items found in your database. Add some rows to get started!")
