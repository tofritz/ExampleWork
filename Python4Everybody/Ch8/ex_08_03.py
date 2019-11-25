fname = input('Enter a filename:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) >= 3 and words[0] == 'From':
        print(words[2])
