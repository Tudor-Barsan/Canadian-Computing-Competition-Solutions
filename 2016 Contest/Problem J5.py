q = int(input())
n = int(input())

sum = 0

dmojistan = [int(a) for a in input().split()]
pegland = [int(b) for b in input().split()]

dmojistan.sort()
pegland.sort()

if q == 1:
    for i in range(len(dmojistan)):
        a = dmojistan[i]
        b = pegland[i]
        sum += max(a, b)

else:
    pegland.sort(reverse=True)
    for i in range(len(dmojistan)):
        a = dmojistan[i]
        b = pegland[i]
        sum += max(a, b)

print(sum)