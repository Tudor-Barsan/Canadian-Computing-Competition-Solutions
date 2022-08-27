A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())

AT = 3 * A3 + 2 * A2 + A1
BT = 3 * B3 + 2 * B2 + B1

if AT > BT:
    print("A")
elif BT > AT:
    print("B")
else:
    print("T")
