from collections import defaultdict
from collections import deque


def solve(p, q, graph, n):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(p)
    visited[p] = True
    while queue:
        current = queue.pop()
        if current == q:
            return True
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False


n, m = [int(x) for x in input().split()]

comp_t = defaultdict(list)

for i in range(m):
    a, b = [int(x) for x in input().split()]
    comp_t[a].append(b)

p, q = [int(x) for x in input().split()]


if solve(p, q, comp_t, n):
    print("yes")
elif solve(q, p, comp_t, n):
    print("no")
else:
    print("unknown")