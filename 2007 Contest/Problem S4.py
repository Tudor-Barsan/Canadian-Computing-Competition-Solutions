from collections import defaultdict
import sys
sys.setrecursionlimit(10000)


def total_paths(i):
    if i == n:
        return 1
    if cache[i] != -1:
        return cache[i]
    sum = 0
    for next in paths[i]:
        sum += total_paths(next)
    cache[i] = sum
    return sum


n = int(input())
paths = defaultdict(list)
cache = [-1] * (n+1)

x, y = [int(a) for a in input().split()]

while x != 0 and y != 0:
    paths[x].append(y)
    x, y = [int(a) for a in input().split()]

print(total_paths(1))
