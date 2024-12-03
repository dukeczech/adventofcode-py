# Using zip https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list

safe1 = 0
safe2 = 0

def issafe(row: list):
    pairs = list(zip(row, row[1:]))
    if all(earlier > later for earlier, later in pairs) or all(earlier < later for earlier, later in pairs):
        # Get all the differences between tro elements
        differ = list(map(lambda x: abs(x[0] - x[1]), pairs))
        # Check the differential range
        differ = list(map(lambda x: 0 < x < 4, differ))
        return all(differ)
    return False


with open("day2.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        print("-----------------------")
        sequence = list(map(int, line.split()))
        pairs = list(zip(sequence, sequence[1:]))

        safe1 += 1 if issafe(sequence) else 0

        if(issafe(sequence)):
            safe2 += 1
            print(sequence, "is OK")
            continue
        else:
            # Start removing the elements and check the result
            found = False
            for i in range(len(sequence)):
                removed = list(sequence)
                removed.pop(i)
                if (issafe(removed)):
                    safe2 += 1
                    print(removed, "is OK after removed", sequence[i], "from", sequence)
                    found = True
                    break
            if not found:
                print(sequence, "is KO")
                pass


print("How many reports are safe?")
print(" Answer:", safe1)

print("How many reports are now safe?")
print(" Answer:", safe2)

