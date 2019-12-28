import urllib.request

try:
    url = input('Enter URL: ')
    fhand = urllib.request.urlopen(url)

except:
    print('Enter a valid URL')
    quit()

count = 0

for line in fhand:
    count += len(line)
    if count <= 3000:
        print(line.decode().strip())

print('Character Length:', count)
