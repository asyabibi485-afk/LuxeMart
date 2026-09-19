import streamlit as st
from supabase import create_client


# ============================================================
# LUXEMART
# ============================================================

APP_NAME = "LuxeMart"
TAGLINE = "LUXURY • STYLE • ELEGANCE"

st.set_page_config(
    page_title="LuxeMart",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SUPABASE
# ============================================================

try:
    SUPABASE_URL = st.secrets["supabase"]["url"]
    SUPABASE_KEY = st.secrets["supabase"]["key"]
    ADMIN_EMAIL = st.secrets["admin"]["email"]

    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

except Exception as e:
    st.error("Supabase configuration could not be loaded.")
    st.code(str(e))
    st.stop()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Shop"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "product_page" not in st.session_state:
    st.session_state.product_page = 1

if "search" not in st.session_state:
    st.session_state.search = ""

if "category" not in st.session_state:
    st.session_state.category = "All"


# ============================================================
# IMAGE SOURCES
# ============================================================

CLOTHES_IMAGE = (
    "https://images.pexels.com/photos/"
    "994523/pexels-photo-994523.jpeg"
)

CLOTHES_IMAGE_2 = (
    "https://images.pexels.com/photos/"
    "996329/pexels-photo-996329.jpeg"
)

ABAYA_IMAGE = (
    "https://images.pexels.com/photos/"
    "13791265/pexels-photo-13791265.jpeg"
)

JEWELLERY_IMAGE = (
    "https://images.pexels.com/photos/"
    "1191531/pexels-photo-1191531.jpeg"
)

BRACELET_IMAGE = (
    "https://images.pexels.com/photos/"
    "1927259/pexels-photo-1927259.jpeg"
)

BAG_IMAGE = (
    "https://images.pexels.com/photos/"
    "1152077/pexels-photo-1152077.jpeg"
)

WATCH_IMAGE = (
    "https://images.pexels.com/photos/"
    "190819/pexels-photo-190819.jpeg"
)

PERFUME_IMAGE = (
    "https://images.pexels.com/photos/"
    "965989/pexels-photo-965989.jpeg"
)

PERFUME_IMAGE_2 = (
    "https://images.pexels.com/photos/"
    "1961795/pexels-photo-1961795.jpeg"
)

BEAUTY_IMAGE = (
    "https://images.pexels.com/photos/"
    "2113855/pexels-photo-2113855.jpeg"
)

KIDS_IMAGE = (
    "https://images.pexels.com/photos/"
    "167964/pexels-photo-167964.jpeg"
)


# ============================================================
# PRODUCT DATABASE
# ============================================================

PRODUCTS = []


def add_product(
    product_id,
    name,
    category,
    price,
    source_url,
    image,
    badge=""
):
    PRODUCTS.append(
        {
            "id": product_id,
            "name": name,
            "category": category,
            "price": float(price),
            "source_url": source_url,
            "image": image,
            "badge": badge,
        }
    )


# ============================================================
# SOURCE LINKS
# ============================================================

NAQSHI_URL = (
    "https://www.naqshiofficial.com/collections/casual-pret"
)

HIJAB_URL = (
    "https://thehijabcompany.pk/products/nawal-abaya-copy"
)

NECKLACE_URL = (
    "https://meerzah.pk/products/"
    "fancy-design-crystal-stones-gold-plated-necklace-set-for-girls-women"
)

BAG_URL = (
    "https://bagstore.pk/product/elegance-hand-bag-for-women-bs007/"
)

VIOLET_BAG_URL = (
    "https://discountstore.pk/products/"
    "womens-purses-and-handbags-shoulder-bags-ladies-designer-"
    "top-handle-satchel-tote-bag-violet"
)

BRACELET_URL = (
    "https://meerzah.pk/products/"
    "luminous-design-gold-plated-crystal-stones-tulip-bracelet-for-girls-women"
)

BRACELET_SET_URL = (
    "https://abwholesale.pk/products/"
    "uni-10608-classy-diamond-silver-chain-bracelet-set-of-4"
)

WATCH_URL = (
    "https://voguealaska.pk/products/"
    "j-co-inspired-premium-quality-mens-watch"
)

STYLO_URL = (
    "https://stylo.pk/collections/watches"
)

CHASE_PERFUME_URL = (
    "https://chasevalue.pk/products/"
    "valuables-perfume-men-50ml-blue-water-valuable-a20519603"
)

BLUE_EDP_URL = (
    "https://aromaconcepts.pk/products/the-blue-edp"
)


# ============================================================
# NAQSHI PRODUCTS
# ============================================================

NAQSHI_PRODUCTS = [

    ("Cecily", 13990),
    ("Easten", 13990),
    ("Gunash", 13990),
    ("Liam", 12990),
    ("Louisa", 13990),
    ("Maddox", 12990),
    ("Willow", 12990),
    ("Mabel", 9030),
    ("Riedel", 6993),
    ("Isla", 7693),
    ("Fiona", 7693),
    ("Juni", 9093),
    ("Lona", 7693),
    ("Ophelia", 6999),
    ("Deniz", 7980),
    ("Faye", 7693),
    ("Vera", 8393),
    ("Kashmeera", 15393),
    ("Izna", 15393),
    ("Andalib", 9093),
    ("Anasia", 15393),
    ("Seraya", 16093),
    ("Farnood", 16093),
    ("Shabeera", 15393),
    ("Tasveeb", 16093),
    ("Jaizah", 10493),
    ("Fizba", 9093),
    ("Baseera", 10493),
    ("Zimra", 9093),
    ("Menesa", 10493),
    ("Duraan", 7693),
    ("Umeed", 8393),
    ("Nagma", 9093),
    ("Piper", 6293),

    # KEEP MARY NAME EXACTLY
    ("Mary", 7693),

    ("Melia", 7693),
    ("Hoorish", 8393),
    ("Ordhni", 7693),
    ("Ruhab", 6993),
    ("Rubab", 6993),
    ("Areeb", 9793),
    ("Umaiza", 12990),
    ("Isma", 6993),
    ("Arunika", 10493),
    ("Alvin", 7693),
    ("Kiswa", 8043),
    ("Kinara", 10990),
    ("Parwaaz", 7693),
    ("Zimda", 8043),
    ("Shahtaaj", 15992),
    ("Shagufta", 15992),
    ("Noor Jahaan", 15992),
    ("Anjuman", 15192),
    ("Rukhsaar", 13192),
    ("Abeera", 10493),
]


product_id = 1

for name, price in NAQSHI_PRODUCTS:

    image = (
        CLOTHES_IMAGE
        if product_id % 2
        else CLOTHES_IMAGE_2
    )

    badge = "SALE" if price < 10000 else ""

    add_product(
        product_id,
        name,
        "Clothes",
        price,
        NAQSHI_URL,
        image,
        badge
    )

    product_id += 1


# ============================================================
# EXACT PRODUCTS FROM PROVIDED LINKS
# ============================================================

EXACT_PRODUCTS = [

    {
        "name": "Nawal Abaya",
        "category": "Abaya",
        "price": 6490,
        "url": HIJAB_URL,
        "image": ABAYA_IMAGE,
        "badge": "NEW",
    },

    {
        "name": (
            "Fancy Design Crystal Stones Gold Plated "
            "Necklace Set for Girls/Women"
        ),
        "category": "Jewellery",
        "price": 3000,
        "url": NECKLACE_URL,
        "image": JEWELLERY_IMAGE,
        "badge": "",
    },

    {
        "name": "Elegance hand bag for women – BS007",
        "category": "Bags",
        "price": 3700,
        "url": BAG_URL,
        "image": BAG_IMAGE,
        "badge": "",
    },

    {
        "name": (
            "Womens Purses and Handbags Shoulder Bags "
            "Ladies Designer Top Handle Satchel Tote Bag - Violet"
        ),
        "category": "Bags",
        "price": 22806,
        "url": VIOLET_BAG_URL,
        "image": BAG_IMAGE,
        "badge": "SALE",
    },

    {
        "name": (
            "Luminous Design Gold Plated Crystal Stones "
            "Tulip Bracelet for Girls/Women"
        ),
        "category": "Jewellery",
        "price": 1150,
        "url": BRACELET_URL,
        "image": BRACELET_IMAGE,
        "badge": "",
    },

    {
        "name": (
            "UNI-10608 - Classy Diamond & Silver Chain "
            "- Bracelet Set of 4"
        ),
        "category": "Jewellery",
        "price": 599,
        "url": BRACELET_SET_URL,
        "image": JEWELLERY_IMAGE,
        "badge": "SALE",
    },

    {
        "name": "J. Co Inspired Premium Quality Men's Watch",
        "category": "Watches",
        "price": 7400,
        "url": WATCH_URL,
        "image": WATCH_IMAGE,
        "badge": "",
    },

    {
        "name": "Two Tone Gents Watch J34033",
        "category": "Watches",
        "price": 2940,
        "url": STYLO_URL,
        "image": WATCH_IMAGE,
        "badge": "SALE",
    },

    {
        "name": "Valuables Perfume for Men – 50ml (Blue Water)",
        "category": "Perfume",
        "price": 699,
        "url": CHASE_PERFUME_URL,
        "image": PERFUME_IMAGE,
        "badge": "",
    },

    {
        "name": "THE BLUE EDP",
        "category": "Perfume",
        "price": 4500,
        "url": BLUE_EDP_URL,
        "image": PERFUME_IMAGE_2,
        "badge": "",
    },

    {
        "name": "Premium Makeup Set",
        "category": "Beauty",
        "price": 4499,
        "url": "https://www.pexels.com/",
        "image": BEAUTY_IMAGE,
        "badge": "",
    },
]


for item in EXACT_PRODUCTS:

    add_product(
        product_id,
        item["name"],
        item["category"],
        item["price"],
        item["url"],
        item["image"],
        item["badge"]
    )

    product_id += 1


# ============================================================
# STYLO WATCHES
# ============================================================

STYLO_PRODUCTS = [

    ("Brown Gents Watch J34034", 4410),
    ("Golden Gents Watch J34102", 4140),
    ("Silver Gents Watch J34102", 4140),
    ("Two Tone Gents Watch J34102", 4140),
    ("Golden Gents Watch J34105", 4140),
    ("Golden Gents Watch J34107", 4140),
    ("Two Tone Gents Watch J34107", 4140),
    ("Silver Gents Watch J34109", 4490),
    ("Golden Gents Watch J34101", 4740),
    ("Silver Gents Watch J34101", 4740),
    ("Silver Gents Watch J34103", 4740),
    ("Two Tone Gents Watch J34103", 4740),
    ("Kids Ferozy Watch J20013", 470),
    ("Kids Pink Watch J20013", 470),
    ("Kids Jamani Watch J20013", 470),
]


for name, price in STYLO_PRODUCTS:

    if name.startswith("Kids"):

        category = "Kids"
        image = KIDS_IMAGE

    else:

        category = "Watches"
        image = WATCH_IMAGE

    add_product(
        product_id,
        name,
        category,
        price,
        STYLO_URL,
        image,
        "SALE"
    )

    product_id += 1


# ============================================================
# EXTRA PRODUCTS
# Ensures 20 pages x 4 products = 80 products
# ============================================================

EXTRA_PRODUCTS = [

    (
        "Luxury Rose Perfume",
        "Perfume",
        2999,
        PERFUME_IMAGE
    ),

    (
        "Royal Oud Perfume",
        "Perfume",
        4499,
        PERFUME_IMAGE_2
    ),

    (
        "Vanilla Dream Perfume",
        "Perfume",
        2799,
        PERFUME_IMAGE
    ),

    (
        "Classic Luxury Sunglasses",
        "Accessories",
        2999,
        "https://images.pexels.com/photos/"
        "46710/pexels-photo-46710.jpeg"
    ),

    (
        "Elegant Fashion Handbag",
        "Bags",
        5499,
        BAG_IMAGE
    ),

    (
        "Classic Pearl Necklace",
        "Jewellery",
        3499,
        JEWELLERY_IMAGE
    ),

    (
        "Elegant Crystal Bracelet",
        "Jewellery",
        2499,
        BRACELET_IMAGE
    ),

    (
        "Premium Beauty Collection",
        "Beauty",
        4499,
        BEAUTY_IMAGE
    ),

    (
        "Luxury Evening Dress",
        "Clothes",
        5999,
        CLOTHES_IMAGE
    ),

    (
        "Classic Casual Kurti",
        "Clothes",
        2499,
        CLOTHES_IMAGE_2
    ),

]


for name, category, price, image in EXTRA_PRODUCTS:

    add_product(
        product_id,
        name,
        category,
        price,
        "https://www.pexels.com/",
        image,
        ""
    )

    product_id += 1


# ============================================================
# 20 PAGE SETTINGS
# ============================================================

PRODUCTS_PER_PAGE = 4
TOTAL_PAGES = 20


# ============================================================
# CATEGORIES
# ============================================================

CATEGORIES = [
    "All",
    "Clothes",
    "Abaya",
    "Jewellery",
    "Bags",
    "Watches",
    "Perfume",
    "Beauty",
    "Kids",
    "Accessories",
]


# ============================================================
# FUNCTIONS
# ============================================================

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

    st.session_state.cart.append(
        product_id
    )

    st.toast(
        "Added to cart 🛒"
    )


def toggle_favorite(product_id):

    if product_id in st.session_state.favorites:

        st.session_state.favorites.remove(
            product_id
        )

        st.toast(
            "Removed from favorites"
        )

    else:

        st.session_state.favorites.append(
            product_id
        )

        st.toast(
            "Added to favorites ❤️"
        )


def safe_image(url):

    try:

        st.image(
            url,
            use_container_width=True
        )

    except Exception:

        st.info(
            "Product image unavailable."
        )


def logout_admin():

    try:

        supabase.auth.sign_out()

    except Exception:

        pass

    st.session_state.admin_logged_in = False
    st.session_state.page = "Shop"

    st.rerun()


# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at top left,
            #fff4fa 0%,
            transparent 34%
        ),
        radial-gradient(
            circle at top right,
            #f1e8ff 0%,
            transparent 34%
        ),
        linear-gradient(
            135deg,
            #fffaff 0%,
            #f8f4ff 48%,
            #eef8ff 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}

h1,
h2,
h3,
h4 {
    color: #16121b !important;
    font-weight: 850 !important;
}

p,
label,
li {
    color: #17151c !important;
}

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #fbf0ff 0%,
            #f0f6ff 100%
        );
    border-right: 1px solid #e3d7ed;
}

[data-testid="stSidebar"] h1 {
    color: #722c91 !important;
}

.stButton > button {
    background: white !important;
    color: #15121a !important;
    border: 1px solid #dac9e7 !important;
    border-radius: 14px !important;
    min-height: 42px !important;
    font-weight: 750 !important;
}

.stButton > button:hover {
    background: #f5eaff !important;
    border-color: #a66bc9 !important;
}

.stLinkButton > a {
    border-radius: 14px !important;
    font-weight: 750 !important;
}

[data-testid="stTextInput"] input {
    background: white !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #dac9e7 !important;
    border-radius: 12px !important;
}

[data-testid="stTextArea"] textarea {
    background: white !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    border: 1px solid #dac9e7 !important;
    border-radius: 12px !important;
}

[data-baseweb="select"] > div {
    background: white !important;
    color: #000000 !important;
    border-radius: 12px !important;
    border: 1px solid #dac9e7 !important;
}

[data-baseweb="select"] * {
    color: #000000 !important;
}

[data-testid="stSlider"] {
    color: #722c91 !important;
}

.product-card {
    background: white;
    border: 1px solid #eee5f5;
    border-radius: 22px;
    padding: 12px;
    margin-bottom: 22px;
    box-shadow:
        0 8px 25px
        rgba(68, 38, 91, 0.07);
}

.hero-box {
    background:
        linear-gradient(
            135deg,
            #f8e9ff,
            #edf4ff
        );
    border: 1px solid #e4d5ef;
    border-radius: 26px;
    padding: 30px;
    margin-bottom: 25px;
}

.price-text {
    font-size: 21px;
    font-weight: 850;
    color: #6e2a91;
}

.badge-text {
    font-weight: 800;
    color: #9a276a;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title(
        "🛍️ LuxeMart"
    )

    st.caption(
        TAGLINE
    )

    st.divider()

    st.subheader(
        "Navigation"
    )

    if st.button(
        "🏠 SHOP",
        use_container_width=True,
        key="nav_shop"
    ):

        go_to("Shop")

    if st.button(
        f"❤️ FAVORITES ({len(st.session_state.favorites)})",
        use_container_width=True,
        key="nav_favorites"
    ):

        go_to("Favorites")

    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        use_container_width=True,
        key="nav_cart"
    ):

        go_to("Cart")

    if st.button(
        "ℹ️ ABOUT",
        use_container_width=True,
        key="nav_about"
    ):

        go_to("About")

    if st.button(
        "📞 CONTACT",
        use_container_width=True,
        key="nav_contact"
    ):

        go_to("Contact")

    if st.button(
        "🔐 ADMIN",
        use_container_width=True,
        key="nav_admin"
    ):

        go_to("Admin")

    st.divider()

    st.subheader(
        "Categories"
    )

    for category in CATEGORIES:

        if st.button(
            category,
            use_container_width=True,
            key=f"category_{category}"
        ):

            st.session_state.category = category
            st.session_state.product_page = 1
            st.session_state.page = "Shop"

            st.rerun()

    st.divider()

    st.caption(
        f"🛍️ {len(PRODUCTS)} Products"
    )

    st.caption(
        "📚 20 Collection Pages"
    )

# ============================================================
# TOP HEADER
# ============================================================

header_left, header_middle, header_right = st.columns(
    [4, 4, 2]
)

with header_left:

    st.markdown(
        "## 🛍️ LuxeMart"
    )

    st.caption(
        "Luxury fashion, beauty and lifestyle."
    )

with header_middle:

    search_top = st.text_input(
        "Search",
        value=st.session_state.search,
        placeholder="Search products...",
        label_visibility="collapsed",
        key="top_search"
    )

    if search_top != st.session_state.search:

        st.session_state.search = search_top
        st.session_state.product_page = 1

with header_right:

    if st.button(
        f"🛒 CART ({len(st.session_state.cart)})",
        use_container_width=True,
        key="header_cart"
    ):

        go_to("Cart")

st.divider()

# ============================================================
# SHOP
# ============================================================

if st.session_state.page == "Shop":

    st.markdown(
        '<div class="hero-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        "### ✨ Discover Your Luxury"
    )

    st.write(
        "Fashion, abayas, jewellery, bags, watches, "
        "perfumes and beauty essentials."
    )

    st.write(
        "Explore the LuxeMart collection with easy "
        "search, filters, favorites and shopping cart."
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    hero_left, hero_right = st.columns(
        [1.4, 1]
    )

    with hero_left:

        st.subheader(
            "✨ Premium Collection"
        )

        st.write(
            "Discover products for everyday style "
            "and special occasions."
        )

        m1, m2, m3 = st.columns(3)

        with m1:

            st.metric(
                "Products",
                len(PRODUCTS)
            )

        with m2:

            st.metric(
                "Pages",
                TOTAL_PAGES
            )

        with m3:

            st.metric(
                "Categories",
                len(CATEGORIES) - 1
            )

    with hero_right:

        safe_image(
            ABAYA_IMAGE
        )

    st.divider()

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
            placeholder="Search by name or category...",
            key="shop_search"
        )

        if search != st.session_state.search:

            st.session_state.search = search
            st.session_state.product_page = 1

    with category_col:

        category = st.selectbox(
            "Category",
            CATEGORIES,
            index=CATEGORIES.index(
                st.session_state.category
            ),
            key="shop_category"
        )

        if category != st.session_state.category:

            st.session_state.category = category
            st.session_state.product_page = 1

    with sort_col:

        sort_option = st.selectbox(
            "Sort",
            [
                "Featured",
                "Price: Low to High",
                "Price: High to Low",
                "Name: A-Z"
            ],
            key="shop_sort"
        )

    max_price = st.slider(
        "Maximum Price",
        min_value=500,
        max_value=30000,
        value=30000,
        step=500
    )
# ========================================================
    # FILTER
    # ========================================================

    filtered = []

    for product in PRODUCTS:

        if category != "All":

            if product["category"] != category:
                continue

        if search.strip():

            search_text = (
                product["name"]
                + " "
                + product["category"]
            ).lower()

            if search.lower() not in search_text:
                continue

        if product["price"] > max_price:
            continue

        filtered.append(product)

   # ========================================================
    # SORT
    # ========================================================

    if sort_option == "Price: Low to High":

        filtered.sort(
            key=lambda x: x["price"]
        )

    elif sort_option == "Price: High to Low":

        filtered.sort(
            key=lambda x: x["price"],
            reverse=True
        )

    elif sort_option == "Name: A-Z":

        filtered.sort(
            key=lambda x: x["name"].lower()
        )

    st.caption(
        f"{len(filtered)} product(s) found"
    )
# ========================================================
    # PRODUCT DISPLAY
    # ========================================================

    if not filtered:

        st.warning(
            "No products found. Try another search."
        )

    else:

        total_pages = (
            len(filtered)
            + PRODUCTS_PER_PAGE
            - 1
        ) // PRODUCTS_PER_PAGE

        if total_pages > TOTAL_PAGES:
            total_pages = TOTAL_PAGES

        if st.session_state.product_page > total_pages:

            st.session_state.product_page = total_pages

        if st.session_state.product_page < 1:

            st.session_state.product_page = 1

        current_page = st.session_state.product_page

        start = (
            current_page - 1
        ) * PRODUCTS_PER_PAGE

        end = start + PRODUCTS_PER_PAGE

        current_products = filtered[start:end]

        columns = st.columns(4)

        for index, product in enumerate(
            current_products
        ):

            with columns[index]:

                st.markdown(
                    '<div class="product-card">',
                    unsafe_allow_html=True
                )

                safe_image(
                    product["image"]
                )

                if product["badge"]:

                    st.markdown(
                        f'<p class="badge-text">'
                        f'🔥 {product["badge"]}'
                        f'</p>',
                        unsafe_allow_html=True
                    )

                st.subheader(
                    product["name"]
                )

                st.caption(
                    product["category"]
                )

                st.markdown(
                    f'<p class="price-text">'
                    f'{money(product["price"])}'
                    f'</p>',
                    unsafe_allow_html=True
                )

                if product["id"] in st.session_state.favorites:

                    favorite_label = (
                        "❤️ FAVORITE"
                    )

                else:

                    favorite_label = (
                        "♡ FAVORITE"
                    )

                if st.button(
                    favorite_label,
                    key=f"fav_{product['id']}",
                    use_container_width=True
                ):

                    toggle_favorite(
                        product["id"]
                    )

                    st.rerun()

                if st.button(
                    "🛒 ADD TO CART",
                    key=f"add_{product['id']}",
                    use_container_width=True
                ):

                    add_to_cart(
                        product["id"]
                    )

                    st.rerun()

                st.link_button(
                    "🔗 VIEW SOURCE PRODUCT",
                    product["source_url"],
                    use_container_width=True
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

        st.divider()
# ====================================================
        # PAGE NAVIGATION
        # ====================================================

        st.subheader(
            "📚 Collection Pages"
        )

        st.caption(
            f"Page {current_page} of {total_pages}"
        )

        # First 10 pages
        first_pages = list(
            range(
                1,
                min(10, total_pages) + 1
            )
        )

        if first_pages:

            page_cols = st.columns(
                len(first_pages)
            )

            for i, page_number in enumerate(
                first_pages
            ):

                with page_cols[i]:

                    label = (
                        f"📍 {page_number}"
                        if page_number == current_page
                        else str(page_number)
                    )

                    if st.button(
                        label,
                        key=f"page_a_{page_number}",
                        use_container_width=True
                    ):

                        st.session_state.product_page = (
                            page_number
                        )

                        st.rerun()

        # Second 10 pages
        if total_pages > 10:

            second_pages = list(
                range(
                    11,
                    total_pages + 1
                )
            )

            page_cols = st.columns(
                len(second_pages)
            )

            for i, page_number in enumerate(
                second_pages
            ):

                with page_cols[i]:

                    label = (
                        f"📍 {page_number}"
                        if page_number == current_page
                        else str(page_number)
                    )

                    if st.button(
                        label,
                        key=f"page_b_{page_number}",
                        use_container_width=True
                    ):

                        st.session_state.product_page = (
                            page_number
                        )

                        st.rerun()

        st.write("")

        previous_col, current_col, next_col = st.columns(
            [1, 2, 1]
        )

        with previous_col:

            if current_page > 1:

                if st.button(
                    "← PREVIOUS",
                    key="previous_page",
                    use_container_width=True
                ):

                    st.session_state.product_page -= 1
                    st.rerun()

        with current_col:

            st.markdown(
                f"### Page {current_page} / {total_pages}"
            )

        with next_col:

            if current_page < total_pages:

                if st.button(
                    "NEXT →",
                    key="next_page",
                    use_container_width=True
                ):

                    st.session_state.product_page += 1
                    st.rerun()
# ============================================================
# FAVORITES
# ============================================================

elif st.session_state.page == "Favorites":

    st.header("❤️ My Favorites")

    favorite_products = []

    for product_id in st.session_state.favorites:
        product = get_product(product_id)

        if product:
            favorite_products.append(product)

    if not favorite_products:

        st.info("You have no favorite products yet.")

        if st.button(
            "🛍️ CONTINUE SHOPPING",
            use_container_width=True,
            key="favorite_shop",
        ):
            go_to("Shop")

    else:

        columns = st.columns(4)

        for index, product in enumerate(favorite_products):

            with columns[index % 4]:

                safe_image(product["image"])

                st.subheader(product["name"])
                st.caption(product["category"])
                st.write(f"**{money(product['price'])}**")

                if st.button(
                    "🛒 ADD TO CART",
                    key=f"favorite_cart_{product['id']}",
                    use_container_width=True,
                ):
                    add_to_cart(product["id"])
                    st.rerun()

                if st.button(
                    "REMOVE ❤️",
                    key=f"remove_favorite_{product['id']}",
                    use_container_width=True,
                ):
                    st.session_state.favorites.remove(
                        product["id"]
                    )
                    st.rerun()


# ============================================================
# CART
# ============================================================

elif st.session_state.page == "Cart":

    st.header("🛒 Shopping Cart")

    if not st.session_state.cart:

        st.info("Your cart is empty.")

        if st.button(
            "🛍️ CONTINUE SHOPPING",
            use_container_width=True,
            key="empty_cart_shop",
        ):
            go_to("Shop")

    else:

        for index, product_id in enumerate(
            list(st.session_state.cart)
        ):

            product = get_product(product_id)

            if not product:
                continue

            col1, col2, col3 = st.columns([5, 2, 1])

            with col1:
                st.write(f"🛍️ **{product['name']}**")
                st.caption(product["category"])

            with col2:
                st.write(money(product["price"]))

            with col3:

                if st.button(
                    "REMOVE",
                    key=f"remove_cart_{index}",
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

        st.divider()

        total = cart_total()

        st.subheader(f"Total: {money(total)}")


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.header("ℹ️ About LuxeMart")

    st.subheader("Luxury • Style • Elegance")

    st.write(
        "LuxeMart is a modern online shopping experience "
        "for fashion, beauty, jewellery, perfumes, accessories "
        "and elegant lifestyle products."
    )

    st.divider()

    st.write("✨ Fashion")
    st.write("💎 Jewellery")
    st.write("👜 Accessories")
    st.write("🌸 Perfumes")
    st.write("💄 Beauty")
    st.write("👗 Clothes")


# ============================================================
# CONTACT
# ============================================================

elif st.session_state.page == "Contact":

    st.header("📞 Contact LuxeMart")

    st.write("We are happy to hear from you.")

    st.divider()

    contact_col1, contact_col2 = st.columns(2)

    with contact_col1:

        st.subheader("📞 Phone")
        st.write("03169707804")

        st.subheader("📧 Email")
        st.write("asyabibi485@gmail.com")

    with contact_col2:

        st.subheader("💬 Send a Message")

        contact_name = st.text_input(
            "Your Name",
            key="contact_name",
        )

        contact_phone = st.text_input(
            "Your Phone",
            key="contact_phone",
        )

        contact_message = st.text_area(
            "Your Message",
            placeholder="Write your message here...",
            key="contact_message",
        )

        if st.button(
            "SEND MESSAGE",
            use_container_width=True,
            key="send_contact",
        ):

            if not contact_name.strip():

                st.error("Please enter your name.")

            elif not contact_message.strip():

                st.error("Please enter your message.")

            else:

                st.success(
                    "Thank you! Your message has been received."
                )


# ============================================================
# ADMIN
# ============================================================

elif st.session_state.page == "Admin":

    st.header("🔐 Admin Dashboard")

    if not st.session_state.admin_logged_in:

        st.info(
            "Login using your configured Supabase admin account."
        )

        admin_email = st.text_input(
            "Admin Email",
            key="admin_email",
        )

        admin_password = st.text_input(
            "Password",
            type="password",
            key="admin_password",
        )

        if st.button(
            "LOGIN",
            use_container_width=True,
            key="admin_login",
        ):

            try:

                result = supabase.auth.sign_in_with_password(
                    {
                        "email": admin_email.strip(),
                        "password": admin_password,
                    }
                )

                if result.user is None:

                    st.error("Login failed.")

                else:

                    logged_email = result.user.email or ""

                    if logged_email.lower() != ADMIN_EMAIL.lower():

                        try:
                            supabase.auth.sign_out()
                        except Exception:
                            pass

                        st.error(
                            "This account is not authorized as admin."
                        )

                    else:

                        st.session_state.admin_logged_in = True

                        st.success(
                            "Admin login successful."
                        )

                        st.rerun()

            except Exception as e:

                st.error("Login failed.")
                st.code(str(e))

    else:

        st.success(
            f"Logged in as {ADMIN_EMAIL}"
        )

        if st.button(
            "LOGOUT",
            use_container_width=True,
            key="admin_logout",
        ):
            logout_admin()

        st.divider()

        st.subheader("📦 Customer Orders")

        try:

            response = (
                supabase
                .table("orders")
                .select("*")
                .order("created_at", desc=True)
                .execute()
            )

            orders = response.data or []

            if not orders:

                st.info("No orders received yet.")

            else:

                st.metric(
                    "Total Orders",
                    len(orders),
                )

                st.divider()

                for order in orders:

                    order_id = order.get("id", "N/A")

                    customer_name = order.get(
                        "customer_name",
                        "",
                    )

                    with st.expander(
                        f"🧾 Order #{order_id} — {customer_name}"
                    ):

                        st.write(
                            f"**Customer:** {customer_name}"
                        )

                        st.write(
                            f"**Phone:** "
                            f"{order.get('customer_phone', '')}"
                        )

                        st.write(
                            f"**Address:** "
                            f"{order.get('customer_address', '')}"
                        )

                        st.write(
                            f"**Total:** "
                            f"{money(order.get('total_amount', 0))}"
                        )

                        st.write(
                            f"**Date:** "
                            f"{order.get('created_at', '')}"
                        )

                        st.divider()

                        st.write("**Order Items:**")

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
                                items_response.data or []
                            )

                            if items:

                                for item in items:

                                    st.write(
                                        f"🛍️ "
                                        f"{item.get('product_name', '')} "
                                        f"x "
                                        f"{item.get('quantity', 1)} "
                                        f"— "
                                        f"{money(item.get('price', 0))}"
                                    )

                            else:

                                st.caption(
                                    "No items found."
                                )

                        except Exception as e:

                            st.error(
                                f"Unable to load order items: {e}"
                            )

        except Exception as e:

            st.error(
                "Unable to load customer orders."
            )

            st.code(str(e))
            
