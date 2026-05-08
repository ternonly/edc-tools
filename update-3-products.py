"""
Update 3 already-listed products: corrected body_html + upload images.
- AXE: add folding knife (7.2cm) capability
- WRENCH: add folding knife (7.5cm) capability
- PLIERS: change material to Stainless Steel finish; correct blade to 7.2cm
"""
import base64
import json
import os
import sys
import urllib.request
import urllib.error

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API = '2026-01'
IMG_DIR = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final'

PRODUCTS = {
    '8486561021997': {  # AXE
        'sku': 'S72-AXE',
        'images': ['axe-styled-02.jpg', 'axe-real-01.jpg', 'axe-styled-03.jpg'],
        'body_html': """<h3>Built to break, built to build.</h3>
<p>The Desert Breacher is your single-tool answer to roadside emergencies, off-road camp setup, and urban breach scenarios. Engineered for 50&deg;C desert conditions and tested against MIL-STD-810H impact standards.</p>
<h4>Key capabilities</h4>
<ul>
<li><strong>Vehicle Breach</strong> &mdash; Hardened steel head splits side windows in one strike</li>
<li><strong>Camp Build</strong> &mdash; Wood splitting, stake driving, branch clearing in one tool</li>
<li><strong>Built-in Folding Knife</strong> &mdash; 7.2 cm 3CR13 stainless blade integrated into the handle, deploys one-handed for cordage and field-cut work</li>
<li><strong>Multi-Tool Integration</strong> &mdash; Hammer face, claw, hex wrench, and bottle opener built into the handle</li>
<li><strong>Desert-Grade Coating</strong> &mdash; Black phosphate finish resists sand abrasion and Gulf humidity</li>
<li><strong>Tactical Carry</strong> &mdash; MOLLE-compatible nylon sheath included</li>
</ul>
<h4>Specifications</h4>
<table>
<tr><td><strong>Total Length</strong></td><td>20 cm</td></tr>
<tr><td><strong>Folding Knife Blade</strong></td><td>7.2 cm</td></tr>
<tr><td><strong>Head Material</strong></td><td>3CR13 Hardened Steel</td></tr>
<tr><td><strong>Handle</strong></td><td>Glass-fiber reinforced nylon, anti-slip rubber grip</td></tr>
<tr><td><strong>Weight</strong></td><td>485 g</td></tr>
<tr><td><strong>Dimensions</strong></td><td>20 &times; 11 &times; 3.4 cm</td></tr>
<tr><td><strong>Sheath</strong></td><td>1000D Nylon, MOLLE-compatible</td></tr>
</table>
<h4>What's in the box</h4>
<ul>
<li>1 &times; Desert Breacher Multi-Function Axe (with built-in folding knife)</li>
<li>1 &times; MOLLE Nylon Sheath</li>
<li>1 &times; Survival72 Quick-Reference Card</li>
</ul>
<h4>Shipping &amp; Returns</h4>
<p>Free shipping on orders over $35. Cash on Delivery available across UAE, Saudi Arabia, Qatar, Kuwait, and Oman. 30-day return window from delivery date.</p>"""
    },
    '8486561185837': {  # WRENCH
        'sku': 'S72-WRENCH',
        'images': ['wrench-styled-02.jpg', 'wrench-real-01.jpg', 'wrench-styled-03.jpg'],
        'body_html': """<h3>When the road fails you, this doesn't.</h3>
<p>The Roadside Fix is the EDC wrench every off-road driver and home prepper needs. Engineered for vehicle breakdowns, trailer emergencies, and improvised mechanical work in the harshest desert conditions.</p>
<h4>Key capabilities</h4>
<ul>
<li><strong>Universal Wrench Profile</strong> &mdash; Adjustable jaw fits 6 standard hex sizes (8mm-19mm)</li>
<li><strong>Plier Function</strong> &mdash; Hardened steel jaws grip nuts, bolts, wires</li>
<li><strong>Wire Cutter</strong> &mdash; Built-in cutter for emergency repair work</li>
<li><strong>Built-in Folding Knife</strong> &mdash; 7.5 cm 3CR13 stainless blade integrated into the handle, deploys one-handed for cord, tape and packaging</li>
<li><strong>Bottle Opener &amp; Hex Driver</strong> &mdash; Integrated into the spine</li>
<li><strong>Sand-Resistant Hinge</strong> &mdash; Sealed pivot keeps grit out in desert conditions</li>
</ul>
<h4>Specifications</h4>
<table>
<tr><td><strong>Total Length</strong></td><td>15.2 cm (closed)</td></tr>
<tr><td><strong>Folding Knife Blade</strong></td><td>7.5 cm</td></tr>
<tr><td><strong>Material</strong></td><td>3CR13 Hardened Stainless Steel</td></tr>
<tr><td><strong>Finish</strong></td><td>Black phosphate, anti-corrosion</td></tr>
<tr><td><strong>Weight</strong></td><td>320 g</td></tr>
<tr><td><strong>Dimensions</strong></td><td>15.2 &times; 4.2 &times; 10.6 cm</td></tr>
<tr><td><strong>Pouch</strong></td><td>1000D Nylon, belt-loop compatible</td></tr>
</table>
<h4>What's in the box</h4>
<ul>
<li>1 &times; Roadside Fix Multi-Function Wrench (with built-in folding knife)</li>
<li>1 &times; Nylon Belt Pouch</li>
<li>1 &times; Survival72 Quick-Reference Card</li>
</ul>
<h4>Shipping &amp; Returns</h4>
<p>Free shipping on orders over $35. Cash on Delivery available across UAE, Saudi Arabia, Qatar, Kuwait, and Oman. 30-day return window from delivery date.</p>"""
    },
    '8486561218605': {  # PLIERS
        'sku': 'S72-PLIERS',
        'images': ['pliers-real-01.jpg', 'pliers-real-02.jpg', 'pliers-styled-03.jpg', 'pliers-styled-04.jpg'],
        'body_html': """<h3>Precision when seconds matter.</h3>
<p>The Field Precision delivers surgical control for emergency repair, fine cutting, and intricate gripping work. The everyday-carry tool that bridges the gap between brute force and finesse.</p>
<h4>Key capabilities</h4>
<ul>
<li><strong>Needle-Nose Tip</strong> &mdash; Reach into tight spaces traditional pliers can't</li>
<li><strong>Wire Cutter &amp; Stripper</strong> &mdash; Hardened cutting blades handle copper, aluminum, fence wire</li>
<li><strong>Folding Knife Blade</strong> &mdash; Razor-sharp 7.2 cm stainless blade for cordage and field-cut work</li>
<li><strong>Integrated Bottle Opener</strong> &mdash; Always within reach</li>
<li><strong>One-Handed Deploy</strong> &mdash; Spring-assist opening for emergency speed</li>
</ul>
<h4>Specifications</h4>
<table>
<tr><td><strong>Closed Length</strong></td><td>11.7 cm</td></tr>
<tr><td><strong>Open Length</strong></td><td>17 cm</td></tr>
<tr><td><strong>Material</strong></td><td>Stainless Steel (natural silver finish)</td></tr>
<tr><td><strong>Folding Knife Blade</strong></td><td>7.2 cm</td></tr>
<tr><td><strong>Weight</strong></td><td>275 g</td></tr>
<tr><td><strong>Dimensions</strong></td><td>11.7 &times; 5.5 &times; 3.4 cm (closed)</td></tr>
</table>
<h4>What's in the box</h4>
<ul>
<li>1 &times; Field Precision Multi-Function Pliers</li>
<li>1 &times; Nylon Belt Pouch</li>
<li>1 &times; Survival72 Quick-Reference Card</li>
</ul>
<h4>Shipping &amp; Returns</h4>
<p>Free shipping on orders over $35. Cash on Delivery available across UAE, Saudi Arabia, Qatar, Kuwait, and Oman. 30-day return window from delivery date.</p>"""
    }
}

ALT_TEXT = {
    'axe-styled-02.jpg':   'Desert Breacher tactical axe with folding knife dual view',
    'axe-real-01.jpg':     'Desert Breacher tactical axe with deployed 7.2cm folding knife',
    'axe-styled-03.jpg':   'Desert Breacher tactical axe on black background',
    'wrench-styled-02.jpg':'Roadside Fix tactical wrench dimensions 15.2x4.2x10.6cm',
    'wrench-real-01.jpg':  'Roadside Fix tactical wrench with deployed 7.5cm folding knife',
    'wrench-styled-03.jpg':'Roadside Fix tactical wrench on black background',
    'pliers-real-01.jpg':  'Field Precision multi-function tactical pliers fully open',
    'pliers-real-02.jpg':  'Field Precision tactical pliers with deployed 7.2cm folding knife',
    'pliers-styled-03.jpg':'Field Precision tactical pliers integrated tools deployed',
    'pliers-styled-04.jpg':'Field Precision tactical pliers on black background',
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

def update_product(pid, body_html):
    status, resp = http('PUT', f'/products/{pid}.json', {
        'product': {'id': int(pid), 'body_html': body_html}
    })
    print(f'  PUT product {pid}: HTTP {status}')
    if status >= 400:
        print('    ERROR:', str(resp)[:300])
        return False
    return True

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
    img_id = resp.get('image', {}).get('id', '?')
    print(f'    [OK]   {fname}  pos={position}  img_id={img_id}')
    return True

def main():
    for pid, cfg in PRODUCTS.items():
        print(f'\n=== {cfg["sku"]} (product {pid}) ===')
        update_product(pid, cfg['body_html'])
        for i, fn in enumerate(cfg['images'], start=1):
            upload_image(pid, fn, i)
    print('\nDONE')

if __name__ == '__main__':
    main()
