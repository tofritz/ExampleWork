def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return count

word = input('Enter a word:')
letter = input('Enter a letter to count in word:')
print("There are {} {}'s in your word".format(count(word,letter), letter))
