import urllib.request, json, sys

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API_VER = '2026-01'
BLOG_ID = '97993064493'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

def post_article(title, body, tags):
    url = f'https://{SHOP}/admin/api/{API_VER}/blogs/{BLOG_ID}/articles.json'
    data = {'article': {'title': title, 'body_html': body, 'tags': tags, 'published': True, 'author': 'Cole Mercer'}}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=HDRS, method='POST')
    with urllib.request.urlopen(req) as r:
        print(f'Article "{title}" posted: {r.status}')

# 1. Update About Page
about_html = """
<div style="max-width: 800px; margin: 0 auto; line-height: 1.8; color: #333;">
  <p style="font-size: 1.2rem; font-weight: 700; color: #111; margin-bottom: 2rem;">I remember exactly where I was when I realized the "preparedness" industry was broken.</p>
  
  <p>I was training a group of families in the Empty Quarter. A simple battery terminal failure on a lead vehicle should have been a 5-minute fix. Instead, it became a 2-hour ordeal because the "survival multi-tool" someone had bought online snapped under the torque of a real nut. It was a toy masquerading as a tool.</p>

  <p>I’m <strong>Cole Mercer</strong>. For a decade, I’ve taught families across the GCC how to survive the first 72 hours of a crisis. I don’t teach "tactical cosplay." I teach household self-sufficiency—because when a flash flood hits or a supply chain gaps, help isn't coming for at least three days.</p>

  <p>I founded <strong>Survival72</strong> because I was tired of seeing families rely on gear built for mountain hikers. We live in a desert. Our heat reaches 50°C. Our sand is abrasive. Our vehicles are different. We need gear that respects those realities.</p>

  <p style="font-weight: 700;">The Three-Tool System is my answer.</p>
  
  <p>I stripped away the fluff. You don’t need a 20-in-1 gadget. You need a <strong>Breacher Axe</strong> for entry, a <strong>Roadside Wrench</strong> for utility, and <strong>Precision Pliers</strong> that won't melt or bend when you need them most. Each tool is built to survive a month-long stress cycle in the Empty Quarter before I even think about selling it to you.</p>

  <p>I’m not building a tactical brand. I’m building a promise. When you carry Survival72, you carry my ten years of experience in the field. You carry the confidence that if things go wrong, you’re the one who makes them right.</p>

  <div style="margin-top: 3rem; padding: 2rem; border: 1px solid #C9A96E; background: #fffbf2; text-align: center;">
    <p style="font-style: italic; margin-bottom: 1rem;">"The first 72 hours decide everything. I make the gear that stands behind a family during those hours."</p>
    <p style="font-weight: 700;">— Cole Mercer</p>
  </div>
</div>
"""

url_about = f'https://{SHOP}/admin/api/{API_VER}/pages.json?handle=about'
req_about = urllib.request.Request(url_about, headers=HDRS)
with urllib.request.urlopen(req_about) as r:
    page = json.loads(r.read())['pages'][0]
    pid = page['id']
    url_u = f'https://{SHOP}/admin/api/{API_VER}/pages/{pid}.json'
    data_u = {'page': {'id': pid, 'body_html': about_html}}
    req_u = urllib.request.Request(url_u, data=json.dumps(data_u).encode(), headers=HDRS, method='PUT')
    with urllib.request.urlopen(req_u) as r_u:
        print(f'About Page Updated: {r_u.status}')

# 2. Post Blog Articles
post_article(
    "Pliers vs. Multi-tools: Why Dedicated Grip Wins",
    "<p>A multi-tool is a master of none. When you need to strip a corroded wire in 50°C heat or grip a stuck bolt on a desert-caked generator, the flimsy hinges of a pocket tool fail. This guide explains why dedicated, long-handle precision pliers are the non-negotiable anchor of your 72-hour kit.</p>",
    "Tactical, Pliers, Education"
)

post_article(
    "Wrench Sizing: The 10mm Standard & Survival Scenarios",
    "<p>If you can't shut off your water main or disconnect a dead car battery, your kit is decorative. Most emergency scenarios in the Gulf revolve around utility management and vehicle recovery. We break down the exact wrench specs you need to handle everything from residential gate valves to heavy-duty roof rack adjustments.</p>",
    "Utility, Wrench, Field Guide"
)

post_article(
    "Axe Geometry: Why the Breacher Blade Matters",
    "<p>In a desert environment, an axe isn't just for wood. It's for door breach, sand-stake extraction, and emergency vehicle access. The Survival72 Breacher Axe uses a unique 45-degree bevel geometry optimized for high-impact prying and cold-forged durability. Learn how to use it safely and effectively.</p>",
    "Axe, Breach, Recovery"
)
