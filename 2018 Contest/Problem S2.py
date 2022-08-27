def rot_90(l):
    return [list(reversed(x)) for x in zip(*l)]


def check(grid):
    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] <= grid[0][0]:
                return False
    return True


n = int(input())
grid = []

for i in range(n):
    l = [int(a) for a in input().split()]
    grid.append(l)

while not check(grid):
    rot_90(grid)

print(grid)
