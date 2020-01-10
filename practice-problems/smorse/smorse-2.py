import string
morseAlpha = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseList = morseAlpha.split()
morseDict = dict(zip(morseAlpha.split(), string.ascii_lowercase))

test = ".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----.."


def get_letter(seq):
    for morse, letter in morseDict.items():
        if seq == morse:
            return letter


def decode(query):
    return([word for (word, morse) in wordsDict.items() if morse == query])


# brute-force replace characters as encountered

# def smalpha_1(smorse: str):
#     alpha = ''
#     while len(smorse) > 0:
#         if smorse[0:2] in morseDict.keys():
#             alpha += morseDict.pop(smorse[0:2])
#             smorse = smorse[2:]
#         elif smorse[1:3] in morseDict.keys():
#             alpha += morseDict.pop(smorse[0:2])
#             smorse = smorse[2:]
#     return(alpha)


# print(smalpha_1(test))


# pop out of list sorted by morse length after substitution

# def smalpha_2(smorse: str):
#     toReplace = list(morseDict.items())
#     toReplace.sort(reverse=True, key=lambda x: len(x[0]))
#     for (morse, letter) in toReplace:
#         smorse = smorse.replace(morse, letter, 1)
#         toReplace.pop(0)
#     return(smorse)


# print(smalpha_2(test))

# count frequency of morse in smorse, replace low > high freq.

morseFreq = {morse: 0 for morse in morseDict.keys()}  # counter


# def reset():
#     morseFreq = dict.fromkeys(morseFreq, 0)

def reset():
    for morse, freq in morseFreq.items():
        morseFreq[morse] = 0


def count(smorse: str):
    for morse, freq in morseFreq.items():
        morseFreq[morse] = smorse.count(morse)


# def rank(rankFreq):
#     rankFreq = list(morseFreq.items())
#     rankFreq.sort(key=lambda x: x[1])
#     return rankFreq


def smalpha_freq(smorse: str):
    counter = 26
    count(smorse)
    rankFreq = list(morseFreq.items())
    rankFreq.sort(key=lambda x: x[1])
    while counter > 0:
        smorse = smorse.replace(rankFreq[0][0], morseDict[rankFreq[0][0]], 1)
        del morseFreq[rankFreq[0][0]]
        del rankFreq[0]
        counter -= 1
    return smorse


print(smalpha_freq(test))
