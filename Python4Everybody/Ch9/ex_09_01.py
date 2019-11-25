fname = 'words.txt'
fhand = open(fname, 'r')
text = fhand.read()
dwords = dict()
lwords = text.split()
for i in lwords:
    dwords[i] = None
print(lwords)
print(dwords)
