# fig04_02.py
"""Simulating the dice game Craps."""
## This program will simulate the dice game Craps
## It will do so 1 million times, in blocks of 1000
## It will then print the following statistics
## Win%, Loss%, and RollCount% (Resolved at and Cumulative)


import random

wins_dictionary = dict()
wins = 0
updates = 1000
update_games = 1000
games_passed = 0

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2

def result():
    rolls = 1
    die_values = roll_dice()  # first roll
    display_dice(die_values)

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        rolls += 1
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        return (True, rolls)
    else:
        return (False, rolls)



# This will simulate 1000 games 1000 times = 1 million times
for i in range(updates):
    print("Completing update " + str(i))
    for i in range(update_games):
        win, rolls = result()
        if (rolls in wins_dictionary):
            wins_dictionary[rolls] += 1
        else:
            wins_dictionary[rolls] = 1
        if win:
            wins += 1

# Percent won and lost
print("Percentage of wins: " + str(round((wins/(updates*update_games) * 100), 2)) + "%")
print("Percentage of wins: " + str(round(100 -(wins/(updates*update_games) * 100), 2)) + "%")
print("Percentage of wins/losses based on the total number of rolls")


# Resolved and Cumulative Percentages
wins_dictionary_sorted = sorted(wins_dictionary.items())
cumulative_wins = 0

print("          % Resolved        Cumulative %")
print("Rolls   on this roll   of games resolved")

for roll, roll_wins in wins_dictionary_sorted:
    resolved_wins = round(roll_wins / (updates*update_games) * 100, 2)
    cumulative_wins += resolved_wins
    cumulative_wins = round(cumulative_wins, 2)
    print("" * (5 - len(str(roll))) + str(roll) + "         " + str(resolved_wins) + "%             " + str(cumulative_wins) + "%")

























##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
