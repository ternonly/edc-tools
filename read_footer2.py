import urllib.request, json, re
SHOP='wyntnb-8b.myshopify.com'; TOKEN='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'
THEME_ID='151511040045'; API_VER='2026-01'
HDRS={'X-Shopify-Access-Token':TOKEN}

url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]=sections/footer.liquid'
req=urllib.request.Request(url,headers=HDRS)
with urllib.request.urlopen(req) as r:
    data=json.loads(r.read())
liquid=data['asset']['value']

m=re.search(r'\{%-?\s*schema\s*-?%\}(.+?)\{%-?\s*endschema\s*-?%\}',liquid,re.DOTALL)
schema=json.loads(m.group(1))

# Print full menu block schema
for b in schema.get('blocks',[]):
    if b['type'] == 'menu':
        print('Full menu block:')
        print(json.dumps(b, indent=2))
        break

# Also print current index.json footer section config if any
url2=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]=templates/index.json'
req2=urllib.request.Request(url2,headers=HDRS)
with urllib.request.urlopen(req2) as r2:
    idx=json.loads(json.loads(r2.read())['asset']['value'])

print()
print('Current index sections referencing footer-type:', [k for k,v in idx['sections'].items()])
