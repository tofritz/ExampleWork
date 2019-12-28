fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        sppos = line.find(' ')
        fnum = float(line[sppos + 1:])
        total = total + fnum

average = total / count
print('Average spam confidence:', average)
