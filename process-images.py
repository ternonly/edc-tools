# Process product images: resize + erase Chinese annotations + add watermark
# Rules:
#  - "real" photos (实拍): resize, erase any Chinese text overlays, ADD watermark
#  - "styled" photos (美化): only resize (already have watermark or are clean stock)
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images'
OUT = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final'
os.makedirs(OUT, exist_ok=True)

# Files that NEED watermark added (raw real photos)
NEED_WATERMARK = {
    'axe-real-01.jpg', 'wrench-real-01.jpg',
    'pliers-real-01.png', 'pliers-real-02.jpg',
    'kit-real-flat.jpg', 'kit-real-open.jpg', 'kit-real-shop.jpg',
}

# Chinese annotation regions to erase (relative coordinates 0..1: x0,y0,x1,y1)
# Verified by visual inspection of raw photos.
ERASE_REGIONS = {
    'axe-real-01.jpg':    [(0.18, 0.66, 0.78, 0.78)],
    'wrench-real-01.jpg': [(0.28, 0.70, 0.82, 0.82)],
    'pliers-real-02.jpg': [(0.16, 0.27, 0.82, 0.40)],
}

MAX_SIDE = 2000
JPEG_Q = 88

def find_font(size):
    for path in [
        r'C:/Windows/Fonts/arialbd.ttf',
        r'C:/Windows/Fonts/arial.ttf',
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def sample_bg_color(img, x0, y0, x1, y1):
    """Sample a small strip of background color from area BELOW the erase box."""
    w, h = img.size
    sy0 = min(h - 5, int(y1) + 5)
    sy1 = min(h, sy0 + 20)
    if sy1 - sy0 < 5:
        sy0 = max(0, int(y0) - 25); sy1 = max(5, int(y0) - 5)
    sx0 = max(0, int(x0)); sx1 = min(w, int(x1))
    crop = img.crop((sx0, sy0, sx1, sy1)).convert('RGB')
    # Average color
    pixels = list(crop.getdata())
    if not pixels:
        return (240, 240, 240)
    r = sum(p[0] for p in pixels) // len(pixels)
    g = sum(p[1] for p in pixels) // len(pixels)
    b = sum(p[2] for p in pixels) // len(pixels)
    return (r, g, b)

def erase_chinese(img, fn):
    """Cover Chinese text with sampled background color, soft-feathered edges."""
    if fn not in ERASE_REGIONS:
        return img
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w, h = img.size
    for (rx0, ry0, rx1, ry1) in ERASE_REGIONS[fn]:
        x0, y0, x1, y1 = int(rx0*w), int(ry0*h), int(rx1*w), int(ry1*h)
        bg = sample_bg_color(img, x0, y0, x1, y1)
        bw, bh = x1 - x0, y1 - y0
        # Solid patch in sampled bg color
        patch = Image.new('RGB', (bw, bh), bg)
        # Feathered alpha mask: opaque center, soft fade at edges
        mask = Image.new('L', (bw, bh), 255)
        feather = max(8, min(bw, bh) // 6)
        mdraw = ImageDraw.Draw(mask)
        # Fade only outermost ring
        for i in range(feather):
            alpha = int(255 * (i / feather))
            mdraw.rectangle([i, i, bw - 1 - i, bh - 1 - i], outline=alpha)
        mask = mask.filter(ImageFilter.GaussianBlur(radius=feather // 2))
        img.paste(patch, (x0, y0), mask)
    return img

def add_watermark(img):
    """Add centered diagonal SURVIVAL72 (~14% dark gray) + bottom-right brand box."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    w, h = img.size

    # === Centered diagonal SURVIVAL72 ===
    layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    text_main = 'SURVIVAL72'
    font_size_main = int(min(w, h) * 0.13)
    font_main = find_font(font_size_main)

    # Render onto a temporary transparent canvas then rotate
    tmp_w = int(w * 1.5); tmp_h = int(h * 0.4)
    txt_img = Image.new('RGBA', (tmp_w, tmp_h), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(txt_img)
    bbox = tdraw.textbbox((0, 0), text_main, font=font_main)
    tw = bbox[2] - bbox[0]; th = bbox[3] - bbox[1]
    tx = (tmp_w - tw) // 2; ty = (tmp_h - th) // 2
    # Dark gray, ~14% opacity, with subtle stroke for readability on any background
    tdraw.text((tx, ty), text_main, font=font_main,
               fill=(40, 40, 40, 36),
               stroke_width=2, stroke_fill=(255, 255, 255, 28))
    txt_rot = txt_img.rotate(-22, resample=Image.BICUBIC, expand=True)

    rw, rh = txt_rot.size
    layer.paste(txt_rot, ((w - rw) // 2, (h - rh) // 2), txt_rot)
    img = Image.alpha_composite(img, layer)

    # === Bottom-right brand box ===
    layer2 = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw2 = ImageDraw.Draw(layer2)
    line1 = 'Survival72'
    line2 = 'IG: @survival72bob'
    line3 = 'X: @Survival72EDC'
    fs_box = max(14, int(min(w, h) * 0.018))
    font_box = find_font(fs_box)

    bb1 = draw2.textbbox((0, 0), line1, font=font_box)
    bb2 = draw2.textbbox((0, 0), line2, font=font_box)
    bb3 = draw2.textbbox((0, 0), line3, font=font_box)
    text_w = max(bb1[2], bb2[2], bb3[2])
    line_h = bb1[3] + 4
    pad = int(fs_box * 0.8)
    box_w = text_w + pad * 2
    box_h = line_h * 3 + pad * 2

    margin = int(fs_box * 1.2)
    x0 = w - box_w - margin
    y0 = h - box_h - margin

    draw2.rectangle([x0, y0, x0 + box_w, y0 + box_h], fill=(0, 0, 0, 165))
    draw2.text((x0 + pad, y0 + pad), line1, font=font_box, fill=(255, 255, 255, 235))
    draw2.text((x0 + pad, y0 + pad + line_h), line2, font=font_box, fill=(220, 220, 220, 220))
    draw2.text((x0 + pad, y0 + pad + line_h * 2), line3, font=font_box, fill=(220, 220, 220, 220))

    img = Image.alpha_composite(img, layer2)
    return img

def resize(img):
    w, h = img.size
    if max(w, h) <= MAX_SIDE:
        return img
    if w >= h:
        nh = int(h * MAX_SIDE / w); nw = MAX_SIDE
    else:
        nw = int(w * MAX_SIDE / h); nh = MAX_SIDE
    return img.resize((nw, nh), Image.LANCZOS)

def process(fn):
    src = os.path.join(SRC, fn)
    img = Image.open(src)
    img = resize(img)

    # Step 1: erase Chinese annotations on raw photos (BEFORE watermark)
    img = erase_chinese(img, fn)

    # Step 2: add watermark on raw photos only
    if fn in NEED_WATERMARK:
        img = add_watermark(img)

    base, _ = os.path.splitext(fn)
    out_fn = base + '.jpg'
    if img.mode == 'RGBA':
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1])
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    out_path = os.path.join(OUT, out_fn)
    img.save(out_path, 'JPEG', quality=JPEG_Q, optimize=True)
    sz = os.path.getsize(out_path) // 1024
    print(f'  -> {out_fn} {sz}KB')

files = sorted(os.listdir(SRC))
print(f'Processing {len(files)} files...')
for fn in files:
    if fn.lower().endswith(('.jpg','.jpeg','.png')):
        flags = []
        if fn in ERASE_REGIONS: flags.append('ERASE')
        if fn in NEED_WATERMARK: flags.append('WM')
        if not flags: flags = ['--']
        print(f'[{",".join(flags)}] {fn}')
        try:
            process(fn)
        except Exception as e:
            print(f'  ERR: {e}')
print('DONE')
