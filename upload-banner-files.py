"""Upload Hero Banner via Shopify Files API (GraphQL stagedUploads + fileCreate)
to get a permanent CDN file with GID, usable as hero section image_1."""
import urllib.request, json, os, mimetypes, uuid

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
TOKEN = "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"
SHOP = "wyntnb-8b.myshopify.com"
API_VER = "2026-01"
SRC = os.path.join(PROJ, "hero-banner-final.jpg")
GQL_URL = f"https://{SHOP}/admin/api/{API_VER}/graphql.json"

def gql(query, variables=None):
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(GQL_URL, data=payload, headers={
        "X-Shopify-Access-Token": TOKEN,
        "Content-Type": "application/json"
    })
    return json.loads(urllib.request.urlopen(req).read().decode())

# 1. stagedUploadsCreate — get target URL
size = os.path.getsize(SRC)
fname = "hero-banner-final.jpg"
mime = "image/jpeg"

stage_q = """
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets { url resourceUrl parameters { name value } }
    userErrors { field message }
  }
}
"""
stage_vars = {"input": [{
    "filename": fname,
    "mimeType": mime,
    "httpMethod": "POST",
    "resource": "FILE",
    "fileSize": str(size),
}]}
r = gql(stage_q, stage_vars)
print("STAGED:", json.dumps(r, indent=2)[:600])
target = r["data"]["stagedUploadsCreate"]["stagedTargets"][0]
upload_url = target["url"]
resource_url = target["resourceUrl"]
params = target["parameters"]

# 2. POST file as multipart to upload_url
boundary = uuid.uuid4().hex
body = b""
for p in params:
    body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{p['name']}\"\r\n\r\n{p['value']}\r\n".encode()
with open(SRC, "rb") as f:
    file_bytes = f.read()
body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{fname}\"\r\nContent-Type: {mime}\r\n\r\n".encode()
body += file_bytes + f"\r\n--{boundary}--\r\n".encode()

up_req = urllib.request.Request(upload_url, data=body, headers={
    "Content-Type": f"multipart/form-data; boundary={boundary}",
    "Content-Length": str(len(body))
})
up_resp = urllib.request.urlopen(up_req)
print(f"UPLOAD HTTP {up_resp.status}")

# 3. fileCreate to register
fc_q = """
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files { id alt fileStatus ... on MediaImage { image { url width height } } }
    userErrors { field message }
  }
}
"""
fc_vars = {"files": [{
    "originalSource": resource_url,
    "contentType": "IMAGE",
    "alt": "Survival72 Hero Banner - Desert dawn with 3-tool system"
}]}
r2 = gql(fc_q, fc_vars)
print("FILECREATE:", json.dumps(r2, indent=2))

# Save result
with open(os.path.join(PROJ, "hero-banner-upload-result.json"), "w") as f:
    json.dump(r2, f, indent=2)
