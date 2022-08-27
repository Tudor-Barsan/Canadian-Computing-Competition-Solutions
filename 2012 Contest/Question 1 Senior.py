j = int(input())
count = 0

for a in range(1, j - 2):
    for b in range(a + 1, j - 1):
        for c in range(b + 1, j):
            count += 1

print(count)