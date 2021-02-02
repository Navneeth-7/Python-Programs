import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = "http://py4e-data.dr-chuck.net/comments_1040091.json"
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
#print(json.dumps(js, indent=4))

sum=0
for item in js['comments']:
    sum = sum + int(item['count'])

print(sum)