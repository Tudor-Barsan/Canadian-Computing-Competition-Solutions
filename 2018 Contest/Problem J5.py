from collections import defaultdict
from collections import deque

def solve (graph, n):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append([1][1])
    visited[1][1] = True




n = int(input())
l = []
graph = defaultdict(list)

for i in range(n):
    l.append([int(x) for x in input().split()])

a = 1
for i in l:
    temp_list = i[1:len(i)]
    graph[a].append(j for j in temp_list)
    a += 1


print(graph)


# graph[a].append(b)
#
# l = [1, 2, 3, 4, 5]
# j = []
#
# j.append(l[1:len(l)])
#
# print(j)