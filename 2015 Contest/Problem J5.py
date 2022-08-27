def count(n ,k ,min):
    if k == n:
        return 1
    elif k == 1:
        return 1
    elif (n, k, min) in cache:
        return cache[(n, k, min)]
    sum = 0
    for m in range(min, n//k + 1):
        sum += count(n - m, k - 1, m)
    cache[n, k, min] = sum
    return sum


n = int(input())
k = int(input())

cache = {}

print(count(n, k, 1))
