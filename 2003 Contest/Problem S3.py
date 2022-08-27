from collections import deque


def get_area(i, j, board, visited):
    area = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        row, col = queue.popleft()
        area += 1
        for r1, c1 in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
            if board[r1][c1] == "." and not visited[r1][c1]:
                queue.append((r1, c1))
                visited[r1][c1] = True
    return area


f = int(input())
r = int(input())
c = int(input())

board = []
for i in range(r):
    board.append(input())

visited = [[False for i in range(c)] for j in range(r)]
areas = []

for i in range(r):
    for j in range(c):
        if board[i][j] == "." and not visited[i][j]:
            area = get_area(i, j, board, visited)
            areas.append(area)

areas.sort(reverse=True)

rooms = 0
for a in areas:
    if f > a:
        rooms += 1
        f = f - a
    else:
        break

print(f"{rooms} rooms, {f} square metre(s) left over")
