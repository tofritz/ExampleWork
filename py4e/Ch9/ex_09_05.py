fname = input('Enter a filename: ')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

emails = dict()

for line in fhand:
    words = line.split()
    if len(words) >= 2 and words[0] == 'From':
        address = words[1].split('@')
        emails[address[1]] = emails.get(address[1], 0) + 1

print(emails)
