from random import randint
from os import name, system

# clears screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# prints scores
def reveal_score():
    print("you:", user)
    print("comp:", comp)

#create a list of play options
t = ["rock", "paper", "scissors"]
comp = 0
user = 0

TIE_PT = 1 # Points for a tie
WIN_PT = 2 # Points for a win
LOSS_PT = 0 # Points for a loss
MAX_PTS = 15 # Max points for a game

#assign a random play to the computer
computer = t[randint(0,2)]

# beginning message
print("{:^50}".format("Rock-Paper-Scissors!"))
print("{} points to win the game!\n{} points for each win \n{} point for a tie \n{} points for each loss\n".format(MAX_PTS, WIN_PT, TIE_PT, LOSS_PT))

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
            print("\tYou lose!", computer, "cut", player)
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

if user >= MAX_PTS and comp >= MAX_PTS:
    print("Fair game!")
elif user >= MAX_PTS:
    print("Congrats you win!")
elif comp >= MAX_PTS:
    print("Try again next time!")
