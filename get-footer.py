import urllib.request, json
SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"

# List section JSONs in theme
url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]=sections/footer-group.json"
req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
try:
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read())
        with open("sections_footer-group.json", "w", encoding="utf-8") as f:
            f.write(d["asset"]["value"])
        print(("saved sections_footer-group.json " + str(len(d['asset']['value'])) + " chars").encode())
except urllib.error.HTTPError as e:
    print((str(e.code) + ": " + e.read().decode()[:200]).encode())
