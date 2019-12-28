fname = input('Enter a filename:')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

emails = dict()

for line in fhand:
    words = line.split()
    if len(words) >= 2 and words[0] == 'From':
        emails[words[1]] = emails.get(words[1], 0) + 1

lst = list()
for address, count in list(emails.items()):
    lst.append((count, address))

mostcommon = sorted(lst, reverse=True)[0]

print(mostcommon[1], mostcommon[0])
