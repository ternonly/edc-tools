import urllib.request, json
SHOP = "wyntnb-8b.myshopify.com"
TOKEN = "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"
API_VER = "2026-01"

hdrs = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

about_html = """<div style="max-width: 880px; margin: 0 auto;">
<h2>Built by an Educator. Tested by the Desert.</h2>
<p>Survival72 was founded by <strong>Cole Mercer</strong>, an emergency preparedness educator who has spent the last decade training families across the GCC how to handle the first 72 hours of any disruption &mdash; when help has not yet arrived.</p>

<h3>Why 72 Hours</h3>
<p>Government and Red Crescent guidance across UAE, Saudi Arabia and the wider Gulf region all converge on the same number: <strong>72 hours</strong>. Three days is the window in which a household needs to be self-sufficient &mdash; for power outages, regional flash floods, sandstorm-related supply gaps, or extended highway closures.</p>
<p>Most "survival kits" sold online are built for cold-climate hikers. They fail in our environment. Our gear is engineered for one purpose: keeping a Gulf family functional through that 72-hour window.</p>

<h3>The Three-Tool System</h3>
<p>Three tools &mdash; Axe, Wrench, Pliers &mdash; chosen for the practical scenarios a family in our region will actually face: shelter access, vehicle recovery, utility shut-off. Nothing tactical-cosplay. Nothing decorative.</p>
<ul>
<li><strong>Desert Breacher Axe</strong> &mdash; Door breach + sand-loose vehicle stake-out</li>
<li><strong>Roadside Fix Wrench</strong> &mdash; Universal valve + battery terminal + jack handle</li>
<li><strong>Field Precision Pliers</strong> &mdash; Wire / fence / cable in 50&deg;C heat</li>
</ul>

<h3>Desert-Tested Means Tested in the Desert</h3>
<p>Every product carries the <em>Desert-Tested</em> mark only after surviving 30 days of field cycle in Empty Quarter conditions: 50&deg;C ambient, abrasive sand exposure, salt-fog corrosion, and repeat thermal shock. We do not certify gear we have not personally broken.</p>

<h3>What We Are Not</h3>
<p>We are not a tactical lifestyle brand. We do not sell to militaries, security companies, or political organizations. We exist to serve families &mdash; the parent restocking the boot of the SUV before a desert weekend, the homeowner preparing for the rainy season in Oman, the corporate gift program that wants to send something genuinely useful instead of another thermos.</p>

<p style="margin-top:40px; padding:20px; background:#f6f4ee; border-left:4px solid #C9A96E; font-style: italic;">
"The first 72 hours decide everything. We make the gear that stands behind a family during those hours."<br>
&mdash; Cole Mercer, Founder
</p>

<p><a href="/collections/edc-tools" style="display:inline-block; background:#1A1A1A; color:#C9A96E; padding:14px 28px; text-decoration:none; font-weight:bold; margin-top:20px;">Explore the 3-Tool System &rarr;</a></p>
</div>"""

wholesale_html = """<div style="max-width: 980px; margin: 0 auto;">
<h2>Wholesale &amp; Custom Solutions for Middle East Retailers</h2>
<p style="font-size: 1.1em; color: #555;">Trade-license-verified. ISO 9001 supply chain. Lead time from <strong>14 days</strong>. Custom branding from <strong>50 units</strong>.</p>

<h3>Our Three B2B Programs</h3>
<table style="width:100%; border-collapse:collapse; margin-bottom: 30px;">
<tr style="background:#1A1A1A; color:#C9A96E;"><th style="padding:14px; text-align:left;">Program</th><th style="padding:14px; text-align:left;">Best For</th><th style="padding:14px; text-align:left;">MOQ</th></tr>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:12px;"><strong>Wholesale</strong></td><td style="padding:12px;">Hardware retailers, outdoor stores, e-commerce resellers</td><td style="padding:12px;">100 units</td></tr>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:12px;"><strong>Custom Branding</strong></td><td style="padding:12px;">Private label / OEM / co-branded retail SKUs</td><td style="padding:12px;">500 units</td></tr>
<tr style="border-bottom:1px solid #ddd;"><td style="padding:12px;"><strong>Corporate Gifting</strong></td><td style="padding:12px;">Bank Eid gifts, oil &amp; gas safety promotions, government</td><td style="padding:12px;">50 units</td></tr>
</table>

<h3>Why Retailers Choose Survival72</h3>
<ul>
<li><strong>ISO 9001 certified manufacturing</strong> &mdash; Audit reports available on request</li>
<li><strong>MIL-STD-810H environmental tested</strong> &mdash; 50&deg;C operational rating</li>
<li><strong>14-day standard lead time</strong> for in-stock SKUs; 30 days for custom branding</li>
<li><strong>Free pre-production sample</strong> for orders over 500 units</li>
<li><strong>UAE Trade License verified</strong> &mdash; Certificate provided after first contact</li>
</ul>

<h3>How It Works</h3>
<ol>
<li><strong>Inquire</strong> &mdash; WhatsApp or form below. We respond within 4 business hours.</li>
<li><strong>Catalog &amp; Quote</strong> &mdash; PDF catalog + quote sent within 24 hours.</li>
<li><strong>Sample / PO</strong> &mdash; Approve sample, then issue PO. 30% deposit, 70% before shipment.</li>
<li><strong>Fulfill</strong> &mdash; FCL/LCL shipping to Jebel Ali, Dammam, Doha, Muscat. DDP terms available.</li>
</ol>

<div style="background:#f6f4ee; padding:30px; margin-top:40px; border-radius:6px;">
<h3 style="margin-top:0;">Request a Quote</h3>
<p>For inquiries, please email us at <strong>wholesale@survival72.com</strong> with the following:</p>
<ul>
<li>Company name + Trade license number</li>
<li>Country / Emirate of operation</li>
<li>Estimated quantity (50&ndash;500 / 500&ndash;5000 / 5000+)</li>
<li>Program of interest (Wholesale / Custom Branding / Corporate Gifting)</li>
<li>Target ship date</li>
</ul>
<p style="margin-top:20px;"><strong>WhatsApp B2B line:</strong> Coming soon &mdash; HK number activating Q2 2026.</p>
<p><em>4-hour business response guaranteed (UAE timezone, Sun&ndash;Thu 09:00&ndash;18:00 GST).</em></p>
</div>

<p style="text-align:center; margin-top:30px; color:#888; font-size:0.9em;">Trusted supplier mark: ISO 9001 &middot; MIL-STD-810H &middot; UAE Trade License Verified</p>
</div>"""

for handle, title, body in [
    ("about", "About Survival72", about_html),
    ("wholesale", "Wholesale & Custom", wholesale_html),
]:
    payload = {"page": {"title": title, "handle": handle, "body_html": body, "published": True}}
    req = urllib.request.Request(
        f"https://{SHOP}/admin/api/{API_VER}/pages.json",
        data=json.dumps(payload).encode("utf-8"), headers=hdrs, method="POST"
    )
    try:
        with urllib.request.urlopen(req) as r:
            d = json.loads(r.read())
            print(("OK " + handle + ": id=" + str(d['page']['id']) + " url=/pages/" + d['page']['handle']).encode())
    except urllib.error.HTTPError as e:
        print(("ERR " + handle + " " + str(e.code) + ": " + e.read().decode()[:300]).encode())
