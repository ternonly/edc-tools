import urllib.request, json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
THEME = '151511040045'
HDRS = {'X-Shopify-Access-Token': TOKEN}

# Read
req = urllib.request.Request(
    f'https://{SHOP}/admin/api/2026-01/themes/{THEME}/assets.json?asset[key]=layout/theme.liquid',
    headers=HDRS
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
val = data['asset']['value']

# Show body line
for l in val.split('\n'):
    if '<body' in l:
        print('BODY TAG:', repr(l.strip()))
        break

OLD = 'page-width-{{ settings.page_width }} card-hover-effect-{{ settings.card_hover_effect }}'
ADD = '{% if request.page_type == "page" %} page-{{ page.handle }}{% endif %}'

if OLD in val and ADD not in val:
    new_val = val.replace(OLD, OLD + ADD, 1)
    print('Patching theme.liquid ...')
    HDRS2 = dict(HDRS)
    HDRS2['Content-Type'] = 'application/json'
    payload = {'asset': {'key': 'layout/theme.liquid', 'value': new_val}}
    req2 = urllib.request.Request(
        f'https://{SHOP}/admin/api/2026-01/themes/{THEME}/assets.json',
        data=json.dumps(payload).encode(), headers=HDRS2, method='PUT'
    )
    with urllib.request.urlopen(req2) as r2:
        res = json.loads(r2.read())
        print('theme.liquid updated, size:', res['asset']['size'])
elif ADD in val:
    print('Already patched.')
else:
    print('OLD string not found! Check body tag manually.')
