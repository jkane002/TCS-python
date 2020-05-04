import random

teamone_pts = 0
teamtwo_pts = 0
gameEndPoint = 24

twopointer = 2
threepointer = 3

class home:
    teamName = ""
    teampts = 0
    possession = False

    def __init__(self, teamName, teampts, pos):
        self.teamName = teamName
        self.teampts = teampts
        self.possession = pos

class away:
    teamName = ""
    teampts = 0
    possession = False

    def __init__(self, teamName, teampts):
        self.teamName = teamName
        self.teampts = teampts
        self.possession = pos

def teamOneSelection():
    teamName_home = input("Type in the name of your team: ")
    team_one = home(teamName_home, 0, False)

    return team_one

def teamTwoSelection():
    teamName_away = input("Type in the name of the away team: ")
    team_two = home(teamName_away, 0, False)

    return team_two


def dribble():
    if random.randint(1,10) > 1:
        print("\tDribbling the ball")
    else:
        print("\tBall is stolen!!")
        swapPossession()
    play()

def twoShot():
    if random.randint(1,10) > 6:
        print("\t2 points!!!")
        updateScore(2)
        swapPossession()
    else:
        print("\tMiss")
        if random.randint(1,10) > 6:
            print("\tOffensive Rebound")
        else:
            swapPossession()
    play()

def threeShot():
    if random.randint(1,10) > 8:
        print("\t3 points!!!")
        updateScore(3)
        swapPossession()
    else:
        print("\tMiss")
        if random.randint(1,10) > 6:
            print("\tOffensive Rebound")
        else:
            swapPossession()
    play()

def passBall():
    if random.randint(1,10) > 3:
        print("\tPassing to teammate")
    else:
        print("\tBall is stolen!!!")
        swapPossession()
    play()

def swapPossession():
    if hometeam.possession:
        hometeam.possession = False
        awayteam.possession = True
        print("\n\t" + awayteam.teamName + " has possession!\n")
    else:
        hometeam.possession = True
        awayteam.possession = False
        print("\n\t" + hometeam.teamName + " has possession!\n")

def score(home, away):
    print("\n")
    print(home.teamName + ": " + str(home.teampts))
    print(away.teamName + ": " + str(away.teampts))


def updateScore(num):
    if hometeam.possession:
        hometeam.teampts += num
        score(hometeam, awayteam)
    elif awayteam.possession:
        awayteam.teampts += num
        score(hometeam, awayteam)
    else:
        print("Somehow there is an error in updateScore")


def playFactory(play):
    if play == dribble:
        dribble()
    if play == twoShot:
        twoShot()
    if play == threeShot:
        threeShot()
    if play == passBall:
        passBall()

    '''
    keys: 1, dribble
          2, 2 twopointer
          3, 3 threepointer
          4, pass

    dribble 90% keep basketball
    pass 70% keep
    shoot
        2 pt 40% make
        3 pt 20% make
    offensive rebounds 40%
    '''

def play():
    if hometeam.teampts >= gameEndPoint or awayteam.teampts >= gameEndPoint:
        print("\n\t THAT IS GAME!!\n")
        score(hometeam, awayteam)
        return

    switcher = {
        1: dribble,
        2: twoShot,
        3: threeShot,
        4: passBall
    }
    case = 0
    try:
        case = int(input("1, 2, 3, or 4: "))
    except ValueError:
        print("Invalid move. Try again")
        play()

    if case in range(1,5):
        case = int(case)
        playFactory(switcher[case])
    else:
        print("Invalid move: Press again")
        play()


if __name__ == "__main__":
    print("Tipoff! Select your teams")
    hometeam = teamOneSelection()
    awayteam = teamTwoSelection()
    print("To play\n1: dribble, 2: shoot a 2, 3: shoot a 3, 4: pass\n")
    print("Score up to {} points\n".format(gameEndPoint))

    teampick = random.randint(0,1)
    if teampick == 0:
        hometeam.possession = True
        awayteam.possession = False
        print(hometeam.teamName + " has possession")
    else:
        hometeam.possession = False
        awayteam.possession = True
        print(awayteam.teamName + " has possession")


    score(hometeam,awayteam)
    play()
