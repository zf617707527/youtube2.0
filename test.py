import json
final = {}
with open('verified_proxies.json',encoding='utf-8') as f:
    # for line in f:
        a = json.load(f)
        # final[a['type']] = a['host']+':'+a['port']
print(a)
for i in a:
    final[i['type']] = str(i['host'])+':'+str(i['port'])
print(final)