from string import ascii_lowercase
import time

morse_alphabet = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
morse_to_char = dict(zip(morse_alphabet, ascii_lowercase))
char_to_morse = dict(zip(ascii_lowercase, morse_alphabet))


def recurse(smorse, remaining = set(morse_alphabet), found = []):
    if not smorse:
        yield found
        return
    
    for morse in remaining:
        if morse == smorse[:len(morse)]:
            found.append(morse)
            trim = remaining.copy()
            trim.remove(morse)
            yield from recurse(smorse[len(morse):], trim, found)
            found.pop()

def smalpha(smorse):
    for found in recurse(smorse):
        return ''.join([morse_to_char[morse] for morse in found])

def encode(string: str):
    return ''.join(char_to_morse[char] for char in string)

def check(input):
    output = smalpha(input)
    assert encode(output) == input
    assert set(output) == set(ascii_lowercase)
    return output

def challenge():
    check('.--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..')
    return print('Challenge Passed!')

def challenge2():
    start = time.time()
    with open('inputs.txt', 'r') as input:
        check(smorse.rstrip() for smorse in input.readlines())
    end = time.time()
    print(f'Optional bonus 1 complete! Time elapsed: {end - start:0.2f} seconds.')

challenge()
challenge2()