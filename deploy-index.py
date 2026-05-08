"""PUT new templates/index.json to Horizon theme."""
import urllib.request, json, os

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
TOKEN = "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"
THEME_ID = 151511040045
URL = f"https://wyntnb-8b.myshopify.com/admin/api/2026-01/themes/{THEME_ID}/assets.json"

with open(os.path.join(PROJ, "horizon-index-NEW.json"), encoding="utf-8") as f:
    new_value = f.read()

payload = json.dumps({"asset": {"key": "templates/index.json", "value": new_value}}).encode()
req = urllib.request.Request(URL, data=payload, method="PUT", headers={
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json"
})
try:
    r = urllib.request.urlopen(req)
    res = json.loads(r.read().decode())
    print(f"OK HTTP {r.status}")
    print(f"  updated_at: {res['asset'].get('updated_at')}")
    print(f"  size:       {res['asset'].get('size')} bytes")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"FAIL HTTP {e.code}")
    print(body[:2500])
