import json

with open('./data/000.json', 'r') as f:
	content = f.read()
	

d = json.loads(content)

print(d.get('glossary')) # print(d['glossary'])

# 연습

print(d.get['glossSeeAlso'])






