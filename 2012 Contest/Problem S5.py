def is_safe(maze, x, y, r, c):
    if 0 < x <= r and 0 < y <= c and maze[x][y] == 0:
        return True
    return False


def solve(maze, x, y, r, c):
    global count
    if x == r and y == c:
        count += 1
        return
    if is_safe(maze, x + 1, y, r, c):
        solve(maze, x + 1, y, r, c)
    if is_safe(maze, x, y + 1, r, c):
        solve(maze, x, y + 1, r, c)


r, c = input().split()

count = 0

maze = [[0 for i in range(int(c) + 1)] for j in range(int(r) + 1)]

k = int(input())
for i in range(k):
    a, b = input().split()
    maze[int(a)][int(b)] = 1


solve(maze, 1, 1, int(r), int(c))
print(count)