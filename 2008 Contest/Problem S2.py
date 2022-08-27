import math


def how_many_pennies(radius):
    count = 0
    radius2 = radius ** 2
    for x in range(radius + 1):
        count += int(math.sqrt(radius2 - x * x))
    count = count * 4 + 1
    print(count)


l = []
i = int(input())
l.append(i)
while i != 0:
    i = int(input())
    l.append(i)
l = l[:-1]

for j in l:
    how_many_pennies(j)