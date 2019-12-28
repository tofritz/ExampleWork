import re

fhandle = open('regex_sum_42.txt', 'r')
data = fhandle.read()

lst = re.findall('[0-9]+', data)

count = 0

for string in lst:
    add = int(string)
    count = count + add

print('Sum: ', count)
