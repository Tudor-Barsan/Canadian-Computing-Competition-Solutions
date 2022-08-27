from collections import defaultdict
from collections import deque


def is_taller (p, q, graph, n):
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
graph = defaultdict(list)

for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)

p, q = [int(x) for x in input().split()]

if is_taller(p, q, graph, n):
    print("yes")
elif is_taller(q, p, graph, n):
    print("no")
else:
    print("unknown")