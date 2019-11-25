word = input('Enter a word:')
letter = input('Enter a letter to count in word:')
print("There are {} {}'s in your word".format(str.count(word, letter), letter))
