def max_sugar(i):
    global sugar, n, cache

    if i > n - 1:
        return 0

    if cache[i] is not None:
        return cache[i]

    result = max(sugar[i] + max_sugar(i + 2), max_sugar(i + 1))
    cache[i] = result
    return result


n = int(input())

sugar = []
b = []
cache = [None] * n

for i in range(n):
    sugar.append(int(input()))

m = int(input())

for i in range(m):
    b.append(int(input()))

print(max_sugar(0))