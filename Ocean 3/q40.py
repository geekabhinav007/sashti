# 40. Write a function that displays the spiral: RULLDDRRRUUULLLL… and so on. It should keep displaying until it has displayed 1,000,000 Letters in this pattern. (5 points)


i = 0
j = 0

while (i < 1000000):
    j = j + 1
    for k in range(j):
        print("R", end="")
        i = i + 1
    for l in range(j):
        print("U", end="")
        i = i + 1
    j = j + 1
    for m in range(j):
        print("L", end="")
        i = i + 1
    for n in range(j):
        print("D", end="")
        i = i + 1
