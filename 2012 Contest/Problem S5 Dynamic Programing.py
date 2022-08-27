r, c = [int(a) for a in input().split()]
k = int(input())
cats = []
for i in range(k):
    x, y = [int(a) for a in input().split()]
    cats.append((x, y))

maze = []
fixed = []

for r1 in range(0, r + 1):
    row = [0] * (c + 1)
    f_row = [False] * (c + 1)
    maze.append(row)
    fixed.append(f_row)

for cat in cats:
    fixed[cat[0]][cat[1]] = True

maze[1][1] = 1
fixed[1][1] = True

for r1 in range(1, r + 1):
    for c1 in range(1, c + 1):
        if not fixed[r1][c1]:
            maze[r1][c1] = maze[r1 - 1][c1] + maze[r1][c1 - 1]

print(maze[r][c])