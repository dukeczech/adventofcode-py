import re
from functools import reduce

result1 = 0
result2 = 0

data = open('day3.dat').read()

operations = re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', data)

disable = False
for operation in operations:
    # Calculate the first part
    pair = list(map(int, re.findall("\d+", operation)))
    if(pair):
        result1 += reduce(lambda x, y: x * y, pair, 1)

    # Calculate the second part
    if(operation == 'do()'):
        disable = False
    elif (operation == 'don\'t()'):
        disable = True
    else:
        if(not disable):
            result2 += reduce(lambda x, y: x * y, pair, 1)



print("What do you get if you add up all of the results of the multiplications?")
print(" Answer:", result1)

print("Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?")
print(" Answer:", result2)