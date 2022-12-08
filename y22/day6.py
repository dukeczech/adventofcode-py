
index1: int = 0
index2: int = 0
with open("day6.dat") as file:
    line = file.read()

    for i in range(0, len(line)):
        unique_chars1 = list(set(line[i:i + 4]))
        unique_chars2 = list(set(line[i:i + 14]))
        if(len(unique_chars1) == 4 and index1 == 0):
            index1 = i + 4
        if (len(unique_chars2) == 14 and index2 == 0):
            index2 = i + 14
        if(index1 > 0 and index2 > 0):
            break

print("How many characters need to be processed before the first start-of-packet marker is detected?")
print(" Answer:", index1)

print("How many characters need to be processed before the first start-of-message marker is detected?")
print(" Answer:", index2)