# Simulates one game of Hi Ho! Cherry-O
 
import random
 
spinnerChoices = [-1, -2, -3, -4, 2, 2, 10]
turns = 0
cherriesOnTree = 10
 
# Take a turn as long as you have more than 0 cherries
while cherriesOnTree > 0:
 
    # Spin the spinner
    spinIndex = random.randrange(0, 7)
    spinResult = spinnerChoices[spinIndex]
 
    # Print the spin result    
    print ("You spun " + str(spinResult) + ".")
 
    # Add or remove cherries based on the result
    cherriesOnTree += spinResult
 
    # Make sure the number of cherries is between 0 and 10   
    if cherriesOnTree > 10:
        cherriesOnTree = 10
    elif cherriesOnTree < 0:
        cherriesOnTree = 0
 
    # Print the number of cherries on the tree       
    print ("You have " + str(cherriesOnTree) + " cherries on your tree.")
 
    turns += 1
 
# Print the number of turns it took to win the game
print ("It took you " + str(turns) + " turns to win the game.")
lastline = raw_input(">")