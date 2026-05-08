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
        return r.status

# Read existing index.json to get marquee section id and update its settings
data = get_asset('templates/index.json')
index = json.loads(data['asset']['value'])
print('Current order:', index['order'])
print('Sections:', list(index['sections'].keys()))

# Find marquee section key
marquee_key = None
for k, v in index['sections'].items():
    if v.get('type') == 'marquee':
        marquee_key = k
        break

print(f'Marquee section key: {marquee_key}')

# Update marquee text in the section settings via locale overrides won't work easily
# Instead update the marquee section file's default text
# Let's fetch the marquee liquid and see the settings schema
mq_data = get_asset('sections/marquee.liquid')
mq = mq_data['asset']['value']
# Print schema portion
schema_start = mq.index('{% schema %}')
print(mq[schema_start:schema_start+1500])
