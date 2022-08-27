import math

a = int(input())
b = int(input())
count = 0

for x in range(a, b + 1):
    x3 = (math.ceil(x ** (1/3))) ** 3
    x2 = (math.ceil(x ** (1/2))) ** 2
    if x == x2 and x == x3:
        count += 1

print(count)