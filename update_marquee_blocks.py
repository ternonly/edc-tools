import urllib.request, json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
THEME_ID = '151511040045'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

def get_asset(key):
    url = f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]={key}'
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def put_asset(key, value):
    url = f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
    body = json.dumps({'asset': {'key': key, 'value': value}}).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=HDRS, method='PUT')
    with urllib.request.urlopen(req) as r:
        resp_body = r.read()
        if r.status >= 400:
            print('BODY:', resp_body[:500])
        return r.status

# Read current index.json
data = get_asset('templates/index.json')
index = json.loads(data['asset']['value'])

# Check marquee block schema to understand text block settings
mq_data = get_asset('sections/marquee.liquid')
mq = mq_data['asset']['value']
# Extract block type "text" settings
import re
schema_match = re.search(r'\{%- schema -%\}(.+?)\{%- endschema -%\}', mq, re.DOTALL)
if not schema_match:
    schema_match = re.search(r'\{% schema %\}(.+?)\{% endschema %\}', mq, re.DOTALL)
schema = json.loads(schema_match.group(1))
# Find text block
for blk in schema.get('blocks', []):
    if blk['type'] == 'text':
        print('Text block settings:', json.dumps(blk, indent=2)[:1000])
        break
