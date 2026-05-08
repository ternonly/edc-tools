import urllib.request, json

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

def rest_post_page(handle, title, body_html):
    url = f'https://{SHOP}/admin/api/{API_VER}/pages.json'
    data = {'page': {'title': title, 'handle': handle, 'body_html': body_html}}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=HDRS, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        # Check if handle already exists (422)
        if e.code == 422:
            # Need to update instead
            # First find the ID
            search_url = f'https://{SHOP}/admin/api/{API_VER}/pages.json?handle={handle}'
            req_search = urllib.request.Request(search_url, headers=HDRS)
            with urllib.request.urlopen(req_search) as r_search:
                pages = json.loads(r_search.read())['pages']
                if pages:
                    pid = pages[0]['id']
                    update_url = f'https://{SHOP}/admin/api/{API_VER}/pages/{pid}.json'
                    req_update = urllib.request.Request(update_url, data=json.dumps(data).encode(), headers=HDRS, method='PUT')
                    with urllib.request.urlopen(req_update) as r_update:
                        return json.loads(r_update.read())
        return e.read().decode()

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

GIFT_HTML = """
<style>
  .s72-gift-page { font-family: var(--font-body-family); color: #1a1a1a; line-height: 1.6; }
  .gift-hero { background: #111; color: #fff; padding: 100px 24px; text-align: center; }
  .gift-hero__kicker { color: #C9A96E; text-transform: uppercase; letter-spacing: 0.2em; font-size: 12px; margin-bottom: 20px; }
  .gift-hero__title { font-size: clamp(32px, 6vw, 56px); font-weight: 700; margin-bottom: 24px; line-height: 1.1; }
  .gift-hero__sub { font-size: 18px; color: #aaa; max-width: 600px; margin: 0 auto 40px; }
  
  .gift-grid { max-width: 1100px; margin: 80px auto; padding: 0 24px; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
  @media (max-width: 768px) { .gift-grid { grid-template-columns: 1fr; gap: 40px; text-align: center; } }
  .gift-grid__img { background: #f5f5f5; height: 400px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #ccc; border: 1px solid #eee; }
  
  .gift-section-title { font-size: 28px; font-weight: 700; margin-bottom: 20px; }
  .gift-section-text { font-size: 16px; color: #555; margin-bottom: 30px; }
  
  .gift-reviews { background: #f9f8f6; padding: 80px 24px; }
  .gift-reviews__inner { max-width: 1100px; margin: 0 auto; }
  .gift-reviews__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px; }
  .gift-review-card { background: #fff; padding: 30px; border-radius: 4px; border: 1px solid #eee; }
  .gift-review-card__stars { color: #C9A96E; margin-bottom: 15px; }
  .gift-review-card__text { font-style: italic; font-size: 15px; margin-bottom: 20px; color: #333; }
  .gift-review-card__meta { font-size: 13px; color: #888; }
  .gift-review-card__meta strong { color: #1a1a1a; }
  
  .gift-cta-section { text-align: center; padding: 100px 24px; border-top: 1px solid #eee; }
  .gift-cta-btn { background: #1a1a1a; color: #fff; padding: 20px 60px; border-radius: 4px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; text-decoration: none; display: inline-block; transition: background 0.2s; }
  .gift-cta-btn:hover { background: #C9A96E; color: #1a1a1a; }
  .gift-cta-sub { margin-top: 20px; color: #888; font-size: 14px; }
</style>

<div class="s72-gift-page">
  <section class="gift-hero">
    <p class="gift-hero__kicker">Exclusive Presentation</p>
    <h1 class="gift-hero__title">The Elite Gift Kit.<br>Ready to Deploy.</h1>
    <p class="gift-hero__sub">Give the gift of absolute reliability. All three modules, presented in our signature magnetic clamshell box.</p>
    <a href="/products/survival72-modular-configurator?auto_kit=elite" class="gift-cta-btn">Send the Elite Kit &rarr;</a>
  </section>

  <section class="gift-grid">
    <div class="gift-grid__img">[Premium Magnetic Box Image]</div>
    <div>
      <h2 class="gift-section-title">The Unboxing Experience</h2>
      <p class="gift-section-text">A quality tool deserves a quality introduction. Our Elite Kit is housed in a 2mm weighted gray-board box with a hidden magnetic closure. No wrapping paper needed—just a simple, industrial elegance that says "this is for life."</p>
      <ul style="color: #666; margin-bottom: 30px;">
        <li>Custom-cut high-density EVA foam inserts</li>
        <li>Soft-touch matte black finish</li>
        <li>Diagonal Survival72 silver foil branding</li>
        <li>Includes Field Guide printed quick-start card</li>
      </ul>
      <a href="/products/survival72-modular-configurator?auto_kit=elite" style="color: #C9A96E; font-weight: 700; text-decoration: none;">Customize this kit &rarr;</a>
    </div>
  </section>

  <section class="gift-reviews">
    <div class="gift-reviews__inner">
      <div style="text-align: center;">
        <p class="gift-hero__kicker" style="margin-bottom: 10px;">Gift Stories</p>
        <h2 class="gift-section-title">Shared by Those Who Give and Receive</h2>
      </div>
      <div class="gift-reviews__grid">
        <div class="gift-review-card">
          <div class="gift-review-card__stars">★★★★★</div>
          <p class="gift-review-card__text">"I bought this for my son's graduation from Engineering school. He appreciated the modular design immediately. The box made it feel like a serious milestone gift."</p>
          <p class="gift-review-card__meta">Sent by <strong>Omar F.</strong> to his son</p>
        </div>
        <div class="gift-review-card">
          <div class="gift-review-card__stars">★★★★★</div>
          <p class="gift-review-card__text">"My wife surprised me with the Elite Kit for my birthday. I’m a bit of a gear snob, but the build quality on these pliers is fantastic. Best gift I've had in years."</p>
          <p class="gift-review-card__meta">Received by <strong>Thomas W.</strong> from his wife</p>
        </div>
        <div class="gift-review-card">
          <div class="gift-review-card__stars">★★★★★</div>
          <p class="gift-review-card__text">"We gave this as a farewell gift to a colleague moving abroad. Practical, premium, and very cool. The whole team chip-in was worth it for his reaction to the box."</p>
          <p class="gift-review-card__meta">Given by <strong>Team Tech-Logic</strong></p>
        </div>
      </div>
    </div>
  </section>

  <section class="gift-cta-section">
    <h2 class="gift-section-title">One Kit. Every Situation Covered.</h2>
    <p style="color: #666; max-width: 500px; margin: 0 auto 40px;">Order today and we’ll prepare the Elite Kit for shipment within 24 hours. Free shipping included.</p>
    <a href="/products/survival72-modular-configurator?auto_kit=elite" class="gift-cta-btn">Order the Elite Gift Kit &rarr;</a>
    <p class="gift-cta-sub">Total: $145.00 — Includes 3 Modules + Premium Box</p>
  </section>
</div>
"""

print('Corporate Page Result:', rest_post_page('corporate-partnerships', 'Corporate & Bespoke', CORP_HTML))
print('Gift Page Result:', rest_post_page('gift-sets', 'The Elite Gift Kit', GIFT_HTML))
