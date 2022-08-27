from collections import defaultdict
import sys


def printSolution(m, n, sol1):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(sol1[i][j],end =' ')
        print()


def is_safe(r, c, sol, m, n):
    if 0 < r <= m and 0 < c <= n and sol[r][c] == 0:
        return True
    return False


def build_cache(cache, m, n, board):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cache[board[i][j]].append((i, j))


def get_next_cells(row1, col1, cache):
    return cache[row1 * col1]


def solve(board, sol, row, col, m, n, cache):
    if row == 1 and col == 1:
        sol[1][1] = 1
        return True
    for r, c in cache[row * col]:
        if sol[r][c] == 0:
            sol[r][c] = 1
            if solve(board, sol, r, c, m, n, cache):
                return True
            sol[r][c] = 0
    return False


sys.setrecursionlimit(8000)

m = int(input())
n = int(input())

sol = [[0 for i in range(n + 1)] for j in range(m + 1)]
board = list()
board.append([0 for i in range(n + 1)])

for i in range(m):
    l = [0]
    l.extend([int(x) for x in input().split()])
    board.append(l)

sol[m][n] = 1
cell_cache = defaultdict(list)

build_cache(cell_cache, m, n, board)

if solve(board, sol, m, n, m, n, cell_cache):
    print("yes")
else:
    print("no")

# printSolution(m, n, sol)