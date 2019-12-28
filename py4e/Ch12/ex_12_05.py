import socket

try:
    url = input('Enter URL: ')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = url.split('/')[2]
    mysock.connect((host, 80))
    mysock.send(('GET ' + url + ' HTTP/1.0\r\n\r\n').encode())

except:
    print('Enter a valid URL')
    quit()

doc = []

while True:
    data = mysock.recv(512)
    if (len(data) < 1): break
    doc.append(data.decode())

mysock.close()

doc_joined = ''.join(doc)

pos = doc_joined.find('\r\n\r\n')
print(doc_joined[pos:])
