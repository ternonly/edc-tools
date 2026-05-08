$json = Get-Content -Raw 'C:\Users\Administrator\.accio\accounts\1754445659\agents\DID-0D58EF-FA849A\project\ig_post.json'
& accio-mcp-cli call COMPOSIO_MULTI_EXECUTE_TOOL --json $json
