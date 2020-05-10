import random

'''
initialize team points to 0
gameEndPoint to 24
and allocate points for a two and three pointer
'''
teamone_pts
teamtwo_pts
gameEndPoint

twopointer
threepointer

class home:
    teamName = ""
    teampts = 0
    possession = False

    '''
    Create a constructor with parameters: teamName, teampts, and possession
    '''


class away:
    teamName = ""
    teampts = 0
    possession = False

    '''
    Create a constructor with parameters: teamName, teampts, and possession
    '''

def teamOneSelection():
    '''
    1. create a var called teamName_home
    assign it by asking the user to type in the name of their team
    2. using your constructor, create an instance of home called team_one
        set points to 0 and possession to false
    '''

    return team_one

def teamTwoSelection():
    '''
    1. create a var called teamName_away
    assign it by asking the user to type in the name of the away team
    2. using your constructor, create an instance of home called team_two
        set points to 0 and possession to false
    '''

    return team_two


def dribble():
    '''
    using random.randint ranging from 1 to 10
    use the probability to dribble
    '''
        print("\tDribbling the ball")
    else:
        print("\tBall is stolen!!")
        swapPossession()
    play()

def twoShot():
    '''
    using random.randint ranging from 1 to 10
    use the probability to make a 2 ptr
    '''
        print("\t2 points!!!")
        updateScore(2)
        swapPossession()
    else:
        print("\tMiss")
        '''
        using random.randint ranging from 1 to 10
        use the probability to make an offensive rebound
        '''
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
        '''
        using random.randint ranging from 1 to 10
        use the probability to make an offensive rebound
        '''
            print("\tOffensive Rebound")
        else:
            swapPossession()
    play()

def passBall():
    '''
    using random.randint ranging from 1 to 10
    use the probability to pass the ball
    '''
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

    '''
    Create a factory or a bunch of if statements going to different functions
    have conditionals for dribble, twoShot, threeShot, and passBall
    '''


    '''
    DONT NEED TO CODE
    JUST FOR YOUR INFORMATION
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
        '''
        set home's possession to True and away to False
        '''
        print(hometeam.teamName + " has possession")
    else:
        '''
        set away's possession to True and home to False
        '''
        print(awayteam.teamName + " has possession")

    score(hometeam,awayteam)
    play()
