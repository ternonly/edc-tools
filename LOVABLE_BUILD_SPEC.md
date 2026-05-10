# Survival72™ — Lovable Build Spec

> **Complete code-ready implementation requirements for rebuilding survival72gear.com on Lovable.dev**
> Generated: 2026-05-08 | Updated: 2026-05-10

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
- Menu items: Shop / Blog / About / Wholesale / Contact
- Cart icon (right side) with item count badge + account icon (person silhouette)
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

### 5.11 Gift Box Detail Drawer — Standalone Detail Page with Admin Upload

The Gift Box gets its own **"View Details"** drawer, exactly like the 3 product modules. It also has a dedicated **standalone detail page** (`/products/gift-box`) where an admin (logged-in user with `role = admin`) can upload images/videos from the frontend.

#### 5.11.1 Gift Box Card Enhancement

On the Kit Configurator, the gift box row now includes:
- **Thumbnail preview**: Shows the gift box image on hover (same as product cards)
- **"View Details ›"** button → opens the gift box drawer
- **"View Large Image ⤢"** click → opens the same lightbox as product previews

#### 5.11.2 Gift Box Drawer Contents

Slide-up drawer (same 88vh, same CSS as product drawers):

```html
<div class="drawer" id="gift-drawer">
  <div class="drawer-header">
    <span>Elite Magnetic Gift Box</span>
    <button class="drawer-close">✕</button>
  </div>

  <!-- Photo Gallery: 6 slots, admin-uploadable -->
  <section class="gallery-section">
    <h3>Gallery</h3>
    <div class="gallery-grid">
      <div class="gallery-slot admin-upload-slot" data-slot="1">
        <img src="" alt="Gift Box Front" />
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
      <div class="gallery-slot admin-upload-slot" data-slot="2">
        <img src="" alt="Gift Box Open" />
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
      <div class="gallery-slot admin-upload-slot" data-slot="3">
        <img src="" alt="Gift Box Interior" />
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
      <div class="gallery-slot admin-upload-slot" data-slot="4">
        <img src="" alt="Gift Box Detail" />
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
      <div class="gallery-slot admin-upload-slot" data-slot="5">
        <img src="" alt="Gift Box Lifestyle" />
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
      <div class="gallery-slot admin-upload-slot" data-slot="6">
        <img src="" alt="Gift Box Unboxing" />
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
    </div>
  </section>

  <!-- Video: 2 slots, admin-uploadable -->
  <section class="video-section">
    <h3>Videos</h3>
    <div class="video-grid">
      <div class="video-slot admin-upload-slot" data-slot="v1">
        <div class="video-placeholder">▶ Paste YouTube link or upload video</div>
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
      <div class="video-slot admin-upload-slot" data-slot="v2">
        <div class="video-placeholder">▶ Paste YouTube link or upload video</div>
        <button class="admin-upload-btn" title="Upload">+</button>
      </div>
    </div>
  </section>

  <!-- Specs Table -->
  <section class="specs-section">
    <h3>Specifications</h3>
    <table>
      <tr><td>Material</td><td>2mm gray board + magnetic closure</td></tr>
      <tr><td>Interior</td><td>High-density EVA foam, black suede lining</td></tr>
      <tr><td>Dimensions</td><td>18 × 14 × 4 cm</td></tr>
      <tr><td>Weight</td><td>~185 g (optimized for shipping)</td></tr>
      <tr><td>Contents</td><td>3 tool slots + S72 Field Guide slot + tool card slot</td></tr>
      <tr><td>Finish</td><td>Matte black exterior, gold foil S72 logo</td></tr>
      <tr><td>Closure</td><td>Hidden magnetic clasp</td></tr>
      <tr><td>Includes</td><td>Gift box, EVA inlay, 24-page Field Guide</td></tr>
    </table>
  </section>
</div>
```

#### 5.11.3 Standalone Gift Box Product Page (`/products/gift-box`)

Full-width product detail page with:
- **Hero image** (left) — 1:1, click for lightbox zoom (same as configurator)
- **Product info** (right) — title, price ($29), bullet features, [Add to Cart] button
- **Gallery section** — same 6-slot grid, admin-uploadable
- **Video section** — same 2-slot grid, admin-uploadable
- **Admin upload mode** — visible only when `user.role === 'admin'`

#### 5.11.4 Admin Frontend Upload System

**How it works:**
1. Any user can browse the page normally.
2. If the user is logged in AND has `role = 'admin'`, an **"Edit Mode"** toggle appears in the top-right corner of each gallery/video section.
3. Toggle ON → all slots show a **"+" upload button** overlay.
4. Click "+" → native file picker opens (accept: `image/*` for gallery, `video/*` or `.mp4` for video).
5. Selected file → **upload to Supabase Storage** bucket `s72-product-assets`.
6. After upload → update the `product_assets` table, refresh the slot to show the new image/video.
7. For YouTube: paste the URL into an input field → stores the `<iframe>` embed code.

**Database Table: `product_assets`**
| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Asset ID |
| `product_id` | VARCHAR(50) | 'pliers' / 'wrench' / 'axe' / 'gift-box' |
| `slot` | VARCHAR(10) | '1'-'6' (image) or 'v1'-'v2' (video) |
| `type` | VARCHAR(10) | 'image' or 'video' |
| `url` | TEXT | Supabase storage URL or YouTube embed |
| `uploaded_by` | UUID FK→users | Admin who uploaded |
| `created_at` | TIMESTAMP | Upload time |

**CSS: Admin upload button**
```css
.admin-upload-btn {
  display: none;
  position: absolute; top: 8px; right: 8px;
  width: 32px; height: 32px; border-radius: 50%;
  background: #1a1a1a; color: #fff; border: none;
  font-size: 18px; cursor: pointer; z-index: 10;
}
.edit-mode .admin-upload-btn { display: flex; align-items: center; justify-content: center; }
.admin-upload-btn:hover { background: #c9a96e; }
```

**Gallery slot CSS:**
```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}
.gallery-slot {
  position: relative;
  aspect-ratio: 1;
  border: 1.5px dashed #ddd;
  border-radius: 6px;
  overflow: hidden;
  background: #fafafa;
}
.gallery-slot img {
  width: 100%; height: 100%;
  object-fit: cover;
}
.gallery-slot img:not([src]), .gallery-slot img[src=""] {
  display: none;
}
```

**Admin role check (frontend):**
```javascript
// Fetch from users table
const { data: { user } } = await supabase.auth.getUser();
const { data: profile } = await supabase
  .from('users')
  .select('role')
  .eq('id', user.id)
  .single();

if (profile?.role === 'admin') {
  document.body.classList.add('edit-mode');
}
```

---

## 6. STATIC POLICY PAGES (Updated 2026-05-10)

### 6.1 Return & Refund Policy (`/pages/return-policy`)

```
Title: 7-Day No-Questions Return — 7天无条件退货
Content:
  "If you're not satisfied for any reason, return within 7 days for a full refund.
   No restocking fees. No fine print. Buyer pays return shipping."
  Conditions: Resalable condition + original packaging. Gift box foam tray intact.
  Defective items: We cover return shipping. Personal preference: Buyer covers.
  Process: Email survival72bob@gmail.com with order number. Reply within 12h.
  Refund: Within 5 business days. COD orders: original payment method or bank transfer.
  All contact email: survival72bob@gmail.com
```

### 6.2 Shipping Policy (`/pages/shipping-policy`)

```
Title: Shipping Policy — 48h Fulfillment
  Processing: 48h | Cut-off: 14:00 GST | Fri: 12:00
  All tracked + insured.

  Rate Table:
  +--------------+----------+-----------+--------+----------+
  | Region       | Standard | Express   | Free > | Time     |
  +--------------+----------+-----------+--------+----------+
  | UAE          | AED 45   | AED 45    | AED 350| 8-12 day |
  | Saudi Arabia | AED 60   | AED 65    | AED 500| 8-12 day |
  | Kuwait       | AED 60   | AED 75    | AED 550| 8-12 day |
  | Qatar        | AED 60   | AED 75    | AED 550| 8-12 day |
  | Oman         | AED 60   | AED 75    | AED 550| 8-12 day |
  | Bahrain      | AED 60   | AED 75    | AED 550| 8-12 day |
  | Europe       | €15      | €35       | €150   | 8-12 day |
  | North America| $15      | $30       | $150   | 8-12 day |
  | Asia-Pacific | $20      | $40       | $200   | 8-12 day |
  +--------------+----------+-----------+--------+----------+

  COD available: UAE + Saudi Arabia only.
```

### 6.3 Warranty (`/pages/warranty`)

```
Title: 2-Year Unconditional Guarantee — 2年质保
Content:
  "If it breaks under normal use within 2 years, we replace it.
   No warranty card. No debates."

  OR: 40% off a re-purchase (buyer pays shipping).

  Covered: Manufacturing defects, material failure, functional breakage under intended use.
  NOT covered: Loss/theft, cosmetic wear (scratches, patina), fire/flood/combat damage.

  Claim: Email survival72bob@gmail.com with photo.
         Replacement shipped within 48h — BEFORE you return the original.
```

### 6.4 Privacy Policy (`/pages/privacy-policy`)

```
Title: Privacy Policy — Your Data, Your Trust
Content:
  We collect: Name, shipping address, email, phone (required for GCC courier contact).
  We NEVER: Sell/rent data. Share except for order fulfillment. Store payment details.
  We DO: Order updates + optional promos. Unsubscribe link in every email.
          Delete data within 30 days on request.
```

### 6.5 Terms of Service (`/pages/terms-of-service`)

Standard ecommerce terms page. Include: order acceptance, pricing, liability limits, governing law (UAE).

### 6.6 B2B & Government Procurement (`/pages/wholesale`)

```
Title: B2B & Government Procurement
Content:
  Clients: Govt agencies, security contractors, corporate gift programs across GCC.
  MOQ: Tiered discount starting at 25 units.
  Custom: Laser-engrave your agency/company logo on every tool.
  Packaging: Magnetic gift box + custom inlay per unit.
  Fulfillment: Bulk orders ship within 5 business days.
  Payment: Government PO accepted — standard procurement workflow.

  Procurement Process (5 steps):
    1. Inquiry → Email survival72bob@gmail.com
    2. Quote → Formal quotation within 24h (weekdays)
    3. Sample → Complimentary evaluation kit
    4. PO & Production → Begins immediately
    5. Delivery → Air freight + full tracking

  Industries: Security & Defense · Infrastructure · Emergency Response · Gifting · Diplomatic
  All contact: survival72bob@gmail.com
```

### 6.7 Military & First Responder Discount (`/pages/military-discount`)

```
Title: Military & First Responder Discount — 10% Off
Content:
  Discount: 10% off all orders.
  Eligible: Active military, law enforcement, firefighters, EMS.
  Verification: GOVX ID verification — prompt appears at checkout.
  How GOVX works:
    1. Click the GOVX verification link at checkout
    2. Sign in or create a GOVX ID account
    3. Verify your military/first responder status
    4. Discount auto-applied to your cart
```

### 6.8 Order Cancellation (`/pages/cancellation-policy`)

```
Title: Order Cancellation
Content:
  Orders processed immediately after confirmation.
  Once in fulfillment (~2h), cannot be cancelled.
  After shipment: follow the standard return process.
  All contact: survival72bob@gmail.com
```

### 6.9 Contact (`/pages/contact`)

```
Title: Contact Survival72
Content:
  Email: survival72bob@gmail.com
  Response: Within 12h

  Form fields: Name, Email, Order Number (optional), Message
  On submit: POST to form handler / email API. Show success toast: "Thanks! We'll reply within 12h."
```

---

## 7. NEW: MEMBER SYSTEM

### 7.1 Overview
A lightweight customer account system that lets users:
- Sign up / Sign in with email + password
- View order history from a single dashboard
- Track shipments by order
- Apply GOVX military discount via verification

### 7.2 Database Schema

**Table: `users`**
| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Unique user identifier |
| `email` | VARCHAR(255) UNIQUE | Login email |
| `password_hash` | VARCHAR(255) | Bcrypt-hashed password |
| `name` | VARCHAR(255) | Display name |
| `phone` | VARCHAR(50) | For GCC courier contact |
| `address` | TEXT | Shipping address |
| `govx_verified` | BOOLEAN default false | GOVX ID verified flag |
| `govx_id` | VARCHAR(100) | GOVX user ID reference |
| `created_at` | TIMESTAMP | Account creation date |

### 7.3 Auth Pages

**Page: `/account/login`**
```
Layout: Centered card (max-width 400px), dark minimal background (#111).
Fields: Email + Password + [Sign In] button.
Links: "Forgot password?" → /account/reset-password
       "Create account" → /account/register
```

**Page: `/account/register`**
```
Layout: Same centered card style.
Fields: Name, Email, Password, Confirm Password + [Create Account] button.
After registration: auto-sign-in → redirect to /account.
```

**Page: `/account` — Unified Member Dashboard**

Protected route (requires authentication). Single-page dashboard with tabbed navigation.

```
┌──────────────────────────────────────────────────────────┐
│ 👤 Welcome back, Ahmed        [GOVX Verified ✓]          │
├──────────────────────────────────────────────────────────┤
│ [My Cart] [My Orders] [Tracking] [Profile] [Settings]    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│   (Active tab content renders here)                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**5 Tabs:**

**Tab 1 — My Cart (persistent across devices)**
```
Shows the user's active shopping cart — synced with Shopify cart.

  ┌───────────────────────────────────────────────────────┐
  │ MY CART                                     (3 items) │
  │                                                       │
  │ [Pliers image]  Precision Multi-Pliers         $52    │
  │                 × 1        [Remove]                   │
  │ ───────────────────────────────────────────────────── │
  │ [Wrench image]  Roadside Wrench                $42    │
  │                 × 1        [Remove]                   │
  │ ───────────────────────────────────────────────────── │
  │ [Axe image]     Desert Breacher Axe            $49    │
  │                 × 1        [Remove]                   │
  │ ───────────────────────────────────────────────────── │
  │ [Gift Box img]  Elite Magnetic Gift Box  +$29 (locked)│
  │ ───────────────────────────────────────────────────── │
  │                                   Subtotal:   $143    │
  │                     Military Discount 10%:  -$14.30   │
  │                                   Shipping:   Free    │
  │                                   ────────────────    │
  │                                   TOTAL:      $128.70 │
  │                                                       │
  │                    [Continue Shopping] [Checkout ▸]    │
  └───────────────────────────────────────────────────────┘

  - Cart data stored in localStorage + synced to Supabase on login
  - On click "Checkout" → redirects to Shopify checkout with cart items
  - "Continue Shopping" → /pages/shop-the-kit
```

**Tab 2 — My Orders (paid + processing)**
```
  Filter: [All] [Processing] [Shipped] [Delivered] [Cancelled]

  Table columns:
  Order #  | Date      | Items           | Total   | Status   | Action
  ─────────┼───────────┼─────────────────┼─────────┼──────────┼─────────
  #1021    | May 12    | Pliers + Gift   | $81     | Shipped  | [Track]
  #1009    | May 08    | Axe             | $49     | Deliv'd  | [View]
  #0995    | May 01    | Full Kit        | $145    | Proc'ing | [View]

  Click [Track] → jumps to Tab 3 (Tracking) pre-filled with that order
  Click [View]  → expands inline with order line items + tracking timeline
  Click row → expands showing:
    - Line items (name, qty, unit price, image thumbnail)
    - Shipping address
    - Payment method (COD / Card)
    - Timeline: Ordered → Confirmed → Processing → Shipped → Delivered
```

**Tab 3 — Real-Time Logistics Tracking**
```
  ┌──────────────────────────────────────────────────────────┐
  │ TRACKING: Order #1021                         [Refresh]  │
  │ Courier: Aramex  |  Tracking #: ARX-20240512-0091       │
  │ ETA: May 18–20                                          │
  │ ────────────────────────────────────────────────────────│
  │                                                         │
  │   ● Order Confirmed       May 12  14:00  Dubai          │
  │   │                                                      │
  │   ● Processing Complete   May 12  18:30  Warehouse      │
  │   │                                                      │
  │   ● Picked Up by Courier  May 13  09:15  Dubai Hub      │
  │   │                                                      │
  │   ● In Transit            May 14  06:00  Riyadh SC       │
  │   │                                                      │
  │   ○ Out for Delivery       Est. May 18                   │
  │   │                                                      │
  │   ○ Delivered              Est. May 18–20                │
  │                                                         │
  │   ┌─────────────────────────────────────────────────┐   │
  │   │        Google Maps Embed (route Dubai→Riyadh)    │   │
  │   │              📍 Current location marker           │   │
  │   └─────────────────────────────────────────────────┘   │
  │                                                         │
  │   External: [Track on Aramex.com →]                     │
  └──────────────────────────────────────────────────────────┘

  Real-time refresh:
  - Every 60 seconds, polls GET /api/tracking/{order_id}
  - If new tracking event received → animate timeline dot from ○ → ●
  - Last event pulses green to draw attention
  - "Live" badge in top-right corner when within 60s of last update

  Tracking data source:
  - Option A: Fetch from Shopify Fulfillment API per-order
  - Option B: Webhook from Aramex/DHL → insert into tracking_events table
  - Option C (MVP): Admin manually updates status via dashboard,
                  customer sees a simple polling-based UI
```

**Tab 4 — My Profile**
```
  ┌───────────────────────────────────────────────────────┐
  │ PROFILE                                               │
  │                                                       │
  │ Name:    [Ahmed Al-Rashid           ] [Save]          │
  │ Email:   [ahmed@email.com           ] [Save]          │
  │ Phone:   [+971 50 123 4567          ] [Save]          │
  │ Address: [Villa 12, Jumeirah 1       ] [Save]          │
  │          [Dubai, UAE                 ]                 │
  │                                                       │
  │ ─────────────────────────────────────────────────────  │
  │ GOVX Military Status: ✓ Verified (10% active)          │
  │ Member since: April 2026                               │
  │ Total orders: 5  |  Total spent: AED 2,140             │
  └───────────────────────────────────────────────────────┘
```

**Tab 5 — Settings**
```
  Language: [English ▾]
  Currency: [AED ▾]
  Browsing Direction: [Auto ▾] (LTR/RTL)
  Email Notifications: [✓] Order updates  [✓] Promotions
  [Delete Account] (red, with confirmation modal)
```

### 7.4 Auth Implementation (Frontend)

Use **Supabase Auth** (simplest for Lovable):
1. Install `@supabase/supabase-js`
2. Create Supabase project, get `anon_key` + `project_url`
3. Use `supabase.auth.signUp()` / `signInWithPassword()` / `signOut()`
4. Protect routes with auth context (React Context or vanilla JS auth check)

### 7.5 GOVX ID Verification Flow

```
User clicks "Verify with GOVX ID" on /account page
  ↓
GOVX OAuth popup opens → user logs into GOVX
  ↓
GOVX returns: { govx_user_id, status: "verified", affiliation: "military" }
  ↓
Save to users.govx_verified = true, users.govx_id = returned_id
  ↓
User sees gold badge + 10% discount auto-applied at checkout
  ↓
At checkout: if user.govx_verified → auto-apply 10% to cart total
```

---

## 8. NEW: ORDER SYSTEM

### 8.1 Overview
Customer-facing order management integrated with Shopify data. Users see their orders in the account dashboard.

### 8.2 Data Flow

```
Shopify Admin (source of truth)
  ↓ Webhook: order/create, order/fulfill, order/update
  ↓ Or: fetch via Shopify Admin API GraphQL
  ↓
Local DB: orders table (syncs from Shopify)
  ↓
Frontend: /account → My Orders section
```

### 8.3 Database Schema

**Table: `orders`**
| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Local order ID |
| `shopify_order_id` | VARCHAR(50) | Shopify order number (e.g. #1004) |
| `user_id` | UUID FK→users | Customer foreign key |
| `status` | VARCHAR(30) | processing / shipped / in_transit / out_for_delivery / delivered / cancelled |
| `subtotal` | DECIMAL(10,2) | Order total before discounts |
| `discount` | DECIMAL(10,2) | GOVX or promo discount |
| `total_price` | DECIMAL(10,2) | Final order total |
| `currency` | VARCHAR(3) | AED / USD / EUR |
| `payment_method` | VARCHAR(30) | cod / card |
| `shipping_address` | TEXT | Customer shipping address (JSON) |
| `tracking_number` | VARCHAR(100) | Courier tracking code |
| `tracking_url` | VARCHAR(500) | Direct link to courier tracking page |
| `courier` | VARCHAR(50) | Aramex / DHL / FedEx |
| `eta_min` | DATE | Earliest estimated delivery |
| `eta_max` | DATE | Latest estimated delivery |
| `created_at` | TIMESTAMP | Order date |
| `updated_at` | TIMESTAMP | Last status change |

**Table: `order_items`**
| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Line item ID |
| `order_id` | UUID FK→orders | Parent order |
| `product_name` | VARCHAR(255) | Product title |
| `variant_name` | VARCHAR(100) | e.g. "Pliers + Wrench" |
| `quantity` | INT | Units ordered |
| `unit_price` | DECIMAL(10,2) | Price per unit |
| `image_url` | VARCHAR(500) | Product thumbnail |

### 8.4 Shopify Integration

If using Shopify as ecommerce backend:
- **Option A (Recommended):** Fetch orders via Shopify Storefront API with customer access token
  - User logs in → get `customerAccessToken` → query `customer.orders` GraphQL
  - No local DB needed — real-time Shopify data
- **Option B:** Webhook → local DB sync
  - Register webhook URL in Shopify Admin → receive `orders/create`, `orders/fulfilled` events
  - Store in Supabase/Postgres `orders` table
- **Option C (Simplest for Lovable):** Direct Shopify embed
  - Use Shopify Buy Button cart + Shopify's built-in customer accounts
  - `/account` links to Shopify-native account page

### 8.5 UI: My Orders Table

```
┌──────────────────────────────────────────────────────────────┐
│ MY ORDERS                                                    │
│                                                              │
│ Order #    Date        Status        Total     Action         │
│ ──────────────────────────────────────────────────────────── │
│ #1004      May 10     ● Shipped     $145      [Track ▸]      │
│ #0998      May 03     ✓ Delivered   $52       [Track ▸]      │
│ #0987      Apr 28     ⌧ Cancelled   $79       [View ▸]       │
└──────────────────────────────────────────────────────────────┘
```

Status badges: Green "Shipped", Blue "Processing", Gray "Cancelled", Gold "Delivered".

---

## 9. NEW: LOGISTICS TRACKING SYSTEM

### 9.1 Overview
Real-time shipment tracking embedded directly in the member dashboard (Tab 3). Customer sees a live-updating timeline + map with courier data. No need for a standalone tracking page — it's all in the unified `/account` dashboard for a seamless experience.

### 9.2 How Real-Time Tracking Works

```
Data flow:
  1. Admin updates order status in Shopify → triggers webhook
  2. Webhook inserts row into tracking_events table
  3. Frontend polls GET /api/tracking/{order_id} every 60s
  4. New event detected → UI auto-animates timeline
  5. Map marker moves to latest location
```

### 9.3 Real-Time Update Logic (JavaScript)

```javascript
// On member dashboard Tab 3 load:
let lastEventId = null;

async function pollTracking(orderId) {
  const res = await fetch(`/api/tracking/${orderId}`);
  const { events } = await res.json();

  // If new events since last poll:
  const newEvents = events.filter(e => !lastEventId || e.id > lastEventId);
  if (newEvents.length > 0) {
    lastEventId = events[events.length - 1].id;
    // Animate new timeline dots from ○ → ● (pulse green)
    newEvents.forEach(e => animateTimelineDot(e));
    // Update map marker
    if (e.location_coords) updateMapMarker(e.location_coords);
    // Flash "Live" badge
    flashLiveBadge();
  }
}

// Start polling when tab becomes active
document.querySelector('[data-tab="tracking"]').addEventListener('click', () => {
  pollTracking(currentOrderId);
  trackingInterval = setInterval(() => pollTracking(currentOrderId), 60000);
});

// Stop polling when leaving tab
document.querySelectorAll('[data-tab]:not([data-tab="tracking"])').forEach(tab => {
  tab.addEventListener('click', () => clearInterval(trackingInterval));
});
```

### 9.4 Database: `tracking_events`

| Column | Type | Description |
|--------|------|-------------|
| `id` | SERIAL (PK) | Auto-increment event ID (used for "new since" detection) |
| `order_id` | UUID FK→orders | Parent order |
| `status` | VARCHAR(50) | confirmed / processing / picked_up / in_transit / out_for_delivery / delivered |
| `location` | VARCHAR(255) | e.g. "Dubai Sort Center, UAE" |
| `location_coords` | POINT or JSON | `{lat: 25.2048, lng: 55.2708}` |
| `timestamp` | TIMESTAMPTZ | Event time (with timezone) |
| `courier` | VARCHAR(50) | Aramex / DHL / FedEx |
| `note` | TEXT | Optional detail (e.g., "Package handed to driver") |
| `created_at` | TIMESTAMPTZ DEFAULT now() | Record creation time |

### 9.5 API Endpoint

```
GET /api/tracking/{order_id}
Auth: Bearer token (Supabase session)

Response 200:
{
  "order_id": "uuid",
  "tracking_number": "ARX-20240512-0091",
  "tracking_url": "https://www.aramex.com/track/ARX-20240512-0091",
  "courier": "Aramex",
  "eta": { "min": "2026-05-18", "max": "2026-05-20" },
  "events": [
    {
      "id": 1,
      "status": "confirmed",
      "location": "Dubai, UAE",
      "coords": { "lat": 25.2048, "lng": 55.2708 },
      "timestamp": "2026-05-12T14:00:00+04:00",
      "note": null
    },
    {
      "id": 2,
      "status": "picked_up",
      "location": "Dubai Hub, UAE",
      "coords": { "lat": 25.2528, "lng": 55.3644 },
      "timestamp": "2026-05-13T09:15:00+04:00",
      "note": "Package handed to driver"
    }
  ],
  "is_live": true   // true if last event < 60 minutes ago
}
```

### 9.6 Map Implementation

```html
<!-- Google Maps Embed with route polyline -->
<div id="tracking-map" style="width:100%; height:300px; border-radius:8px;"></div>

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
<script>
function initTrackingMap(events) {
  const map = new google.maps.Map(document.getElementById('tracking-map'), {
    zoom: 6,
    center: { lat: 25.0, lng: 47.0 }, // Centered on GCC
  });

  // Draw route polyline connecting all events
  const path = events
    .filter(e => e.coords)
    .map(e => ({ lat: e.coords.lat, lng: e.coords.lng }));
  new google.maps.Polyline({ path, geodesic: true,
    strokeColor: '#1A1A1A', strokeOpacity: 0.8, strokeWeight: 2
  }).setMap(map);

  // Place markers
  events.filter(e => e.coords).forEach((e, i) => {
    const marker = new google.maps.Marker({
      position: { lat: e.coords.lat, lng: e.coords.lng },
      map,
      label: i === events.length - 1 ? '📍' : '',
      title: `${e.status} — ${e.location}`
    });
    if (i === events.length - 1) {
      // Pulse animation on latest marker (CSS keyframe on marker icon)
      marker.setAnimation(google.maps.Animation.BOUNCE);
      setTimeout(() => marker.setAnimation(null), 2000);
    }
  });
}
</script>
```

### 9.7 MVP Fallback

If Shopify webhook + map integration is too complex for initial Lovable build:

**Simplified approach:**
1. Use `tracking_events` table with manual admin entry (via a simple `/admin/tracking` page)
2. Map: use a static Google Maps image with markers (`/staticmap` API, no JS)
3. Timeline: still rendered from DB data — this is the core user value
4. Polling: still works, just with manually entered data
5. Upgrade to webhook/courier API later

---

## 10. GOVX ID VERIFICATION SYSTEM

### 10.1 What It Is
GOVX ID is a third-party verification service that confirms military, law enforcement, firefighter, and EMS affiliation. It issues a verified badge that ecommerce sites can trust for discount eligibility.

### 10.2 Integration Steps

```
1. Register at GOVX.com/business → get API credentials
2. Add GOVX button to checkout flow
3. User clicks → GOVX popup → authenticates
4. GOVX returns verification token
5. Store token in user.govx_verified = true
6. Apply 10% discount to cart total if user.govx_verified
```

### 10.3 UI: Checkout Discount Entry Point

```
At checkout page (/cart or /checkout):

  ┌────────────────────────────────────────────┐
  │ Military / First Responder?                │
  │ [Verify with GOVX ID →]     Get 10% off   │
  └────────────────────────────────────────────┘

After verification:
  ┌────────────────────────────────────────────┐
  │ ✓ Military Discount Active — 10% applied   │
  └────────────────────────────────────────────┘
```

### 10.4 GOVX Auth Flow (Frontend)

```javascript
// On "Verify with GOVX ID" click:
const govxWindow = window.open('https://verify.govx.com/oauth/authorize?...', 'govx', 'width=500,height=600');

// GOVX redirects back with ?code=xxx
// Exchange code for token via your backend
const { govx_user_id, affiliation } = await verifyGovxCode(code);

// Update user record
await supabase.from('users').update({
  govx_verified: true,
  govx_id: govx_user_id
}).eq('id', currentUser.id);

// Show gold badge, apply discount
```

### 10.5 Discount Application Logic

```
At checkout total calculation:
  if (currentUser && currentUser.govx_verified) {
    subtotal = cartTotal;
    discount = subtotal * 0.10;
    total = subtotal - discount;
    showLineItem("Military Discount (10%)", "-$" + discount);
  }
```

---

## 11. RESPONSIVE BREAKPOINTS

| Breakpoint | Behavior |
|------------|----------|
| **> 768px** | Full desktop layout |
| **768px** | s72-system: cards stack to 1 column; gift block stacks vertically |
| **700px** | Kit page: 2-col becomes single column (preview above cards) |
| **600px** | s72-proof stats: 4-col → 2-col |
| **Mobile** | ≈ 375-430px — hamburger nav, stacked layouts, full-width sections |

---

## 12. PRODUCT IMAGES TO PREPARE

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

## 13. ANIMATIONS & TRANSITIONS

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

## 14. INTERACTION SUMMARY (JavaScript Behaviors)

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
 5. **Gift Box:**
    - Thumbnail hover → preview image swap (same as product cards)
    - "View Large Image ⤢" click → fullscreen lightbox
    - "View Details" click → slide-up gift drawer with gallery + video + specs
    - Admin Edit Mode → "+" button appears on each image/video slot
    - Admin click "+" → native file picker → upload to Supabase Storage
 6. **Language Switcher:**
    - Dropdown select → reload all `data-i18n` strings instantly
    - Persist choice to `localStorage`
    - Auto-detect from `navigator.language` on first visit
    - Arabic selects auto-apply RTL direction
 7. **RTL Mode:**
    - `html[dir="rtl"]` → entire layout mirrors
    - Arabic fonts load (Cairo, Noto Naskh Arabic, Tajawal)
    - All CSS logical properties handle margin/padding/border/float flip
 8. **Mobile responsive:** All components collapse/restack below breakpoints

---

## 15. BUILD ORDER (Lovable Implementation Sequence)

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
| 11 | **Gift Box Detail Page** + Admin Upload System | §5.11, Supabase Storage + product_assets table |
| 12 | **Policy pages** (Return, Shipping, Warranty, Privacy, B2B, Military, Cancellation, Contact) | None (text content ready) |
| 13 | **Multi-Language System** (i18n: en/ar/zh) | §17, i18next library, JSON translation files |
| 14 | **Auth system** (Signup, Login, Account dashboard) | Supabase project |
| 15 | **Order system** (My Orders table, order detail view) | Auth + Shopify data |
| 16 | **Logistics tracking** (Tracking page with timeline + map) | Order data |
| 17 | **GOVX ID verification** (GOVX button, verification flow, discount logic) | Auth system |
| 18 | **RTL Middle East Browsing Mode** | §18, Arabic fonts, CSS logical properties, rtl.css |
| 19 | Responsive testing + polish | All |
| 20 | Cart integration | Shopify API or localStorage |

---

## 16. SINGLE CONTACT EMAIL (Global)

All customer-facing email references point to: **survival72bob@gmail.com**

| Page | Email |
|------|-------|
| Return Policy | survival72bob@gmail.com |
| Warranty Claims | survival72bob@gmail.com |
| B2B Inquiries | survival72bob@gmail.com |
| Contact Page | survival72bob@gmail.com |
| Order Issues | survival72bob@gmail.com |

---

## 17. MULTI-LANGUAGE SYSTEM (i18n)

### 17.1 Supported Languages

| Code | Language | Direction | Default |
|------|----------|-----------|---------|
| `en` | English | LTR | ✅ |
| `ar` | Arabic (العربية) | **RTL** | — |
| `zh` | Chinese (简体中文) | LTR | — |

### 17.2 Language Switcher UI

A dropdown in the **top-right corner of the header**, next to the account icon:

```
┌──────────────────────┐
│ 🌐  English    ▾     │
│     العربية          │
│     简体中文          │
└──────────────────────┘
```

On mobile: icon-only (🌐 globe icon), tap to show dropdown.

**Behavior:**
- Selection persists in `localStorage('s72-lang')`
- On page load, auto-detect from `navigator.language` if no saved preference
- Switching language reloads all visible UI strings instantly (no page refresh)

### 17.3 Implementation Approach: JSON Translation Files

**Use `i18next`** (lightweight, framework-agnostic, RTL-aware):

```
/public/locales/
  en/
    common.json
    homepage.json
    kit.json
    policy.json
    account.json
  ar/
    common.json
    homepage.json
    kit.json
    policy.json
    account.json
  zh/
    common.json
    homepage.json
    kit.json
    policy.json
    account.json
```

### 17.4 Translation File Structure (example: `en/common.json`)

```json
{
  "nav": {
    "shop": "Shop",
    "about": "About",
    "wholesale": "Wholesale",
    "contact": "Contact"
  },
  "buttons": {
    "add_to_cart": "Add to Cart",
    "view_details": "View Details",
    "shop_now": "Shop Now",
    "build_kit": "Build Your Kit"
  },
  "currency": {
    "aed": "AED",
    "usd": "USD",
    "eur": "EUR"
  },
  "marquee": {
    "tools_system": "3 Tools · 1 System",
    "ships_48h": "Ships Within 48h",
    "guarantee_2yr": "2-Year Guarantee",
    "gift_ready": "Gift-Ready Packaging",
    "free_shipping": "Free Shipping Over $100"
  },
  "footer": {
    "rights": "© 2024 Survival72. All rights reserved.",
    "return_policy": "Return Policy",
    "shipping": "Shipping",
    "warranty": "Warranty",
    "privacy": "Privacy",
    "terms": "Terms"
  }
}
```

### 17.5 Translation File Structure (example: `ar/common.json`)

```json
{
  "nav": {
    "shop": "المتجر",
    "about": "حول",
    "wholesale": "الجملة",
    "contact": "اتصل بنا"
  },
  "buttons": {
    "add_to_cart": "أضف إلى السلة",
    "view_details": "عرض التفاصيل",
    "shop_now": "تسوق الآن",
    "build_kit": "بناء مجموعتك"
  },
  "currency": {
    "aed": "درهم",
    "usd": "دولار",
    "eur": "يورو"
  },
  "marquee": {
    "tools_system": "٣ أدوات · نظام واحد",
    "ships_48h": "يشحن خلال ٤٨ ساعة",
    "guarantee_2yr": "ضمان سنتين",
    "gift_ready": "جاهز للإهداء",
    "free_shipping": "شحن مجاني للطلبات فوق ١٠٠$"
  },
  "footer": {
    "rights": "© ٢٠٢٤ Survival72. جميع الحقوق محفوظة.",
    "return_policy": "سياسة الإرجاع",
    "shipping": "الشحن",
    "warranty": "الضمان",
    "privacy": "الخصوصية",
    "terms": "الشروط"
  }
}
```

### 17.6 Translation File Structure (example: `zh/common.json`)

```json
{
  "nav": {
    "shop": "商城",
    "about": "关于",
    "wholesale": "批发",
    "contact": "联系"
  },
  "buttons": {
    "add_to_cart": "加入购物车",
    "view_details": "查看详情",
    "shop_now": "立即购买",
    "build_kit": "定制套装"
  },
  "currency": {
    "aed": "迪拉姆",
    "usd": "美元",
    "eur": "欧元"
  },
  "marquee": {
    "tools_system": "三合一 · 模块系统",
    "ships_48h": "48小时内发货",
    "guarantee_2yr": "2年质保",
    "gift_ready": "礼盒包装",
    "free_shipping": "满 $100 免运费"
  },
  "footer": {
    "rights": "© 2024 Survival72. 版权所有。",
    "return_policy": "退换政策",
    "shipping": "配送",
    "warranty": "保修",
    "privacy": "隐私",
    "terms": "条款"
  }
}
```

### 17.7 i18n JavaScript Integration

```html
<!-- In <head> -->
<script src="https://unpkg.com/i18next@latest/i18next.min.js"></script>
<script src="https://unpkg.com/i18next-http-backend@latest/i18nextHttpBackend.min.js"></script>
```

```javascript
// i18n-init.js
i18next
  .use(i18nextHttpBackend)
  .init({
    lng: localStorage.getItem('s72-lang') || navigator.language.split('-')[0] || 'en',
    fallbackLng: 'en',
    backend: { loadPath: '/locales/{{lng}}/{{ns}}.json' },
    ns: ['common', 'homepage', 'kit', 'policy', 'account'],
    defaultNS: 'common'
  }, () => {
    // Update all [data-i18n] elements
    document.querySelectorAll('[data-i18n]').forEach(el => {
      el.textContent = i18next.t(el.dataset.i18n);
    });
    // Set direction attribute
    document.documentElement.dir = i18next.dir();
    document.documentElement.lang = i18next.language;
  });

// Language switcher handler
document.getElementById('lang-switcher').addEventListener('change', (e) => {
  const lang = e.target.value;
  i18next.changeLanguage(lang, () => {
    localStorage.setItem('s72-lang', lang);
    document.documentElement.dir = i18next.dir();
    document.documentElement.lang = lang;
    updateAllTexts(); // Re-render all i18n-bound text
  });
});
```

### 17.8 HTML Markup Pattern

Every user-visible string uses `data-i18n` attribute:

```html
<!-- Before: hardcoded text -->
<button>Add to Cart</button>

<!-- After: i18n-ready -->
<button data-i18n="buttons.add_to_cart">Add to Cart</button>
```

For dynamic content (like the kit configurator title):

```html
<h1 data-i18n="kit.title">Survival72™ Modular System</h1>
<p data-i18n="kit.subtitle">Build your kit.</p>
```

---

## 18. RTL (RIGHT-TO-LEFT) MIDDLE EAST BROWSING MODE

### 18.1 Trigger

Activated automatically when user selects **Arabic (العربية)** language. Also exposed as an independent toggle in settings:

```
Settings → Browsing Direction → LTR / RTL
```

Default: auto (follows language choice — Arabic = RTL, English/ZH = LTR).

### 18.2 Global RTL CSS Override

```css
/* rtl.css — loaded only when dir="rtl" on <html> */
html[dir="rtl"] {
  /* Mirror the entire layout */
  direction: rtl;
  text-align: right;
  font-family: 'Helvetica Neue', 'Noto Naskh Arabic', 'Cairo', Arial, sans-serif;
}

/* Flip horizontal layouts */
html[dir="rtl"] .s72-grid,
html[dir="rtl"] .s72-proof__stats,
html[dir="rtl"] .s72-edu__grid,
html[dir="rtl"] .gallery-grid,
html[dir="rtl"] .video-grid {
  direction: rtl;
}

/* Mirror navigation */
html[dir="rtl"] .nav-menu {
  flex-direction: row-reverse;
}

/* Mirror kit configurator layout */
html[dir="rtl"] .kit-main-layout {
  /* Left (RTL) = preview | Right (RTL) = product cards */
  grid-template-columns: 1fr 1fr;
  /* No flip needed if using CSS logical properties */
}

/* Use logical properties for margins & paddings */
html[dir="rtl"] .product-card {
  margin-left: 0;
  margin-right: 16px;
}

html[dir="rtl"] .s72-btn {
  /* Logical padding */
  padding-inline: 48px;
  padding-block: 18px;
}

/* Flip icons that have direction */
html[dir="rtl"] .arrow-right {
  transform: scaleX(-1);
}

html[dir="rtl"] .drawer-close {
  right: auto;
  left: 16px;
}

/* Mirror the marquee direction */
html[dir="rtl"] .marquee-track {
  animation-direction: reverse;
}

/* RTL-specific: Arabic numbers rendering */
html[dir="rtl"] .price,
html[dir="rtl"] .stat-number {
  /* Arabic numerals will render as هندسة (٠١٢٣) */
  unicode-bidi: plaintext;
}

/* Flip lightbox close button position */
html[dir="rtl"] .lb-close {
  right: auto;
  left: 24px;
}

/* Admin upload button position */
html[dir="rtl"] .admin-upload-btn {
  right: auto;
  left: 8px;
}
```

### 18.3 CSS Logical Properties (Preferred over RTL-specific rules)

**Always prefer CSS logical properties** — they automatically adapt to `dir="rtl"` without extra CSS:

| Physical (Avoid) | Logical (Use) |
|-----------------|---------------|
| `margin-left` | `margin-inline-start` |
| `margin-right` | `margin-inline-end` |
| `padding-left` | `padding-inline-start` |
| `padding-right` | `padding-inline-end` |
| `text-align: left` | `text-align: start` |
| `text-align: right` | `text-align: end` |
| `border-left` | `border-inline-start` |
| `border-right` | `border-inline-end` |
| `left` | `inset-inline-start` |
| `right` | `inset-inline-end` |
| `float: left` | `float: inline-start` |
| `float: right` | `float: inline-end` |

### 18.4 Arabic Typography Stack

```css
body[lang="ar"] {
  font-family:
    'Noto Naskh Arabic',   /* Google Font — excellent readability */
    'Cairo',                /* Clean sans-serif Arabic */
    'Tajawal',              /* Modern, geometric Arabic */
    'Segoe UI',             /* Windows Arabic fallback */
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;          /* Slightly larger for Arabic legibility */
  line-height: 1.8;         /* Arabic needs more line height */
}
```

### 18.5 Google Fonts to Load

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Noto+Naskh+Arabic:wght@400;600;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
```

### 18.6 RTL-Aware i18next Configuration

```javascript
// i18next auto-detects RTL from the language code
i18next.init({
  lng: 'ar',
  // i18next.dir('ar') returns 'rtl' automatically
});

document.documentElement.dir = i18next.dir();
```

### 18.7 RTL Preview: What the Customer Sees

When browsing in Arabic mode:
- Header: Logo on right, nav flows right-to-left, language switcher on left
- Homepage: All sections mirrored — hero text right-aligned, cards flow RTL
- Kit Configurator: Product cards on right, preview image on left (mirrored from LTR)
- Drawers: slide from right side for consistency
- Lightbox: close button top-left instead of top-right
- Buttons: "Add to Cart" reads أضف إلى السلة (right-to-left)
- Numbers: Use Arabic-Indic digits (٠١٢٣) in Arabic mode ← toggleable setting

### 18.8 RTL Testing Checklist

- [ ] Navigation mirror ✓
- [ ] Hero text right-aligned ✓
- [ ] Product card grid flows RTL ✓
- [ ] Kit configurator mirrored layout ✓
- [ ] Drawer slides from correct side ✓
- [ ] Lightbox buttons positioned correctly ✓
- [ ] All icons that imply direction are flipped ✓
- [ ] Arabic text is readable (no broken joins) ✓
- [ ] Arabic numbers render correctly ✓
- [ ] Mobile hamburger menu works ✓
- [ ] English/Chinese switching back to LTR works ✓
- [ ] Mixed content (Arabic + English numbers) displays correctly ✓

---

---
## 20. BLOG SYSTEM — SEO-OPTIMIZED CONTENT HUB

### 20.1 Overview
A full-featured blog platform accessible at `/blog`. Designed for publishing professional EDC/preparedness articles, tutorial videos, and gear reviews — **engineered for Google organic traffic capture** via proper SEO metadata, structured data, sitemap integration, and fast Core Web Vitals.

### 20.2 Blog Architecture

```
/blog                        → Blog listing page (paginated, 9 posts/page)
/blog/category/{slug}        → Filter by category
/blog/{year}/{month}/{slug}  → Single article page (SEO-friendly URL)
```

### 20.3 Blog Home (`/blog`)

```
Layout:
┌──────────────────────────────────────────────────────────┐
│  BLOG — The Field Guide                                   │
│  Expert EDC tips, survival tactics, and gear deep-dives.  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ [Featured    │  │ [Featured    │  │ [Latest      │   │
│  │  Post Card]  │  │  Post Card]  │  │  Post Card]  │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ [Post Card]  │  │ [Post Card]  │  │ [Post Card]  │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                          │
│  ← Previous   Page 1 of 3   Next →                       │
│                                                          │
│  ─── SIDEBAR (right column, desktop only) ───            │
│  Categories: [EDC] [Survival] [Gear] [Tactical]          │
│  Popular posts: Top 5 by page views                      │
│  Newsletter signup: "Get weekly field tips" + email input│
└──────────────────────────────────────────────────────────┘
```

**Post Card (blog listing):**
```html
<article class="blog-card">
  <a href="/blog/2026/05/how-to-choose-edc-pliers">
    <img src="..." alt="EDC pliers comparison" loading="lazy" width="400" height="267" />
    <span class="blog-card__category">EDC</span>
    <h2 class="blog-card__title">How to Choose EDC Pliers: 5 Factors Most People Miss</h2>
    <p class="blog-card__excerpt">Not all pliers are built for everyday carry. Here's what to look for in grip, steel, and portability...</p>
    <div class="blog-card__meta">
      <span>May 12, 2026</span>
      <span>·</span>
      <span>4 min read</span>
    </div>
  </a>
</article>
```

**Blog Card CSS:**
```css
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 32px;
  padding: 40px 0;
}
.blog-card {
  border: 1px solid var(--color-border);
  border-radius: 6px;
  overflow: hidden;
  transition: box-shadow 0.2s;
}
.blog-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.08); }
.blog-card img {
  width: 100%; height: 200px;
  object-fit: cover;
}
.blog-card__category {
  display: inline-block;
  background: #1a1a1a; color: #fff;
  font-size: 10px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 1px;
  padding: 4px 10px; border-radius: 3px;
  margin: 16px 16px 0;
}
.blog-card__title {
  font-size: 18px; font-weight: 700;
  margin: 10px 16px;
  line-height: 1.35;
}
.blog-card__excerpt {
  font-size: 14px; color: #666;
  margin: 0 16px 14px;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.blog-card__meta {
  font-size: 12px; color: #999;
  margin: 0 16px 16px;
}
```

### 20.4 Single Article Page (`/blog/{year}/{month}/{slug}`)

```
Layout: Max-width 720px centered column.

  ┌───────────────────────────────────────────────┐
  │  CATEGORY: EDC                                │
  │                                               │
  │  How to Choose EDC Pliers:                    │
  │  5 Factors Most People Miss                   │
  │                                               │
  │  By Cole Mercer  ·  May 12, 2026  ·  4 min   │
  │                                               │
  │  ═══════════════════════════════════════════  │
  │                                               │
  │  [Featured Image — 1200×630, centered]        │
  │                                               │
  │  <article content — rich text with H2/H3,     │
  │   bullet lists, bold/italic, blockquotes>     │
  │                                               │
  │  ──────────────────────────────────────────   │
  │                                               │
  │  ### Video: Hands-On Pliers Comparison        │
  │  [YouTube / Vimeo embed — 16:9 responsive]    │
  │                                               │
  │  ──────────────────────────────────────────   │
  │                                               │
  │  Share: [Twitter] [Facebook] [LinkedIn]       │
  │                                               │
  │  ← Previous Post        Next Post →           │
  │                                               │
  │  Related Posts (3 cards at bottom)             │
  └───────────────────────────────────────────────┘
```

### 20.5 SEO Optimization — Complete Checklist

#### 20.5.1 Meta Tags (per article)

```html
<head>
  <!-- Primary SEO -->
  <title>How to Choose EDC Pliers: 5 Factors Most People Miss | Survival72</title>
  <meta name="description" content="Not all EDC pliers are built equal. We break down grip ergonomics, steel grades, jaw geometry, and portability — so you buy once and carry with confidence." />

  <!-- Canonical URL -->
  <link rel="canonical" href="https://survival72gear.com/blog/2026/05/how-to-choose-edc-pliers" />

  <!-- Open Graph (Facebook, LinkedIn, WhatsApp) -->
  <meta property="og:title" content="How to Choose EDC Pliers: 5 Factors Most People Miss" />
  <meta property="og:description" content="Not all EDC pliers are built equal..." />
  <meta property="og:image" content="https://survival72gear.com/images/blog/edc-pliers-guide-og.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://survival72gear.com/blog/2026/05/how-to-choose-edc-pliers" />
  <meta property="og:site_name" content="Survival72" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="How to Choose EDC Pliers: 5 Factors Most People Miss" />
  <meta name="twitter:description" content="Not all EDC pliers are built equal..." />
  <meta name="twitter:image" content="https://survival72gear.com/images/blog/edc-pliers-guide-og.jpg" />

  <!-- Article-specific -->
  <meta property="article:published_time" content="2026-05-12T08:00:00+04:00" />
  <meta property="article:modified_time" content="2026-05-12T08:00:00+04:00" />
  <meta property="article:author" content="Cole Mercer" />
  <meta property="article:section" content="EDC" />
</head>
```

#### 20.5.2 JSON-LD Structured Data (per article)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Choose EDC Pliers: 5 Factors Most People Miss",
  "description": "Not all EDC pliers are built equal. We break down grip ergonomics, steel grades, jaw geometry, and portability.",
  "image": "https://survival72gear.com/images/blog/edc-pliers-guide-og.jpg",
  "author": {
    "@type": "Person",
    "name": "Cole Mercer",
    "url": "https://survival72gear.com/about"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Survival72",
    "logo": {
      "@type": "ImageObject",
      "url": "https://survival72gear.com/logo.png"
    }
  },
  "datePublished": "2026-05-12T08:00:00+04:00",
  "dateModified": "2026-05-12T08:00:00+04:00",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://survival72gear.com/blog/2026/05/how-to-choose-edc-pliers"
  }
}
</script>
```

#### 20.5.3 BlogListing Structured Data

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Survival72 Field Guide",
  "description": "Expert EDC tips, survival tactics, and gear deep-dives for everyday preparedness.",
  "url": "https://survival72gear.com/blog",
  "publisher": {
    "@type": "Organization",
    "name": "Survival72"
  }
}
</script>
```

#### 20.5.4 BreadcrumbList Structured Data (per article)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1,
      "name": "Home", "item": "https://survival72gear.com/" },
    { "@type": "ListItem", "position": 2,
      "name": "Blog", "item": "https://survival72gear.com/blog" },
    { "@type": "ListItem", "position": 3,
      "name": "EDC", "item": "https://survival72gear.com/blog/category/edc" },
    { "@type": "ListItem", "position": 4,
      "name": "How to Choose EDC Pliers" }
  ]
}
</script>
```

#### 20.5.5 Breadcrumb UI (visible)

```html
<nav class="breadcrumb" aria-label="Breadcrumb">
  <a href="/">Home</a> ›
  <a href="/blog">Blog</a> ›
  <a href="/blog/category/edc">EDC</a> ›
  <span>How to Choose EDC Pliers</span>
</nav>
```

#### 20.5.6 Sitemap & RSS

**Dynamic XML Sitemap** (`/sitemap-blog.xml`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url>
    <loc>https://survival72gear.com/blog/2026/05/how-to-choose-edc-pliers</loc>
    <lastmod>2026-05-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://survival72gear.com/images/blog/edc-pliers-guide-og.jpg</image:loc>
      <image:caption>EDC pliers comparison guide</image:caption>
    </image:image>
  </url>
  <!-- ... more URLs -->
</urlset>
```

**RSS Feed** (`/blog/feed.xml`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Survival72 Field Guide</title>
    <link>https://survival72gear.com/blog</link>
    <description>Expert EDC tips, survival tactics, and gear deep-dives.</description>
    <atom:link href="https://survival72gear.com/blog/feed.xml" rel="self" type="application/rss+xml"/>
    <item>
      <title>How to Choose EDC Pliers: 5 Factors Most People Miss</title>
      <link>https://survival72gear.com/blog/2026/05/how-to-choose-edc-pliers</link>
      <guid>https://survival72gear.com/blog/2026/05/how-to-choose-edc-pliers</guid>
      <pubDate>Mon, 12 May 2026 08:00:00 +0400</pubDate>
      <description><![CDATA[Not all EDC pliers are built equal...]]></description>
    </item>
  </channel>
</rss>
```

#### 20.5.7 robots.txt

```
Sitemap: https://survival72gear.com/sitemap.xml
Sitemap: https://survival72gear.com/sitemap-blog.xml

User-agent: *
Allow: /
Disallow: /account/
Disallow: /admin/
```

#### 20.5.8 Internal Linking Strategy

Every product-mentioning blog post links to the product pages:
```html
<p>The <a href="/pages/shop-the-kit">Precision Multi-Pliers</a> use 420 stainless steel, which is standard for EDC tools in the $50 range.</p>
```

This creates authority flow: Blog → Product pages → improved product page ranking.

### 20.6 Database: `blog_posts`

| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Post ID |
| `slug` | VARCHAR(255) UNIQUE | URL slug (e.g., "how-to-choose-edc-pliers") |
| `title` | VARCHAR(255) | Article title (max 65 chars for SEO) |
| `excerpt` | TEXT | 150-160 char meta description |
| `content` | TEXT | Full HTML article body |
| `category` | VARCHAR(50) | EDC / Survival / Gear / Tactical / Tutorial |
| `tags` | TEXT[] | Array of tags (e.g., ["pliers","beginner","gear"]) |
| `featured_image` | VARCHAR(500) | URL to 1200×630 OG image |
| `author` | VARCHAR(100) | "Cole Mercer" |
| `status` | VARCHAR(20) | draft / published |
| `reading_time` | INT | Minutes to read |
| `views` | INT DEFAULT 0 | Page view counter |
| `published_at` | TIMESTAMPTZ | Publish date |
| `updated_at` | TIMESTAMPTZ | Last edit |

### 20.7 Blog Admin Page (`/admin/blog`)

Simple admin panel for writing and publishing articles:

```
┌─────────────────────────────────────────────────────┐
│  BLOG ADMIN                                          │
│                                                      │
│  [+ New Post]                                        │
│                                                      │
│  Status    Title                          Date       │
│  ─────────────────────────────────────────────────── │
│  Published How to Choose EDC Pliers       May 12     │
│  Draft     Why GCC Needs Modular Tools    May 10     │
│  Published 72-Hour Kit Checklist          May 08     │
└─────────────────────────────────────────────────────┘
```

**Post Editor** (when clicking "+ New Post" or editing):
```
Title:  [__________________________________________]
Slug:   [how-to-choose-edc-pliers____________] (auto-generated from title)
Category: [EDC ▾]
Tags:    [pliers] [beginner] [gear]  [+ Add Tag]

Featured Image: [Upload from device ▸]
  → Auto-resize to 1200×630, optimize WebP

Content (Rich Text):
┌─────────────────────────────────────────────────┐
│ [B] [I] [H2] [H3] [List] [Quote] [Link] [Video] │
│                                                   │
│ <textarea / rich text editor>                     │
│                                                   │
└─────────────────────────────────────────────────┘

SEO Preview:
  Title:  [How to Choose EDC Pliers: 5 Factors...] (58/65)
  URL:    survival72gear.com/blog/2026/05/how-to...
  Desc:   [Not all EDC pliers are built equal...] (147/160)

[Save Draft]  [Publish ▸]
```

**Rich text editor:** Use **TipTap** (lightweight, headless, works with Lovable):
```html
<script src="https://unpkg.com/@tiptap/core@latest/dist/tiptap-core.umd.min.js"></script>
<script src="https://unpkg.com/@tiptap/starter-kit@latest/dist/tiptap-starter-kit.umd.min.js"></script>
```

### 20.8 Video Embed in Articles

In the rich text editor, the [Video] button opens a modal:
```
  Paste YouTube / Vimeo URL: [______________________________]
  [Insert Video ▸]
```

Renders as responsive 16:9 embed:
```html
<div class="video-embed" style="position:relative; padding-bottom:56.25%; height:0; margin:32px 0;">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID"
    style="position:absolute; top:0; left:0; width:100%; height:100%; border-radius:6px;"
    frameborder="0" allowfullscreen loading="lazy">
  </iframe>
</div>
```

Also add **VideoObject** schema for Google Video rich results:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "EDC Pliers Hands-On Comparison",
  "description": "Side-by-side comparison of 5 EDC pliers",
  "thumbnailUrl": "https://survival72gear.com/images/blog/video-thumb.jpg",
  "uploadDate": "2026-05-12",
  "contentUrl": "https://www.youtube.com/watch?v=VIDEO_ID",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID"
}
</script>
```

### 20.9 Core Web Vitals Optimization

| Metric | Target | Implementation |
|--------|--------|---------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Serve images as WebP, preload hero image, lazy-load below-fold |
| **FID** (First Input Delay) | < 100ms | Defer non-critical JS, use async for analytics |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Explicit width/height on all images, font-display:swap |
| **TTFB** (Time to First Byte) | < 800ms | CDN cache blog pages, static generation for /blog listing |

```html
<!-- Image best practices -->
<img src="image.webp" alt="..." width="400" height="267" loading="lazy" decoding="async" />

<!-- Preload hero/featured image -->
<link rel="preload" as="image" href="hero.webp" type="image/webp" />

<!-- Font optimization -->
<style>@font-face { font-family: '...'; font-display: swap; }</style>
```

### 20.10 Blog Categories (Predefined)

| Category | Slug | Description |
|----------|------|-------------|
| EDC | edc | Everyday carry gear reviews, comparisons, tips |
| Survival | survival | 72-hour kit, emergency prep, bug-out strategies |
| Gear | gear | Deep-dive tool reviews, material science, durability tests |
| Tactical | tactical | Professional-grade field techniques, military crossover |
| Tutorial | tutorial | Step-by-step how-tos, maintenance guides, sharpening |

---

## 21. FINAL FEATURE AUDIT — COMPLETENESS VERIFICATION

### 21.1 Page Inventory

| # | Page | Route | Status |
|---|------|-------|--------|
| 1 | Homepage | `/` | ✅ Spec complete (§4) |
| 2 | Shop the Kit (Configurator) | `/pages/shop-the-kit` | ✅ Spec complete (§5) |
| 3 | Gift Box Detail | `/products/gift-box` | ✅ Spec complete (§5.11) |
| 4 | Blog Listing | `/blog` | ✅ Spec complete (§20) |
| 5 | Blog Single Article | `/blog/{y}/{m}/{slug}` | ✅ Spec complete (§20) |
| 6 | Blog Category | `/blog/category/{slug}` | ✅ Spec complete (§20) |
| 7 | Blog Admin | `/admin/blog` | ✅ Spec complete (§20.7) |
| 8 | Member Login | `/account/login` | ✅ Spec complete (§7.3) |
| 9 | Member Register | `/account/register` | ✅ Spec complete (§7.3) |
| 10 | Member Dashboard | `/account` | ✅ Spec complete (§7.3) |
| 11 | Return Policy | `/pages/return-policy` | ✅ Spec complete (§6.1) |
| 12 | Shipping Policy | `/pages/shipping-policy` | ✅ Spec complete (§6.2) |
| 13 | Warranty | `/pages/warranty` | ✅ Spec complete (§6.3) |
| 14 | Privacy Policy | `/pages/privacy-policy` | ✅ Spec complete (§6.4) |
| 15 | Terms of Service | `/pages/terms-of-service` | ✅ Spec complete (§6.5) |
| 16 | B2B Wholesale | `/pages/wholesale` | ✅ Spec complete (§6.6) |
| 17 | Military Discount | `/pages/military-discount` | ✅ Spec complete (§6.7) |
| 18 | Cancellation Policy | `/pages/cancellation-policy` | ✅ Spec complete (§6.8) |
| 19 | Contact | `/pages/contact` | ✅ Spec complete (§6.9) |
| 20 | About | `/pages/about` | ✅ Referenced (§3.1) |
| 21 | Sitemap (blog) | `/sitemap-blog.xml` | ✅ Spec complete (§20.5) |
| 22 | RSS Feed | `/blog/feed.xml` | ✅ Spec complete (§20.5) |

### 21.2 System Inventory

| # | System | Implementation |
|---|--------|---------------|
| 1 | Auth (Signup/Login/Logout) | Supabase Auth (§7.4) |
| 2 | Member Dashboard (5 tabs) | `/account` unified page (§7.3) |
| 3 | Cart Persistence | localStorage + Supabase sync (§7.3 Tab 1) |
| 4 | Order History | `orders` table + Shopify API (§8) |
| 5 | Real-Time Logistics Tracking | Polling every 60s + Google Maps (§9) |
| 6 | GOVX ID Verification | OAuth flow + 10% checkout discount (§10) |
| 7 | Multi-Language (en/ar/zh) | i18next + JSON files (§17) |
| 8 | RTL Mode (Arabic) | CSS logical properties + font stack (§18) |
| 9 | Admin Asset Upload | Supabase Storage + product_assets table (§5.11) |
| 10 | Blog CMS | TipTap editor + `blog_posts` table (§20) |
| 11 | Blog SEO (Meta/OG/JSON-LD/Sitemap/RSS) | Full stack (§20.5) |
| 12 | GCC Currency (AED) + COD | §19 |
| 13 | Kit Configurator + Lightbox | Vanilla JS + variant mapping (§5) |
| 14 | Product Detail Drawers (3 tools + gift) | Slide-up drawers (§5.9, §5.11) |

### 21.3 Database Tables (All)

| Table | Purpose | Status |
|-------|---------|--------|
| `users` | Auth + profile + GOVX + cart | ✅ §7.2 |
| `orders` | Order data from Shopify | ✅ §8.3 |
| `order_items` | Line items per order | ✅ §8.3 |
| `tracking_events` | Real-time shipment events | ✅ §9.4 |
| `product_assets` | Admin-uploaded images/videos | ✅ §5.11.4 |
| `blog_posts` | Blog articles | ✅ §20.6 |

### 21.4 Code Quality Checklist

| Check | Status |
|-------|--------|
| CSS color variables used globally (no hardcoded hex outside :root) | ✅ §2.1 |
| Typography scale defined as single source of truth | ✅ §2.2 |
| CSS logical properties preferred over physical (RTL-ready) | ✅ §18.3 |
| Lazy loading on all blog images (`loading="lazy"`) | ✅ §20.5 |
| Explicit width/height on all images (CLS prevention) | ✅ §20.5 |
| `font-display: swap` on all @font-face | ✅ §20.9 |
| Open Graph + Twitter Card on every page | ✅ §20.5 |
| JSON-LD structured data on blog articles | ✅ §20.5 |
| BreadcrumbList schema on blog articles | ✅ §20.5 |
| Sitemap auto-generated for blog | ✅ §20.5 |
| RSS feed for blog | ✅ §20.5 |
| `robots.txt` with sitemap references | ✅ §20.5 |
| Internal linking strategy (blog → products) | ✅ §20.5 |
| All customer emails point to `survival72bob@gmail.com` only | ✅ §16 |
| i18n-ready: all user-facing strings via `data-i18n` | ✅ §17 |
| RTL: Arabic fonts, logical properties, direction flip | ✅ §18 |
| Mobile responsive: hamburger nav, stacked grids | ✅ §11 |

### 21.5 SEO Scorecard (Target)

| Metric | Target | Implementation |
|--------|--------|---------------|
| Meta title per page | 50–65 chars | ✅ |
| Meta description per page | 120–160 chars | ✅ |
| Canonical URL per page | Present | ✅ |
| OG:Image per page | 1200×630 | ✅ |
| JSON-LD Article schema | Per blog post | ✅ |
| JSON-LD BreadcrumbList | Per blog post | ✅ |
| JSON-LD VideoObject | Per video embed | ✅ |
| JSON-LD Organization | Site-wide | ✅ |
| robots.txt | Present | ✅ |
| XML Sitemap | Auto-generated | ✅ |
| RSS Feed | Present | ✅ |
| Internal links (blog→product) | Per article | ✅ |
| Core Web Vitals (LCP < 2.5s) | WebP + lazy load + preload | ✅ |

### 21.6 Build Order (Final — 22 Steps)

| Step | Component | Section |
|------|-----------|---------|
| 1 | Global CSS reset + color system + typography | §2 |
| 2 | Navigation (Header + Footer) — with Blog + Account icon | §3 |
| 3 | Hero Banner section | §4.1 |
| 4 | Marquee section | §4.2 |
| 5 | s72-problem section | §4.3 |
| 6 | s72-system section (cards + gift + CTAs) | §4.4 |
| 7 | s72-edu section | §4.5 |
| 8 | s72-proof section | §4.6 |
| 9 | s72-promise trust bar | §4.7 |
| 10 | Kit Configurator page (full standalone page) | §5 |
| 11 | Gift Box Detail Page + Admin Upload System | §5.11 |
| 12 | Policy pages (9 pages) — single email: survival72bob@gmail.com | §6 |
| 13 | Multi-Language System (i18n: en/ar/zh) | §17 |
| 14 | Auth system (Signup, Login, Unified Dashboard with Cart/Orders/Tracking) | §7 |
| 15 | Order system (My Orders with real-time status badges) | §8 |
| 16 | Logistics tracking (real-time polling + timeline + Google Maps) | §9 |
| 17 | GOVX ID verification (10% discount) | §10 |
| 18 | Blog System (listing, article, admin, SEO, sitemap, RSS) | §20 |
| 19 | RTL Middle East Browsing Mode | §18 |
| 20 | Cart integration (Shopify API) | §5.8 |
| 21 | GCC currency + COD | §19 |
| 22 | Responsive testing + polish | §11 |

---


