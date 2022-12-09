forest: list = list()


def is_visible(forest: list, x: int, y: int):
    visible: [bool] = [True] * 4
    for i in range(0, len(forest[y])):
        if (i < x and forest[y][i] >= forest[y][x]):
            visible[0] = False
        if (i > x and forest[y][i] >= forest[y][x]):
            visible[1] = False
    for j in range(0, len(forest)):
        if (j < y and forest[j][x] >= forest[y][x]):
            visible[2] = False
        if (j > y and forest[j][x] >= forest[y][x]):
            visible[3] = False
    for v in visible:
        if (v):
            return True
    return False


def get_score(forest: list, x: int, y: int):
    score: int = 1
    trees_visible: [int] = [0] * 4

    for i in reversed(range(0, x)):
        current = forest[y][i]
        if (current < forest[y][x]):
            trees_visible[2] += 1
        else:
            trees_visible[2] += 1
            break
    for i in range(x + 1, len(forest[y])):
        current = forest[y][i]
        if (current < forest[y][x]):
            trees_visible[3] += 1
        else:
            trees_visible[3] += 1
            break
    for j in reversed(range(0, y)):
        current = forest[j][x]
        if (current < forest[y][x]):
            trees_visible[0] += 1
        else:
            trees_visible[0] += 1
            break
    for j in range(y + 1, len(forest)):
        current = forest[j][x]
        if (current < forest[y][x]):
            trees_visible[1] += 1
        else:
            trees_visible[1] += 1
            break

    for v in trees_visible:
        score *= v
    return score


with open("day8.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        forest.append(list(line))

count1: int = 0
count2: int = 0
for i in range(0, len(forest)):
    for j in range(0, len(forest[0])):
        if (is_visible(forest, i, j)):
            count1 += 1
        score = get_score(forest, i, j)
        if (score > count2):
            count2 = score

print("Consider your map; how many trees are visible from outside the grid?")
print(" Answer", count1)

print("Consider each tree on your map. What is the highest scenic score possible for any tree?")
print(" Answer", count2)
