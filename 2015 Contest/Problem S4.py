from collections import defaultdict
import heapq


def dijkstra(graph, start, end, hull, n):
    d = {x: 10000 for x in range(1, n+1)}
    d[start] = 0
    heap = [(start, 0, 0)]
    visited = set()
    curr_damage = 0
    while heap:
        (island, time, damage) = heapq.heappop(heap)
        if island in visited:
            continue
        visited.add(island)

        for destination, time, damage in graph[island]:
            if destination not in visited and d[destination] > d[island] + time and (curr_damage + damage) < hull:
                d[destination] = d[island] + time
                curr_damage += damage
                heapq.heappush(heap, (destination, d[destination], damage))

    for key in d:
        if key == end:
            if d[key] == 10000:
                return -1
            return d[key]


k, n, m = [int(a) for a in input().split()]
graph = defaultdict(list)

for i in range(m):
    a, b, t, h = [int(x) for x in input().split()]
    graph[a].append([b, t, h])

a, b = [int(x) for x in input().split()]


print(dijkstra(graph, a, b, k, n))
