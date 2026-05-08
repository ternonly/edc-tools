import base64, json, os, urllib.request, urllib.error

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API = '2026-01'
IMG_DIR = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final'
JSON_DIR = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project'

def http(method, path, body=None):
    url = f'https://{SHOP}/admin/api/{API}{path}'
    data = json.dumps(body).encode('utf-8') if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        'X-Shopify-Access-Token': TOKEN,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8') or '{}')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='ignore')

with open(os.path.join(JSON_DIR, 'product-create-axe-wrench.json'), encoding='utf-8') as f:
    payload = json.load(f)

print('JSON parsed OK')
status, resp = http('POST', '/products.json', payload)
print(f'POST: HTTP {status}')
if status >= 400:
    print('ERROR:', str(resp)[:400])
    raise SystemExit(1)
prod = resp['product']
pid = prod['id']
print(f'pid={pid}  variant_id={prod["variants"][0]["id"]}  handle={prod["handle"]}')

imgs = ['kit-real-flat.jpg', 'axe-real-01.jpg', 'wrench-real-01.jpg', 'kit-real-shop.jpg']
alts = {
    'kit-real-flat.jpg':  'Survival72 Break & Build Kit flat lay',
    'kit-real-shop.jpg':  'Survival72 Break & Build Kit in workshop scene',
    'axe-real-01.jpg':    'Desert Breacher tactical axe with deployed folding knife',
    'wrench-real-01.jpg': 'Roadside Fix tactical wrench with deployed folding knife',
}
for i, fn in enumerate(imgs, start=1):
    fp = os.path.join(IMG_DIR, fn)
    with open(fp, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    body = {'image': {'attachment': b64, 'filename': fn, 'alt': alts[fn], 'position': i}}
    s, r = http('POST', f'/products/{pid}/images.json', body)
    if s >= 400:
        print(f'  [FAIL] {fn}: {s} {str(r)[:200]}')
    else:
        print(f'  [OK]   {fn} pos={i} img_id={r["image"]["id"]}')

# Append to created-combos.json
out = os.path.join(JSON_DIR, 'created-combos.json')
existing = []
if os.path.exists(out):
    with open(out, encoding='utf-8') as f:
        existing = json.load(f)
existing.append({'sku': 'S72-AXE-WRENCH', 'product_id': pid, 'variant_id': prod['variants'][0]['id'], 'handle': prod['handle']})
with open(out, 'w', encoding='utf-8') as f:
    json.dump(existing, f, indent=2)
print('DONE')
