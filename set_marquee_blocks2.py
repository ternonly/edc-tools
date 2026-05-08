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

def put_asset(key, value_str):
    url = f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
    body = json.dumps({'asset': {'key': key, 'value': value_str}}).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=HDRS, method='PUT')
    try:
        with urllib.request.urlopen(req) as r:
            resp = r.read()
            print(f'HTTP {r.status}')
            return r.status
    except urllib.error.HTTPError as e:
        body = e.read()
        print(f'HTTP {e.code}: {body[:600]}')
        return e.code

data = get_asset('templates/index.json')
index = json.loads(data['asset']['value'])

credibility_items = [
    "<p>3 Tools · 1 System</p>",
    "<p>Ships Within 48h</p>",
    "<p>2-Year Guarantee</p>",
    "<p>Gift-Ready Packaging</p>",
    "<p>Free Shipping Over $100</p>",
    "<p>3 Tools · 1 System</p>",
    "<p>Ships Within 48h</p>",
]

blocks = {}
block_order = []
for i, text in enumerate(credibility_items):
    block_id = f'cred_{i}'
    blocks[block_id] = {
        "type": "text",
        "settings": {
            "text": text
        }
    }
    block_order.append(block_id)

index['sections']['marquee'] = {
    "type": "marquee",
    "blocks": blocks,
    "block_order": block_order,
    "settings": {
        "color_scheme": "scheme-2",
        "movement_direction": "reverse",
        "gap_between_elements": 48
    }
}

print('Uploading...')
put_asset('templates/index.json', json.dumps(index, indent=2))
print('Done.')
