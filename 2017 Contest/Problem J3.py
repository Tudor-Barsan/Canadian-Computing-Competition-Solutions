x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
t = int(input())

if t - abs(x1 - x2 + y1 - x2) == 0:
    print("Y")
if t - abs(x1 - x2 + y1 - x2) > 0 and (t - abs(x1 - x2 + y1 - x2)) % 2 == 0:
    print("Y")
else:
    print("N")