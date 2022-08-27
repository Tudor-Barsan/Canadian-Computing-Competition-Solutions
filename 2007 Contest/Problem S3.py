def solve(start, end, list):
    check = [0] * 10000
    check[0] = 1
    count = 0
    friend = False
    position = start
    while not friend:
        check[position] = 1
        position = list[position]
        if position == end:
            friend = True
            break
        if check[position] == 1:
            break
        count += 1
    if friend:
        print(f"Yes {count}")
    else:
        print("No")


n = int(input())
l = []
for i in range(n):
    a, b = input().split()
    l.append((a, b))

friends = [0] * 10000

for a, b in l:
    friends[int(a)] = int(b)


test = []
x = None
y = None
while (x, y) != (str(0), str(0)):
    x, y = input().split()
    test.append((int(x), int(y)))


for (a, b) in test[:-1]:
    solve(a, b, friends)
