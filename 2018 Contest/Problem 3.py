a, b, c, d = [int(s) for s in input().split()]

print(0, a, a+b, a+b+c, a+b+c+d)
print(a, 0, b, abs(b+c), abs(b+c+d))
print(a+b, b, 0, c, c+d)
print(a+b+c, b+c, c, 0, d)
print(a+b+c+d, b+c+d, c+d, d, 0)