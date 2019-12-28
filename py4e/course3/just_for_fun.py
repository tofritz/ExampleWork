import re

print(sum([int(i) for i in re.findall('\d+', open('regex_sum_33073.txt').read())]))
