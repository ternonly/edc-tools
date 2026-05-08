import urllib.request, json

SHOP='wyntnb-8b.myshopify.com'; TOKEN='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'
THEME_ID='151511040045'; API_VER='2026-01'
HDRS={'X-Shopify-Access-Token':TOKEN,'Content-Type':'application/json'}

def get_asset(key):
    url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]={key}'
    req=urllib.request.Request(url,headers=HDRS)
    with urllib.request.urlopen(req) as r: return json.loads(r.read())['asset']['value']

def put_asset(key, value_str):
    url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
    body=json.dumps({'asset':{'key':key,'value':value_str}}).encode('utf-8')
    req=urllib.request.Request(url,data=body,headers=HDRS,method='PUT')
    try:
        with urllib.request.urlopen(req) as r:
            print(f'  HTTP {r.status}')
    except urllib.error.HTTPError as e:
        print(f'  HTTP {e.code}: {e.read()[:400]}')

raw = get_asset('sections/header-group.json')
hg = json.loads(raw)

# Print all sections in header-group
print(f'Sections in header-group: {list(hg["sections"].keys())}')
for k, v in hg['sections'].items():
    print(f'\n[{k}] type={v.get("type","")}')
    s = v.get('settings', {})
    # Look for menu-related settings
    for sk, sv in s.items():
        if 'menu' in sk.lower() or 'nav' in sk.lower():
            print(f'  MENU SETTING: {sk} = {sv}')
    if not any('menu' in sk.lower() for sk in s):
        print(f'  settings keys: {list(s.keys())[:10]}')
