import re

fname = input('Enter a filename:')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

rex = input('Enter a regular expression: ')
count = 0

for line in fhand:
    line = line.rstrip()
    if re.search(rex, line): count = count + 1

print('mbox.txt had', count, 'lines that matched', rex)
