"""Fetch any single Shopify theme asset to inspect schema."""
import urllib.request, json, sys, os

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
TOKEN = "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"
THEME_ID = 151511040045

def fetch(key, save_as=None):
    url = f"https://wyntnb-8b.myshopify.com/admin/api/2026-01/themes/{THEME_ID}/assets.json?asset[key]={key}"
    req = urllib.request.Request(url, headers={"X-Shopify-Access-Token": TOKEN})
    try:
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read().decode())
        val = data["asset"]["value"]
        if save_as:
            out = os.path.join(PROJ, save_as)
            with open(out, "w", encoding="utf-8") as f:
                f.write(val)
            print(f"OK: {key} -> {out} ({len(val)} chars)")
        else:
            print(val[:3000])
        return val
    except urllib.error.HTTPError as e:
        print(f"FAIL {key}: HTTP {e.code} {e.reason}")
        return None

if __name__ == "__main__":
    keys = sys.argv[1:] if len(sys.argv) > 1 else ["sections/hero.liquid"]
    for k in keys:
        save_name = k.replace("/", "_").replace(".liquid", ".liquid.txt")
        fetch(k, save_name)
