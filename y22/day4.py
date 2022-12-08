
class Pair():
    start: [int] = [0, 0]
    end: [int] = [0, 0]

    def __init__(self, p1: str, p2: str):
        self.start[0] = int(p1.split("-")[0])
        self.start[1] = int(p2.split("-")[0])
        self.end[0] = int(p1.split("-")[1])
        self.end[1] = int(p2.split("-")[1])

    def __str__(self):
        return str(self.start[0]) + "-" + str(self.end[0]) + "," + \
               str(self.start[1]) + "-" + str(self.end[1])

    def contains(self):
        if(self.start[0] >= self.start[1] and self.end[0] <= self.end[1]):
            return True
        if(self.start[0] <= self.start[1] and self.end[0] >= self.end[1]):
            return True
        return False

    def overlaps(self):
        if (self.start[1] <= self.end[0] and self.start[1] >= self.start[0]):
            return True
        if (self.end[1] <= self.end[0] and self.end[1] >= self.start[0]):
            return True
        if (self.start[0] >= self.start[1] and self.end[0] <= self.end[1]):
            return True
        return False


count1: int = 0
count2: int = 0
with open("day4.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        a = line.split(",")
        p = Pair(a[0], a[1])
        if(p.contains()):
            count1 += 1
        if(p.overlaps()):
            count2 += 1

print("In how many assignment pairs does one range fully contain the other?")
print(" Answer:", count1)

print("In how many assignment pairs do the ranges overlap?")
print(" Answer:", count2)