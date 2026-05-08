import urllib.request, json, os

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
THEME_ID = '151511040045'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

def put_asset(key, value):
    url = f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
    body = json.dumps({'asset': {'key': key, 'value': value}}).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=HDRS, method='PUT')
    with urllib.request.urlopen(req) as r:
        return r.status

# Minimal standalone section schema that wraps raw HTML via custom_liquid setting
SCHEMA_SUFFIX = '''
{% schema %}
{
  "name": "S72 Custom",
  "settings": [],
  "presets": [{"name": "S72 Custom"}]
}
{% endschema %}
'''

section_map = [
    ('s72-problem', 'theme_new/section_problem.html'),
    ('s72-system',  'theme_new/section_system.html'),
    ('s72-edu',     'theme_new/section_edu.html'),
    ('s72-proof',   'theme_new/section_proof.html'),
    ('s72-gift',    'theme_new/section_gift.html'),
    ('s72-promise', 'theme_new/section_promise.html'),
]

for sec_id, html_file in section_map:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    liquid = html + '\n' + SCHEMA_SUFFIX
    asset_key = f'sections/{sec_id}.liquid'
    try:
        status = put_asset(asset_key, liquid)
        print(f'OK  {asset_key}: HTTP {status}')
    except Exception as e:
        print(f'ERR {asset_key}: {e}')

# Now rebuild index.json with all 8 sections in correct order
index = {
  "sections": {
    "hero": {
      "type": "hero",
      "settings": {
        "image_1": "shopify://shop_images/hero-banner-final.jpg",
        "toggle_overlay": True,
        "color_scheme": "scheme-5",
        "section_height": "large"
      }
    },
    "marquee": {
      "type": "marquee",
      "settings": {
        "color_scheme": "scheme-2"
      }
    },
    "s72_problem": {
      "type": "s72-problem",
      "settings": {}
    },
    "s72_system": {
      "type": "s72-system",
      "settings": {}
    },
    "s72_edu": {
      "type": "s72-edu",
      "settings": {}
    },
    "s72_proof": {
      "type": "s72-proof",
      "settings": {}
    },
    "s72_gift": {
      "type": "s72-gift",
      "settings": {}
    },
    "featured_configurator": {
      "type": "featured-product",
      "settings": {
        "product": "survival72-modular-configurator"
      }
    },
    "s72_promise": {
      "type": "s72-promise",
      "settings": {}
    }
  },
  "order": [
    "hero",
    "marquee",
    "s72_problem",
    "s72_system",
    "s72_edu",
    "s72_proof",
    "s72_gift",
    "featured_configurator",
    "s72_promise"
  ]
}

try:
    status = put_asset('templates/index.json', json.dumps(index, indent=2))
    print(f'OK  templates/index.json: HTTP {status}')
except Exception as e:
    print(f'ERR templates/index.json: {e}')

print('Done.')
