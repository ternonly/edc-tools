"""Bump theme cache by writing then deleting a dummy asset."""
import json, urllib.request, time

SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"

url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json"
hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

# Re-PUT templates/index.json to bump theme version
with open("templates_index.json", encoding="utf-8") as f:
    new_value = f.read()

payload = {"asset": {"key": "templates/index.json", "value": new_value}}
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                              headers=hdrs, method="PUT")
with urllib.request.urlopen(req) as r:
    print(f"PUT index status: {r.status}".encode())

# Re-PUT header-group.json
with open("sections_header-group.json", encoding="utf-8") as f:
    new_value = f.read()

payload = {"asset": {"key": "sections/header-group.json", "value": new_value}}
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                              headers=hdrs, method="PUT")
with urllib.request.urlopen(req) as r:
    print(f"PUT header-group status: {r.status}".encode())

print(b"Done. Wait 30 seconds then re-fetch.")
