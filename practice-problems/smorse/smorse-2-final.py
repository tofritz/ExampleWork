from string import ascii_lowercase
import time

morse_alphabet = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
morse_to_char = dict(zip(morse_alphabet, ascii_lowercase))
char_to_morse = dict(zip(ascii_lowercase, morse_alphabet))
found = []


def recurse(smorse, remaining=set(morse_alphabet)):
    if not smorse:
        yield found
        return

    for morse in remaining:
        if morse == smorse[:len(morse)]:
            found.append(morse)
            trim = remaining.copy()
            trim.remove(morse)
            # recurse  with trimmed set once morse found
            yield from recurse(smorse[len(morse):], trim)
            # backtrack if no morse in set remaining match next smorse
            found.pop()


def smalpha(smorse):
    for found in recurse(smorse):
        return ''.join(morse_to_char[morse] for morse in found)


def encode(string: str):
    return ''.join(char_to_morse[char] for char in string)


def check(input):
    global found
    found.clear()
    output = smalpha(input)
    assert encode(output) == input
    assert set(output) == set(ascii_lowercase)
    return output


def challenge():
    check('.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..')
    check('.----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-')
    check('..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-..')
    return print('Challenge Passed!')


def bonus1():
    start = time.time()
    with open('inputs.txt', 'r') as file:
        for line in file:
            smorse = line.rstrip()
            check(smorse)
    end = time.time()
    print(
        f'Optional bonus 1 complete! Time elapsed: {end - start:0.2f} seconds.')


challenge()
bonus1()  # Time elapsed: 75.57 seconds
