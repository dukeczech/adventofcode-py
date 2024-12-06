result1 = 0
result2 = 0

data = open('day5.dat').read().splitlines()

rules = dict()
updates = list()

for line in data:
    if ("|" in line):
        values = line.split("|")
        rules.setdefault(values[0], []).append(values[1])
    elif ("," in line):
        updates.append(line.split(","))


# print("Rules:", rules)
# print("Updates:", updates)


def getparents(element: str) -> set():
    parents = set()
    if (element == None):
        return None
    for key in rules:
        for value in rules[key]:
            if (element == value):
                parents.add(key)
    return parents


def find(array: list, element: str) -> int:
    if (element in array):
        return array.index(element)
    return None


# First part check
def check(array: list) -> bool:
    for i in range(len(array)):
        parents = getparents(array[i])
        for p in parents:
            found = find(update, p)
            if (found != None and found > i):
                return False
    return True


# Second part check
def checkandfix(array: list) -> bool:
    for i in range(len(array)):
        parents = getparents(array[i])
        for p in parents:
            found = find(update, p)
            if (found != None and found > i):
                # Try to swap the elements
                a = update[found]
                b = update[i]
                update[found] = b
                update[i] = a
                checkandfix(update)
                return True
    return False


# Run the first part
for update in updates:
    correct = check(update)
    if (correct):
        result1 += int(update[len(update) // 2])

# Run the second part
for update in updates:
    fixed = checkandfix(update)
    if (fixed):
        result2 += int(update[len(update) // 2])

print("What do you get if you add up the middle page number from those correctly-ordered updates?")
print(" Answer:", result1)

print("What do you get if you add up the middle page numbers after correctly ordering just those updates?")
print(" Answer:", result2)
