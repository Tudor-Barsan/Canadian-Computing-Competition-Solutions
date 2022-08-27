n = int(input())
l = []

for i in range(n):
    l.append(input())

for line in l:
    current = None
    counter = 0
    for c in line:
        if current is None:
            current = c
            counter += 1
        elif current == c:
            counter += 1
        else:
            print(counter, end="")
            print(current, end="")
            current = c
            counter = 1
    print(counter, end="")
    print(current)