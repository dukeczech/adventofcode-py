import functools


def compare(left, right):
    if (isinstance(left, int) and isinstance(right, int)):
        if (left < right):
            return 1
        elif (left > right):
            return -1
        else:
            return 0
    elif (isinstance(left, int) and isinstance(right, list)):
        left = [left]
        return compare(left, right)
    elif (isinstance(left, list) and isinstance(right, int)):
        right = [right]
        return compare(left, right)
    elif (isinstance(left, list) and isinstance(right, list)):
        if (len(left) > len(right)):
            for l in range(0, len(left)):
                if (l == len(right)):
                    return -1
                elif (l == len(left)):
                    return 1
                else:
                    result = compare(left[l], right[l])
                    if (result > 0):
                        return 1
                    elif (result < 0):
                        return -1
                    else:
                        continue
        else:
            for r in range(0, len(right)):
                if (r == len(left)):
                    return 1
                else:
                    result = compare(left[r], right[r])
                    if (result > 0):
                        return 1
                    elif (result < 0):
                        return -1
                    else:
                        continue
        return 0


packets = []
sum1: int = 0
key2: int = 0
with open("day13.dat") as file:
    lines = file.read().splitlines()
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i + 1])
        packets.append(left)
        packets.append(right)

        if (compare(left, right) > 0):
            sum1 += int((i / 3) + 1)

# Include two additional divider packets:
packets.append([[2]])
packets.append([[6]])
packets.sort(key=functools.cmp_to_key(compare), reverse=True)

key2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print("Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?")
print(" Answer:", sum1)

print("Organize all of the packets into the correct order. What is the decoder key for the distress signal?")
print(" Answer:", key2)
