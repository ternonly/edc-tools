Build a complete ecommerce website for Survival72™, an EDC (Everyday Carry) modular tools brand targeting GCC / Middle East market.

---

## TECH STACK
- Supabase (Auth + Database + Storage)
- i18next (multi-language: English, Arabic, Chinese)
- TipTap (blog rich text editor)
- Google Maps API (tracking)
- Vanilla HTML/CSS/JS (no React/Vue framework — keep it simple for Lovable)

---

## COLOR SYSTEM
```css
--bg-primary: #FFFFFF;
--bg-ink: #111111;
--bg-warm: #F9F8F6;
--text-primary: #1A1A1A;
--text-secondary: #666666;
--gold: #C9A96E;
--gold-dark: #B8934A;
--border: #E8E8E8;
```
Typography: Helvetica Neue, Arial, sans-serif. All sizes in CSS custom properties.

---

## PAGES TO BUILD (in order)

### 1. Global Header/Footer
- Logo: "SURVIVAL72" text, left side
- Nav: Shop | Blog | About | Wholesale | Contact
- Right side: cart icon + account icon
- Sticky, hamburger on mobile
- Language switcher dropdown (🌐 English / العربية / 简体中文) top-right
- Footer: quick links, © Survival72

### 2. Homepage — 8 sections, single scroll

**Section 1 — Hero Banner** (full viewport height)
```
Background image: industrial tactical aesthetic
Overlay text: "BUILT FOR THE 72 HOURS THAT MATTER"
Subtitle: "Professional-grade modular tools. Carry confidence, not clutter."
Button: "Shop the Kit" → /pages/shop-the-kit
```

**Section 2 — Marquee** (black bar, infinite horizontal scroll)
```
"3 Tools · 1 System | Ships Within 48h | 2-Year Guarantee | Gift-Ready Packaging | Free Shipping Over $100"
```

**Section 3 — s72-problem** (dark #111 background, centered editorial)
```
Kicker: "Why it matters"
Title: "Why carry three separate tools when one decision covers everything?"
Body: gap-between-home-and-where-you-are narrative
```

**Section 4 — s72-system** (3-column card grid)
```
Card 1: Precision Pliers — $52
Card 2: Roadside Wrench — $42
Card 3: Breacher Axe — $49
Below: Gift Integration block (gold tag: "The Ultimate Gift")
CTA: "Configure Your Elite Gift Set" → /pages/shop-the-kit?auto_kit=elite
```

**Section 5 — s72-edu** (background #F9F8F6, 3 blog teaser cards)
"Why Pliers Beat a Swiss Army Knife"
"How to Read a Wrench Size"
"What Makes a Good Axe Head"
Each: tag + title + excerpt + "Read the guide →" → /blog

**Section 6 — s72-proof** (stats row + 3 review cards)
Stats: 2,300+ Kits Delivered | 4.9 Rating | 48h Ships | 2yr Guarantee
Reviews: 3 real-person testimonials (Khaled R. Dubai, Priya M. Abu Dhabi, James T. Riyadh)

**Section 7 — s72-promise** (4 trust items, warm bg)
Free Shipping $100+ | 2-Year Guarantee | 7-Day Returns | Gift-Ready Box

### 3. Kit Configurator — `/pages/shop-the-kit`

This is the CORE interactive page. Full-width, custom HTML/CSS/JS.

**Layout:** 2-column (1:1), stacks on mobile.
Left: Big preview image (sticky, 1:1 aspect ratio). Click → fullscreen lightbox (⤢ icon).
Right: 3 product cards + gift box row + price bar + Add to Cart button.

**3 Product Cards** (horizontal: 88px thumb | 1fr body):
- Pliers — $52 | Wrench — $42 | Axe — $49
- Each: hover → preview updates left | click → toggle selection with ✓ badge
- "View Details" → slide-up drawer (88vh from bottom)

**Gift Box Row:** Dashed gold border, UNLOCKS when all 3 products selected.
- Shows: "Select all 3 modules to unlock"
- Unlocked: "Elite Magnetic Gift Box — +$29"
- Has its own "View Details" drawer with 6 gallery slots + 2 video slots

**Pricing Logic (client-side JS):**
- 2 products → $15 off
- 3 products → $27 off
- Elite (all 3 + box) = 52+42+49-27+29 = $145

**Variant IDs for Add to Cart:**
- Plier only: 44902746980397
- Wrench only: 44902747078701
- Axe only: 44902740820013
- Plier+Wrench: 44902746882093
- Wrench+Axe: 44902747111469
- Plier+Axe: 44902747013165
- All 3 (no box): 44902746914861
- Elite (all 3+box): 44902746947629
- Cart: POST to /cart/add.js

**URL param:** ?auto_kit=elite → auto-select all 3 + box

**Bottom Drawer (per product):** 6 image slots + 2 video slots + specs table.
- Pliers specs: PA-92A, 25-in-1, 420 Stainless, 10.5cm, 180g
- Wrench specs: KA-62A, 9 bits, CR-V Steel, 12cm, 145g
- Axe specs: XI-G8, 8-in-1, 3CR13 Steel, G10 Handle, 24cm, 320g

**Gift Box standalone page:** `/products/gift-box`
- Same drawer + full detail layout
- Specs: 2mm gray board, 18×14×4cm, ~185g, magnetic closure

### 4. Blog System — `/blog`

**Pages:**
- `/blog` — Listing page, 9 posts/page, pagination. Sidebar: categories, top 5 posts, newsletter signup.
- `/blog/category/{slug}` — Filter by: EDC, Survival, Gear, Tactical, Tutorial
- `/blog/{year}/{month}/{slug}` — Single article with breadcrumb

**Article page:**
- Full-width 720px centered column
- Featured image (1200×630)
- Rich text content (H2/H3, lists, quotes, bold, italic)
- Video embed: YouTube/Vimeo 16:9 responsive iframe
- Share buttons (Twitter, Facebook, LinkedIn)
- Related posts (3 cards at bottom)

**Admin:** `/admin/blog`
- TipTap rich text editor
- SEO preview panel (title length, URL, meta description)
- Upload featured image → auto-resize to 1200×630, WebP format

**SEO (per article):**
- Meta title (50-65 chars) + description (120-160 chars)
- Open Graph (og:title, og:description, og:image 1200×630, og:type article)
- Twitter Card (summary_large_image)
- Canonical URL
- JSON-LD: Article + BreadcrumbList + VideoObject + Organization
- Sitemap: /sitemap-blog.xml (auto-generated)
- RSS: /blog/feed.xml
- robots.txt: reference both sitemaps
- Internal links: blog articles → product pages

### 5. Policy Pages (9 total) — ALL email: survival72bob@gmail.com
- `/pages/return-policy` — 7-Day Returns, buyer pays shipping, refund within 5 days
- `/pages/shipping-policy` — 48h processing, GCC rates table (AED 45-75), EU (€15-35), NA ($15-30)
- `/pages/warranty` — 2 years: repair or 40% off re-purchase
- `/pages/privacy-policy` — GDPR-compliant
- `/pages/terms-of-service` — Standard terms
- `/pages/wholesale` — B2B, 25 MOQ, laser engraving, government PO accepted
- `/pages/military-discount` — 10% off via GOVX ID
- `/pages/cancellation-policy` — Orders enter fulfillment ~2h, then non-cancellable
- `/pages/contact` — Form: Name, Email, Order#, Message. Reply within 12h.

### 6. Auth System — Supabase Auth
- `/account/login` — Centered card, dark bg. Email + Password + Sign In. Links: Forgot / Register.
- `/account/register` — Name, Email, Password, Confirm. Auto-sign-in → redirect to /account.

### 7. Unified Member Dashboard — `/account` (protected route)

**5 Tabs in one page:**

**Tab 1 — My Cart**
- Shows active cart items with images, quantities, prices
- Auto-applies military 10% discount if user.govx_verified
- Shipping calculated by region
- [Continue Shopping] + [Checkout] buttons
- Cart synced to Supabase on login

**Tab 2 — My Orders**
- Table: Order# | Date | Items | Total | Status | [Track]
- Filter: All / Processing / Shipped / Delivered / Cancelled
- Status badges color-coded
- Click row → expands with line items + shipping address + payment method

**Tab 3 — Real-Time Tracking**
- Vertical timeline stepper (● confirmed → ● processing → ● picked up → ○ in transit → ○ out for delivery → ○ delivered)
- Google Maps embed with route polyline + location markers
- Courier info: Aramex/DHL, tracking number, tracking URL
- ETA: earliest-latest dates
- Polls GET /api/tracking/{order_id} every 60s
- New events → green pulse animation on timeline dot
- "Live" badge when last event < 60 minutes ago

**Tab 4 — Profile**
- Editable: Name, Email, Phone, Address
- GOVX badge: gold "Verified ✓" if active
- Stats: member since, total orders, total spent

**Tab 5 — Settings**
- Language: en/ar/zh
- Currency: AED/USD/EUR
- Browsing direction: Auto/LTR/RTL
- Email notifications toggles
- Delete account (with confirmation)

### 8. GOVX ID Verification
- Button at checkout + in account: "Verify with GOVX ID"
- OAuth popup → user logs into GOVX
- Returns: { govx_user_id, status: "verified", affiliation }
- Save to users.govx_verified = true
- Auto-apply 10% discount to cart total at checkout

### 9. Admin Frontend Upload
- Any logged-in user with `role = 'admin'` sees "Edit Mode" toggle
- Gallery slots show "+" upload button
- Click → native file picker → upload to Supabase Storage bucket `s72-product-assets`
- Store in `product_assets` table (id, product_id, slot, type, url, uploaded_by)
- Works on all 3 product drawers + gift box drawer + gift box standalone page

### 10. RTL / Arabic Mode
- Triggered when language = Arabic (العربية)
- html[dir="rtl"] → entire layout mirrors
- USE CSS LOGICAL PROPERTIES throughout: margin-inline-start, padding-inline-end, text-align: start, inset-inline-start. NEVER use margin-left/right in new code.
- Arabic fonts: Cairo (sans), Noto Naskh Arabic (serif), Tajawal (modern)
- Load from Google Fonts with font-display: swap
- Arabic numbers: use Arabic-Indic digits (٠١٢٣) when lang=ar
- Kit configurator: product cards on right, preview on left (mirrored)
- Drawers slide from right. Lightbox close button on left.
- Marquee direction reverse. Arrow icons flip.

---

## DATABASE TABLES (Supabase Postgres)

**users:** id, email, password_hash, name, phone, address, role (default 'customer'), govx_verified, govx_id, created_at

**orders:** id, shopify_order_id, user_id (FK→users), status, subtotal, discount, total_price, currency, payment_method, shipping_address (JSON), tracking_number, tracking_url, courier, eta_min, eta_max, created_at, updated_at

**order_items:** id, order_id (FK→orders), product_name, variant_name, quantity, unit_price, image_url

**tracking_events:** id (SERIAL), order_id (FK→orders), status, location, location_coords (JSON {lat,lng}), timestamp (TIMESTAMPTZ), courier, note, created_at

**product_assets:** id, product_id, slot, type, url, uploaded_by (FK→users), created_at

**blog_posts:** id, slug (UNIQUE), title, excerpt, content (HTML), category, tags (TEXT[]), featured_image, author, status, reading_time, views, published_at, updated_at

---

## API ENDPOINTS
- POST /api/auth/register → Supabase signUp
- POST /api/auth/login → Supabase signInWithPassword
- GET /api/orders/{user_id} → fetch user's orders
- GET /api/orders/{order_id}/items → line items
- GET /api/tracking/{order_id} → tracking events + courier info + ETA
- GET /api/blog/posts?page=1&category=edc → paginated posts
- GET /api/blog/posts/{slug} → single post
- POST /api/admin/upload → admin file upload

---

## IMAGES TO PREPARE
- hero-banner-final.jpg (1920×1080)
- s72_pliers_1.png | s72_wrench_1.jpg | s72_axe_1.jpg (product shots)
- s72_gift_box_kit-gift-box.jpg (gift box)
- Blog OG images: 1200×630 per article

---

## ANIMATIONS
- Card hover: border darkens + subtle shadow
- Button hover: darken + translateY(-2px)
- Preview image: opacity fade (0.3s)
- Drawer: slide up from bottom (0.35s cubic-bezier)
- Lightbox: scale 0.93→1 + fade (0.2s)
- Marquee: infinite translateX (20s linear)
- Tracking new event: timeline dot pulses green (○→●)

---

## BREAKPOINTS
- Desktop: >768px
- Tablet: 600–768px (2-col becomes 1-col)
- Mobile: <600px (stacked, full-width, hamburger nav)

---

Start building from step 1. Show me the homepage first. Only use the technologies specified above. Do NOT introduce React, Next.js, or Tailwind — plain HTML/CSS/JS with Supabase and i18next only.
