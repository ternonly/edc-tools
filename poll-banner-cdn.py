"""Poll the uploaded MediaImage until READY, then save CDN URL."""
import urllib.request, json, os, time

PROJ = r"C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project"
TOKEN = "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"
GQL = "https://wyntnb-8b.myshopify.com/admin/api/2026-01/graphql.json"
GID = "gid://shopify/MediaImage/29476917313581"

q = """query($id: ID!) {
  node(id: $id) {
    ... on MediaImage { id fileStatus alt image { url width height } }
  }
}"""

for i in range(15):
    req = urllib.request.Request(GQL, data=json.dumps({"query": q, "variables": {"id": GID}}).encode(),
        headers={"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req).read().decode())
    node = r["data"]["node"]
    print(f"[{i}] status={node['fileStatus']}  image={node.get('image')}")
    if node["fileStatus"] == "READY" and node.get("image"):
        out = {"gid": GID, "numeric_id": GID.split("/")[-1], **node}
        with open(os.path.join(PROJ, "hero-banner-cdn.json"), "w") as f:
            json.dump(out, f, indent=2)
        print(f"\n✅ READY")
        print(f"   numeric_id: {out['numeric_id']}")
        print(f"   url:        {node['image']['url']}")
        print(f"   dim:        {node['image']['width']}x{node['image']['height']}")
        break
    time.sleep(2)
else:
    print("Timeout — still processing.")
