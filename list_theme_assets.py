import urllib.request, json

SHOP='wyntnb-8b.myshopify.com'; TOKEN='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'
THEME_ID='151511040045'; API_VER='2026-01'
HDRS={'X-Shopify-Access-Token':TOKEN}

url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
req=urllib.request.Request(url,headers=HDRS)
with urllib.request.urlopen(req) as r:
    data=json.loads(r.read())

assets = data['assets']
# Filter for JSON files
json_files = [a['key'] for a in assets if a['key'].endswith('.json')]
print('JSON files in theme:')
for k in sorted(json_files):
    print(f'  {k}')
