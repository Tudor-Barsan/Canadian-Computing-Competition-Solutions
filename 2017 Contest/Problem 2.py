n = int(input())
k = int(input())

total = n

for i in range(k):
    n *= 10
    total += n

print(total)