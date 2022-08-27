from collections import deque


def get_next_cells(board, row, col, r, c):
    next_cells = []
    if board[row][col] == "+":
        if row + 1 < r and board[row + 1][col] != "*":
            next_cells.append((row + 1, col))
        if row - 1 >= 0 and board[row - 1][col] != "*":
            next_cells.append((row - 1, col))
        if col + 1 < c and board[row][col + 1] != "*":
            next_cells.append((row, col + 1))
        if col - 1 >= 0 and board[row][col - 1] != "*":
            next_cells.append((row, col - 1))

    elif board[row][col] == "|":
        if row + 1 < r and board[row + 1][col] != "*":
            next_cells.append((row + 1, col))
        if row - 1 >= 0 and board[row - 1][col] != "*":
            next_cells.append((row - 1, col))

    else:
        if col + 1 < c and board[row][col + 1] != "*":
            next_cells.append((row, col + 1))
        if col - 1 >= 0 and board[row][col - 1] != "*":
            next_cells.append((row, col - 1))

    return next_cells


def solve(board, row, col):
    visited = [[False for a in range(col)] for b in range(row)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    while queue:
        r, c, d = queue.popleft()
        if r == row - 1 and c == col - 1:
            return d
        for r1, c1 in get_next_cells(board, r, c, row, col):
            if not visited[r1][c1]:
                queue.append((r1, c1, d + 1))
                visited[r1][c1] = True
    return -1


t = int(input())

results =[]

for i in range(t):
    r = int(input())
    c = int(input())
    board = [[None for a in range(c)] for b in range(r)]
    for r1 in range(r):
        l = list(input())
        for c1 in range(c):
            board[r1][c1] = l[c1]

    results.append(solve(board, r, c))

for i in results:
    print(i)