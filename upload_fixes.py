import urllib.request, json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
THEME_ID = '151511040045'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

SCHEMA_SUFFIX = '''
{% schema %}
{
  "name": "S72 Custom",
  "settings": [],
  "presets": [{"name": "S72 Custom"}]
}
{% endschema %}
'''

def put_asset(key, value_str):
    url = f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
    body = json.dumps({'asset': {'key': key, 'value': value_str}}).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=HDRS, method='PUT')
    try:
        with urllib.request.urlopen(req) as r:
            print(f'  HTTP {r.status}')
            return r.status
    except urllib.error.HTTPError as e:
        print(f'  HTTP {e.code}: {e.read()[:300]}')
        return e.code

# Upload fixed sections
fixes = [
    ('sections/s72-system.liquid',  'theme_new/section_system.html'),
    ('sections/s72-proof.liquid',   'theme_new/section_proof.html'),
]

for asset_key, html_file in fixes:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    liquid = html + '\n' + SCHEMA_SUFFIX
    print(f'Uploading {asset_key}...')
    put_asset(asset_key, liquid)

print('Done.')
