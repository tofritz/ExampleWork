import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter a location: ')
url = 'http://py4e-data.dr-chuck.net/geojson?'

apiurl = url + urllib.parse.urlencode({'address':location})

data = urllib.request.urlopen(apiurl, context=ctx).read().decode()
js = json.loads(data)

print('place_id = ', js['results'][0]['place_id'])
