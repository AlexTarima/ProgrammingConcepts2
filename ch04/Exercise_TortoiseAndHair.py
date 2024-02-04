## This program will simulate a race between a tortoise and a hair

import random

RACE_END = 70

def move_tortoise(tortoise):
    ## Move tortoise's position
    move = random.randrange(1, 11)  # randomize move to choose

    # determine moves by percent
    if 1 <= move <= 5:  # fast plod
        tortoise += 3
    elif move in (6, 7):  # slip
        tortoise -= 6
    else:  # slow plod
        tortoise += 1

    # ensure tortoise doesn't slip beyond start position or past the finish
    if tortoise < 1:
        tortoise = 1
    elif tortoise > RACE_END: 
        tortoise = RACE_END

    return tortoise


def move_hare(hare):
    ## Move tortoise's position
    move = random.randrange(1, 11)  # randomize move to choose

    # determine moves by percent
    if 1 <= move <= 2:  # sleep
        hare += 0
    elif move in (3, 4):  # big hop
        hare += 9
    elif move == 5: # big slip
        hare -= 12
    elif move in (6,8): # small hop
        hare += 1
    else: # small slip
        hare -= 2

    # ensure tortoise doesn't slip beyond start position or past the finish
    if hare < 1:
        hare = 1
    elif hare > RACE_END: 
        hare = RACE_END

    return hare


def print_positions(tortoise, hare, RACE_END):
    if tortoise == hare:
        print(" " * (tortoise - 1) + "OUCH!!!" + " " * abs(RACE_END - tortoise))
        return
    elif (tortoise > hare):
        print(" " * (hare - 1) + "H" + " " * (tortoise - hare) + "T" + " " * abs(RACE_END - tortoise))
    else:
        print(" " * (tortoise - 1) + "H" + " " * (hare - tortoise) + "T" + " " * abs(RACE_END - hare))


def main(tortoise, hare, RACE_END):
    print("BANG !!!!!\nAND THEY'RE OFF !!!!!")
    won = False

    while(not won):
        tortoise = move_tortoise(tortoise)
        hare = move_hare(hare)
        print_positions(tortoise, hare, RACE_END)
        if (tortoise >= 70 or hare >= 70):
            won = True
    if (tortoise > hare):
        print("TORTOISE WINS!!! YAY!!!")
    elif (hare > tortoise):
        print("HARE WINS!!! YAY!!!")
    else:
        print("It's a tie")



main(1,1,RACE_END)
