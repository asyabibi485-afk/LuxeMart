-- =====================================================
-- LUXEMART SUPABASE DATABASE
-- Clothes + Home Products + Customer Orders + Admin
-- =====================================================

create extension if not exists pgcrypto;

-- PRODUCTS
create table if not exists public.products (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    description text default '',
    price numeric(12,2) not null default 0,
    category text not null check (category in ('Clothes', 'Home')),
    image_url text default '',
    active boolean not null default true,
    created_at timestamptz not null default now()
);

-- ORDERS
create table if not exists public.orders (
    id uuid primary key default gen_random_uuid(),
    customer_name text not null,
    phone text not null,
    address text not null,
    notes text default '',
    total numeric(12,2) not null default 0,
    status text not null default 'pending'
        check (status in ('pending','confirmed','shipped','delivered','cancelled')),
    created_at timestamptz not null default now()
);

-- ORDER ITEMS
create table if not exists public.order_items (
    id uuid primary key default gen_random_uuid(),
    order_id uuid not null references public.orders(id) on delete cascade,
    product_id uuid references public.products(id) on delete set null,
    product_name text not null,
    quantity integer not null default 1 check (quantity > 0),
    unit_price numeric(12,2) not null default 0
);

-- ENABLE RLS
alter table public.products enable row level security;
alter table public.orders enable row level security;
alter table public.order_items enable row level security;

-- PRODUCTS POLICIES
drop policy if exists "products_public_read" on public.products;
create policy "products_public_read"
on public.products for select
to anon, authenticated
using (active = true);

drop policy if exists "products_authenticated_all" on public.products;
create policy "products_authenticated_all"
on public.products for all
to authenticated
using (true)
with check (true);

-- ORDERS POLICIES
drop policy if exists "orders_public_insert" on public.orders;
create policy "orders_public_insert"
on public.orders for insert
to anon, authenticated
with check (true);

drop policy if exists "orders_authenticated_read" on public.orders;
create policy "orders_authenticated_read"
on public.orders for select
to authenticated
using (true);

drop policy if exists "orders_authenticated_update" on public.orders;
create policy "orders_authenticated_update"
on public.orders for update
to authenticated
using (true)
with check (true);

-- ORDER ITEMS POLICIES
drop policy if exists "order_items_public_insert" on public.order_items;
create policy "order_items_public_insert"
on public.order_items for insert
to anon, authenticated
with check (true);

drop policy if exists "order_items_authenticated_read" on public.order_items;
create policy "order_items_authenticated_read"
on public.order_items for select
to authenticated
using (true);

-- DEMO PRODUCTS
insert into public.products
(name, description, price, category, image_url, active)
select 'Classic Linen Set', 'Elegant premium linen outfit.', 8500, 'Clothes', '', true
where not exists (select 1 from public.products where name = 'Classic Linen Set');

insert into public.products
(name, description, price, category, image_url, active)
select 'Signature Evening Dress', 'Luxury evening dress.', 12900, 'Clothes', '', true
where not exists (select 1 from public.products where name = 'Signature Evening Dress');

insert into public.products
(name, description, price, category, image_url, active)
select 'Minimal Ceramic Vase', 'Modern luxury home decoration.', 4200, 'Home', '', true
where not exists (select 1 from public.products where name = 'Minimal Ceramic Vase');

insert into public.products
(name, description, price, category, image_url, active)
select 'Soft Luxe Cushion Set', 'Premium decorative cushion set.', 3800, 'Home', '', true
where not exists (select 1 from public.products where name = 'Soft Luxe Cushion Set');
