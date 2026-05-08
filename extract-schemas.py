"""Extract {% schema %} JSON from .liquid files and dump key fields."""
import os, re, json, glob

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"

files = [
    "sections_hero.liquid.txt",
    "sections_header-announcements.liquid.txt",
    "sections_marquee.liquid.txt",
    "sections_media-with-content.liquid.txt",
    "sections_featured-product.liquid.txt",
    "sections_header.liquid.txt",
    "sections_footer.liquid.txt",
]

for fn in files:
    p = os.path.join(PROJ, fn)
    if not os.path.exists(p):
        continue
    content = open(p, encoding="utf-8").read()
    m = re.search(r"\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}", content, re.DOTALL)
    if not m:
        print(f"\n### {fn}: NO SCHEMA")
        continue
    try:
        sch = json.loads(m.group(1))
    except Exception as e:
        print(f"\n### {fn}: BAD JSON {e}")
        continue
    print(f"\n### {fn} -> name={sch.get('name')}")
    print(f"  blocks: {[b.get('type') for b in sch.get('blocks', []) if isinstance(b, dict)]}")
    print(f"  presets: {[p.get('name') for p in sch.get('presets', []) if isinstance(p, dict)]}")
    print(f"  settings: ({len(sch.get('settings', []))})")
    for s in sch.get("settings", []):
        if not isinstance(s, dict): continue
        sid = s.get("id")
        st = s.get("type")
        sd = s.get("default")
        if st in ("image_picker", "video", "select", "checkbox", "color", "text", "richtext"):
            d = f" default={sd}" if sd is not None else ""
            print(f"    - {sid:30s} type={st:14s}{d}")
