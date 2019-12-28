fname = input('Enter a file:')

try:
    fhand = open(fname)
except:
    print('Incorrect filename')
    exit()

unique_words = []

for line in fhand:
    words = line.split()
    for i in range(len(words)):
        if words[i] not in unique_words:
            unique_words.append(words[i])

unique_words.sort()
print(unique_words)
