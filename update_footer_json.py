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
            return r.status
    except urllib.error.HTTPError as e:
        print(f'  HTTP {e.code}: {e.read()[:500]}')
        return e.code

# Try to read sections/footer.json (Horizon theme pattern)
try:
    raw = get_asset('sections/footer.json')
    print('Found sections/footer.json:')
    print(raw[:1200])
except Exception as e:
    print(f'sections/footer.json not found: {e}')

# Try templates/footer.json
try:
    raw2 = get_asset('templates/footer.json')
    print('Found templates/footer.json:')
    print(raw2[:1200])
except Exception as e:
    print(f'templates/footer.json not found: {e}')
