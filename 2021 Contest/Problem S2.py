m = int(input())
n = int(input())
k = int(input())

rows = set()
cols = set()

for i in range(k):
    rule, index = input().split()
    index = int(index)
    if rule == "R":
        if index in rows:
            rows.remove(index)
        else:
            rows.add(index)
    else:
        if index in cols:
            cols.remove(index)
        else:
            cols.add(index)

a = len(rows)
b = len(cols)
total = a * n + b * m - 2 * (a * b)

print(total)

