n = int(input())
people = []

MIN = -10000000000000001
MAX = 200000000000001
min1 = MAX
max1 = MIN
sum = []
diff = []

for i in range(n):
    p, w, d = [int(a) for a in input().split()]
    people.append((p, w, d))
    s = p + d
    k = p - d
    if s < min1:
        min1 = s
    if k > max1:
        max1 = k
    sum.append(s * w)
    diff.append(k * w)

time = []



total = 0
c = min1
for i in people:
    p = i[0]
    w = i[1]
    d = i[2]
    if c > p:
        if c - p > d:
            total += ((c - p) - d) * w
    else:
        if p - c > d:
            total += ((p - c) - d) * w
best = total

for c in range(min1 + 1, max1 + 1):
    for i in people:
        p = i[0]
        w = i[1]
        d = i[2]
        if (p + d) < c:
            total += ((c - p) - d) * w
        if (p - d) > c:
            total -= ((p - d) - c) * w

    if total < best:
        best = total

print(best)


