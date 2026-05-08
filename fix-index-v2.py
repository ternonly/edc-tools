"""
Fix 3 issues in templates/index.json:
1. Hero h_btn1: style_class "button-primary" -> "button" (correct primary value per blocks/button.liquid)
2. KIT featured-product: add static blocks (media + featured-product container with 4 nested static blocks)
3. WHY media-with-content: add image to _media-without-appearance settings (use hero banner)
"""
import json, urllib.request

SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"

# Read current
with open("horizon-index-NEW.json", "r", encoding="utf-8") as f:
    idx = json.load(f)

# ---- Fix 1: Hero primary button ----
idx["sections"]["hero"]["blocks"]["h_btn1"]["settings"]["style_class"] = "button"

# ---- Fix 2: KIT featured-product nested static blocks ----
idx["sections"]["kit"]["blocks"] = {
    "media": {
        "type": "_media-without-appearance",
        "static": True,
        "settings": {
            "media_type": "image",
            "image": "shopify://shop_images/hero-banner-final.jpg",
            "image_position": "cover"
        }
    },
    "featured-product": {
        "type": "_featured-product",
        "static": True,
        "blocks": {
            "featured-product-title": {
                "type": "product-title",
                "static": True,
                "settings": {
                    "type_preset": "h2",
                    "width": "100%"
                }
            },
            "featured-product-price": {
                "type": "_featured-product-price",
                "static": True,
                "settings": {}
            },
            "featured-product-gallery": {
                "type": "_featured-product-gallery",
                "static": True,
                "settings": {}
            },
            "featured-product-swatches": {
                "type": "swatches",
                "static": True,
                "settings": {
                    "hide_padding": True
                }
            }
        }
    }
}

# ---- Fix 3: WHY media-with-content image ----
# Use hero-banner-final.jpg as the why-section media (desert/family vibe)
idx["sections"]["why"]["blocks"]["media"]["settings"] = {
    "media_type": "image",
    "image": "shopify://shop_images/hero-banner-final.jpg",
    "image_position": "cover"
}

# Save backup + new file
with open("horizon-index-NEW-v2.json", "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)

print("Wrote horizon-index-NEW-v2.json".encode())

# Deploy
url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json"
hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

payload = {
    "asset": {
        "key": "templates/index.json",
        "value": json.dumps(idx, ensure_ascii=False, indent=2)
    }
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers=hdrs, method="PUT")
try:
    with urllib.request.urlopen(req) as resp:
        print(f"PUT status: {resp.status}".encode())
        print("OK".encode())
except urllib.error.HTTPError as e:
    print(f"PUT status: {e.code}".encode())
    print(e.read().decode("utf-8", errors="replace").encode("utf-8", errors="replace"))
