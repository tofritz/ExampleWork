fname = input('Enter a filename:')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

count = dict()
for line in fhand:
    words = line.split()
    if len(words) >= 3 and words[0] == 'From':
        count[words[2]] = count.get(words[2], 0) + 1

print(count)
