string = 'X-DSPAM-Confidence: 0.8475'
sppos = string.find(' ')
fnum = float(string[sppos+1:])
print(fnum)
