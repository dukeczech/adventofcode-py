class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


result1 = 0
result2 = 0
debug = False

data = open('day6.dat').read().splitlines()

matrix = []
visited = []
visited2 = []
lastpoint = (0, 0)


# Convert 1d array into 2d array
def clear():
    global data
    global matrix
    global visited
    global visited2
    global lastpoint

    matrix = [[0 for i in range(len(data[0]))] for j in range(len(data))]
    visited = [[0 for i in range(len(data[0]))] for j in range(len(data))]
    visited2 = [[0 for i in range(len(data[0]))] for j in range(len(data))]
    for i in range(0, len(data)):
        matrix[i] = list(data[i])
        visited[i] = list(data[i])
        visited2[i] = list(data[i])
    lastpoint = (0, 0)


def printmatrix(arr: [], bold=None):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if (bold != None and (x, y) in bold):
                print(color.RED, end="")
            print(arr[y][x], end=" ")
            if (bold != None and (x, y) in bold):
                print(color.END, end="")
        print()
    print()


def isvisited(x: int, y: int, mx: [] = visited) -> bool:
    return mx[y][x] == 'M'


def getguard(mx: [] = matrix):
    for y in range(0, len(mx)):
        for x in range(0, len(mx[y])):
            if (mx[y][x] == "^" or mx[y][x] == ">" or mx[y][x] == "v" or mx[y][x] == "<"):
                return (x, y)
    return None


def makestep(mx: [] = matrix):
    global lastpoint

    x = lastpoint[0]
    y = lastpoint[1]

    if (mx[y][x] == "^" or mx[y][x] == ">" or mx[y][x] == "v" or mx[y][x] == "<"):

        direction = mx[y][x]
        nexdirection = None
        nextpoint = (x, y)
        if (direction == "^"):
            nexdirection = ">"
            nextpoint = (x, y - 1)
        elif (direction == ">"):
            nexdirection = "v"
            nextpoint = (x + 1, y)
        elif (direction == "v"):
            nexdirection = "<"
            nextpoint = (x, y + 1)
        elif (direction == "<"):
            nexdirection = "^"
            nextpoint = (x - 1, y)

        visited2[y][x] = visited2[y][x].replace('.', '')
        if (direction not in visited2[y][x]):
            visited2[y][x] += direction

        # Check the limits
        if (nextpoint[0] < 0 or nextpoint[0] >= len(mx[0])):
            # print("Next x is ouside", nextpoint[0])
            visited[y][x] = 'M'
            return False
        if (nextpoint[1] < 0 or nextpoint[1] >= len(mx)):
            # print("Next y is ouside", nextpoint[1])
            visited[y][x] = 'M'
            return False

        # Check the next position
        if (mx[nextpoint[1]][nextpoint[0]] == "."):
            # Step
            visited[y][x] = 'M'
            mx[y][x] = '.'
            mx[nextpoint[1]][nextpoint[0]] = direction
            lastpoint = nextpoint
            return True
        elif (mx[nextpoint[1]][nextpoint[0]] == "#"):
            # Obstacle
            mx[y][x] = nexdirection
            return True


def checkcycle(mx: [] = matrix):
    global lastpoint

    x = lastpoint[0]
    y = lastpoint[1]

    if (mx[y][x] == "^" or mx[y][x] == ">" or mx[y][x] == "v" or mx[y][x] == "<"):

        direction = mx[y][x]
        nextpoint = (x, y)
        if (direction == "^"):
            nextpoint = (x, y - 1)
        elif (direction == ">"):
            nextpoint = (x + 1, y)
        elif (direction == "v"):
            nextpoint = (x, y + 1)
        elif (direction == "<"):
            nextpoint = (x - 1, y)

        # Check the limits
        if (nextpoint[0] < 0 or nextpoint[0] >= len(mx[0])):
            return False
        if (nextpoint[1] < 0 or nextpoint[1] >= len(mx)):
            return False

        # Check cycle (same direction at the current point)
        if (direction in visited2[nextpoint[1]][nextpoint[0]]):
            return True
    return False


def checkmatrix(mx: []):
    global lastpoint

    # Get the starting position
    lastpoint = getguard(mx)
    if (lastpoint is None):
        return True
    while (True):
        if (checkcycle(mx)):
            # This matrix has a cycle
            return False

        # Make one step
        step = makestep(mx)

        if (not step):
            # Step outside the matrix
            break
    return True


def putobstruction(x: int, y: int):
    # Reset the arrays
    clear()
    # Put the obstruction at the next visited position
    if (isvisited(x, y, visited_const)):
        matrix[y][x] = "#"
        visited[y][x] = "#"
        visited2[y][x] = "#"
        # print("Putting the obstruction at", x, y)
        # Check the cycle in the matrix
        if (not checkmatrix(matrix)):
            # print("Cycle at", x, y)
            return True
    return False


# Perform the first step
# Reset the arrays
clear()
# Get the starting position
lastpoint = getguard(matrix)
while (True):
    # Make one step
    step = makestep(matrix)
    # Step outside the matrix
    if (not step):
        break

visited_const = list(map(list, visited))
result1 = sum([i.count('M') for i in visited_const])

# Perform the second step
for y in range(0, len(matrix)):
    for x in range(0, len(matrix[y])):
        if (putobstruction(x, y)):
            result2 += 1

print("How many distinct positions will the guard visit before leaving the mapped area?")
print(" Answer:", result1)

print("How many different positions could you choose for this obstruction?")
print(" Answer:", result2)
