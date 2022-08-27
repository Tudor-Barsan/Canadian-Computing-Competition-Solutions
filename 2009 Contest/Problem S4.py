from collections import defaultdict
import sys
import heapq


def dijkstra(graph, start):
    d = [sys.maxsize for i in range(len(graph) + 1)]
    d[start] = 0
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, c in graph[u]:
            if v not in visited and d[v] > d[u] + c:
                d[v] = d[u] + c
                heapq.heappush(heap, (d[v], v))

    return d


n = int(input())
t = int(input())

graph = defaultdict(list)

for i in range(t):
    x, y, c = [int(x) for x in input().split()]
    graph[x].append((y, c))
    graph[y].append((x, c))

k = int(input())
prices = [0] * (n + 1)
for i in range(k):
    city, price = [int(x) for x in input().split()]
    prices[city] = price
d = int(input())

shipping_cost = dijkstra(graph, d)

best_city = -1
cost_best_city = sys.maxsize

for city in range(1, n + 1):
    pencil = prices[city]
    ship = shipping_cost[city]
    if pencil != 0:
        price = pencil + ship
        if price < cost_best_city:
            best_city = city
            cost_best_city = price


print(cost_best_city)
