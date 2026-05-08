"""Upload Hero Banner to Shopify theme assets/ directory (base64 attachment)."""
import urllib.request, json, base64, os

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
TOKEN = "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"
THEME_ID = 151511040045
SRC = os.path.join(PROJ, "hero-banner-final.jpg")
URL = f"https://wyntnb-8b.myshopify.com/admin/api/2026-01/themes/{THEME_ID}/assets.json"

with open(SRC, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

payload = json.dumps({"asset": {"key": "assets/hero-banner-final.jpg", "attachment": b64}}).encode()
req = urllib.request.Request(URL, data=payload, method="PUT", headers={
    "X-Shopify-Access-Token": TOKEN,
    "Content-Type": "application/json"
})
try:
    r = urllib.request.urlopen(req)
    res = json.loads(r.read().decode())
    print(f"OK HTTP {r.status}")
    print(f"  key:        {res['asset']['key']}")
    print(f"  public_url: {res['asset'].get('public_url')}")
    print(f"  size:       {res['asset'].get('size')}")
except urllib.error.HTTPError as e:
    print(f"FAIL {e.code}: {e.read().decode()[:500]}")
