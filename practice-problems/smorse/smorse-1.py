import string
morseList = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseDict = dict(zip(string.ascii_lowercase, morseList.split()))

# function for encoding a given word into a string of morse


def encode(word):
    return(''.join([morseDict[letter] for letter in word]))


print(encode('sos'))

with open('enable1.txt', 'r') as f:
    words = [line.rstrip() for line in f.readlines()]


wordsDict = {word: encode(word) for word in words}

# function for decoding a morse string into possible words


def decode(query):
    return([word for (word, morse) in wordsDict.items() if morse == query])


print(decode('-....--....'))

# bonus 1: Find sequence that is code for n words


def morseWithNumWords(num):
    morseFreq = dict.fromkeys(set(wordsDict.values()), 0)
    for word, morse in wordsDict.items():
        morseFreq[morse] = 1 + morseFreq.get(morse, 0)
    return([morse for morse, freq in morseFreq.items() if num == freq])


print(morseWithNumWords(13))  # '-....--....'

# bonus 2: Find word with n dashes in a row.


def wordWithDashes(dashes):
    dashString = '-' * dashes
    return([word for (word, morse) in wordsDict.items() if dashString in morse])


print(wordWithDashes(15))  # "bottommost"

# bonus 3: Find words that contain the same number of dots and dashes


def balanced(chars):
    equal = []
    words = []
    for (word, morse) in wordsDict.items():
        if (morse.count('.') == morse.count('-')):
            equal.append(word)
    for item in equal:
        if len(item) == chars:
            words.append(item)
    return(words)


print(balanced(21))  # [counterdemonstrations, overcommercialization]

# bonus 4: Find morse palindrome with n characters.


def palindrome(chars):
    palindrome = []
    words = []
    for (word, morse) in wordsDict.items():
        if (morse == morse[::-1]):
            palindrome.append(word)
    for item in palindrome:
        if len(item) == chars:
            words.append(item)
    return(words)


print(palindrome(13))  # intransigence

# bonus 5: Find x-character morse sequences that do not appear in encoding of any word.


def missingSequence(chars):
    binarySequences = list(range(0, (2 ** chars) + 1)) # find all possible binary representations up to length n
    sequences = []
    for num in binarySequences:
        seq = bin(num).lstrip('0b').replace('1', '-').replace('0', '.') # filter list to n-length binaries and substitute 0,1 for .,-
        if len(seq) >= chars:
            sequences.append(seq)
    for morse in wordsDict.values(): # check if each seq is in morse and remove if it is. (much faster removing as it shortens array results in smaller loops
        if len(morse) >= chars:
            for seq in sequences:
                if seq in morse:
                    sequences.remove(seq)  

    return(sequences)


print(missingSequence(13))
# ['--.---.---.--', '--.---.------', '---.---.---.-', '---.---.-----', '---.----.----']
