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

# Print full header_section settings and blocks
hs = hg['sections']['header_section']
print('header_section full settings:')
print(json.dumps(hs.get('settings', {}), indent=2))
print()
print('header_section blocks:')
for bk, bv in hs.get('blocks', {}).items():
    print(f'  [{bk}] type={bv.get("type","")} settings={json.dumps(bv.get("settings",{}))[:120]}')
