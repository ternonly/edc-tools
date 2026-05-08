import urllib.request, json

SHOP='wyntnb-8b.myshopify.com'; TOKEN='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'
THEME_ID='151511040045'; API_VER='2026-01'
HDRS={'X-Shopify-Access-Token':TOKEN,'Content-Type':'application/json'}

def get_asset(key):
    url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]={key}'
    req=urllib.request.Request(url,headers=HDRS)
    with urllib.request.urlopen(req) as r: return json.loads(r.read())['asset']['value']

raw = get_asset('sections/header-group.json')
hg = json.loads(raw)

# Find menu setting in header section
hs_key = list(hg['sections'].keys())[0]
hs = hg['sections'][hs_key]
print(f'Header section key: {hs_key}')
print(f'Header settings: {json.dumps(hs.get("settings",{}), indent=2)[:600]}')
