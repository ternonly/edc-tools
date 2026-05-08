import urllib.request, json
SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
API_VER = "2026-01"

# REST API: Online Store > Navigation menus
url = f"https://{SHOP}/admin/api/{API_VER}/menus.json"
req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
try:
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        for m in data.get("menus", []):
            print(f"{m['handle']:20} {m['title']:30} -> {len(m.get('items',[]))} items".encode())
            for it in m.get("items", []):
                print(f"    - {it.get('title')} -> {it.get('subject')}/{it.get('subject_id')}".encode())
except urllib.error.HTTPError as e:
    print(f"ERR {e.code}: {e.read().decode()}".encode())
