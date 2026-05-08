"""Force cache invalidation by writing a tiny dummy asset."""
import json, urllib.request, time

SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"

url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json"
hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

# Write a dummy asset with current timestamp - this bumps the theme version
ts = int(time.time())
payload = {
    "asset": {
        "key": f"assets/cache-bust-{ts}.txt",
        "value": str(ts)
    }
}
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                              headers=hdrs, method="PUT")
with urllib.request.urlopen(req) as r:
    print(f"PUT cache-bust status: {r.status}".encode())

# Now also delete a non-essential asset to bump
del_url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]=assets/cache-bust-{ts}.txt"
req = urllib.request.Request(del_url, headers=hdrs, method="DELETE")
try:
    with urllib.request.urlopen(req) as r:
        print(f"DELETE status: {r.status}".encode())
except Exception as e:
    print(f"delete err: {e}".encode())
