fname = input('Enter filename:')
fhand = open(fname, 'r')
keys = dict()

for line in fhand:
    words = line.split()
    for word in words:
        keys[word] = None

print(keys)

while True:
    test = input('Enter a word to check for:')
    if test in keys:
        print(test, 'was found!')
    elif test == 'done':
        print('Done with checks!')
        quit()
    else:
        print('Try again...')
