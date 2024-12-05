
result1 = 0
result2 = 0

data = open('day4.dat').read().splitlines()

# Convert 1d array into 2d array
matrix = [[0 for i in range(len(data[0]))] for j in range(len(data))]
for i in range(0, len(data)):
    matrix[i] = list(data[i])

# Safe get and match function (checking the limits)
def safe_match(i: int, j: int, s: str) -> bool:
    if(i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[i])):
        for ch in s:
            if(matrix[i][j] == ch):
                return True
    return False

# Solve part one
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if(safe_match(i, j, 'X')):
            # Right
            if(safe_match(i, j + 1, 'M')):
                if (safe_match(i, j + 2, 'A')):
                    if (safe_match(i, j + 3, 'S')):
                        result1 += 1
            # Left
            if (safe_match(i, j - 1, 'M')):
                if (safe_match(i, j - 2, 'A')):
                    if (safe_match(i, j - 3, 'S')):
                        result1 += 1
            # Down
            if (safe_match(i + 1, j, 'M')):
                if (safe_match(i + 2, j, 'A')):
                    if (safe_match(i + 3, j, 'S')):
                        result1 += 1
            # Up
            if (safe_match(i - 1, j, 'M')):
                if (safe_match(i - 2, j, 'A')):
                    if (safe_match(i - 3, j, 'S')):
                        result1 += 1
            # Diagonal right up
            if (safe_match(i - 1, j + 1, 'M')):
                if (safe_match(i - 2, j + 2, 'A')):
                    if (safe_match(i - 3, j + 3, 'S')):
                        result1 += 1
            # Diagonal right down
            if (safe_match(i + 1, j + 1, 'M')):
                if (safe_match(i + 2, j + 2, 'A')):
                    if (safe_match(i + 3, j + 3, 'S')):
                        result1 += 1
            # Diagonal left up
            if (safe_match(i - 1, j - 1, 'M')):
                if (safe_match(i - 2, j - 2, 'A')):
                    if (safe_match(i - 3, j - 3, 'S')):
                        result1 += 1
            # Diagonal left down
            if (safe_match(i + 1, j - 1, 'M')):
                if (safe_match(i + 2, j - 2, 'A')):
                    if (safe_match(i + 3, j - 3, 'S')):
                        result1 += 1

# Solve part two
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if (safe_match(i, j, 'A')):
            if (safe_match(i - 1, j - 1, 'M')):
                if (safe_match(i + 1, j + 1, 'S')):
                    if (safe_match(i - 1, j + 1, 'M')):
                        if (safe_match(i + 1, j - 1, 'S')):
                            result2 += 1
                    if (safe_match(i - 1, j + 1, 'S')):
                        if (safe_match(i + 1, j - 1, 'M')):
                            result2 += 1
            if (safe_match(i - 1, j - 1, 'S')):
                if (safe_match(i + 1, j + 1, 'M')):
                    if (safe_match(i - 1, j + 1, 'M')):
                        if (safe_match(i + 1, j - 1, 'S')):
                            result2 += 1
                    if (safe_match(i - 1, j + 1, 'S')):
                        if (safe_match(i + 1, j - 1, 'M')):
                            result2 += 1


print("How many times does XMAS appear?")
print(" Answer:", result1)

print("How many times does an X-MAS appear?")
print(" Answer:", result2)