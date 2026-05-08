import urllib.request, json
SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
API_VER = "2026-01"
url = f"https://{SHOP}/admin/api/{API_VER}/pages.json"
req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
    for p in data.get("pages", []):
        print(f"{p['id']:20} {p['handle']:30} {p['title']}".encode())
