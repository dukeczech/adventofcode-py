import operator

result1 = 0
result2 = 0

data = open('day7.dat').read().splitlines()


def evaluate1(testvalue: int, total: int, array: [], steps: str):
    global result1

    if (len(array) == 0):
        if (total == testvalue):
            # print("Calibration result OK:", testvalue, "=", steps)
            return True
    else:
        if (len(steps) == 0):
            a1 = evaluate1(testvalue, array[0] + total, array[1:], str(array[0]))
            a2 = evaluate1(testvalue, array[0] * total, array[1:], str(array[0]))
            return a1 or a2
        else:
            a1 = evaluate1(testvalue, array[0] + total, array[1:], steps + " + " + str(array[0]))
            a2 = evaluate1(testvalue, array[0] * total, array[1:], steps + " * " + str(array[0]))
            return a1 or a2
    return False


def evaluate2(testvalue: int, total: int, array: [], steps: str):
    global result1

    if (len(array) == 0):
        if (total == testvalue):
            # print("Calibration result OK:", testvalue, "=", steps)
            return True
    else:
        if (len(steps) == 0):
            a1 = evaluate2(testvalue, array[0] + total, array[1:], str(array[0]))
            a2 = evaluate2(testvalue, array[0] * total, array[1:], str(array[0]))
            a3 = evaluate2(testvalue, int(str(total) + str(array[0])), array[1:], str(array[0]))
            return a1 or a2 or a3
        else:
            a1 = evaluate2(testvalue, array[0] + total, array[1:], steps + " + " + str(array[0]))
            a2 = evaluate2(testvalue, array[0] * total, array[1:], steps + " * " + str(array[0]))
            a3 = evaluate2(testvalue, int(str(total) + str(array[0])), array[1:], steps + " || " + str(array[0]))
            return a1 or a2 or a3
    return False


for line in data:
    testvalue = int(line.split()[0].strip(':'))
    operators = list(map(int, line.split()[1:]))

    if (evaluate1(testvalue, 0, operators, "")):
        result1 += testvalue
    if (evaluate2(testvalue, 0, operators, "")):
        result2 += testvalue

print("What is their total calibration result?")
print(" Answer:", result1)

print("How many different positions could you choose for this obstruction?")
print(" Answer:", result2)
