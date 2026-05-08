import urllib.request, json, re

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
        print(f'  HTTP {e.code}: {e.read()[:400]}')
        return e.code

# Read settings_data.json
raw = get_asset('config/settings_data.json')
settings = json.loads(raw)

# Find footer section key in current
print('Top-level keys in settings_data:', list(settings.keys())[:10])

# settings_data has "current" key with all section configs
current = settings.get('current', settings)
sections = current.get('sections', {})
print('Section keys:', list(sections.keys())[:20])

# Find footer section
footer_key = None
for k, v in sections.items():
    if isinstance(v, dict) and v.get('type') == 'footer':
        footer_key = k
        print(f'Footer section key: {k}')
        print('Current footer config:', json.dumps(v, indent=2)[:800])
        break

if not footer_key:
    print('No footer section found — checking all types:')
    for k, v in sections.items():
        if isinstance(v, dict):
            print(f'  {k}: type={v.get("type","")}')
