# Survival72™ — Lovable Build Spec

> **Complete code-ready implementation requirements for rebuilding survival72gear.com on Lovable.dev**
> Generated: 2026-05-08

---

## 1. BRAND IDENTITY

| Token | Value |
|-------|-------|
| **Brand Name** | Survival72™ |
| **Tagline** | "Built for the 72 hours that matter" |
| **Product Category** | EDC (Everyday Carry) Modular Tools |
| **Target Market** | GCC / Middle East — COD + AED currency |
| **Brand Personality** | Professional, tactical, calm, decisive |
| **Visual Benchmark** | Spyderco, Victorinox — industrial luxury |

---

## 2. GLOBAL STYLES & COLOR SYSTEM

### 2.1 Color Palette

```css
:root {
  --color-bg-primary: #FFFFFF;
  --color-bg-ink:     #111111;   /* s72-problem section bg */
  --color-bg-warm:    #F9F8F6;   /* s72-edu, s72-promise bg */

  --color-text-primary:   #1A1A1A;
  --color-text-secondary: #666666;
  --color-text-muted:     #888888;
  --color-text-dark-bg:   #AAAAAA;

  --color-gold:       #C9A96E;
  --color-gold-dark:  #B8934A;
  --color-black:      #1A1A1A;
  --color-border:     #E8E8E8;
  --color-border-light: #EEEEEE;
}
```

### 2.2 Typography

```css
font-family: 'Helvetica Neue', Arial, sans-serif;
```

| Element | Size | Weight | Tracking |
|---------|------|--------|----------|
| Hero title | clamp(28px, 5vw, 48px) | 700 | normal |
| Section title | clamp(24px, 3.5vw, 38px) | 700 | normal |
| H2 (system title) | 42px | 700 | -1px |
| H3 card title | 20px | 700 | normal |
| Kicker | 12px | 400 | 2px / 0.2em |
| Body | 14-16px | 400 | normal |
| Button | 14px | 700 | 1px / 0.08em |
| Price | 15-26px | 600-700 | normal |

### 2.3 Global CSS Reset & Helpers

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1a1a1a; background: #fff; line-height: 1.5; }
```

### 2.4 S72 Custom CSS Injection

```css
/* s72-custom.css — loaded globally via theme.liquid */

/* Kit page full-width override */
body.page-shop-the-kit .main-page,
body.page-shop-the-kit main,
body.page-shop-the-kit .page-width {
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}
body.page-shop-the-kit .main-page > *:first-child {
  display: none !important;
}

/* Hide native variant picker on product pages */
variant-picker, variant-selects, variant-radios,
.variant-picker, .block-variant-picker,
.product-form__input, .product-form__input--pill,
.product-form__input--dropdown,
[data-block-type="variant-picker"],
[class*="variant-picker"] {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
}
```

---

## 3. PAGE STRUCTURE

### 3.1 Navigation (Global Header)

- Logo: "SURVIVAL72" text mark, left-aligned
- Menu items: Shop / About / Wholesale / Contact
- Cart icon (right side) with item count badge
- Desktop: horizontal nav; Mobile: hamburger drawer
- Sticky on scroll

### 3.2 Footer

- Standard ecommerce footer with quick links: About, Contact, Return Policy, Wholesale
- © 2024 Survival72. All rights reserved.

---

## 4. HOMEPAGE — SECTION ORDER & FULL SPECS

The homepage is a single-page scroll with sections loaded in this exact order:

```
1. Hero Banner
2. Marquee (scrolling credits bar)
3. s72-problem (Why It Matters)
4. s72-system (Modular System + Gift Integration)
5. s72-edu (Field Guide)
6. s72-proof (Social Proof + Testimonials)
7. featured_configurator (Product configurator)
8. s72-promise (Trust bar)
```

---

### 4.1 Hero Banner

**Layout:** Full viewport height hero image with overlay text.

```html
<section style="height: 100vh; background: url('/hero-banner-final.jpg') center/cover;">
  <div style="
    position: absolute; inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.5));
    display: flex; align-items: center; justify-content: center;
  ">
    <div style="text-align: center; color: #fff;">
      <h1 style="font-size: clamp(36px, 8vw, 72px); font-weight: 700; margin-bottom: 20px;">
        BUILT FOR THE<br>72 HOURS THAT MATTER
      </h1>
      <p style="font-size: 18px; opacity: 0.85; margin-bottom: 36px;">
        Professional-grade modular tools. Carry confidence, not clutter.
      </p>
      <a href="/pages/shop-the-kit" style="
        background: #1A1A1A; color: #fff; padding: 18px 56px;
        font-size: 14px; font-weight: 700; text-transform: uppercase;
        letter-spacing: 1px; text-decoration: none;
        border: 2px solid transparent; transition: 0.3s;
      ">Shop the Kit</a>
    </div>
  </div>
</section>
```

**Image:** Hero banner image — industrial tactical aesthetic, desert or urban emergency theme.
- Upload as `/hero-banner-final.jpg`
- Dimensions: 1920×1080 or taller

---

### 4.2 Marquee — Scrolling Credits Bar

**Layout:** Infinite horizontal scroll of trust badges.

```html
<section style="background: #1A1A1A; padding: 14px 0; overflow: hidden;">
  <div style="display: flex; gap: 48px; animation: marquee 20s linear infinite;">
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">3 Tools · 1 System</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">Ships Within 48h</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">2-Year Guarantee</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">Gift-Ready Packaging</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">Free Shipping Over $100</span>
    <!-- Duplicate for seamless loop -->
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">3 Tools · 1 System</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">Ships Within 48h</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">2-Year Guarantee</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">Gift-Ready Packaging</span>
    <span style="color: #fff; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; white-space: nowrap;">Free Shipping Over $100</span>
  </div>
</section>

<style>
@keyframes marquee {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
</style>
```

---

### 4.3 s72-problem — "Why It Matters"

**Layout:** Dark background, centered editorial statement.

```css
.s72-problem {
  background: #111;
  padding: 80px 24px;
  text-align: center;
}
.s72-problem__kicker {
  font-size: 12px; letter-spacing: 0.2em;
  text-transform: uppercase; color: #C9A96E;
  margin-bottom: 24px;
}
.s72-problem__title {
  font-size: clamp(28px, 5vw, 48px);
  font-weight: 700; color: #fff;
  line-height: 1.15; margin-bottom: 28px;
}
.s72-problem__body {
  font-size: 18px; color: #aaa; line-height: 1.8;
}
.s72-problem__body em { color: #fff; font-style: normal; }
```

```html
<section class="s72-problem">
  <p class="s72-problem__kicker">Why it matters</p>
  <h2 class="s72-problem__title">Why carry three separate tools<br>when one decision covers everything?</h2>
  <p class="s72-problem__body">
    Most people have a wrench in the garage,<br>
    a knife in a drawer, and <em>nothing in their bag.</em><br><br>
    That gap between home and wherever you actually are<br>
    is exactly what Survival72 fills.
  </p>
</section>
```

---

### 4.4 s72-system — Modular System Showcase

**Layout:** Centered header → 3-column card grid → Gift integration → CTA buttons.

#### 4.4.1 Card Grid (3 columns on desktop, 1 on mobile)

```css
.s72-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.s72-card {
  border: 1px solid #eee; padding: 40px 32px;
  text-align: center; transition: 0.3s;
}
.s72-card:hover {
  border-color: #1a1a1a;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}
@media (max-width: 768px) { .s72-grid { grid-template-columns: 1fr; } }
```

**3 Cards:**
| Card | Icon | Title | Description |
|------|------|-------|-------------|
| 1 | 🔧 | Precision Pliers | 7.2-inch cold-forged steel. High-torque grip with integrated wire cutter and survival notch. |
| 2 | 🔩 | Roadside Wrench | Optimized for vehicle battery terminals and plumbing valves. Universal fit for emergency mechanics. |
| 3 | 🪓 | Breacher Axe | Short-handle emergency axe with 45-degree bevel. Engineered for entry, recovery, and heavy prep. |

These use emoji as placeholders — **replace with real product icons/illustrations**.

#### 4.4.2 Gift Integration Block

Left-right layout — image placeholder left, content right. Gold-tagged premium section.

```css
.s72-gift-integration {
  background: #f9f9f9; padding: 60px;
  border: 1px solid #eee; display: flex;
  align-items: center; gap: 60px; margin-top: 40px;
}
@media (max-width: 768px) {
  .s72-gift-integration { flex-direction: column; padding: 32px; gap: 32px; }
}
```

**Content:**
- Tag: "The Ultimate Gift" (gold badge #C9A96E)
- Title: "The Unboxing Experience"
- Body text about premium packaging
- Checklist items with ✓ gold checkmarks:
  1. **Premium Packaging:** 2mm weighted gray-board box with a hidden magnetic closure.
  2. **Protection:** Custom-cut high-density EVA foam lined with black suede.
  3. **Education:** Includes the physical 24-page Survival72™ Field Guide.
- Button: "Configure Your Elite Gift Set" → links to `/pages/shop-the-kit?auto_kit=elite`

#### 4.4.3 System CTA

Two buttons centered at bottom:
1. **Primary (filled black):** "Configure Your Elite Gift Set" → `/pages/shop-the-kit?auto_kit=elite`
2. **Secondary (outline):** "Shop the Kit" → `/pages/shop-the-kit`

```css
.s72-btn {
  display: inline-block; background: #1a1a1a; color: #fff;
  padding: 18px 48px; font-size: 14px; font-weight: 700;
  text-decoration: none; text-transform: uppercase;
  letter-spacing: 1px; transition: 0.3s;
}
.s72-btn:hover { background: #333; transform: translateY(-2px); }
/* Outline variant */
.s72-btn--outline {
  background: transparent; color: #1a1a1a;
  border: 1px solid #1a1a1a;
}
```

---

### 4.5 s72-edu — Field Guide Blog Cards

**Layout:** Warm background (#F9F8F6), 3-column grid of article cards.

```css
.s72-edu { background: #f9f8f6; padding: 80px 24px; }
.s72-edu__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px; margin-bottom: 36px;
}
.s72-edu-card {
  background: #fff; border: 1px solid #e8e8e8;
  border-radius: 4px; padding: 32px 28px;
}
```

**3 Article Cards:**
| Tag | Title | Excerpt |
|-----|-------|---------|
| 3 min read | Why Pliers Beat a Swiss Army Knife for Everyday Use | Most multi-tools give you a bit of everything. Pliers give you the one thing you actually need: grip... |
| 2 min read | How to Read a Wrench Size (And Why Most People Get It Wrong) | Metric vs. imperial, open-end vs. adjustable. A quick guide... |
| 4 min read | What Makes a Good Axe Head (And What to Ignore) | Weight, edge geometry, handle angle. The details that separate a useful axe from a decoration... |

Each card has a `"Read the guide →"` link pointing to `/blogs/field-guide`.
Bottom CTA: `"Explore all Field Guide articles →"` linking to `/blogs/field-guide`.

---

### 4.6 s72-proof — Social Proof & Testimonials

#### 4.6.1 Stats Row (4 columns → 2 on mobile)

```css
.s72-proof__stats {
  display: grid; grid-template-columns: repeat(4, 1fr);
  border: 1px solid #e8e8e8; border-radius: 4px;
  margin-bottom: 48px; overflow: hidden;
}
@media (max-width: 600px) { .s72-proof__stats { grid-template-columns: repeat(2, 1fr); } }
```

**4 Stat Cells:**
| Number | Label |
|--------|-------|
| 2,300+ | Kits Delivered |
| 4.9 | Average Rating |
| 48h | Ships Within |
| 2yr | Guarantee |

#### 4.6.2 Review Cards (3 cards in responsive grid)

Each review card:
```css
.s72-review-card {
  border: 1px solid #e8e8e8; border-radius: 4px; padding: 28px;
}
.s72-review-card__stars { color: #C9A96E; font-size: 14px; letter-spacing: 3px; } /* gold stars ★★★★★ */
```

**3 Testimonials:**
1. **Khaled R.** — Dubai, UAE — "I have carried the wrench module every day for three months..."
2. **Priya M.** — Abu Dhabi, UAE — "Bought the full kit as a gift for my father..."
3. **James T.** — Expatriate, Riyadh — "Not flashy. Just does what it promises..."

#### 4.6.3 CTA
Button: "Build My Kit →" → `/pages/shop-the-kit?auto_kit=elite`
Hover effect: background turns gold `#C9A96E`, text turns black.

---

### 4.7 s72-promise — Trust Bar (Bottom)

4-item horizontal trust bar with divider lines between items.

```css
.s72-promise {
  background: #f9f8f6; padding: 40px 24px;
  border-top: 1px solid #e8e8e8;
  border-bottom: 1px solid #e8e8e8;
}
.s72-promise__item:not(:last-child)::after {
  content: ""; position: absolute; right: 0; top: 20%;
  height: 60%; width: 1px; background: #ddd;
}
```

**4 Trust Items:**
| Value | Label |
|-------|-------|
| Free Shipping | on orders over $100 |
| 2-Year Guarantee | on every module |
| 30-Day Returns | no questions asked |
| Gift-Ready | magnetic box available |

---

## 5. SHOP THE KIT PAGE (`/pages/shop-the-kit`) — FULL CONFIGURATOR

This is the **core interactive page** of the site. It is a standalone page (NOT a product page) built entirely with custom HTML/CSS/JS. Everything below must be implemented exactly as specified.

### 5.1 Page Header

```html
<h1 style="font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;">Survival72™ Modular System</h1>
<p style="font-size:13px;color:#888;">Build your kit. Every tool engineered for 72-hour deployment.</p>
```

### 5.2 Mode Toggle (Two Buttons)

Two full-width toggle buttons side by side:

| Button | Function | State |
|--------|----------|-------|
| **Build Your Kit** | Manual selection mode (default active) | Black fill, white text |
| **Elite Gift Set — $145** | Auto-select all 3 + gift box | Gold border + fill `#B8934A` |

```css
.mode-btn {
  flex: 1; padding: 14px 12px;
  border: 1.5px solid #d0d0d0; background: #fafafa;
  cursor: pointer; text-align: center;
  font-size: 11px; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase;
  transition: 0.2s; line-height: 1.5;
}
.mode-btn.active  { border-color: #1a1a1a; background: #1a1a1a; color: #fff; }
.mode-btn.elite   { border-color: #b8934a; background: #b8934a; color: #fff; }
```

### 5.3 Main Layout

Two-column grid (1:1), stacks on mobile (max-width: 700px):

```
┌──────────────────────┬──────────────────────────┐
│                      │ Product Cards (right)    │
│   Big Preview Image  │                          │
│   (left, sticky)     │  ┌─────────────────────┐ │
│                      │  │ Pliers — $52        │ │
│   ┌────────────────┐ │  └─────────────────────┘ │
│   │                │ │  ┌─────────────────────┐ │
│   │  1:1 preview   │ │  │ Wrench — $42        │ │
│   │  (zoom hint ⤢) │ │  └─────────────────────┘ │
│   │                │ │  ┌─────────────────────┐ │
│   └────────────────┘ │  │ Axe — $49           │ │
│                      │  └─────────────────────┘ │
│                      │                          │
│                      │  Gift Box row            │
│                      │  Price Bar               │
│                      │  [Add to Cart] button    │
└──────────────────────┴──────────────────────────┘
```

### 5.4 Preview Box (Left) — With Lightbox Zoom

**Normal state:** 1:1 aspect ratio sticky container. Shows hint text "Hover a product to preview" initially. When a product card is hovered, the corresponding product image fades in (opacity transition).

**Zoom behavior:**
- Cursor: `zoom-in`
- Bottom-right corner: small `⤢` icon badge visible on hover
- **Click** → Lightbox opens full-screen

**Lightbox:**
```css
.lb-overlay {
  position: fixed; inset: 0; z-index: 19000;
  background: rgba(0,0,0,0.92);
  display: none; cursor: zoom-out;
}
.lb-overlay.open { display: flex; align-items: center; justify-content: center; }
.lb-overlay img {
  max-width: 90vw; max-height: 90vh;
  object-fit: contain;
  border-radius: 3px;
  animation: lb-in 0.2s ease;
}
@keyframes lb-in { from { opacity: 0; transform: scale(0.93); } to { opacity: 1; transform: scale(1); } }
```

Close button (✕) in top-right corner. Escape key closes. Click anywhere on overlay closes.

### 5.5 Product Cards (Right Column)

Each card is a horizontal grid: `88px thumbnail | 1fr body`, with a `✓` checkmark badge (black circle, top-right) when selected.

**3 Products:**

| ID | Module | Name | Image | Price |
|----|--------|------|-------|-------|
| pliers | Module 01 — Pliers | Precision Multi-Pliers | `s72_pliers_1.png` | $52 |
| wrench | Module 02 — Wrench | Roadside Wrench | `s72_wrench_1.jpg` | $42 |
| axe | Module 03 — Axe | Desert Breacher Axe | `s72_axe_1.jpg` | $49 |

**Card behavior:**
- `onmouseenter` → preview image updates on the left
- `onclick` → toggle selection (add/remove from kit)
- Each card has a "View Details ›" button → opens a sliding bottom drawer

### 5.6 Gift Box Row

Dashed gold border, only **unlocks** (becomes clickable) when ALL 3 products are selected.

```css
.gift-row {
  border: 1.5px dashed #d0b980; background: #fffdf5;
  display: grid; grid-template-columns: 68px 1fr auto;
  align-items: center; gap: 12px; padding: 13px;
  cursor: pointer; transition: 0.25s;
}
.gift-row.locked { opacity: 0.4; pointer-events: none; }
.gift-row.selected { border: 2px solid #b8934a; border-style: solid; }
```

**When locked:** Shows overlay text "Select all 3 modules to unlock".

| Thumbnail | Info | Price |
|-----------|------|-------|
| Gift box image | Elite Magnetic Gift Box<br><small>Premium clamshell case · EVA foam inlays · S72 Field Guide</small> | + $29 |

### 5.7 Price Bar

Dark bar (#1a1a1a) with dynamic pricing:

```
┌─────────────────────────────────────────────┐
│ KIT TOTAL                    YOU SAVE $27   │
│ $145.00                                     │
│ (hint text when nothing selected)           │
└─────────────────────────────────────────────┘
```

**Pricing Logic (Client-Side JS):**

```javascript
// Base prices
const PRICES = { pliers: 52, wrench: 42, axe: 49 };
const BOX_PRICE = 29;

// Discounts
// 2 products selected → $15 off
// 3 products selected → $27 off

// Kit combos:
// Elite (all 3 + box) = 52 + 42 + 49 - 27 + 29 = $145
// Any 3 no box = 52 + 42 + 49 - 27 = $116
// Any 2 = sum - $15
// Single item = full price
```

### 5.8 Add to Cart Button

Button text updates dynamically:
- Nothing selected: "Select a Module" (disabled, gray)
- Items selected: "Add to Cart — $XX.XX"

On click:
1. Calculate variant key: `(pliers?1:0)-(wrench?1:0)-(axe?1:0)-(box?1:0)`
2. Map to variant ID (see Variant ID Map below)
3. POST to `/cart/add.js` with `{ items: [{ id: variantId, quantity: 1 }] }`
4. Button shows "Adding…" → "✓ Added to Cart" → resets after 2s

**Variant ID Map:**

| Combo (P-W-A-B) | Variant ID | Price |
|-----------------|------------|-------|
| 1-0-0-0 | 44902746980397 | $52 |
| 0-1-0-0 | 44902747078701 | $42 |
| 0-0-1-0 | 44902740820013 | $49 |
| 1-1-0-0 | 44902746882093 | $79 |
| 0-1-1-0 | 44902747111469 | $76 |
| 1-0-1-0 | 44902747013165 | $86 |
| 1-1-1-0 | 44902746914861 | $116 |
| 1-1-1-1 | 44902746947629 | $145 |

> **For Lovable:** If integrating with Shopify Cart API is not supported, implement Add to Cart via Shopify's Buy Button SDK or direct `/cart/add.js` fetch. If neither, build the cart logic entirely client-side with localStorage and provide a checkout redirect.

### 5.9 Bottom Drawer — Product Details

Each product has a slide-up drawer (88vh height, from bottom) with:

**Drawer contents for each product:**

| Section | Plier (PA-92A) | Wrench (KA-62A) | Axe (XI-G8) |
|---------|----------------|-----------------|-------------|
| **Photo Gallery** | 6 image slots (editable) | 6 image slots | 6 image slots |
| **Video** | 2 video/iframe slots | 2 video/iframe slots | 2 video/iframe slots |
| **Specs Table** | 9 rows | 9 rows | 9 rows |

**Photo Gallery slots** are empty placeholder divs with dashed borders, containing instructional text: "Upload via Shopify Files then paste here". User manually pastes `<img src="...">` tags later.

**Video slots** empty dashed-border divs with ▶ icon and "Paste <video> or YouTube iframe here" text.

**Specs tables:**

```
Pliers (PA-92A):
Model: PA-92A | Functions: 25-in-1 | Material: 420 Stainless Steel
Folded Length: 10.5 cm | Weight: 180 g | Jaw Opening: 25 mm
Blade: Serrated + Straight | Finish: Sandblasted + Black Oxide
Includes: Nylon Sheath, S72 Card

Wrench (KA-62A):
Model: KA-62A | Bits: 9 (PH1, PH2, SL4, SL6, H3, H4, H5, T25, T30)
Material: CR-V Drop-Forged Steel | Folded Length: 12 cm
Weight: 145 g | Drive: 1/4" (6.35 mm) | Ratchet: Reversible
Finish: Satin Chrome | Includes: Bit Pouch, S72 Card

Axe (XI-G8):
Model: XI-G8 | Functions: 8-in-1 | Head Material: 3CR13 Stainless Steel
Handle: G10 Composite | Overall Length: 24 cm | Head Weight: 180 g
Total Weight: 320 g | Edge: 25° Bevel, Field-Sharpenable
Includes: Ballistic Nylon Sheath, S72 Card
```

**Drawer CSS:**
```css
.drawer {
  position: fixed; bottom: 0; left: 0; right: 0; height: 88vh;
  background: #fff; z-index: 9001;
  transform: translateY(100%);
  transition: transform 0.35s cubic-bezier(0.32, 0, 0.15, 1);
  border-radius: 14px 14px 0 0; overflow: hidden;
}
.drawer.open { transform: translateY(0); }
.drawer-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.5);
  z-index: 9000; backdrop-filter: blur(3px);
}
```

**JS Behavior:**
- `openDrawer(tool)` → shows overlay + drawer slides up + body overflow hidden
- `closeDrawer()` → hides overlay + drawer slides down
- Escape key closes
- Clicking overlay closes
- Drawers should NOT interfere with the lightbox (different z-index layers: drawer 9000, lightbox 19000)

### 5.10 URL Parameter Support

- `?auto_kit=elite` → auto-selects all 3 products + gift box on page load
- This is used by homepage CTA buttons

---

## 6. STATIC PAGES

### 6.1 About (`/pages/about`)
Page title: "About Survival72"
Content: Brand story about EDC professionalism, 72-hour preparedness philosophy, team background.

### 6.2 Wholesale & Custom (`/pages/wholesale`)  
Page title: "Wholesale & Custom"
Content: B2B inquiry information for corporate gifts and bulk orders.

### 6.3 Contact (`/pages/contact`)
Standard contact page with form or email info.

### 6.4 Return Policy (`/pages/return-policy`)
30-day return policy details.

### 6.5 Our Promise (`/pages/our-promise`)
Brand promise/guarantee information.

### 6.6 Corporate & Bespoke (`/pages/corporate-partnerships`)
Corporate partnership and custom branding inquiries.

---

## 7. RESPONSIVE BREAKPOINTS

| Breakpoint | Behavior |
|------------|----------|
| **> 768px** | Full desktop layout |
| **768px** | s72-system: cards stack to 1 column; gift block stacks vertically |
| **700px** | Kit page: 2-col becomes single column (preview above cards) |
| **600px** | s72-proof stats: 4-col → 2-col |
| **Mobile** | ≈ 375-430px — hamburger nav, stacked layouts, full-width sections |

---

## 8. PRODUCT IMAGES TO PREPARE

Upload these images (host on your Lovable assets or CDN):

| File | Use |
|------|-----|
| `hero-banner-final.jpg` | Homepage hero background (1920×1080+) |
| `s72_pliers_1.png` | Pliers product shot |
| `s72_wrench_1.jpg` | Wrench product shot |
| `s72_axe_1.jpg` | Axe product shot |
| `s72_gift_box_kit-gift-box.jpg` | Gift box product shot |
| Gift box lifestyle shot | s72-system gift integration block |
| 3 product detail gallery images each | Bottom drawer photo slots |

---

## 9. ANIMATIONS & TRANSITIONS

| Element | Effect |
|---------|--------|
| Card hover | Border darkens, subtle box-shadow |
| Button hover | Darken background + translateY(-2px) |
| Preview image | Opacity 0→1 fade (0.3s) |
| Drawer | Slide up from bottom (0.35s cubic-bezier) |
| Lightbox | Scale 0.93→1 + fade (0.2s ease) |
| Marquee | Infinite translateX scroll (20s linear) |
| Selection checkmark | Instant toggle |

---

## 10. INTERACTION SUMMARY (JavaScript Behaviors)

1. **Marquee:** CSS animation, auto-playing infinite loop
2. **Configurator:**
   - Product toggle (click card → add/remove from selection)
   - Gift box unlock (all 3 selected → gift row becomes interactive)
   - Price calculation (reactive to selection changes)
   - Variant mapping (selection combo → Shopify variant ID)
   - Add to Cart (fetch POST to `/cart/add.js`)
   - Elite mode (URL param or button click → auto-select all)
3. **Preview + Lightbox:**
   - Card hover → preview image swap
   - Preview click → fullscreen lightbox
   - ESC / overlay click → close lightbox
4. **Bottom Drawer:**
   - "View Details" click → slide-up drawer
   - ESC / overlay click → close drawer
5. **Mobile responsive:** All components collapse/restack below breakpoints

---

## 11. BUILD ORDER (Lovable Implementation Sequence)

| Step | Component | Dependencies |
|------|-----------|--------------|
| 1 | Global CSS reset + color system + typography | None |
| 2 | Navigation (Header + Footer) | None |
| 3 | Hero Banner section | Images |
| 4 | Marquee section | None |
| 5 | s72-problem section | None |
| 6 | s72-system section (cards + gift + CTAs) | None |
| 7 | s72-edu section | None |
| 8 | s72-proof section | None |
| 9 | s72-promise trust bar | None |
| 10 | **Kit Configurator page** (full standalone page) | Images, variant IDs |
| 11 | Static pages (About, Wholesale, etc.) | None |
| 12 | Responsive testing + polish | All |
| 13 | Cart integration | Shopify API or localStorage |
