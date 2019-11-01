# Things to think about:
# How can I make this game better?
# What other features can I implement?
# 5 TODOS

from random import randint
from os import name, system

#create a list of play options
t = ["rock", "paper", "scissors"]
comp = 0
user = 0

# TODO
TIE_PT = 0 # Points for a tie
WIN_PT = 0 # Points for a win
LOSS_PT = 0 # Points for a loss
MAX_PTS = 0 # Max total points for a match

#assign a random play to the computer
computer = t[randint(0,2)]

# clears screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#TODO
# prints scores
def reveal_score():
    # This function reveals the scores of both the user and the computer
    # what can you do so that the terminal looks like this:
    # you: 15 # where 15 is the number of points you have
    # comp: 20 # and 20 is the number of points the computer has
    pass


# beginning message
print("{:^50}".format("Rock-Paper-Scissors!"))
#TODO
# I want to print out how many points it is to win the entire match, win a game, tie, and lose
# hint use str.format

player = True
while player and user < MAX_PTS and comp < MAX_PTS:
    player = input("\nrock, paper, scissors? Type STOP to stop: ")
    if player == "stop" or player == "STOP":
        reveal_score()
        break
    elif player == computer:
        clear()
        comp += TIE_PT
        user += TIE_PT
        print("\tYou both chose", player)
        print("\tTie!")
        reveal_score()
    elif player == "rock":
        if computer == "paper":
            clear()
            comp += WIN_PT
            print("\tcomputer chose", computer)
            print("\tYou lose!", computer, "covers", player)
            reveal_score()
        else:
            clear()
            user += WIN_PT
            print("\tcomputer chose", computer)
            print("\tYou win!", player, "smashes", computer)
            reveal_score()
    elif player == "paper":
        if computer == "scissors":
            clear()
            comp += WIN_PT
            print("\tcomputer chose", computer)
            #TODO
            # following the win/loss statements
            # print out the result of this game
            reveal_score()
        else:
            clear()
            user += WIN_PT
            print("\tcomputer chose", computer)
            print("\tYou win!", player, "covers", computer)
            reveal_score()
    elif player == "scissors":
        if computer == "rock":
            clear()
            comp += WIN_PT
            print("\tcomputer chose", computer)
            print("\tYou lose...", computer, "smashes", player)
            reveal_score()
        else:
            clear()
            user += WIN_PT
            print("\tcomputer chose", computer)
            print("\tYou win!", player, "cut", computer)
            reveal_score()
    else:
        print("That's not a valid play. Check your spelling!")

    player = True
    computer = t[randint(0,2)]

#TODO
# print "Fair game!" if the user and computer ties
# print "Congrats you win!" if the you, the user, wins
# print "Try again next time" if the computer wins
