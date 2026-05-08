import base64
import json
import urllib.request
import os

SHOP = 'wyntnb-8b.myshopify.com'
TOKEN = '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'
API_VER = '2026-01'
HDRS = {'X-Shopify-Access-Token': TOKEN, 'Content-Type': 'application/json'}

FILES_TO_UPLOAD = {
    "pliers": "C:/Users/Administrator/Desktop/edc set/1688素材包/多功能钳子/1.png",
    "wrench": "C:/Users/Administrator/Desktop/edc set/1688素材包/多功能扳手/1.jpg",
    "axe": "C:/Users/Administrator/Desktop/edc set/1688素材包/多功能斧头/1.jpg",
    "gift_box": "C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project/product-images-final/kit-gift-box.jpg"
}

def upload_to_files(file_path, key):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    
    filename = f"s72_{key}_{os.path.basename(file_path)}"
    
    # Using GraphQL for fileCreate
    mutation = """
    mutation fileCreate($files: [FileCreateInput!]!) {
      fileCreate(files: $files) {
        files {
          ... on MediaImage {
            image {
              url
            }
          }
        }
        userErrors {
          field
          message
        }
      }
    }
    """
    
    variables = {
        "files": [
            {
                "originalSource": f"data:image/jpeg;base64,{encoded}" if file_path.endswith(".jpg") else f"data:image/png;base64,{encoded}",
                "contentType": "IMAGE"
            }
        ]
    }
    
    # Fallback to REST if GraphQL fileCreate is complex with data URI (sometimes it is)
    # Actually REST images.json is for products. 
    # For global Files, GraphQL is best.
    
    # Let's use the stagedUploads approach if needed, but data URI usually works for small-medium files.
    # If it fails, I'll use the product image upload as a workaround and then get the CDN link.
    
    # Workaround: Upload to a dummy product or the configurator product to get CDN link.
    url = f'https://{SHOP}/admin/api/{API_VER}/products/8487770259501/images.json'
    data = {
        "image": {
            "attachment": encoded,
            "filename": filename
        }
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=HDRS, method='POST')
    try:
        with urllib.request.urlopen(req) as r:
            res = json.loads(r.read().decode())
            print(f"{key}: {res['image']['src']}")
            return res['image']['src']
    except Exception as e:
        print(f"Failed to upload {key}: {e}")

if __name__ == "__main__":
    urls = {}
    for key, path in FILES_TO_UPLOAD.items():
        url = upload_to_files(path, key)
        if url:
            urls[key] = url
    
    with open("uploaded_urls.json", "w") as f:
        json.dump(urls, f)
