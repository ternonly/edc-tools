"""Fix Why media — change image_picker value format.
Try multiple formats; PUT each variant separately and observe.
"""
import urllib.request, json, time

SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"
hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

# Read current
with open("horizon-index-NEW-v2.json", "r", encoding="utf-8") as f:
    idx = json.load(f)

# Variant under test - GID format (most likely correct for new image_picker JSON)
test_value = "shopify://files/hero-banner-final.jpg"

# Find the why media block and update image
why = idx["sections"]["why"]
why["blocks"]["media"]["settings"]["image"] = test_value
print(("setting why.media.image to: " + test_value).encode())

# Write to disk for record
with open("horizon-index-NEW-v3.json", "w", encoding="utf-8") as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)

# PUT
url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json"
payload = {"asset": {"key": "templates/index.json", "value": json.dumps(idx)}}
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=hdrs, method="PUT")
try:
    with urllib.request.urlopen(req) as r:
        print(("PUT v3 status: " + str(r.status)).encode())
except urllib.error.HTTPError as e:
    print(("ERR " + str(e.code)).encode())
    print(e.read().decode("utf-8", errors="replace").encode("utf-8", errors="replace"))
