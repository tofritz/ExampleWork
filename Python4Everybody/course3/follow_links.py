from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = int(input('Enter iterations:'))
position = int(input('Enter position:'))

for _ in range(count+1):
    html = urlopen(url, context=ctx).read()
    print('Retrieving: ', url)
    soup = BeautifulSoup(html, "html.parser")
    url = soup('a')[position-1].get('href', None)
