import socket
count = 0

try:
    url = input('Enter URL: ')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = url.split('/')[2]
    mysock.connect((host, 80))
    mysock.send(('GET ' + url + ' HTTP/1.0\r\n\r\n').encode())

except:
    print('Enter a valid URL')
    quit()

while True:
    data = mysock.recv(512)
    if (len(data) < 1): break
    count += len(data)
    while count <= 3000:
        print(data.decode(), end = '')
        break

mysock.close()

print('\r\nCharacter length:', count)
