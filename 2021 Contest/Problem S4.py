from bisect import bisect_left, insort
from collections import defaultdict
from collections import deque


def calculate_time_for_walkways():
    queue = deque()
    queue.append((n, 0))
    visited = [False] * (n+1)
    while queue:
        node, t = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        time_walkway[node] = t

        for next in graph[node]:
            if not visited[next]:
                queue.append((next, t + 1))


def update_times(old_idx, new_idx):
    if s[new_idx] == n:
        old_score = old_idx
        new_score = new_idx
        replace_score(old_score, new_score)
    elif time_walkway[s[new_idx]] != -1:
        old_score = old_idx + time_walkway[s[new_idx]]
        new_score = new_idx + time_walkway[s[new_idx]]
        replace_score(old_score, new_score)


def replace_score(old_score, new_score):
    i = bisect_left(times, old_score)
    del times[i]
    insort(times, new_score)


def calculate_time(ix, iy):
    update_times(ix, iy)
    update_times(iy, ix)
    return times[0]


def calculate_initial_time():
    for i in range(0, n):
        if s[i] == n:
            times.append(i)
        elif time_walkway[s[i]] != -1:
            times.append(i + time_walkway[s[i]])
    times.sort()


n, w, d = [int(x) for x in input().split()]
graph = defaultdict(list)
for i in range(w):
    a, b = [int(x) for x in input().split()]
    graph[b].append(a)

time_walkway = [-1] * (n+1)
calculate_time_for_walkways()
s = [int(x) for x in input().split()]
times = []
calculate_initial_time()

last_n_pos = n + 1
for i in range(d):
    x, y = [int(z) for z in input().split()]
    s[x-1], s[y-1] = s[y-1], s[x-1]
    val1 = calculate_time(x-1, y-1)
    print(val1)
