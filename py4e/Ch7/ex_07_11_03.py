fname = input('Enter a file name:')
if fname == 'na na boo boo':
    print('Liar, Liar, Pants on Fire!')
    raise SystemExit

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    raise SystemExit

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
