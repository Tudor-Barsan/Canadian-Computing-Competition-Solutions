n = int(input())

heights = [int(a) for a in input().split()]
widths = [int(a) for a in input().split()]

total = 0

for i in range(len(widths)):
    total += widths[i] * (float(heights[i] + heights[i + 1]) / 2)

if int(total) == total:
    print(int(total))
else:
    print(total)