import base64
import json
import urllib.request
import os

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
PROD_ID = '8487770259501'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

IMAGE_DIR = 'C:/Users/Administrator/Desktop/edc set/1688素材包/多功能钳子'
DETAIL_DIR = os.path.join(IMAGE_DIR, '钳子详情')

# Selected images (prioritizing quality and diversity)
IMAGE_FILES = [
    os.path.join(IMAGE_DIR, '影棚拍摄-22778.JPG'),
    os.path.join(IMAGE_DIR, '1.png'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22746.JPG'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22782.JPG'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22834.JPG'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22846.JPG'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22941.JPG'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22967.JPG'),
    os.path.join(IMAGE_DIR, '影棚拍摄-22973.JPG'),
    os.path.join(DETAIL_DIR, '1.jpg')
]

from PIL import Image
import io

# ... (previous code)

def upload_image(file_path, index):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    filename = f"pliers_{index}.jpg"
    
    try:
        with Image.open(file_path) as img:
            # Resize if > 20MP
            if img.width * img.height > 20_000_000:
                scale = (20_000_000 / (img.width * img.height)) ** 0.5
                new_size = (int(img.width * scale), int(img.height * scale))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                print(f"Resized {os.path.basename(file_path)} to {new_size}")
            
            # Convert to RGB if needed (JPG/PNG handling)
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=90)
            encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return

    data = {
        "image": {
            "attachment": encoded,
            "filename": filename
        }
    }
    
    url = f'https://{SHOP}/admin/api/{API_VER}/products/{PROD_ID}/images.json'
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=HDRS, method='POST')
    
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read().decode())
            print(f"Uploaded {filename}: ID {res['image']['id']}")
            return res['image']['id']
    except Exception as e:
        print(f"Failed to upload {filename}: {e}")

if __name__ == "__main__":
    image_ids = []
    for i, img in enumerate(IMAGE_FILES):
        img_id = upload_image(img, i+1)
        if img_id:
            image_ids.append(img_id)
    
    print(f"\nAll images uploaded. IDs: {image_ids}")
