"""Add bottom-right brand watermark to Hero Banner. No center diagonal."""
from PIL import Image, ImageDraw, ImageFont
import os

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
SRC = os.path.join(PROJ, "hero-banner-raw.png")
OUT = os.path.join(PROJ, "hero-banner-final.jpg")

img = Image.open(SRC).convert("RGB")
W, H = img.size
print(f"Source: {W}x{H}")

# Resize to standard hero width (max 2400px) keeping aspect
TARGET_W = 2400
if W > TARGET_W:
    new_h = int(H * TARGET_W / W)
    img = img.resize((TARGET_W, new_h), Image.LANCZOS)
    W, H = img.size
    print(f"Resized: {W}x{H}")

draw = ImageDraw.Draw(img, "RGBA")

# Bottom-right brand box
box_w, box_h = 540, 110
margin = 28
x1 = W - margin
y1 = H - margin
x0 = x1 - box_w
y0 = y1 - box_h

# Semi-transparent black box
draw.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 165))

# Try to find a font
font_paths = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\arial.ttf",
]
font_brand = font_small = None
for p in font_paths:
    if os.path.exists(p):
        font_brand = ImageFont.truetype(p, 34)
        font_small = ImageFont.truetype(p, 20)
        break
if not font_brand:
    font_brand = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Brand text
draw.text((x0 + 22, y0 + 14), "SURVIVAL72", fill=(201, 169, 110, 255), font=font_brand)
draw.text((x0 + 22, y0 + 60), "IG: @survival72bob  X: @Survival72EDC", fill=(220, 220, 220, 230), font=font_small)

img.save(OUT, "JPEG", quality=92, optimize=True)
print(f"Saved: {OUT}  size={os.path.getsize(OUT)/1024:.1f}KB  dim={img.size}")
