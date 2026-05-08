"""Create 3 bundle products + upload images."""
import base64, json, os, urllib.request, urllib.error

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API = '2026-01'
IMG_DIR = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final'
JSON_DIR = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project'

# JSON file -> images list (in display order)
COMBOS = [
    ('product-create-axe-pliers.json',    ['kit-real-flat.jpg', 'axe-real-01.jpg', 'pliers-real-01.jpg', 'axe-styled-03.jpg']),
    ('product-create-wrench-pliers.json', ['kit-real-flat.jpg', 'wrench-real-01.jpg', 'pliers-real-02.jpg', 'wrench-styled-03.jpg']),
    ('product-create-axe-wrench.json',    ['kit-real-flat.jpg', 'axe-real-01.jpg', 'wrench-real-01.jpg', 'kit-real-shop.jpg']),
]

ALT_TEXT = {
    'kit-real-flat.jpg':  'Survival72 multi-tool bundle flat lay',
    'kit-real-shop.jpg':  'Survival72 multi-tool bundle in workshop scene',
    'axe-real-01.jpg':    'Desert Breacher tactical axe with deployed folding knife',
    'wrench-real-01.jpg': 'Roadside Fix tactical wrench with deployed folding knife',
    'pliers-real-01.jpg': 'Field Precision multi-function tactical pliers',
    'pliers-real-02.jpg': 'Field Precision tactical pliers with deployed folding knife',
    'axe-styled-03.jpg':  'Desert Breacher tactical axe on black background',
    'wrench-styled-03.jpg':'Roadside Fix tactical wrench on black background',
}

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

def upload_image(pid, fname, position):
    fp = os.path.join(IMG_DIR, fname)
    with open(fp, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    body = {'image': {
        'attachment': b64,
        'filename': fname,
        'alt': ALT_TEXT.get(fname, fname),
        'position': position,
    }}
    status, resp = http('POST', f'/products/{pid}/images.json', body)
    if status >= 400:
        print(f'    [FAIL] {fname}: HTTP {status} {str(resp)[:200]}')
        return False
    print(f'    [OK]   {fname} pos={position} img_id={resp.get("image",{}).get("id","?")}')
    return True

def main():
    results = []
    for jf, imgs in COMBOS:
        with open(os.path.join(JSON_DIR, jf), encoding='utf-8') as f:
            payload = json.load(f)
        sku = payload['product']['variants'][0]['sku']
        title = payload['product']['title']
        print(f'\n=== {sku} | {title} ===')
        status, resp = http('POST', '/products.json', payload)
        print(f'  POST /products.json: HTTP {status}')
        if status >= 400:
            print('    ERROR:', str(resp)[:400])
            continue
        prod = resp.get('product', {})
        pid = prod.get('id')
        vid = prod.get('variants', [{}])[0].get('id')
        handle = prod.get('handle')
        print(f'    pid={pid}  variant_id={vid}  handle={handle}')
        results.append({'sku': sku, 'product_id': pid, 'variant_id': vid, 'handle': handle})
        for i, fn in enumerate(imgs, start=1):
            upload_image(pid, fn, i)

    # Persist results
    out = os.path.join(JSON_DIR, 'created-combos.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print('\nSaved IDs to', out)
    print('DONE')

if __name__ == '__main__':
    main()
