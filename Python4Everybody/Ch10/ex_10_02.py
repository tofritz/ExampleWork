fname = input('Enter a filename:')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

line_list = [line.strip('\n') for line in fhand if line.startswith('From ')]

hours_dict = {}

for line in line_list:
    time = line.split()[5]
    hour = time.split(':')[0]
    hours_dict[hour] = hours_dict.get(hour, 0) + 1

lst = []

for hour, count in list(hours_dict.items()):
    lst.append((hour, count))

lst.sort()

for hour, count in lst:
    print(hour,count)
