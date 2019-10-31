from random import randint
from os import name, system

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def reveal_score():
    print("you:", user)
    print("comp:", comp)
#create a list of play options
t = ["rock", "paper", "scissors"]
comp = 0
user = 0

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False
print("{:^50}".format("Rock-Paper-Scissors!"))
print("15 points to win the game!\n2 points for each win \n1 point for a tie \n0 points for each loss\n")

while player == False and user < 15 and comp < 15:
    player = input("\nrock, paper, scissors? Type STOP to stop: ")
    if player == "stop" or player == "STOP":
        reveal_score()
        break
    elif player == computer:
        clear()
        comp += 1
        user += 1
        print("\tYou both chose", player)
        print("\tTie!")
        reveal_score()
    elif player == "rock":
        if computer == "paper":
            clear()
            comp += 2
            print("\tcomputer chose", computer)
            print("\tYou lose!", computer, "covers", player)
            reveal_score()
        else:
            clear()
            user += 2
            print("\tcomputer chose", computer)
            print("\tYou win!", player, "smashes", computer)
            reveal_score()
    elif player == "paper":
        if computer == "scissors":
            clear()
            comp += 2
            print("\tcomputer chose", computer)
            print("\tYou lose!", computer, "cut", player)
            reveal_score()
        else:
            clear()
            user += 2
            print("\tcomputer chose", computer)
            print("\tYou win!", player, "covers", computer)
            reveal_score()
    elif player == "scissors":
        if computer == "rock":
            clear()
            comp += 2
            print("\tcomputer chose", computer)
            print("\tYou lose...", computer, "smashes", player)
            reveal_score()
        else:
            clear()
            user += 2
            print("\tcomputer chose", computer)
            print("\tYou win!", player, "cut", computer)
            reveal_score()
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

if user >= 15 and comp >= 15:
    print("Fair game!")
elif user >= 15:
    print("Congrats you win!")
elif comp >= 15:
    print("Try again next time!")
