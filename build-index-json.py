"""Build new templates/index.json for Survival72 home page (7 sections).
Based on Middle East consumer journey design + actual SKUs."""
import json, os, copy

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"

# Load current to inherit defaults
with open(os.path.join(PROJ, "horizon-index-current.json"), encoding="utf-8") as f:
    current = json.loads(f.read())
current_value = json.loads(current["asset"]["value"])

# Banner numeric ID (from Files API upload)
BANNER_ID = 29476917313581

# ==============================================================
# (Note) ANNOUNCEMENT BAR is configured in layout/header section group
#         — not allowed in templates/index.json. Will deploy separately.
# ==============================================================
# 2) HERO — Desert dawn + 3-tool system, with text + dual CTA
# ==============================================================
# Inherit existing hero defaults but override media + text + buttons
hero_existing = copy.deepcopy(current_value["sections"]["hero_jVaWmY"])
hero = {
    "type": "hero",
    "blocks": {
        "h_headline": {
            "type": "text",
            "name": "Headline",
            "settings": {
                "text": "<h1>Built for the 72 Hours That Matter Most</h1>",
                "width": "fit-content",
                "max_width": "narrow",
                "alignment": "left",
                "type_preset": "h1",
                "font": "var(--font-heading--family)",
                "font_size": "3.5rem",
                "line_height": "1.1",
                "letter_spacing": "normal",
                "case": "none",
                "wrap": "balance",
                "color": "#FFFFFF",
                "background": False,
                "background_color": "#00000026",
                "corner_radius": 0,
                "padding-block-start": 0,
                "padding-block-end": 0,
                "padding-inline-start": 0,
                "padding-inline-end": 0
            },
            "blocks": {}
        },
        "h_sub": {
            "type": "text",
            "name": "Subhead",
            "settings": {
                "text": "<h3>Desert-tested EDC tools for families across the GCC. Three tools. One system. Zero compromise.</h3>",
                "width": "fit-content",
                "max_width": "narrow",
                "alignment": "left",
                "type_preset": "p",
                "font": "var(--font-body--family)",
                "font_size": "1.125rem",
                "line_height": "1.5",
                "letter_spacing": "normal",
                "case": "none",
                "wrap": "pretty",
                "color": "#E8E2D5",
                "background": False,
                "background_color": "#00000026",
                "corner_radius": 0,
                "padding-block-start": 8,
                "padding-block-end": 16,
                "padding-inline-start": 0,
                "padding-inline-end": 0
            },
            "blocks": {}
        },
        "h_btn1": {
            "type": "button",
            "name": "Primary CTA",
            "settings": {
                "label": "Shop the 3-Tool System",
                "link": "shopify://collections/edc-tools",
                "open_in_new_tab": False,
                "style_class": "button-primary",
                "width": "fit-content",
                "custom_width": 100,
                "width_mobile": "fit-content",
                "custom_width_mobile": 100
            },
            "blocks": {}
        },
        "h_btn2": {
            "type": "button",
            "name": "Secondary CTA",
            "settings": {
                "label": "Explore the 72-Hour Kit",
                "link": "shopify://products/72-hour-kit-complete-3-tool-survival-system",
                "open_in_new_tab": False,
                "style_class": "button-secondary",
                "width": "fit-content",
                "custom_width": 100,
                "width_mobile": "fit-content",
                "custom_width_mobile": 100
            },
            "blocks": {}
        }
    },
    "block_order": ["h_headline", "h_sub", "h_btn1", "h_btn2"],
    "name": "Hero — Desert dawn",
    "settings": {
        "media_type_1": "image",
        "image_1": f"shopify://shop_images/hero-banner-final.jpg",
        "media_type_2": "image",
        "stack_media_on_mobile": False,
        "custom_mobile_media": False,
        "media_type_1_mobile": "image",
        "image_1_mobile": f"shopify://shop_images/hero-banner-final.jpg",
        "media_type_2_mobile": "image",
        "open_in_new_tab": False,
        "content_direction": "column",
        "vertical_on_mobile": True,
        "horizontal_alignment": "flex-start",
        "vertical_alignment": "center",
        "align_baseline": False,
        "horizontal_alignment_flex_direction_column": "flex-start",
        "vertical_alignment_flex_direction_column": "center",
        "gap": 12,
        "section_width": "full-width",
        "section_height": "large",
        "section_height_custom": 70,
        "color_scheme": "scheme-6",
        "toggle_overlay": True,
        "overlay_color": "#0A0A0A66",
        "overlay_style": "gradient",
        "gradient_direction": "to right",
        "blurred_reflection": False,
        "reflection_opacity": 75,
        "padding-block-start": 80,
        "padding-block-end": 80
    }
}

# ==============================================================
# 3) MARQUEE — Trust bar (4 USPs scrolling)
# ==============================================================
marquee = {
    "type": "marquee",
    "blocks": {
        "trust1": {"type": "text", "settings": {"text": "<h6>Desert-Tested Up to 50°C</h6>", "type_preset": "h6", "color": "var(--color-foreground)", "font": "var(--font-heading--family)", "font_size": "1rem", "letter_spacing": "0.05em", "case": "uppercase", "alignment": "center", "width": "fit-content"}},
        "trust2": {"type": "text", "settings": {"text": "<h6>COD in UAE & Saudi</h6>", "type_preset": "h6", "color": "var(--color-foreground)", "font": "var(--font-heading--family)", "font_size": "1rem", "letter_spacing": "0.05em", "case": "uppercase", "alignment": "center", "width": "fit-content"}},
        "trust3": {"type": "text", "settings": {"text": "<h6>30-Day Returns</h6>", "type_preset": "h6", "color": "var(--color-foreground)", "font": "var(--font-heading--family)", "font_size": "1rem", "letter_spacing": "0.05em", "case": "uppercase", "alignment": "center", "width": "fit-content"}},
        "trust4": {"type": "text", "settings": {"text": "<h6>Built for Family Protection</h6>", "type_preset": "h6", "color": "var(--color-foreground)", "font": "var(--font-heading--family)", "font_size": "1rem", "letter_spacing": "0.05em", "case": "uppercase", "alignment": "center", "width": "fit-content"}}
    },
    "block_order": ["trust1", "trust2", "trust3", "trust4"],
    "name": "Trust bar",
    "settings": {
        "movement_direction": "normal",
        "speed": 30,
        "pause_on_hover": True,
        "color_scheme": "scheme-2",
        "padding-block-start": 16,
        "padding-block-end": 16
    }
}

# ==============================================================
# 4) PRODUCT-LIST — EDC Tools collection (3 single tools)
# ==============================================================
plist_edc = copy.deepcopy(current_value["sections"]["product_list_fa6P9H"])
# Override key settings only
plist_edc["name"] = "EDC Tools — The 3-Tool System"
plist_edc["settings"]["collection"] = "edc-tools"
plist_edc["settings"]["max_products"] = 3
plist_edc["settings"]["columns"] = 3
plist_edc["settings"]["mobile_columns"] = "1"
plist_edc["settings"]["color_scheme"] = "scheme-1"
# Update header text
hdr_blocks = plist_edc["blocks"]["static-header"]["blocks"]
for k, b in hdr_blocks.items():
    if b.get("type") == "_product-list-text":
        b["settings"]["text"] = "<h2>The 3-Tool System</h2>"
    if b.get("type") == "_product-list-button":
        b["settings"]["label"] = "Shop EDC Tools"

# ==============================================================
# 5) FEATURED PRODUCT — KIT
# ==============================================================
featured_kit = {
    "type": "featured-product",
    "blocks": {},
    "name": "Featured — 72-Hour Kit",
    "settings": {
        "product": "72-hour-kit-complete-3-tool-survival-system",
        "layout": "media-left",
        "color_scheme": "scheme-3",
        "section_width": "full-width",
        "padding-block-start": 64,
        "padding-block-end": 64
    }
}

# ==============================================================
# 6) MEDIA-WITH-CONTENT — Why Survival72
# ==============================================================
why_survival = {
    "type": "media-with-content",
    "blocks": {
        "media": {
            "type": "_media-without-appearance",
            "static": True,
            "settings": {}
        },
        "content": {
            "type": "_content-without-appearance",
            "static": True,
            "settings": {
                "horizontal_alignment_flex_direction_column": "flex-start",
                "vertical_alignment_flex_direction_column": "center"
            },
            "blocks": {
                "caption": {
                    "type": "text",
                    "name": "Caption",
                    "settings": {
                        "text": "<h6>Why Survival72</h6>",
                        "type_preset": "h6",
                        "color": "var(--color-foreground)",
                        "letter_spacing": "0.1em",
                        "case": "uppercase"
                    }
                },
                "heading": {
                    "type": "text",
                    "name": "Heading",
                    "settings": {
                        "text": "<h2>Built for the 72 hours that matter most</h2>",
                        "type_preset": "h2",
                        "max_width": "narrow",
                        "wrap": "balance",
                        "color": "var(--color-foreground-heading)"
                    }
                },
                "body": {
                    "type": "text",
                    "name": "Body",
                    "settings": {
                        "text": "<h4>Survival72 exists for one reason: the first 72 hours after a crisis decide everything. Our tools are built for the back of a Land Cruiser, the dust of a desert highway, and the hand of a father responsible for his family's safety. Field-tested in the GCC's harshest conditions. Chosen to perform when it matters most.</h4>",
                        "type_preset": "rte",
                        "max_width": "narrow",
                        "wrap": "pretty",
                        "color": "var(--color-foreground)"
                    }
                },
                "button": {
                    "type": "button",
                    "name": "Button",
                    "settings": {
                        "label": "Read Our Story",
                        "link": "shopify://pages/about",
                        "style_class": "button-secondary"
                    }
                }
            },
            "block_order": ["caption", "heading", "body", "button"]
        }
    },
    "name": "Why Survival72",
    "settings": {
        "media_position": "left",
        "media_width": "medium",
        "media_height": "60svh",
        "section_width": "full-width",
        "extend_media": True,
        "color_scheme": "scheme-3",
        "padding-block-start": 64,
        "padding-block-end": 64
    }
}

# ==============================================================
# 7) PRODUCT-LIST — Bundles (3 combo kits)
# ==============================================================
plist_bundles = copy.deepcopy(current_value["sections"]["product_list_fa6P9H"])
plist_bundles["name"] = "Bundles — Save more, carry more"
plist_bundles["settings"]["collection"] = "bundles"
plist_bundles["settings"]["max_products"] = 3
plist_bundles["settings"]["columns"] = 3
plist_bundles["settings"]["mobile_columns"] = "1"
plist_bundles["settings"]["color_scheme"] = "scheme-2"
hdr_blocks2 = plist_bundles["blocks"]["static-header"]["blocks"]
for k, b in hdr_blocks2.items():
    if b.get("type") == "_product-list-text":
        b["settings"]["text"] = "<h2>2-Tool Bundles</h2>"
    if b.get("type") == "_product-list-button":
        b["settings"]["label"] = "Shop All Bundles"

# ==============================================================
# Assemble
# ==============================================================
new_index = {
    "sections": {
        "hero": hero,
        "marquee": marquee,
        "edc": plist_edc,
        "kit": featured_kit,
        "why": why_survival,
        "bundles": plist_bundles
    },
    "order": ["hero", "marquee", "edc", "kit", "why", "bundles"]
}

with open(os.path.join(PROJ, "horizon-index-NEW.json"), "w", encoding="utf-8") as f:
    json.dump(new_index, f, indent=2, ensure_ascii=False)

print(f"Built new index.json — {len(json.dumps(new_index))} chars, {len(new_index['order'])} sections")
print("Order:", new_index["order"])
