import urllib.request, json
SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"

with open("sections_footer-group-NEW.json", "r", encoding="utf-8") as f:
    val = f.read()

url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json"
hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}
payload = {"asset": {"key": "sections/footer-group.json", "value": val}}
req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=hdrs, method="PUT")
try:
    with urllib.request.urlopen(req) as r:
        print(("PUT footer status: " + str(r.status)).encode())
except urllib.error.HTTPError as e:
    print(("ERR " + str(e.code)).encode())
    print(e.read().decode("utf-8", errors="replace").encode("utf-8", errors="replace"))
