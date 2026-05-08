import os
from PIL import Image, ImageDraw, ImageFont

SRC = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images/axe-real-01.jpg'
OUT = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final/axe-real-01.jpg'

img = Image.open(SRC).convert('RGB')
w, h = img.size
print('Original:', w, 'x', h)

# Crop top 71% (中文在 73-79%)
crop_y = int(h * 0.71)
img2 = img.crop((0, 0, w, crop_y))
print('Cropped:', img2.size)

img2.thumbnail((2000, 2000), Image.LANCZOS)
print('Resized:', img2.size)

img2 = img2.convert('RGBA')
w2, h2 = img2.size

# Center watermark
layer = Image.new('RGBA', (w2, h2), (0,0,0,0))
font = ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', int(min(w2,h2)*0.13))
tmp = Image.new('RGBA', (int(w2*1.5), int(h2*0.4)), (0,0,0,0))
td = ImageDraw.Draw(tmp)
bb = td.textbbox((0,0), 'SURVIVAL72', font=font)
tw, th = bb[2]-bb[0], bb[3]-bb[1]
td.text(((tmp.size[0]-tw)//2, (tmp.size[1]-th)//2), 'SURVIVAL72', font=font,
        fill=(40,40,40,36), stroke_width=2, stroke_fill=(255,255,255,28))
trot = tmp.rotate(-22, resample=Image.BICUBIC, expand=True)
rw, rh = trot.size
layer.paste(trot, ((w2-rw)//2, (h2-rh)//2), trot)
img2 = Image.alpha_composite(img2, layer)

# Brand box
layer2 = Image.new('RGBA', (w2, h2), (0,0,0,0))
d2 = ImageDraw.Draw(layer2)
fs = max(14, int(min(w2,h2)*0.018))
fb = ImageFont.truetype(r'C:/Windows/Fonts/arialbd.ttf', fs)
lines = ['Survival72', 'IG: @survival72bob', 'X: @Survival72EDC']
text_w = max(d2.textbbox((0,0), l, font=fb)[2] for l in lines)
lh = d2.textbbox((0,0), lines[0], font=fb)[3] + 4
pad = int(fs*0.8)
bw = text_w + pad*2; bh = lh*3 + pad*2
m = int(fs*1.2); x = w2-bw-m; y = h2-bh-m
d2.rectangle([x,y,x+bw,y+bh], fill=(0,0,0,165))
for i,l in enumerate(lines):
    fill = (255,255,255,235) if i==0 else (220,220,220,220)
    d2.text((x+pad, y+pad+lh*i), l, font=fb, fill=fill)
img2 = Image.alpha_composite(img2, layer2)

img2 = img2.convert('RGB')
img2.save(OUT, 'JPEG', quality=88, optimize=True)
print('Saved:', os.path.getsize(OUT)//1024, 'KB')

import shutil
d = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final'
shutil.copy(OUT, f'{d}/CHECK-v7-axe.jpg')
print('CHECK-v7 ready')
