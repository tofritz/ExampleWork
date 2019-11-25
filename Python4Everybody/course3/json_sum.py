import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter JSON URL - ')
data = urllib.request.urlopen(url, context=ctx).read().decode()

js = json.loads(data)
total = []

for user in js['comments']:
    total.append(user['count'])

print(sum(total))
