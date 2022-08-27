k = int(input())
l = []

for i in range(k):
    a = int(input())
    if a != 0:
        l.append(a)
    else:
        l.pop()

sum = 0

for i in l:
    sum += i

print(sum)
