
left = []
right = []
sum = 0
score = 0

with open("day1.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        print(line.split())
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

for (l, r) in zip(sorted(left), sorted(right)):
    sum += abs(l - r)

for l in left:
    count = right.count(l)
    score += count * l


print("What is the total distance between your lists?")
print(" Answer:", sum)

print("What is their similarity score?")
print(" Answer:", score)