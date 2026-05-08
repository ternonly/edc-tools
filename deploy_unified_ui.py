import urllib.request
import json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
PROD_ID = '8487770259501'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

PLIERS_IMG = "https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_pliers_1.png"
WRENCH_IMG = "https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_wrench_1.jpg"
AXE_IMG    = "https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_axe_1.jpg"
BOX_IMG    = "https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_gift_box_kit-gift-box.jpg"

body_content = """
<style>
/* ============================================================
   GLOBAL RESET & WRAP
   ============================================================ */
.s72-wrap { max-width: 860px; margin: 0 auto; font-family: inherit; color: #1a1a1a; }

/* ============================================================
   MODE TOGGLE
   ============================================================ */
.s72-toggle { display: flex; gap: 8px; margin-bottom: 24px; }
.s72-toggle-btn {
  flex: 1; padding: 14px 10px; border: 1.5px solid #d0d0d0;
  background: #fafafa; cursor: pointer; text-align: center;
  font-size: 12px; font-weight: 600; letter-spacing: 1.2px;
  text-transform: uppercase; transition: all 0.2s; line-height: 1.4;
}
.s72-toggle-btn.active { border-color: #1a1a1a; background: #1a1a1a; color: #fff; }
.s72-toggle-btn.elite  { border-color: #b8934a; background: #b8934a; color: #fff; }

/* ============================================================
   MAIN LAYOUT: left preview + right configurator
   ============================================================ */
.s72-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: start; }
@media (max-width: 680px) { .s72-layout { grid-template-columns: 1fr; } }

/* Left: big image preview */
.s72-preview {
  position: sticky; top: 20px;
  aspect-ratio: 1/1; background: #f4f4f4;
  display: flex; align-items: center; justify-content: center;
  overflow: hidden; border: 1px solid #e8e8e8;
}
.s72-preview img {
  width: 100%; height: 100%; object-fit: cover;
  transition: opacity 0.25s ease;
}
.s72-preview-hint {
  font-size: 12px; color: #aaa; text-align: center; padding: 20px; line-height: 1.6;
}

/* Right: card grid */
.s72-grid { display: flex; flex-direction: column; gap: 10px; }

/* ============================================================
   TOOL CARDS
   ============================================================ */
.s72-card {
  border: 1.5px solid #e0e0e0; background: #fff; cursor: pointer;
  transition: border-color 0.2s; position: relative;
  display: grid; grid-template-columns: 90px 1fr; align-items: center;
}
.s72-card:hover { border-color: #aaa; }
.s72-card.selected { border-color: #1a1a1a; border-width: 2px; }
.s72-card.selected::after {
  content: '✓'; position: absolute; top: 8px; right: 8px;
  width: 20px; height: 20px; background: #1a1a1a; color: #fff;
  border-radius: 50%; font-size: 11px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  line-height: 20px; text-align: center;
}
.s72-card-thumb {
  width: 90px; height: 90px; overflow: hidden;
  background: #f5f5f5; flex-shrink: 0;
}
.s72-card-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
.s72-card-body { padding: 12px 36px 12px 14px; }
.s72-card-label { font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: #999; margin-bottom: 2px; }
.s72-card-name  { font-size: 13px; font-weight: 700; margin-bottom: 6px; }
.s72-card-footer { display: flex; align-items: center; justify-content: space-between; }
.s72-card-price { font-size: 13px; font-weight: 600; }

/* "View Details" button inside card */
.s72-detail-btn {
  font-size: 10px; letter-spacing: 1px; text-transform: uppercase;
  color: #666; border-bottom: 1px solid #ccc; padding-bottom: 1px;
  background: none; border-top: none; border-left: none; border-right: none;
  cursor: pointer; transition: color 0.15s, border-color 0.15s;
  font-family: inherit;
}
.s72-detail-btn:hover { color: #1a1a1a; border-color: #1a1a1a; }

/* ============================================================
   GIFT BOX ROW
   ============================================================ */
.s72-gift {
  border: 1.5px dashed #d0b980; background: #fffdf5;
  display: grid; grid-template-columns: 72px 1fr auto;
  align-items: center; gap: 14px; padding: 14px;
  cursor: pointer; transition: all 0.25s; position: relative; margin-top: 4px;
}
.s72-gift.locked   { opacity: 0.4; pointer-events: none; }
.s72-gift.selected { border-style: solid; border-color: #b8934a; border-width: 2px; }
.s72-gift-thumb {
  width: 72px; height: 72px; background: #f0ead8; border-radius: 3px;
  overflow: hidden; display: flex; align-items: center; justify-content: center; font-size: 28px;
}
.s72-gift-thumb img { width: 100%; height: 100%; object-fit: cover; }
.s72-gift-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; }
.s72-gift-desc  { font-size: 11px; color: #777; margin-top: 3px; line-height: 1.5; }
.s72-gift-price { font-size: 16px; font-weight: 700; color: #b8934a; white-space: nowrap; }
.s72-gift-unlock {
  position: absolute; inset: 0; background: rgba(255,255,255,0.65);
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; color: #bbb; letter-spacing: 1px; text-transform: uppercase;
}
.s72-gift:not(.locked) .s72-gift-unlock { display: none; }

/* ============================================================
   PRICE BAR
   ============================================================ */
.s72-pricebar {
  margin-top: 16px; background: #1a1a1a; color: #fff;
  padding: 18px 22px; display: flex; justify-content: space-between; align-items: center;
}
.s72-pricebar-label  { font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: #777; margin-bottom: 3px; }
.s72-pricebar-total  { font-size: 26px; font-weight: 700; font-family: monospace; }
.s72-pricebar-saving { font-size: 12px; font-weight: 700; color: #C9A96E; letter-spacing: 1px; text-transform: uppercase; }
.s72-pricebar-hint   { font-size: 12px; color: #666; }

/* ============================================================
   DRAWER OVERLAY + PANEL
   ============================================================ */
.s72-drawer-overlay {
  display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.55);
  z-index: 9000; backdrop-filter: blur(2px);
}
.s72-drawer-overlay.open { display: block; }

.s72-drawer {
  position: fixed; bottom: 0; left: 0; right: 0;
  height: 90vh; background: #fff; z-index: 9001;
  transform: translateY(100%); transition: transform 0.35s cubic-bezier(0.32,0,0.15,1);
  display: flex; flex-direction: column; overflow: hidden;
  border-radius: 16px 16px 0 0;
}
.s72-drawer.open { transform: translateY(0); }

/* Drawer header */
.s72-drawer-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 20px 24px 16px; border-bottom: 1px solid #eee; flex-shrink: 0;
}
.s72-drawer-header h3 { font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin: 0; }
.s72-drawer-close {
  width: 32px; height: 32px; background: #f0f0f0; border: none; border-radius: 50%;
  font-size: 18px; cursor: pointer; display: flex; align-items: center; justify-content: center;
  font-family: inherit; line-height: 1; color: #333;
}
.s72-drawer-close:hover { background: #e0e0e0; }

/* Drawer scrollable body */
.s72-drawer-body { flex: 1; overflow-y: auto; padding: 24px; }

/* ---- Gallery grid ---- */
.s72-drawer-section-title {
  font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
  color: #999; margin: 0 0 14px; border-bottom: 1px solid #f0f0f0; padding-bottom: 8px;
}
.s72-gallery {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 10px; margin-bottom: 32px;
}
.s72-gallery-slot {
  aspect-ratio: 1/1; background: #f6f6f6;
  border: 1.5px dashed #ddd; border-radius: 6px;
  overflow: hidden; display: flex; align-items: center; justify-content: center;
  font-size: 11px; color: #bbb; text-align: center; line-height: 1.5; padding: 12px;
}
.s72-gallery-slot img { width: 100%; height: 100%; object-fit: cover; border-radius: 4px; }
.s72-gallery-slot.filled { border-style: solid; border-color: #e0e0e0; }

/* ---- Video slots ---- */
.s72-videos { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 10px; margin-bottom: 32px; }
.s72-video-slot {
  aspect-ratio: 16/9; background: #f0f0f0; border: 1.5px dashed #ddd; border-radius: 6px;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  font-size: 11px; color: #bbb; text-align: center; padding: 16px; line-height: 1.6;
}
.s72-video-slot span { font-size: 28px; margin-bottom: 6px; display: block; }

/* ---- Specs table ---- */
.s72-specs { width: 100%; border-collapse: collapse; font-size: 13px; margin-bottom: 16px; }
.s72-specs tr { border-bottom: 1px solid #f0f0f0; }
.s72-specs tr:last-child { border-bottom: none; }
.s72-specs td { padding: 10px 8px; vertical-align: top; }
.s72-specs td:first-child { width: 40%; color: #888; font-size: 11px; letter-spacing: 0.8px; text-transform: uppercase; font-weight: 600; }
.s72-specs td:last-child { font-weight: 500; }

/* ============================================================
   HIDE NATIVE SHOPIFY VARIANT PICKER — all known selectors
   ============================================================ */
variant-picker,
variant-selects,
variant-radios,
.variant-picker,
.product-form__input,
.product-form__input--pill,
.product-form__input--dropdown,
[data-section-type="product"] .product-form__variants,
.block-variant-picker { display: none !important; }
</style>


<!-- ============================================================
     HTML
     ============================================================ -->
<div class="s72-wrap">

  <!-- Mode toggle -->
  <div class="s72-toggle">
    <div class="s72-toggle-btn" id="s72-btn-custom" onclick="s72SetMode('custom')">
      Build Your Kit<br><span style="font-size:10px;font-weight:400;opacity:.7">Choose any combination</span>
    </div>
    <div class="s72-toggle-btn" id="s72-btn-elite" onclick="s72SetMode('elite')">
      Elite Gift Set &mdash; $145<br><span style="font-size:10px;font-weight:400;opacity:.7">All 3 tools + Magnetic Box</span>
    </div>
  </div>

  <!-- Left preview + Right configurator -->
  <div class="s72-layout">

    <!-- LEFT: Big image preview -->
    <div class="s72-preview" id="s72-preview">
      <div class="s72-preview-hint">Click a product<br>to preview</div>
    </div>

    <!-- RIGHT: Cards + gift + price -->
    <div>
      <div class="s72-grid">

        <!-- Pliers -->
        <div class="s72-card" id="s72-card-pliers"
             onmouseenter="s72PreviewImg('pliers')"
             onclick="s72ToggleTool('pliers')">
          <div class="s72-card-thumb">
            <img src="https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_pliers_1.png" alt="Pliers">
          </div>
          <div class="s72-card-body">
            <div class="s72-card-label">Module 01 &mdash; Pliers</div>
            <div class="s72-card-name">Precision Multi-Pliers</div>
            <div class="s72-card-footer">
              <span class="s72-card-price">$52</span>
              <button class="s72-detail-btn" onclick="event.stopPropagation(); s72OpenDrawer('pliers')">View Details &rsaquo;</button>
            </div>
          </div>
        </div>

        <!-- Wrench -->
        <div class="s72-card" id="s72-card-wrench"
             onmouseenter="s72PreviewImg('wrench')"
             onclick="s72ToggleTool('wrench')">
          <div class="s72-card-thumb">
            <img src="https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_wrench_1.jpg" alt="Wrench">
          </div>
          <div class="s72-card-body">
            <div class="s72-card-label">Module 02 &mdash; Wrench</div>
            <div class="s72-card-name">Roadside Wrench</div>
            <div class="s72-card-footer">
              <span class="s72-card-price">$42</span>
              <button class="s72-detail-btn" onclick="event.stopPropagation(); s72OpenDrawer('wrench')">View Details &rsaquo;</button>
            </div>
          </div>
        </div>

        <!-- Axe -->
        <div class="s72-card" id="s72-card-axe"
             onmouseenter="s72PreviewImg('axe')"
             onclick="s72ToggleTool('axe')">
          <div class="s72-card-thumb">
            <img src="https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_axe_1.jpg" alt="Axe">
          </div>
          <div class="s72-card-body">
            <div class="s72-card-label">Module 03 &mdash; Axe</div>
            <div class="s72-card-name">Desert Breacher Axe</div>
            <div class="s72-card-footer">
              <span class="s72-card-price">$49</span>
              <button class="s72-detail-btn" onclick="event.stopPropagation(); s72OpenDrawer('axe')">View Details &rsaquo;</button>
            </div>
          </div>
        </div>

      </div><!-- /.s72-grid -->

      <!-- Gift box -->
      <div class="s72-gift locked" id="s72-gift" onclick="s72ToggleGift()">
        <div class="s72-gift-unlock">Select all 3 modules to unlock</div>
        <div class="s72-gift-thumb"><img src="https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_gift_box_kit-gift-box.jpg" alt="Gift Box"></div>
        <div>
          <div class="s72-gift-title">Elite Magnetic Gift Box</div>
          <div class="s72-gift-desc">Premium clamshell case, EVA foam inlays, S72 Field Guide. Gift-ready.</div>
        </div>
        <div class="s72-gift-price">+ $29</div>
      </div>

      <!-- Price bar -->
      <div class="s72-pricebar">
        <div>
          <div class="s72-pricebar-label">Kit Total</div>
          <div class="s72-pricebar-total" id="s72-total">$0.00</div>
        </div>
        <div style="text-align:right">
          <div class="s72-pricebar-saving" id="s72-savings"></div>
          <div class="s72-pricebar-hint"  id="s72-hint">Select a module to begin</div>
        </div>
      </div>

    </div><!-- /right col -->
  </div><!-- /.s72-layout -->
</div><!-- /.s72-wrap -->


<!-- ============================================================
     DRAWERS (one per product)
     ============================================================ -->

<!-- Overlay -->
<div class="s72-drawer-overlay" id="s72-overlay" onclick="s72CloseDrawer()"></div>

<!-- PLIERS DRAWER -->
<div class="s72-drawer" id="s72-drawer-pliers">
  <div class="s72-drawer-header">
    <h3>Precision Multi-Pliers &mdash; PA-92A</h3>
    <button class="s72-drawer-close" onclick="s72CloseDrawer()">&#10005;</button>
  </div>
  <div class="s72-drawer-body">

    <p class="s72-drawer-section-title">Photo Gallery</p>
    <!-- ADD PLIERS IMAGES BELOW — paste <img src="YOUR_CDN_URL"> inside each slot -->
    <!-- To add more slots: duplicate any .s72-gallery-slot div -->
    <div class="s72-gallery">
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
    </div>

    <p class="s72-drawer-section-title">Product Video</p>
    <!-- ADD PLIERS VIDEO BELOW — replace with <video> or <iframe> tag -->
    <div class="s72-videos">
      <div class="s72-video-slot"><span>&#9654;</span>Paste &lt;video&gt; or YouTube&lt;iframe&gt; here</div>
      <div class="s72-video-slot"><span>&#9654;</span>Paste &lt;video&gt; or YouTube&lt;iframe&gt; here</div>
    </div>

    <p class="s72-drawer-section-title">Specifications</p>
    <table class="s72-specs">
      <tr><td>Model</td><td>PA-92A</td></tr>
      <tr><td>Functions</td><td>25-in-1</td></tr>
      <tr><td>Material</td><td>420 Stainless Steel</td></tr>
      <tr><td>Folded Length</td><td>10.5 cm</td></tr>
      <tr><td>Weight</td><td>180 g</td></tr>
      <tr><td>Jaw Opening</td><td>25 mm</td></tr>
      <tr><td>Blade Type</td><td>Serrated + Straight</td></tr>
      <tr><td>Finish</td><td>Sandblasted + Black Oxide</td></tr>
      <tr><td>Includes</td><td>Nylon Sheath, S72 Card</td></tr>
    </table>

  </div>
</div>

<!-- WRENCH DRAWER -->
<div class="s72-drawer" id="s72-drawer-wrench">
  <div class="s72-drawer-header">
    <h3>Roadside Wrench &mdash; KA-62A</h3>
    <button class="s72-drawer-close" onclick="s72CloseDrawer()">&#10005;</button>
  </div>
  <div class="s72-drawer-body">

    <p class="s72-drawer-section-title">Photo Gallery</p>
    <div class="s72-gallery">
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
    </div>

    <p class="s72-drawer-section-title">Product Video</p>
    <div class="s72-videos">
      <div class="s72-video-slot"><span>&#9654;</span>Paste &lt;video&gt; or YouTube&lt;iframe&gt; here</div>
      <div class="s72-video-slot"><span>&#9654;</span>Paste &lt;video&gt; or YouTube&lt;iframe&gt; here</div>
    </div>

    <p class="s72-drawer-section-title">Specifications</p>
    <table class="s72-specs">
      <tr><td>Model</td><td>KA-62A</td></tr>
      <tr><td>Bits Included</td><td>9 (PH1, PH2, SL4, SL6, H3, H4, H5, T25, T30)</td></tr>
      <tr><td>Material</td><td>CR-V Drop-Forged Steel</td></tr>
      <tr><td>Length (folded)</td><td>12 cm</td></tr>
      <tr><td>Weight</td><td>145 g</td></tr>
      <tr><td>Drive Size</td><td>1/4" (6.35 mm)</td></tr>
      <tr><td>Ratchet Direction</td><td>Reversible</td></tr>
      <tr><td>Finish</td><td>Satin Chrome</td></tr>
      <tr><td>Includes</td><td>Bit Holder Pouch, S72 Card</td></tr>
    </table>

  </div>
</div>

<!-- AXE DRAWER -->
<div class="s72-drawer" id="s72-drawer-axe">
  <div class="s72-drawer-header">
    <h3>Desert Breacher Axe &mdash; XI-G8</h3>
    <button class="s72-drawer-close" onclick="s72CloseDrawer()">&#10005;</button>
  </div>
  <div class="s72-drawer-body">

    <p class="s72-drawer-section-title">Photo Gallery</p>
    <div class="s72-gallery">
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
      <div class="s72-gallery-slot">Add image<br>via Shopify Files</div>
    </div>

    <p class="s72-drawer-section-title">Product Video</p>
    <div class="s72-videos">
      <div class="s72-video-slot"><span>&#9654;</span>Paste &lt;video&gt; or YouTube&lt;iframe&gt; here</div>
      <div class="s72-video-slot"><span>&#9654;</span>Paste &lt;video&gt; or YouTube&lt;iframe&gt; here</div>
    </div>

    <p class="s72-drawer-section-title">Specifications</p>
    <table class="s72-specs">
      <tr><td>Model</td><td>XI-G8</td></tr>
      <tr><td>Functions</td><td>8-in-1</td></tr>
      <tr><td>Head Material</td><td>3CR13 Stainless Steel</td></tr>
      <tr><td>Handle Material</td><td>G10 Composite</td></tr>
      <tr><td>Overall Length</td><td>24 cm</td></tr>
      <tr><td>Head Weight</td><td>180 g</td></tr>
      <tr><td>Total Weight</td><td>320 g</td></tr>
      <tr><td>Edge</td><td>Field-Sharpenable, 25° Bevel</td></tr>
      <tr><td>Includes</td><td>Ballistic Nylon Sheath, S72 Card</td></tr>
    </table>

  </div>
</div>


<!-- ============================================================
     JAVASCRIPT
     ============================================================ -->
<script>
(function() {
  /* ---- Variant map ---- */
  var VARIANTS = {
    '0-0-1-0': 44902740820013,
    '1-1-0-0': 44902746882093,
    '1-1-1-0': 44902746914861,
    '1-1-1-1': 44902746947629,
    '1-0-0-0': 44902746980397,
    '1-0-1-0': 44902747013165,
    '0-1-0-0': 44902747078701,
    '0-1-1-0': 44902747111469,
  };

  /* ---- Preview images per tool ---- */
  var PREVIEWS = {
    pliers: 'https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_pliers_1.png',
    wrench: 'https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_wrench_1.jpg',
    axe:    'https://cdn.shopify.com/s/files/1/0751/9030/4813/files/s72_axe_1.jpg',
  };

  var sel = { pliers: false, wrench: false, axe: false };
  var giftSelected = false;

  /* ---- Preview ---- */
  window.s72PreviewImg = function(tool) {
    var box = document.getElementById('s72-preview');
    if (!box) return;
    var hint = box.querySelector('.s72-preview-hint');
    var img  = box.querySelector('img');
    if (!img) {
      img = document.createElement('img');
      box.appendChild(img);
    }
    if (hint) hint.style.display = 'none';
    img.style.opacity = '0';
    img.onload = function() { img.style.opacity = '1'; };
    img.src = PREVIEWS[tool];
    img.alt = tool;
  };

  /* ---- Toggle tool ---- */
  window.s72ToggleTool = function(tool) {
    sel[tool] = !sel[tool];
    s72PreviewImg(tool);
    document.getElementById('s72-btn-elite').classList.remove('elite');
    document.getElementById('s72-btn-custom').classList.add('active');
    s72Update();
  };

  /* ---- Toggle gift ---- */
  window.s72ToggleGift = function() {
    if (s72Count() < 3) return;
    giftSelected = !giftSelected;
    s72Update();
  };

  /* ---- Set mode ---- */
  window.s72SetMode = function(mode) {
    if (mode === 'elite') {
      sel = { pliers: true, wrench: true, axe: true };
      giftSelected = true;
      document.getElementById('s72-btn-elite').classList.add('elite');
      document.getElementById('s72-btn-custom').classList.remove('active');
      s72PreviewImg('pliers');
    } else {
      document.getElementById('s72-btn-custom').classList.add('active');
      document.getElementById('s72-btn-elite').classList.remove('elite');
    }
    s72Update();
  };

  function s72Count() {
    return (sel.pliers?1:0)+(sel.wrench?1:0)+(sel.axe?1:0);
  }

  /* ---- Update UI + variant sync ---- */
  function s72Update() {
    ['pliers','wrench','axe'].forEach(function(t) {
      var c = document.getElementById('s72-card-'+t);
      if (c) { sel[t] ? c.classList.add('selected') : c.classList.remove('selected'); }
    });

    var gift = document.getElementById('s72-gift');
    var all3 = s72Count() === 3;
    if (gift) {
      if (all3) gift.classList.remove('locked'); else { gift.classList.add('locked'); giftSelected = false; }
      giftSelected ? gift.classList.add('selected') : gift.classList.remove('selected');
    }

    var sub      = (sel.pliers?52:0)+(sel.wrench?42:0)+(sel.axe?49:0);
    var count    = s72Count();
    var discount = count===2?15: count===3?27: 0;
    var total    = sub - discount + (giftSelected?29:0);

    var totalEl  = document.getElementById('s72-total');
    var savingEl = document.getElementById('s72-savings');
    var hintEl   = document.getElementById('s72-hint');
    if (totalEl)  totalEl.textContent  = (count>0||giftSelected) ? '$'+total.toFixed(2) : '$0.00';
    if (savingEl) savingEl.textContent = discount>0 ? 'You save $'+discount : '';
    if (hintEl)   hintEl.style.display = count===0 ? '' : 'none';

    /* sync Shopify variant */
    var key = (sel.pliers?1:0)+'-'+(sel.wrench?1:0)+'-'+(sel.axe?1:0)+'-'+(giftSelected?1:0);
    var vid = VARIANTS[key];
    if (vid) {
      var form = document.querySelector('form[action*="/cart/add"]');
      if (form) {
        var inp = form.querySelector('input[name="id"]');
        if (inp) { inp.value = vid; inp.dispatchEvent(new Event('change',{bubbles:true})); }
      }
      var url = new URL(window.location.href);
      url.searchParams.set('variant', vid);
      window.history.replaceState({}, '', url.toString());
    }
  }

  /* ---- Drawer ---- */
  window.s72OpenDrawer = function(tool) {
    document.getElementById('s72-overlay').classList.add('open');
    document.getElementById('s72-drawer-'+tool).classList.add('open');
    document.body.style.overflow = 'hidden';
  };
  window.s72CloseDrawer = function() {
    document.querySelectorAll('.s72-drawer.open').forEach(function(d){ d.classList.remove('open'); });
    document.getElementById('s72-overlay').classList.remove('open');
    document.body.style.overflow = '';
  };
  document.addEventListener('keydown', function(e){ if(e.key==='Escape') s72CloseDrawer(); });

  /* ---- Init ---- */
  document.addEventListener('DOMContentLoaded', function() {
    var params = new URLSearchParams(window.location.search);
    if (params.get('auto_kit') === 'elite') {
      s72SetMode('elite');
    } else {
      s72Update();
    }

    /* Force-hide native variant picker via JS as backup */
    function hideNative() {
      var targets = document.querySelectorAll('variant-picker, variant-selects, variant-radios, .block-variant-picker');
      targets.forEach(function(el){ el.style.setProperty('display','none','important'); });
    }
    hideNative();
    setTimeout(hideNative, 500);
    setTimeout(hideNative, 1500);
  });
})();
</script>
"""

url = f'https://{SHOP}/admin/api/{API_VER}/products/{PROD_ID}.json'
data = {'product': {'id': PROD_ID, 'body_html': body_content}}
req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=HDRS, method='PUT')
try:
    with urllib.request.urlopen(req) as r:
        print(f'Deploy OK: {r.status}')
except Exception as e:
    print(f'Deploy FAILED: {e}')
