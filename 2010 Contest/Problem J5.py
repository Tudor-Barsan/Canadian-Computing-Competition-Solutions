from collections import deque


def solve(sx, sy, ex, ey, visited, board):
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]
    queue = deque()
    queue.append((sx, sy, 0))
    visited[sx][sy] = True
    while queue:
        x, y, d = queue.popleft()
        if x == ex and y == ey:
            return d
        for k in range(8):
            x1 = x + xMove[k]
            y1 = y + yMove[k]
            if 0 < x1 < 9 and 0 < y1 < 9 and not visited[x1][y1]:
                queue.append((x1, y1, d + 1))
                visited[x1][y1] = True
                board[x1][y1] = (x, y)
    return -1


sx, sy = [int(x) for x in input().split()]
ex, ey = [int(x) for x in input().split()]

visited = [[False for i in range(9)] for j in range(9)]
board = [[None for i in range(9)] for j in range(9)]

t = (ex, ey)
l = []

print(solve(sx, sy, ex, ey, visited, board))

while t is not None:
    l.append(t)
    t = board[t[0]][t[1]]

print(list(reversed(l)))

