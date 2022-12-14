import re

knots1: [[]] = [[0] * 2 for _ in range(2)]
knots2: [[]] = [[0] * 2 for _ in range(10)]
tail_visited1: set = set()
tail_visited2: set = set()


def check_knot(current: [], prev: []):
    if (prev[0] == current[0] + 2):
        # move right
        current[0] += 1
        if (prev[1] < current[1]):
            current[1] -= 1
        elif (prev[1] > current[1]):
            current[1] += 1
        else:
            pass
    if (prev[0] == current[0] - 2):
        # move left
        current[0] -= 1
        if (prev[1] < current[1]):
            current[1] -= 1
        elif (prev[1] > current[1]):
            current[1] += 1
        else:
            pass
    if (prev[1] == current[1] + 2):
        # move up
        current[1] += 1
        if (prev[0] < current[0]):
            current[0] -= 1
        elif (prev[0] > current[0]):
            current[0] += 1
        else:
            pass
    if (prev[1] == current[1] - 2):
        # move down
        current[1] -= 1
        if (prev[0] < current[0]):
            current[0] -= 1
        elif (prev[0] > current[0]):
            current[0] += 1
        else:
            pass


with open("day9.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        found = re.match("([RULD]) ([0-9]+)", line)
        if (found):
            for i in range(0, int(found.group(2))):
                if (found.group(1) == "R"):
                    knots1[0][0] += 1
                elif (found.group(1) == "L"):
                    knots1[0][0] -= 1
                elif (found.group(1) == "U"):
                    knots1[0][1] += 1
                elif (found.group(1) == "D"):
                    knots1[0][1] -= 1
                check_knot(knots1[1], knots1[0])
                tail_visited1.add((knots1[-1][0], knots1[-1][1]))

    for line in lines:
        found = re.match("([RULD]) ([0-9]+)", line)
        if (found):
            for i in range(0, int(found.group(2))):
                if (found.group(1) == "R"):
                    knots2[0][0] += 1
                elif (found.group(1) == "L"):
                    knots2[0][0] -= 1
                elif (found.group(1) == "U"):
                    knots2[0][1] += 1
                elif (found.group(1) == "D"):
                    knots2[0][1] -= 1
                for i in range(0, len(knots2) - 1):
                    check_knot(knots2[i + 1], knots2[i])
                tail_visited2.add((knots2[-1][0], knots2[-1][1]))

print("Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?")
print(" Answer:", len(tail_visited1))

print("Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?")
print(" Answer:", len(tail_visited2))
