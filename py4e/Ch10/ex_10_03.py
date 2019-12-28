import string
fname = input('Enter a filename:')

try:
    fhand = open(fname, 'r')
except:
    print('Invalid filename:', fname)
    quit()

char_dict = {}

for line in fhand:
    line = line.translate(line.maketrans('', '', string.whitespace))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower().replace(' ', '')
    chars = list(line)
    for char in chars:
        char_dict[char] = char_dict.get(char, 0) + 1

char_list = []

for char, count in list(char_dict.items()):
    char_list.append((count, char))

char_list.sort(reverse=True)

for count, char in char_list:
    print(char, count)
