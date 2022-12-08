import string


PRIORITIES = dict({ch: pri + 1 for pri, ch in enumerate(string.ascii_lowercase)}.items() |
                      {ch: pri + 27 for pri, ch in enumerate(string.ascii_uppercase)}.items())

def get_priority(el: str):
    return PRIORITIES[el]

class Rucksack():
    compartment: [str] = []

    def __init__(self, input: str):
        self.compartment = [input[:len(input) // 2], input[len(input) // 2:]]

    def __str__(self):
        return "[" + self.compartment[0] + "] [" + self.compartment[1] + "]"

    def get_shared(self):
        for e in self.compartment[0]:
            if(self.compartment[1].find(e) >= 0):
                return e
        return None


class Group():
    groups: [str] = []

    def __init__(self, groups: [str]):
        self.groups = groups

    def __str__(self):
        return str(self.groups)

    def get_badge(self):
        for e1 in self.groups[0]:
            for e2 in self.groups[1]:
                for e3 in self.groups[2]:
                    if(e1 == e2 and e2 == e3):
                        return e1
        return None


priorities1: int = 0
priorities2: int = 0
with open("day3.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        r = Rucksack(line)
        priorities1 += get_priority(r.get_shared())
    for group in range(0, len(lines), 3):
        g = Group(lines[group: group + 3])
        priorities2 += get_priority(g.get_badge())

print("What is the sum of the priorities of those item types?")
print(" Answer:", priorities1)

print("Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?")
print(" Answer:", priorities2)