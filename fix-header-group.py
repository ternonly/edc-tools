"""
Fix header-group.json:
1. Replace default 'Welcome to our store' with 2 rotating announcements
2. Use scheme-2 (dark) for announcement bar
3. Enable transparent header on home page for hero impact
"""
import json, urllib.request

SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"

with open("sections_header-group.json", "r", encoding="utf-8") as f:
    hg = json.load(f)

# --- Replace announcement blocks ---
hg["sections"]["header_announcements_9jGBFp"]["blocks"] = {
    "ann_cod": {
        "type": "_announcement",
        "settings": {
            "text": "🚚 COD Available in UAE & Saudi · Free Shipping over $50",
            "link": "",
            "font": "var(--font-subheading--family)",
            "font_size": "0.8125rem",
            "weight": "500",
            "letter_spacing": "0.02em",
            "case": "none"
        },
        "blocks": {}
    },
    "ann_eid": {
        "type": "_announcement",
        "settings": {
            "text": "🎁 Limited Eid Gift Edition — only while stocks last",
            "link": "shopify://collections/gift-sets",
            "font": "var(--font-subheading--family)",
            "font_size": "0.8125rem",
            "weight": "500",
            "letter_spacing": "0.02em",
            "case": "none"
        },
        "blocks": {}
    }
}
hg["sections"]["header_announcements_9jGBFp"]["block_order"] = ["ann_cod", "ann_eid"]

# Use dark scheme for announcement bar (more "premium tactical" feel)
hg["sections"]["header_announcements_9jGBFp"]["settings"]["color_scheme"] = "scheme-2"
hg["sections"]["header_announcements_9jGBFp"]["settings"]["speed"] = 8

# --- Enable transparent header on home for hero impact ---
hg["sections"]["header_section"]["settings"]["enable_transparent_header_home"] = True

# Save and deploy
with open("sections_header-group-NEW.json", "w", encoding="utf-8") as f:
    json.dump(hg, f, indent=2, ensure_ascii=False)

url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json"
hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}
payload = {
    "asset": {
        "key": "sections/header-group.json",
        "value": json.dumps(hg, ensure_ascii=False, indent=2)
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
