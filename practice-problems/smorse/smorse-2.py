import string
morseAlpha = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseList = morseAlpha.split()
morseDict = dict(zip(morseAlpha.split(), string.ascii_lowercase))

test = ".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----.."


def get_letter(seq):
    for morse, letter in morseDict.items():
        if seq == morse:
            return letter

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

def smalpha_2(smorse: str):
    toReplace = list(morseDict.items())
    toReplace.sort(reverse=True key=lambda x: len(x[0]))
    return toReplace


print(smalpha_2(test))
