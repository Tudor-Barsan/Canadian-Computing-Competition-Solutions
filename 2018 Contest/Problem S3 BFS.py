from collections import deque


def mark_caught(r, c):
    global board, caught, n, m
    caught.add((r, c))
    c1 = c - 1
    while c1 >= 0:
        if board[r][c1] == "W":
            break
        elif board[r][c1] == "." or board[r][c1] == "S":
            caught.add((r, c1))
        c1 -= 1

    c1 = c + 1
    while c1 < m:
        if board[r][c1] == "W":
            break
        elif board[r][c1] == "." or board[r][c1] == "S":
            caught.add((r, c1))
        c1 += 1

    r1 = r + 1
    while r1 < n:
        if board[r1][c] == "W":
            break
        elif board[r1][c] == "." or board[r1][c] == "S":
            caught.add((r1, c))
        r1 += 1

    r1 = r - 1
    while r1 >= 0:
        if board[r1][c] == "W":
            break
        elif board[r1][c] == "." or board[r1][c] == "S":
            caught.add((r1, c))
        r1 -= 1


def get_next(r1, c1, dir):
    if dir == "U":
        return r1 - 1, c1
    if dir == "D":
        return r1 + 1, c1
    if dir == "L":
        return r1, c1 - 1
    if dir == "R":
        return r1, c1 + 1


def solve(rs, cs):
    global board, caught, result, n, m
    if (rs, cs) in caught:
        return
    visited = [[False for c in range(m)] for r in range(n)]
    queue = deque()
    queue.append((rs, cs, 0))
    while queue:
        r1, c1, level = queue.popleft()
        if board[r1][c1] == ".":
            result[(r1, c1)] = level

        level += 1
        for r2, c2 in [(r1 + 1, c1), (r1 - 1, c1), (r1, c1 + 1), (r1, c1 - 1)]:
            loop = False
            loop_cells = set()
            while 0 <= r2 < n and 0 <= c2 < m and board[r2][c2] in ["U", "D", "L", "R"]:
                r2, c2 = get_next(r2, c2, board[r2][c2])
                if (r2,c2) in loop_cells:
                    loop = True
                    break
                loop_cells.add((r2,c2))

            if not loop and (r2, c2) not in caught and 0 <= r2 < n and 0 <= c2 < m and not visited[r2][c2]:
                queue.append((r2, c2, level))
                visited[r2][c2] = True


n, m = [int(a) for a in input().split()]

board = []

for i in range(n):
    board.append(list(input()))

caught = set()
rs = 0
cs = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == "C":
            mark_caught(r, c)
        elif board[r][c] == "S":
            rs, cs = r, c
        elif board[r][c] == "W":
            caught.add((r, c))

result = {}

solve(rs, cs)

for r in range(n):
    for c in range(m):
        if board[r][c] == ".":
            if (r, c) in result:
                print(result[(r, c)])
            else:
                print(-1)
