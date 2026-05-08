import urllib.request, json, sys

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
THEME_ID = '151511040045'
API_VER = '2026-01'

# We'll use the section types that actually exist in the Horizon theme
# Based on the list: hero, media-with-content, featured-product, section
# For rich-text, we'll try 'section' or similar.

new_index = {
  "sections": {
    "hero": {
      "type": "hero",
      "settings": {
        "title": "THE 72-HOUR RULE.",
        "subheading": "BE THE FIRST LINE OF DEFENSE. High-performance modular systems engineered for GCC desert survival. Help is miles away—be ready.",
        "h_btn1_text": "START CONFIGURATION",
        "h_btn1_link": "#shopify-section-featured_configurator"
      }
    },
    "marquee": {
      "type": "marquee",
      "settings": {
        "text": "DESERT TESTED. GCC VERIFIED. | BUILT FOR THE 72 HOURS THAT MATTER MOST. | ISO 9001 CERTIFIED."
      }
    },
    "why": {
      "type": "media-with-content",
      "settings": {
        "heading": "WHY 72 HOURS?",
        "text": "Regional emergency guidelines converge on one number: 72 hours. It is the critical window where a household must be self-sufficient before external aid arrives. Our 3-tool core is built for the specific physics of desert survival: Breach, Recovery, and Precision Repair.",
        "button_text": "LEARN MORE"
      }
    },
    "featured_configurator": {
      "type": "featured-product",
      "settings": {
        "product": "survival72-modular-system-configurator"
      }
    }
  },
  "order": ["hero", "marquee", "why", "featured_configurator"]
}

url = f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
payload = {'asset': {'key': 'templates/index.json', 'value': json.dumps(new_index)}}
hdrs = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=hdrs, method='PUT')
try:
    with urllib.request.urlopen(req) as r:
        print(f'HOMEPAGE UPDATE SUCCESS: status {r.status}')
except urllib.error.HTTPError as e:
    print(f'UPDATE FAILED {e.code}: {e.read().decode()}')
except Exception as e:
    print(f'ERROR: {e}')
