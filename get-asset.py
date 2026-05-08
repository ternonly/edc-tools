import sys, urllib.request, json
SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
THEME_ID = 151511040045
API_VER = "2026-01"
key = sys.argv[1]
url = f"https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]={key}"
req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
try:
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read())
        outname = key.replace("/", "_") + ".txt"
        with open(outname, "w", encoding="utf-8") as f:
            f.write(d["asset"]["value"])
        print(("saved " + outname + " " + str(len(d['asset']['value'])) + " chars").encode())
except urllib.error.HTTPError as e:
    print((str(e.code) + ": " + e.read().decode()[:300]).encode())
