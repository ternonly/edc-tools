import subprocess
import json
import os

json_file = r'C:\Users\Administrator\.accio\accounts\1754445659\agents\DID-0D58EF-FA849A\project\ig_post_min.json'

with open(json_file, 'r', encoding='utf-8') as f:
    json_content = f.read()

# Call accio-mcp-cli via subprocess. The second element is the command, the rest are arguments.
# This avoids shell escaping issues because we're not using shell=True.
command = ["accio-mcp-cli", "call", "COMPOSIO_MULTI_EXECUTE_TOOL", "--json", json_content]

result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return Code:", result.returncode)
