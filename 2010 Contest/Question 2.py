a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

step = 1
Nikky_Dir = True
Nikky_Steps_For_Dir = a
NPosition = 0

Byron_Dir = True
Byron_Steps_For_Dir = c
BPosition = 0

while step <= s:

    if Nikky_Dir:
        NPosition += 1
    else:
        NPosition -= 1

    Nikky_Steps_For_Dir -= 1

    if Nikky_Steps_For_Dir == 0:
        if Nikky_Dir:
            Nikky_Dir = False
            Nikky_Steps_For_Dir = b
        else:
            Nikky_Dir = True
            Nikky_Steps_For_Dir = a

    if Byron_Dir:
        BPosition += 1
    else:
        BPosition -= 1
    Byron_Steps_For_Dir -= 1

    if Byron_Steps_For_Dir == 0:
        if Byron_Dir:
            Byron_Dir = False
            Byron_Steps_For_Dir = d
        else:
            Byron_Dir = True
            Byron_Steps_For_Dir = c

    step += 1

print(f"Positions: {NPosition} {BPosition}")
if NPosition > BPosition:
    print("Nikky")
elif BPosition > NPosition:
    print("Byron")
else:
    print("Tied")