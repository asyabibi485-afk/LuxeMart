# LuxeMart — Luxury Streamlit Marketplace

A polished, responsive Streamlit storefront for **Clothes + Home Products**, connected to Supabase.

## Files

- `app.py` — complete storefront + checkout + seller page + admin dashboard
- `requirements.txt` — Python dependencies
- `supabase_schema.sql` — database schema
- `.streamlit/secrets.toml.example` — example Streamlit secrets

## Supabase

Use the same Supabase project/database from your previous LuxeMart setup.

Run `supabase_schema.sql` in the Supabase SQL Editor if the tables are not already created.

## Streamlit Cloud Secrets

In your Streamlit app:

**Manage app → Settings → Secrets**

Add:

```toml
SUPABASE_URL = "https://YOUR-PROJECT.supabase.co"
SUPABASE_KEY = "YOUR_SUPABASE_PUBLISHABLE_KEY"
```

Use the **publishable/anon key**. Never put a Supabase service-role/secret key in GitHub or frontend code.

## Deploy

1. Upload `app.py`, `requirements.txt`, and `supabase_schema.sql` to your GitHub repository.
2. Open Streamlit Community Cloud.
3. Create a new app from that repository.
4. Select `app.py` as the main file.
5. Add the two secrets above.
6. Deploy.

## Admin

Open the **Admin** tab and sign in using the Supabase Auth email/password you created previously.

The dashboard supports:
- Product listing
- Product deletion
- Add product
- Customer orders
- Order status updates

## Design

The front interface is redesigned to match the supplied luxury reference style:
- Large editorial hero typography
- Cream / black / warm beige palette
- Premium product cards
- Mobile-friendly layout
- Collections section
- Sell With Us section
- Customer checkout
- Admin dashboard
