import urllib.request, json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}
P = '/products/survival72-modular-configurator'

def gql(query, variables=None):
    payload = {'query': query, 'variables': variables or {}}
    req = urllib.request.Request(f'https://{SHOP}/admin/api/{API_VER}/graphql.json', data=json.dumps(payload).encode(), headers=HDRS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

# 1. Update Main Menu
m_query = """mutation menuUpdate($id: ID!, $title: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, items: $items) {
    userErrors { field message }
  }
}"""
m_vars = {
    'id': 'gid://shopify/Menu/243024232493',
    'title': 'Main menu',
    'items': [
        {'title': 'Shop the Kit', 'type': 'HTTP', 'url': P},
        {'title': 'Field Guide', 'type': 'HTTP', 'url': '/blogs/field-guide'},
        {'title': 'Gift Sets', 'type': 'HTTP', 'url': '/pages/gift-sets'},
        {'title': 'About', 'type': 'HTTP', 'url': '/pages/about'},
        {'title': 'Contact', 'type': 'HTTP', 'url': '/pages/contact'},
    ]
}
print("Updating Main Menu...", gql(m_query, m_vars))

# 2. Update Footer Support
f_vars = {
    'id': 'gid://shopify/Menu/243286999085',
    'title': 'footer-support',
    'items': [
        {'title': 'Contact Us', 'type': 'HTTP', 'url': '/pages/contact'},
        {'title': 'Corporate & Bespoke', 'type': 'HTTP', 'url': '/pages/corporate-partnerships'},
        {'title': 'Return Policy', 'type': 'HTTP', 'url': '/pages/return-policy'},
    ]
}
print("Updating Footer Support...", gql(m_query, f_vars))

# 3. Create/Update Corporate Page
p_query = """mutation pageCreate($page: PageCreateInput!) {
  pageCreate(page: $page) {
    page { handle }
    userErrors { field message }
  }
}"""
CORP_HTML = """
<style>
  .corp-hero { background: #1a1a1a; color: #fff; padding: 100px 24px; text-align: center; }
  .corp-content { max-width: 800px; margin: 80px auto; padding: 0 24px; color: #444; line-height: 1.8; }
  .corp-title { font-size: 32px; font-weight: 700; color: #1a1a1a; margin-bottom: 30px; }
  .corp-accent { color: #C9A96E; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; }
</style>
<div class="corp-hero">
  <p class="corp-accent">Strategic Alliances</p>
  <h1 style="font-size: 48px; margin: 20px 0;">Corporate & Bespoke Solutions</h1>
  <p style="color: #aaa; font-size: 18px;">Excellence in preparedness for your organization and leadership.</p>
</div>
<div class="corp-content">
  <h2 class="corp-title">Beyond Bulk. Strategic Partnership.</h2>
  <p>Survival72 doesn’t just provide tools; we provide peace of mind for the world’s most discerning organizations. Our Corporate & Bespoke program is designed for entities that prioritize resilience, quality, and prestige.</p>
  
  <h3 style="margin-top: 40px;">Our Capabilities</h3>
  <ul>
    <li><strong>Executive Gifting:</strong> Custom-branded Elite Kits for leadership and key stakeholders.</li>
    <li><strong>Fleet & Project Supply:</strong> Specialized modular systems for high-stakes field operations.</li>
    <li><strong>Bespoke Laser Engraving:</strong> Precision marking of company logos or individual names on every tool module.</li>
    <li><strong>Dedicated Account Management:</strong> Priority logistics and structured procurement for GCC-wide deployments.</li>
  </ul>
  
  <p style="margin-top: 50px; border-top: 1px solid #eee; padding-top: 30px;">
    To discuss a strategic collaboration or to request a private briefing, please contact our Partnership Director at <strong>partnerships@survival72gear.com</strong> or use our secure contact form.
  </p>
</div>
"""
p_vars = {
    'page': {
        'title': 'Corporate & Bespoke',
        'handle': 'corporate-partnerships',
        'bodyHtml': CORP_HTML
    }
}
print("Creating Corporate Page...", gql(p_query, p_vars))
