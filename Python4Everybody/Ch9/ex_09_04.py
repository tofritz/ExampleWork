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
        emails[words[1]] = emails.get(words[1], 0) + 1

print(emails)

largest = None
for key in emails:
    if largest is None or emails[key] > largest:
        largest = emails[key]
        sender = key

print(sender, largest)
