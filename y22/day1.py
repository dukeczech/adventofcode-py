
class Elf:
    line: int = 0
    foods : list[int] = []

    def __init__(self):
        self.line = 0
        self.foods = []

    def __str__(self):
        return "[" + str(self.line) + "]: " + str(self.foods)

    def __repr__(self):
        return "[" + str(self.line) + "]: " + str(self.foods)

    def __gt__(self, other):
        return self.sum() > other.sum()

    def sum(self):
        return sum(self.foods)


elfs : list[Elf] = []
with open("day1.dat") as file:
    lines = file.read().splitlines()

    elf = Elf()
    for idx, food in enumerate(lines):
        if(len(food) > 0 or len(elf.foods) == 0):
            elf.line = int(idx)
            if(len(food) == 0):
                elf.foods.append(0)
            else:
                elf.foods.append(int(food))
        else:
            elfs.append(elf)
            elf = Elf()
        # Add last element
        if(idx == len(lines) - 1):
            elfs.append(elf)


# print([e for e in elfs])

print("Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
print(" Andwer:", max(elfs).sum())

print("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
print(" Andwer:", sum(e.sum() for e in sorted(elfs, reverse=True)[:3]))