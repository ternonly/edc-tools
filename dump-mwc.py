import re, json, os
PROJ = r'C:/Users/Administrator/.accio/accounts/1754445659/agents/DID-0D58EF-FA849A/project'
content = open(os.path.join(PROJ, 'sections_media-with-content.liquid.txt'), encoding='utf-8').read()
m = re.search(r'\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}', content, re.DOTALL)
sch = json.loads(m.group(1))
out = open(os.path.join(PROJ, 'mwc-schema.json'), 'w', encoding='utf-8')
out.write(json.dumps(sch, indent=2))
out.close()
print("OK saved", len(json.dumps(sch)), "chars")
