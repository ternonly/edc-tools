"""Create S72-KIT product (dual variant) + upload images, set Gift image as Gift variant featured."""
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

with open(os.path.join(JSON_DIR, 'product-create-kit.json'), encoding='utf-8') as f:
    payload = json.load(f)

print('Creating S72-KIT product...')
status, resp = http('POST', '/products.json', payload)
print(f'POST: HTTP {status}')
if status >= 400:
    print('ERROR:', str(resp)[:500])
    raise SystemExit(1)
prod = resp['product']
pid = prod['id']
variants = {v['option1']: v['id'] for v in prod['variants']}
print(f'pid={pid}  variants={variants}  handle={prod["handle"]}')

# Image plan: position 1 = main standard hero, then real shots, gift packaging assigned to Gift variant, outdoor scene last
gift_variant_id = variants['Gift Edition']

images_plan = [
    # (filename, position, variant_ids_to_attach)
    ('kit-real-flat.jpg',     1, []),                   # main featured
    ('kit-real-open.jpg',     2, []),
    ('kit-real-shop.jpg',     3, []),
    ('kit-styled-outdoor.jpg', 4, []),
    ('kit-gift-box.jpg',      5, [gift_variant_id]),    # featured for Gift Edition
]

alts = {
    'kit-real-flat.jpg':      'Survival72 72-Hour Kit three-tool flat lay',
    'kit-real-open.jpg':      'Survival72 72-Hour Kit all tools deployed',
    'kit-real-shop.jpg':      'Survival72 72-Hour Kit in workshop scene',
    'kit-styled-outdoor.jpg': 'Survival72 72-Hour Kit outdoor scene',
    'kit-gift-box.jpg':       'Survival72 72-Hour Kit Gift Edition magnetic clamshell box',
}

for fn, pos, var_ids in images_plan:
    fp = os.path.join(IMG_DIR, fn)
    if not os.path.exists(fp):
        print(f'  [SKIP] {fn} not found')
        continue
    with open(fp, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    img_body = {
        'attachment': b64,
        'filename': fn,
        'alt': alts.get(fn, fn),
        'position': pos,
    }
    if var_ids:
        img_body['variant_ids'] = var_ids
    s, r = http('POST', f'/products/{pid}/images.json', {'image': img_body})
    if s >= 400:
        print(f'  [FAIL] {fn}: {s} {str(r)[:200]}')
    else:
        img_id = r['image']['id']
        print(f'  [OK]   {fn} pos={pos} img_id={img_id} variants_linked={var_ids}')

# Append to created
out = os.path.join(JSON_DIR, 'created-combos.json')
existing = []
if os.path.exists(out):
    with open(out, encoding='utf-8') as f:
        existing = json.load(f)
existing.append({
    'sku': 'S72-KIT-STD', 'product_id': pid, 'variant_id': variants['Standard'], 'handle': prod['handle']
})
existing.append({
    'sku': 'S72-KIT-GIFT', 'product_id': pid, 'variant_id': variants['Gift Edition'], 'handle': prod['handle']
})
with open(out, 'w', encoding='utf-8') as f:
    json.dump(existing, f, indent=2)
print('DONE')
