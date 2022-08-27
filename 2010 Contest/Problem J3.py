def instruction_for_2(c, x):
    if x == "a":
        print(a)
    if x == "b":
        print(b)


def instruction_for_3(c, x, y):
    if c == "1":
        if x == "a":
            a = y
    return x


command = None
a = 0
b = 0
l = []

while command != 7:
    l = input().split()
    if len(l) == 2:
        instruction_for_2(l[0], l[1])
    elif len(l) == 3:
        instruction_for_3(l[0], l[1], l[2])




