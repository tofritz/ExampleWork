fname = input('Enter a filename:')

try:
    fhand = open(fname)
except:
    print('Invalid filename')
    quit()

count = 0
for line in fhand:
    words = line.split()
    if len(words) >= 2 and words[0] == 'From':
        print(words[1])
        count = count + 1

print('There were', count, 'lines in the file with From as the first word')
