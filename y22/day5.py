import collections
import re

stacks1: [collections.deque] = []
stacks2: [collections.deque] = []


with open("day5.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        if(line.strip().startswith("1")):
            stack_count = int(line.split()[-1])
            stacks1 = [collections.deque() for i in range(stack_count)]
            stacks2 = [collections.deque() for i in range(stack_count)]
            break

    for line in lines:
        if(line.strip().startswith("[")):
            col = 0
            for i in range(0, len(line), 4):
                found = re.match("\[([A-Z]+)\]", line[i:i + 4])
                if(found):
                    stacks1[col].append(found.group(1))
                    stacks2[col].append(found.group(1))
                col += 1
        elif(line.strip().startswith("move")):
            found = re.match("move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)
            if(found):
                count = int(found.group(1))
                src1 = stacks1[int(found.group(2)) - 1]
                dst1 = stacks1[int(found.group(3)) - 1]
                src2 = stacks2[int(found.group(2)) - 1]
                dst2 = stacks2[int(found.group(3)) - 1]
                st = list(list(src2)[0:count])
                st.reverse()
                for i in range(0, count):
                    dst1.appendleft(src1.popleft())
                    src2.popleft()
                dst2.extendleft(st)



top1: str = ""
top2: str = ""
for d in stacks1:
    top1 += d.popleft()

for d in stacks2:
    top2 += d.popleft()


print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
print(" Answer:", top1)

print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
print(" Answer:", top2)