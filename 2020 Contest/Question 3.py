n = int(input())
xlist = []
ylist = []


for i in range(n):
    x, y = [int(a) for a in input().split(",")]
    xlist.append(x)
    ylist.append(y)

print(min(xlist) - 1, end=",")
print(min(ylist) - 1)

print(max(xlist) + 1, end=",")
print(max(ylist) + 1)