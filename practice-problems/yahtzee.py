# The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results in a number of ways.
# You are given a Yahtzee dice roll, represented as a sorted list of 5 integers, each of which is between 1 and 6 inclusive.
# Your task is to find the maximum possible score for this roll in the upper section of the Yahtzee score card. Here's what that means.
# For the purpose of this challenge, the upper section of Yahtzee gives you six possible ways to score a roll.
#  1 times the number of 1's in the roll, 2 times the number of 2's, 3 times the number of 3's, and so on up to 6 times the number of 6's.
# For instance, consider the roll [2, 3, 5, 5, 6]. If you scored this as 1's, the score would be 0, since there are no 1's in the roll.
# If you scored it as 2's, the score would be 2, since there's one 2 in the roll.
# Scoring the roll in each of the six ways gives you the six possible scores: 0 2 3 0 10 6
# The maximum here is 10 (2x5), so your result should be 10.
'''
rolls = [2, 3, 5, 5, 6]
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for roll in rolls:
    for number in counts:
        if number == roll:
            counts[number] += roll

print counts
'''
lst = [2, 3, 5, 5, 6, 800,
       200, 200, 200, 200, 200, 300, 300]


def yahtzee(rolls):
    counts = dict.fromkeys(rolls, 0)
    for roll in rolls:
        for key in counts:
            if key == roll:
                counts[key] += roll
    values = list(counts.values())
    return max(values)


print(yahtzee(lst))


def onelineyahtzee(lst):
    return max([lst.count(x) * x for x in lst])


print(onelineyahtzee(lst))
