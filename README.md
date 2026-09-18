# LuxeMart — Customer Orders + Admin Dashboard

A GitHub-ready luxury marketplace for Clothes and Home products.

## Features
- Responsive storefront
- Product search and category filters
- Cart saved in browser
- Customer checkout and order creation
- Optional WhatsApp order notification
- Supabase products/orders/order-items database
- Supabase email/password admin login
- Admin product manager
- Admin order status manager
- GitHub Pages compatible (static frontend)

## 1. Create Supabase project
Create a project at Supabase. Open **SQL Editor**, paste `supabase_schema.sql`, and run it.

Then go to **Authentication → Users** and create an admin user with an email and password. Use that account at `admin.html`.

## 2. Add Supabase keys
Open `config.js` and replace:
- `YOUR_SUPABASE_URL`
- `YOUR_SUPABASE_ANON_OR_PUBLISHABLE_KEY`

Use the browser-safe **anon/publishable** key only. Never put a `service_role` or secret key in the website.

Optional: set `WHATSAPP_NUMBER` in international format, for example `923001234567`.

## 3. Test
Open the site. Products can be browsed and customers can place orders after Supabase is configured.

Open `admin.html`, sign in with the Supabase admin user, and manage products/orders.

## 4. GitHub
Upload all files to a repository. For a static GitHub Pages deployment:
Repository → Settings → Pages → Deploy from branch → `main` / root.

For production, use a custom domain and review Supabase Auth URL settings.

## Important security note
This starter uses authenticated users as admins. For a multi-admin production marketplace, add a dedicated `admin_users`/roles table and stricter RLS policies. Do not expose a Supabase service key in frontend code.

## Customize
Change business name, phone, WhatsApp, contact details, logo, fonts, product categories and images in the files.
