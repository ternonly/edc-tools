import urllib.request, json, os

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
TOKEN = "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"
THEME_ID = 151511040045
url = f"https://wyntnb-8b.myshopify.com/admin/api/2026-01/themes/{THEME_ID}/assets.json?asset[key]=templates/index.json"

req = urllib.request.Request(url, headers={
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json"
})
resp = urllib.request.urlopen(req)
data = json.loads(resp.read().decode())
out_path = os.path.join(PROJ, "horizon-index-current.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

asset_value = json.loads(data["asset"]["value"])
print("=== ORDER (top-down) ===")
for k in asset_value.get("order", []):
    sec = asset_value["sections"].get(k, {})
    print(f"  {k:30s} -> type={sec.get('type')}")
print()
print("=== ALL SECTION KEYS ===")
print(list(asset_value["sections"].keys()))
print()
print(f"Saved raw to {out_path}")
print(f"Updated_at: {data['asset'].get('updated_at')}")
print(f"Size: {len(data['asset']['value'])} chars")
