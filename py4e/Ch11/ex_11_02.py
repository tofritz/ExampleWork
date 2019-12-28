import re

fname = input('Enter a filename:')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

data = [line.rstrip() for line in fhand]
total = 0
count = 0

rex = re.compile('^New Revision: (\d*)')

for line in data:
    numbers = re.findall(rex, line)
    for item in numbers:
        count += 1
        total += int(item)

print(total/count)
