from string import ascii_lowercase

morse_alphabet = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
char_to_morse = dict(zip(ascii_lowercase, morse_alphabet))
morse_to_char = dict(zip(morse_alphabet, ascii_lowercase))


def smalpha(morse: str, found=""):
    if morse == "" and set(found) == set(ascii_lowercase):
        return(''.join(found))

    for letter in {letter for letter in ascii_lowercase if letter not in found}:
        if not morse.startswith(char_to_morse[letter]):
            continue
        _found = found + letter
        _morse = morse[len(char_to_morse[letter]):]
        try:
            return smalpha(_morse, _found)
        except:
            raise SomethingWentWrong
    else:
        raise SomethingWentWrong


class SomethingWentWrong(Exception):
    print("Something went horribly wrong.")
    pass


test = '.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..'
print(smalpha(test))
