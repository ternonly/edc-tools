import urllib.request, json

SHOP='wyntnb-8b.myshopify.com'; TOKEN='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'
THEME_ID='151511040045'; API_VER='2026-01'
HDRS={'X-Shopify-Access-Token':TOKEN,'Content-Type':'application/json'}

def get_asset(key):
    url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json?asset[key]={key}'
    req=urllib.request.Request(url,headers=HDRS)
    with urllib.request.urlopen(req) as r: return json.loads(r.read())['asset']['value']

def put_asset(key, value_str):
    url=f'https://{SHOP}/admin/api/{API_VER}/themes/{THEME_ID}/assets.json'
    body=json.dumps({'asset':{'key':key,'value':value_str}}).encode('utf-8')
    req=urllib.request.Request(url,data=body,headers=HDRS,method='PUT')
    try:
        with urllib.request.urlopen(req) as r:
            print(f'  HTTP {r.status}')
            return r.status
    except urllib.error.HTTPError as e:
        print(f'  HTTP {e.code}: {e.read()[:500]}')
        return e.code

raw = get_asset('sections/footer-group.json')
footer = json.loads(raw)

# Get the footer section key
footer_section_key = list(footer['sections'].keys())[0]
fs = footer['sections'][footer_section_key]

print(f'Footer section key: {footer_section_key}')
print(f'Current blocks: {list(fs["blocks"].keys())}')
print(f'Current block_order: {fs.get("block_order", [])}')

# Helper: make a group block with title + menu blocks
def make_menu_col(col_id, heading, menu_items):
    """
    menu_items: list of (label, url)
    Returns a group block dict with text heading + button links
    """
    inner_blocks = {}
    inner_order = []

    # Heading
    inner_blocks[f'{col_id}_h'] = {
        "type": "text",
        "settings": {
            "text": f"<p><strong>{heading}</strong></p>",
            "alignment": "left",
            "type_preset": "rte",
            "font": "var(--font-heading--family)",
            "font_size": "0.85rem",
            "letter_spacing": "0.12em",
            "case": "uppercase",
            "color": "var(--color-foreground)"
        },
        "blocks": {}
    }
    inner_order.append(f'{col_id}_h')

    for i, (label, url) in enumerate(menu_items):
        bid = f'{col_id}_link_{i}'
        inner_blocks[bid] = {
            "type": "button",
            "settings": {
                "label": label,
                "link": url,
                "style": "link",
                "size": "sm",
                "alignment": "flex-start"
            },
            "blocks": {}
        }
        inner_order.append(bid)

    return {
        "type": "group",
        "settings": {
            "content_direction": "column",
            "vertical_on_mobile": True,
            "horizontal_alignment": "flex-start",
            "vertical_alignment": "flex-start",
            "horizontal_alignment_flex_direction_column": "flex-start",
            "vertical_alignment_flex_direction_column": "flex-start",
            "gap": 8,
            "width": "fit",
            "custom_width": 20,
            "width_mobile": "fill",
            "height": "fit",
            "inherit_color_scheme": True,
            "padding-block-start": 0,
            "padding-block-end": 0,
            "padding-inline-start": 0,
            "padding-inline-end": 0
        },
        "blocks": inner_blocks,
        "block_order": inner_order
    }

P = '/products/survival72-modular-configurator'

col1 = make_menu_col('explore', 'Explore', [
    ('Shop the Kit',  P),
    ('Field Guide',   '/blogs/field-guide'),
    ('Gift Sets',     P),
])

col2 = make_menu_col('support', 'Support', [
    ('Contact Us',        '/pages/contact'),
    ('Wholesale Inquiry', '/pages/wholesale'),
    ('Return Policy',     '/pages/return-policy'),
])

col3 = make_menu_col('brand', 'Brand', [
    ('About Survival72', '/pages/about'),
    ('Our Promise',      '/pages/our-promise'),
])

# Preserve existing brand block (logo + tagline), replace nav blocks
# Keep: group_brand (if exists)
existing_blocks = fs['blocks']
existing_order  = fs.get('block_order', list(existing_blocks.keys()))

# Keep only brand block (first group_brand), replace rest
new_blocks = {}
new_order  = []

if 'group_brand' in existing_blocks:
    # Update tagline to new brand voice
    gb = existing_blocks['group_brand']
    # Update tagline text
    if 'text_brand_tag' in gb['blocks']:
        gb['blocks']['text_brand_tag']['settings']['text'] = (
            "<p>Three tools. One system. Carried daily.<br>"
            "Those who carry, know why.</p>"
        )
    new_blocks['group_brand'] = gb
    new_order.append('group_brand')

# Add three nav columns
new_blocks['group_explore'] = col1
new_order.append('group_explore')

new_blocks['group_support'] = col2
new_order.append('group_support')

new_blocks['group_brand_links'] = col3
new_order.append('group_brand_links')

# Add payment icons and divider at end if they existed
for k in existing_order:
    if k not in new_blocks and existing_blocks[k]['type'] in ('payment-icons','_divider','social-links'):
        new_blocks[k] = existing_blocks[k]
        new_order.append(k)

fs['blocks'] = new_blocks
fs['block_order'] = new_order

print(f'New block_order: {new_order}')
print('Uploading footer-group.json...')
put_asset('sections/footer-group.json', json.dumps(footer, indent=2))
print('Done.')
