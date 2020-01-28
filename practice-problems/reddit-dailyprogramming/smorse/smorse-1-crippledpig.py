# solution by /u/crippledpig. saved here as an example of good formatting and the incorporation
# of a script timer.

from collections import Counter
import itertools as it
import string
import time


def smorse(word: str) -> str:
    morseAlphabet = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
    ''' Converts an English word into a smooshed Morse representation.'''
    alphabet = string.ascii_lowercase
    mapping = dict(zip(alphabet, morseAlphabet))

    return ''.join([mapping[letter] for letter in word.lower()])


def perfectlyBalanced(seq: str):
    return seq.count('.') == seq.count('-')


def isPalindrome(str_: str):
    return str_ == str_[::-1]


start = time.time()

assert(smorse('sos')) == '...---...'
assert(smorse("daily")) == "-...-...-..-.--"
assert(smorse("programmer")) == ".--..-.-----..-..-----..-."
assert(smorse("bits")) == "-.....-..."
assert(smorse("three")) == "-.....-..."

# Bonus
with open('enable1.txt', 'r') as f:
    word2Morse = {word: smorse(word) for word in f.read().splitlines()}

# Bonus #1
seqLength1 = 13
morseCount = Counter(word2Morse.values())
bonus1 = next(mseq for (mseq, count) in morseCount.items()
              if count == seqLength1)

# Bonus #2
dashLength2 = 15
bonus2 = next(word for (word, mseq) in word2Morse.items()
              if dashLength2*'-' in mseq)

# Bonus #3
givenWord3 = 'counterdemonstrations'
wordLength3 = 21
bonus3 = next(word for (word, mseq) in word2Morse.items()
              if (perfectlyBalanced(mseq) and len(word) == wordLength3 and word != givenWord3))

# Bonus #4
givenWord4 = 'protectorate'
wordLength4 = 13
bonus4 = next(word for (word, mseq) in word2Morse.items()
              if (isPalindrome(mseq) and len(word) == wordLength4))

# Bonus #5
givenSeq5 = '--.---.---.--'
seqLength5 = len(givenSeq5)

allSeq = [''.join(seq) for seq in it.product('-.', repeat=seqLength5)]
allSeq.remove(givenSeq5)

for i in word2Morse.values():
    if len(i) >= seqLength5:
        for j in allSeq:
            if j in i:
                allSeq.remove(j)
bonus5 = allSeq

end = time.time()
print(f'Bonus 1: {bonus1}\n\
Bonus 2: {bonus2}\n\
Bonus 3: {bonus3}\n\
Bonus 4: {bonus4}\n\
Bonus 5: {bonus5}\n',
      )
print(f'Program completed in {end - start:0.2f} seconds.')
