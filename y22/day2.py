from enum import Enum

class Choose(str, Enum):
    ROCK = 'X',
    PAPER = 'Y',
    SCISSORS = 'Z',
    OP_ROCK = 'A',
    OP_PAPER = 'B',
    OP_SCISSORS = 'C'


class Need(str, Enum):
    LOSE = 'X',
    DRAW = 'Y',
    WIN = 'Z'


def get_score1(opponent: Choose, you: Choose):
    score: int = 0
    if(you == Choose.ROCK):
        score += 1
        if(opponent == Choose.OP_ROCK):
            score += 3
        elif(opponent == Choose.OP_SCISSORS):
            score += 6
        else:
            score += 0
    if (you == Choose.PAPER):
        score += 2
        if (opponent == Choose.OP_PAPER):
            score += 3
        elif (opponent == Choose.OP_ROCK):
            score += 6
        else:
            score += 0
    if (you == Choose.SCISSORS):
        score += 3
        if (opponent == Choose.OP_SCISSORS):
            score += 3
        elif (opponent == Choose.OP_PAPER):
            score += 6
        else:
            score += 0
    return score

def get_score2(opponent: Choose, you: Need):
    score: int = 0
    if (opponent == Choose.OP_ROCK):
        if(you == Need.LOSE):
            score += get_score1(opponent, Choose.SCISSORS)
        elif (you == Need.WIN):
            score += get_score1(opponent, Choose.PAPER)
        else:
            score += get_score1(opponent, Choose.ROCK)
    elif (opponent == Choose.OP_PAPER):
        if (you == Need.LOSE):
            score += get_score1(opponent, Choose.ROCK)
        elif (you == Need.WIN):
            score += get_score1(opponent, Choose.SCISSORS)
        else:
            score += get_score1(opponent, Choose.PAPER)
    else:
        if (you == Need.LOSE):
            score += get_score1(opponent, Choose.PAPER)
        elif (you == Need.WIN):
            score += get_score1(opponent, Choose.ROCK)
        else:
            score += get_score1(opponent, Choose.SCISSORS)
    return score


score1: int = 0
score2: int = 0
with open("day2.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        a = line.split()
        score1 += get_score1(Choose(a[0]), Choose(a[1]))
        score2 += get_score2(Choose(a[0]), Need(a[1]))

print("What would your total score be if everything goes exactly according to your strategy guide?")
print(" Answer:", score1)

print("Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?")
print(" Answer:", score2)