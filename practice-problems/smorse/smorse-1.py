import string
morseList = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseDict = dict(zip(string.ascii_lowercase, morseList.split()))

# function for encoding a given word into a string of morse


def encode(word):
    return(''.join([morseDict[letter] for letter in word]))


print(encode('sos'))

with open('enable1.txt', 'r') as f:
    words = [line.rstrip() for line in f.readlines()]
f.close()

wordsDict = {word: encode(word) for word in words}

# function for decoding a morse string into possible words


def decode(query):
    return([word for (word, morse) in wordsDict.items() if morse == query])


print(decode('-....--....'))

# bonus 1: Find sequence that is code for x words


def morseWithNumWords(num):
    morseFreq = dict.fromkeys(set(wordsDict.values()), 0)
    for word, morse in wordsDict.items():
        morseFreq[morse] = 1 + morseFreq.get(morse, 0)
    return([morse for morse, freq in morseFreq.items() if num == freq])


print(morseWithNumWords(13))  # '-....--....'

# bonus 2: Find word with x dashes in a row.


def wordWithDashes(dashes):
    dashString = '-' * dashes
    return([word for (word, morse) in wordsDict.items() if dashString in morse])


print(wordWithDashes(15))  # "bottommost"

# bonus 3: Find words that contain the same number of dots and dashes


def balanced():
    equal = []
    for (word, morse) in wordsDict.items():
        dots = morse.count('.')
        dash = morse.count('-')
        
    print(equal)

print(balanced())
