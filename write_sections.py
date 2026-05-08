import os
os.makedirs('theme_new', exist_ok=True)

sections = {}

sections['section_problem.html'] = '''<style>
.s72-problem{background:#111;padding:80px 24px;text-align:center}
.s72-problem__inner{max-width:680px;margin:0 auto}
.s72-problem__kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#C9A96E;margin-bottom:24px}
.s72-problem__title{font-size:clamp(28px,5vw,48px);font-weight:700;color:#fff;line-height:1.15;margin-bottom:28px}
.s72-problem__body{font-size:18px;color:#aaa;line-height:1.8}
.s72-problem__body em{color:#fff;font-style:normal}
</style>
<section class="s72-problem">
  <div class="s72-problem__inner">
    <p class="s72-problem__kicker">Why it matters</p>
    <h2 class="s72-problem__title">Why carry three separate tools<br>when one decision covers everything?</h2>
    <p class="s72-problem__body">
      Most people have a wrench in the garage,<br>
      a knife in a drawer, and <em>nothing in their bag.</em><br><br>
      That gap between home and wherever you actually are<br>
      is exactly what Survival72 fills.
    </p>
  </div>
</section>'''

sections['section_system.html'] = '''<style>
.s72-system{padding:80px 24px;background:#fff}
.s72-system__inner{max-width:1100px;margin:0 auto}
.s72-system__header{text-align:center;margin-bottom:56px}
.s72-system__kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#C9A96E;margin-bottom:12px}
.s72-system__title{font-size:clamp(26px,4vw,42px);font-weight:700;color:#1A1A1A;margin-bottom:0}
.s72-system__grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:32px;margin-bottom:48px}
.s72-tool-card{border:1px solid #e8e8e8;border-radius:4px;padding:36px 28px;text-align:center}
.s72-tool-card__num{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#999;margin-bottom:16px}
.s72-tool-card__img{width:100%;height:180px;background:#f5f5f5;border-radius:3px;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:13px;margin-bottom:20px}
.s72-tool-card__name{font-size:20px;font-weight:700;color:#1A1A1A;margin-bottom:6px}
.s72-tool-card__alias{font-size:13px;color:#C9A96E;text-transform:uppercase;letter-spacing:.1em;margin-bottom:16px}
.s72-tool-card__uses{font-size:14px;color:#666;line-height:1.7;margin-bottom:24px}
.s72-tool-card__price{font-size:28px;font-weight:700;color:#1A1A1A}
.s72-kit-cta{background:#1A1A1A;border:1px solid #C9A96E;border-radius:4px;padding:32px;text-align:center}
.s72-kit-cta__label{font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:#C9A96E;margin-bottom:10px}
.s72-kit-cta__title{font-size:22px;font-weight:700;color:#fff;margin-bottom:8px}
.s72-kit-cta__price{font-size:16px;color:#aaa;margin-bottom:24px}
.s72-kit-cta__price s{color:#666}
.s72-kit-cta__btn{display:inline-block;background:#C9A96E;color:#1A1A1A;font-weight:700;font-size:15px;letter-spacing:.08em;text-transform:uppercase;padding:18px 48px;border-radius:3px;text-decoration:none}
</style>
<section class="s72-system">
  <div class="s72-system__inner">
    <div class="s72-system__header">
      <p class="s72-system__kicker">The Survival72 System</p>
      <h2 class="s72-system__title">Three tools. One decision. Carried daily.</h2>
    </div>
    <div class="s72-system__grid">
      <div class="s72-tool-card">
        <p class="s72-tool-card__num">Module 01</p>
        <div class="s72-tool-card__img">[Image Placeholder]</div>
        <h3 class="s72-tool-card__name">Pliers Module</h3>
        <p class="s72-tool-card__alias">The Fixer</p>
        <p class="s72-tool-card__uses">At home, at camp, in the car boot.<br>The tool you reach for first.</p>
        <div class="s72-tool-card__price">$52</div>
      </div>
      <div class="s72-tool-card">
        <p class="s72-tool-card__num">Module 02</p>
        <div class="s72-tool-card__img">[Image Placeholder]</div>
        <h3 class="s72-tool-card__name">Wrench Module</h3>
        <p class="s72-tool-card__alias">The Mechanic</p>
        <p class="s72-tool-card__uses">Camping stove, furniture, a loose bolt anywhere.<br>Quiet and reliable.</p>
        <div class="s72-tool-card__price">$42</div>
      </div>
      <div class="s72-tool-card">
        <p class="s72-tool-card__num">Module 03</p>
        <div class="s72-tool-card__img">[Image Placeholder]</div>
        <h3 class="s72-tool-card__name">Breacher Axe</h3>
        <p class="s72-tool-card__alias">The Unexpected</p>
        <p class="s72-tool-card__uses">Kindling, rescue, the situations<br>you never planned for.</p>
        <div class="s72-tool-card__price">$49</div>
      </div>
    </div>
    <div class="s72-kit-cta">
      <p class="s72-kit-cta__label">Best Value</p>
      <h3 class="s72-kit-cta__title">Full Deployment Kit &mdash; All Three Modules</h3>
      <p class="s72-kit-cta__price"><s>$143</s>&nbsp;&nbsp;<strong style="color:#fff;font-size:20px">$116</strong>&nbsp;&nbsp;<span style="color:#C9A96E">Save $27</span></p>
      <a href="/products/survival72-modular-configurator" class="s72-kit-cta__btn">Customize My Kit &rarr;</a>
    </div>
  </div>
</section>'''

sections['section_edu.html'] = '''<style>
.s72-edu{background:#f9f8f6;padding:80px 24px}
.s72-edu__inner{max-width:1100px;margin:0 auto}
.s72-edu__header{text-align:center;margin-bottom:48px}
.s72-edu__kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#C9A96E;margin-bottom:12px}
.s72-edu__title{font-size:clamp(24px,3.5vw,38px);font-weight:700;color:#1A1A1A;margin-bottom:10px}
.s72-edu__sub{font-size:16px;color:#888}
.s72-edu__grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-bottom:36px}
.s72-edu-card{background:#fff;border:1px solid #e8e8e8;border-radius:4px;padding:32px 28px}
.s72-edu-card__tag{font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:#C9A96E;margin-bottom:14px}
.s72-edu-card__title{font-size:18px;font-weight:700;color:#1A1A1A;margin-bottom:10px;line-height:1.3}
.s72-edu-card__body{font-size:14px;color:#666;line-height:1.7;margin-bottom:20px}
.s72-edu-card__link{font-size:13px;font-weight:600;color:#1A1A1A;text-decoration:none;border-bottom:1px solid #1A1A1A;padding-bottom:2px}
.s72-edu__cta{text-align:center}
.s72-edu__cta a{font-size:14px;color:#888;text-decoration:underline}
</style>
<section class="s72-edu">
  <div class="s72-edu__inner">
    <div class="s72-edu__header">
      <p class="s72-edu__kicker">Field Guide</p>
      <h2 class="s72-edu__title">Know Your Tools</h2>
      <p class="s72-edu__sub">Short reads. Practical knowledge. No fluff.</p>
    </div>
    <div class="s72-edu__grid">
      <div class="s72-edu-card">
        <p class="s72-edu-card__tag">3 min read</p>
        <h3 class="s72-edu-card__title">Why Pliers Beat a Swiss Army Knife for Everyday Use</h3>
        <p class="s72-edu-card__body">Most multi-tools give you a bit of everything. Pliers give you the one thing you actually need: grip. Here is why that matters more than a dozen blades.</p>
        <a href="/blogs/field-guide" class="s72-edu-card__link">Read the guide &rarr;</a>
      </div>
      <div class="s72-edu-card">
        <p class="s72-edu-card__tag">2 min read</p>
        <h3 class="s72-edu-card__title">How to Read a Wrench Size (And Why Most People Get It Wrong)</h3>
        <p class="s72-edu-card__body">Metric vs. imperial, open-end vs. adjustable. A quick guide to picking the right wrench every time, so you stop stripping bolts.</p>
        <a href="/blogs/field-guide" class="s72-edu-card__link">Read the guide &rarr;</a>
      </div>
      <div class="s72-edu-card">
        <p class="s72-edu-card__tag">4 min read</p>
        <h3 class="s72-edu-card__title">What Makes a Good Axe Head (And What to Ignore)</h3>
        <p class="s72-edu-card__body">Weight, edge geometry, handle angle. The details that separate a useful axe from a decoration. What to actually look for before you buy.</p>
        <a href="/blogs/field-guide" class="s72-edu-card__link">Read the guide &rarr;</a>
      </div>
    </div>
    <div class="s72-edu__cta"><a href="/blogs/field-guide">Explore all Field Guide articles &rarr;</a></div>
  </div>
</section>'''

sections['section_proof.html'] = '''<style>
.s72-proof{background:#fff;padding:80px 24px}
.s72-proof__inner{max-width:1100px;margin:0 auto}
.s72-proof__header{text-align:center;margin-bottom:48px}
.s72-proof__kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#C9A96E;margin-bottom:12px}
.s72-proof__title{font-size:clamp(24px,3.5vw,38px);font-weight:700;color:#1A1A1A;margin-bottom:0}
.s72-proof__stats{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid #e8e8e8;border-radius:4px;margin-bottom:48px;overflow:hidden}
@media(max-width:600px){.s72-proof__stats{grid-template-columns:repeat(2,1fr)}}
.s72-proof__stat{padding:28px 20px;text-align:center;border-right:1px solid #e8e8e8}
.s72-proof__stat:last-child{border-right:none}
.s72-proof__stat-num{font-size:36px;font-weight:700;color:#1A1A1A;display:block;line-height:1}
.s72-proof__stat-label{font-size:13px;color:#888;margin-top:6px}
.s72-proof__reviews{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:24px}
.s72-review-card{border:1px solid #e8e8e8;border-radius:4px;padding:28px}
.s72-review-card__stars{color:#C9A96E;font-size:14px;letter-spacing:3px;margin-bottom:14px}
.s72-review-card__text{font-size:15px;color:#333;line-height:1.75;margin-bottom:20px;font-style:italic}
.s72-review-card__author{font-size:13px;color:#888}
.s72-review-card__author strong{color:#1A1A1A}
</style>
<section class="s72-proof">
  <div class="s72-proof__inner">
    <div class="s72-proof__header">
      <p class="s72-proof__kicker">In the field</p>
      <h2 class="s72-proof__title">Those Who Carry, Know Why.</h2>
    </div>
    <div class="s72-proof__stats">
      <div class="s72-proof__stat"><span class="s72-proof__stat-num">2,300+</span><p class="s72-proof__stat-label">Kits Delivered</p></div>
      <div class="s72-proof__stat"><span class="s72-proof__stat-num">4.9</span><p class="s72-proof__stat-label">Average Rating</p></div>
      <div class="s72-proof__stat"><span class="s72-proof__stat-num">48h</span><p class="s72-proof__stat-label">Ships Within</p></div>
      <div class="s72-proof__stat"><span class="s72-proof__stat-num">2yr</span><p class="s72-proof__stat-label">Guarantee</p></div>
    </div>
    <div class="s72-proof__reviews">
      <div class="s72-review-card">
        <div class="s72-review-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="s72-review-card__text">"I have carried the wrench module every day for three months. Used it twice at home, once in a parking lot. That is exactly what I expected from a good everyday tool."</p>
        <p class="s72-review-card__author"><strong>Khaled R.</strong> &mdash; Dubai, UAE</p>
      </div>
      <div class="s72-review-card">
        <div class="s72-review-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="s72-review-card__text">"Bought the full kit as a gift for my father. The packaging alone made it feel premium. He has not put it down since."</p>
        <p class="s72-review-card__author"><strong>Priya M.</strong> &mdash; Abu Dhabi, UAE</p>
      </div>
      <div class="s72-review-card">
        <div class="s72-review-card__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="s72-review-card__text">"Not flashy. Just does what it promises. I have recommended it to three colleagues already. Good tools are hard to find at this price point."</p>
        <p class="s72-review-card__author"><strong>James T.</strong> &mdash; Expatriate, Riyadh</p>
      </div>
    </div>
  </div>
</section>'''

sections['section_gift.html'] = '''<style>
.s72-gift{background:#1A1A1A;padding:80px 24px}
.s72-gift__inner{max-width:960px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
@media(max-width:700px){.s72-gift__inner{grid-template-columns:1fr;gap:40px}}
.s72-gift__img{background:#242424;border-radius:4px;height:320px;display:flex;align-items:center;justify-content:center;color:#555;font-size:13px;border:1px solid #333}
.s72-gift__kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#C9A96E;margin-bottom:16px}
.s72-gift__title{font-size:clamp(24px,3.5vw,36px);font-weight:700;color:#fff;line-height:1.2;margin-bottom:16px}
.s72-gift__body{font-size:16px;color:#aaa;line-height:1.8;margin-bottom:24px}
.s72-gift__occasions{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:32px}
.s72-gift__tag{font-size:12px;background:#2a2a2a;color:#888;padding:6px 14px;border-radius:20px;border:1px solid #333}
.s72-gift__btn{display:inline-block;background:#C9A96E;color:#1A1A1A;font-weight:700;font-size:14px;letter-spacing:.08em;text-transform:uppercase;padding:16px 40px;border-radius:3px;text-decoration:none}
.s72-gift__price{font-size:13px;color:#555;margin-top:12px}
</style>
<section class="s72-gift">
  <div class="s72-gift__inner">
    <div class="s72-gift__img">[Gift Box Image Placeholder]</div>
    <div>
      <p class="s72-gift__kicker">A Gift They Will Actually Use</p>
      <h2 class="s72-gift__title">The Elite Kit.<br>Ready to give.</h2>
      <p class="s72-gift__body">The full three-module system, presented in a magnetic clamshell box. No wrapping required. Nothing to assemble. A genuinely useful gift from someone with good taste.</p>
      <div class="s72-gift__occasions">
        <span class="s72-gift__tag">Eid Gift</span>
        <span class="s72-gift__tag">Father Day</span>
        <span class="s72-gift__tag">New Home</span>
        <span class="s72-gift__tag">Colleague Farewell</span>
      </div>
      <a href="/products/survival72-modular-configurator" class="s72-gift__btn">Shop the Gift Kit &rarr;</a>
      <p class="s72-gift__price">Elite Kit with magnetic box &mdash; $145</p>
    </div>
  </div>
</section>'''

sections['section_promise.html'] = '''<style>
.s72-promise{background:#f9f8f6;padding:40px 24px;border-top:1px solid #e8e8e8;border-bottom:1px solid #e8e8e8}
.s72-promise__inner{max-width:900px;margin:0 auto;display:flex;flex-wrap:wrap;justify-content:center}
.s72-promise__item{flex:1;min-width:180px;text-align:center;padding:16px 24px;position:relative}
.s72-promise__item:not(:last-child)::after{content:"";position:absolute;right:0;top:20%;height:60%;width:1px;background:#ddd}
.s72-promise__value{font-size:15px;font-weight:600;color:#1A1A1A}
.s72-promise__label{font-size:13px;color:#888;margin-top:4px}
</style>
<section class="s72-promise">
  <div class="s72-promise__inner">
    <div class="s72-promise__item"><div class="s72-promise__value">Free Shipping</div><div class="s72-promise__label">on orders over $100</div></div>
    <div class="s72-promise__item"><div class="s72-promise__value">2-Year Guarantee</div><div class="s72-promise__label">on every module</div></div>
    <div class="s72-promise__item"><div class="s72-promise__value">30-Day Returns</div><div class="s72-promise__label">no questions asked</div></div>
    <div class="s72-promise__item"><div class="s72-promise__value">Gift-Ready</div><div class="s72-promise__label">magnetic box available</div></div>
  </div>
</section>'''

for fname, content in sections.items():
    with open(f'theme_new/{fname}', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'OK {fname} ({len(content):,} chars)')

print('Done.')
