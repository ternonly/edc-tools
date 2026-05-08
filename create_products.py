import urllib.request, json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}
BASE = 'https://cdn.shopify.com/s/files/1/0751/9030/4813/files/'

# Known image URLs grouped by product
PLIERS_IMAGES = [
    BASE + 's72_pliers_1.png',
    BASE + 'pliers_4.jpg',
    BASE + 'pliers_5.jpg',
    BASE + 'pliers_6.jpg',
    BASE + 'pliers_7.jpg',
    BASE + 'pliers_8.jpg',
    BASE + 'pliers_9.jpg',
    BASE + 'pliers_10.jpg',
    BASE + 'optimized_image.webp',
]

WRENCH_IMAGES = [
    BASE + 's72_wrench_1.jpg',
    BASE + '12.jpg',
    BASE + '13.jpg',
    BASE + '14.jpg',
    BASE + '15.jpg',
    BASE + '16.jpg',
    BASE + '11.jpg',
]

AXE_IMAGES = [
    BASE + 's72_axe_1.jpg',
    BASE + '1.jpg',
    BASE + '2.jpg',
    BASE + '3.jpg',
    BASE + '6.jpg',
    BASE + '7.jpg',
    BASE + '8.jpg',
]

PLIERS_DESC = """
<div style="font-family:'Helvetica Neue',sans-serif;max-width:700px;color:#1a1a1a">
  <h2 style="font-size:20px;font-weight:700;letter-spacing:1px;text-transform:uppercase">Survival72™ Precision Multi-Pliers</h2>
  <p style="color:#555;line-height:1.7">Built for professionals who demand reliability in the field. The PA-92A Multi-Pliers delivers 25 functions in a compact, aircraft-grade stainless steel body — engineered for EDC deployment in high-stakes environments.</p>
  <ul style="line-height:2;padding-left:18px">
    <li>25-in-1 multitool — pliers, knife, saw, screwdrivers, can opener &amp; more</li>
    <li>Aircraft-grade 420 stainless steel — corrosion resistant</li>
    <li>Compact folded length: 10.5 cm | Weight: 180g</li>
    <li>Spring-loaded jaw for one-hand operation</li>
    <li>Locking blades for field safety</li>
    <li>Compatible with Survival72™ Elite Magnetic Gift Box</li>
  </ul>
  <p style="margin-top:24px;font-size:13px;color:#888">Ships within 3-5 business days. Free shipping on orders over $99.</p>
</div>
"""

WRENCH_DESC = """
<div style="font-family:'Helvetica Neue',sans-serif;max-width:700px;color:#1a1a1a">
  <h2 style="font-size:20px;font-weight:700;letter-spacing:1px;text-transform:uppercase">Survival72™ Roadside Wrench</h2>
  <p style="color:#555;line-height:1.7">The KA-62A Ratchet Wrench is the most overlooked tool in a professional EDC kit. With 9 interchangeable bits and a compact ratchet mechanism, it covers 90% of roadside and field maintenance tasks.</p>
  <ul style="line-height:2;padding-left:18px">
    <li>9-bit ratchet wrench — Phillips, flathead, hex, Torx &amp; more</li>
    <li>Reversible ratchet — clockwise &amp; counter-clockwise</li>
    <li>Drop-forged CR-V steel — tool-grade durability</li>
    <li>Compact folded length: 12 cm | Weight: 145g</li>
    <li>Magnetic bit holder for fast swaps</li>
    <li>Compatible with Survival72™ Elite Magnetic Gift Box</li>
  </ul>
  <p style="margin-top:24px;font-size:13px;color:#888">Ships within 3-5 business days. Free shipping on orders over $99.</p>
</div>
"""

AXE_DESC = """
<div style="font-family:'Helvetica Neue',sans-serif;max-width:700px;color:#1a1a1a">
  <h2 style="font-size:20px;font-weight:700;letter-spacing:1px;text-transform:uppercase">Survival72™ Desert Breacher Axe</h2>
  <p style="color:#555;line-height:1.7">The XI-G8 is not a novelty — it is a precision-engineered breaching and utility axe designed for desert and urban environments. Where others carry a hatchet, professionals carry this.</p>
  <ul style="line-height:2;padding-left:18px">
    <li>8-function axe — hatchet, hammer, pry bar, bottle opener, hex wrench &amp; more</li>
    <li>G10 composite handle — impact-resistant, non-slip grip</li>
    <li>3CR13 stainless steel head — field-sharpened edge</li>
    <li>Overall length: 24 cm | Weight: 320g</li>
    <li>Includes ballistic nylon sheath</li>
    <li>Compatible with Survival72™ Elite Magnetic Gift Box</li>
  </ul>
  <p style="margin-top:24px;font-size:13px;color:#888">Ships within 3-5 business days. Free shipping on orders over $99.</p>
</div>
"""

PRODUCTS = [
    {
        'title': 'Survival72™ Precision Multi-Pliers',
        'handle': 's72-precision-pliers',
        'body_html': PLIERS_DESC,
        'vendor': 'Survival72',
        'product_type': 'EDC Tool',
        'tags': 'edc, pliers, multitool, survival, tactical',
        'status': 'active',
        'variants': [{'price': '52.00', 'compare_at_price': '69.00', 'sku': 'S72-PA92A', 'inventory_management': None}],
        'images': [{'src': u} for u in PLIERS_IMAGES],
    },
    {
        'title': 'Survival72™ Roadside Wrench',
        'handle': 's72-roadside-wrench',
        'body_html': WRENCH_DESC,
        'vendor': 'Survival72',
        'product_type': 'EDC Tool',
        'tags': 'edc, wrench, ratchet, survival, tactical',
        'status': 'active',
        'variants': [{'price': '42.00', 'compare_at_price': '58.00', 'sku': 'S72-KA62A', 'inventory_management': None}],
        'images': [{'src': u} for u in WRENCH_IMAGES],
    },
    {
        'title': 'Survival72™ Desert Breacher Axe',
        'handle': 's72-desert-breacher-axe',
        'body_html': AXE_DESC,
        'vendor': 'Survival72',
        'product_type': 'EDC Tool',
        'tags': 'edc, axe, hatchet, survival, tactical',
        'status': 'active',
        'variants': [{'price': '49.00', 'compare_at_price': '65.00', 'sku': 'S72-XIG8', 'inventory_management': None}],
        'images': [{'src': u} for u in AXE_IMAGES],
    },
]

results = {}
url = f'https://{SHOP}/admin/api/{API_VER}/products.json'

for p in PRODUCTS:
    data = json.dumps({'product': p}).encode()
    req = urllib.request.Request(url, data=data, headers=HDRS, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read())
            pid = res['product']['id']
            handle = res['product']['handle']
            print(f"Created: {res['product']['title']} | ID:{pid} | /products/{handle}")
            results[handle] = {'id': pid, 'handle': handle, 'title': res['product']['title']}
    except Exception as e:
        print(f"Failed: {p['title']} | {e}")

with open('created_products.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print('Done.')
