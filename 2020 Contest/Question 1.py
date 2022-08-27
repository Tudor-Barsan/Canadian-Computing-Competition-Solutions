S = int(input())
M = int(input())
L = int(input())

Mood = int(S + 2 * M + 3 * L)

if Mood > 9:
    print("happy")
else:
    print("sad")


