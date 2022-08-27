P = int(input())
N = int(input())
R = int(input())

day = 1

while N * R * day < P:
    N = N * R
    day += 1

print(day)
