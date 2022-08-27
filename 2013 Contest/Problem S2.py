w = int(input())
n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

total = 0
cars_crossed = 0
j = 0
k = 0

for i in l:
    if k >= 4:
        total -= l[j]
        total += i
        cars_crossed += 1
        j += 1
        k += 1
    if k < 4:
        total += i
        cars_crossed += 1
        k += 1
    if total > w:
        cars_crossed -= 1
        break

print(cars_crossed)