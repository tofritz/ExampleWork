import string
morseList = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseDict = dict(zip(string.ascii_lowercase, morseList.split()))


def encode(word):
    return(''.join([morseDict[letter] for letter in word]))


print(encode('sos'))

# bonus challenge 1

with open('enable1.txt', 'r') as f:
    words = [line.rstrip() for line in f.readlines()]

wordsDict = {word: encode(word) for word in words}


def decode(word):
    return()
