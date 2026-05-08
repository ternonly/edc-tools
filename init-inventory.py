"""Initialize inventory: 8 SKUs x 100 units at location 84917387309."""
import json, os, urllib.request, urllib.error

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API = '2026-01'
LOCATION_ID = 84917387309

# All 8 variant IDs (from session memory + just-created)
VARIANTS = [
    ('S72-AXE',          44895111675949),
    ('S72-WRENCH',       None),  # need to fetch
    ('S72-PLIERS',       None),  # need to fetch
    ('S72-AXE-PLIERS',   44895136251949),
    ('S72-WRENCH-PLIERS',44895136350253),
    ('S72-AXE-WRENCH',   44895136514093),
    ('S72-KIT-STD',      44895136612397),
    ('S72-KIT-GIFT',     44895136645165),
]

# product_id list to lookup wrench/pliers variants
PRODUCT_LOOKUP = {
    'S72-WRENCH': 8486561185837,
    'S72-PLIERS': 8486561218605,
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

# 1. Resolve missing variant IDs
resolved = []
for sku, vid in VARIANTS:
    if vid is None:
        pid = PRODUCT_LOOKUP[sku]
        s, r = http('GET', f'/products/{pid}.json')
        v = r['product']['variants'][0]
        vid = v['id']
        print(f'Resolved {sku}: variant_id={vid}')
    resolved.append((sku, vid))

# 2. Get inventory_item_id for each variant
inv_items = []
for sku, vid in resolved:
    s, r = http('GET', f'/variants/{vid}.json')
    if s >= 400:
        print(f'  [FAIL get variant] {sku}: {s} {str(r)[:200]}')
        continue
    inv_id = r['variant']['inventory_item_id']
    inv_items.append((sku, vid, inv_id))
    print(f'{sku}: variant={vid} inventory_item={inv_id}')

# 3. Connect inventory to location (idempotent) + set available=100
print('\n--- Connecting + setting inventory ---')
for sku, vid, inv_id in inv_items:
    # Connect (no-op if already connected, returns 422 — ignore)
    s, r = http('POST', '/inventory_levels/connect.json', {
        'location_id': LOCATION_ID,
        'inventory_item_id': inv_id,
    })
    if s >= 400 and 'already' not in str(r).lower():
        print(f'  [connect FAIL] {sku}: {s} {str(r)[:150]}')

    # Set available=100
    s, r = http('POST', '/inventory_levels/set.json', {
        'location_id': LOCATION_ID,
        'inventory_item_id': inv_id,
        'available': 100,
    })
    if s >= 400:
        print(f'  [set FAIL] {sku}: {s} {str(r)[:200]}')
    else:
        print(f'  [OK] {sku} -> 100')

print('\nDONE')
