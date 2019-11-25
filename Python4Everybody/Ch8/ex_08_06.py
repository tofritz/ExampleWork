numbers = []

while True:
    snum = input('Enter a number:')
    if snum == 'done': break
    try:
        fnum = float(snum)
    except:
        print('Invalid entry')
        continue
    numbers.append(fnum)

print('Maximum:', max(numbers))
print('Minimum:', min(numbers))
