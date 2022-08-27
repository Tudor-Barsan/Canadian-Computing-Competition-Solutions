flips = input()
l = []
a = 1
b = 2
c = 3
d = 4

for char in flips:
    l.append(char)

for i in l:
    if i == "H":
        a, c = c, a
        b, d = d, b
    if i == "V":
        a, b = b, a
        c, d = d, c

print(f"{a} {b}")
print(f"{c} {d}")