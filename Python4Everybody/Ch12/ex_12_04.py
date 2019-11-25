import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
count = len(tags)

print('Paragraph Count:', count)
