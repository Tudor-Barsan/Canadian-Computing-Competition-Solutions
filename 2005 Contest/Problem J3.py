l = []

while True:
    s = input()
    if s == "SCHOOL":
        break
    l.append(s)


for i in range(len(l)):
    if l[i] == "L":
        l[i] = "RIGHT"
    elif l[i] == "R":
        l[i] = "LEFT"

l.reverse()

for i in range(len(l)):
    if i % 2 == 0:
        print(f"Turn {l[i]} onto ", end="")
    else:
        print(f"{l[i]} street")

print("your HOME")
