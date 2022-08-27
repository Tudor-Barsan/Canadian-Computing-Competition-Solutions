# line1 = "*x*"
# line2 = " xx"
# line3 = "* *"

k = int(input())

line1 = "*" * k + "x" * k + "*" * k
line2 = " " * k + "xx" * k
line3 = "*" * k + " " * k + "*" * k

for i in range(0, k):
    print(line1)

for i in range(0, k):
    print(line2)

for i in range(0, k):
    print(line3)
