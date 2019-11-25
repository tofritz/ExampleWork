def computepay(h,r):
    if h <= 40:
        stm = h * r
        return stm
    else:
        stm = 40 * r
        otm = (h-40) * (1.5*r)
        pay = stm + otm
        return pay

sh = input('Enter Hours:')
sr = input('Enter Rate:')

try:
    fh = float(sh)
except:
    print('Please enter in arabic numerals')
    quit()
try:
    fr = float(sr)
except:
    print('Please enter in arabic numerals')
    quit()

pay = computepay(fh,fr)
print(pay)
