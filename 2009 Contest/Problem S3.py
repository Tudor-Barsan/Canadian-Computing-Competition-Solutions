def command_i(x, y):
    graph[x][y] = 1
    graph[y][x] = 1


def command_d(x, y):
    graph[x][y] = 0
    graph[y][x] = 0


def command_n(x):
    count = 0
    for i in range(1, 50):
        if graph[x][i] == 1:
            count += 1
    print(count)


def command_f(x):
    count = 0
    for i in range(1, 50):
        if graph[x][i] == 1:
            for j in range(1, 50):
                if graph[i][j] == 1 and graph[x][j] == 0 and j != x:
                    count += 1
    print(count)


def command_s(x, y):
    stack = []
    distance = [1000 for i in range(0, 50)]
    visited = [False for i in range(0, 50)]
    stack.append(x)
    visited[x] = True
    distance[x] = 0
    while stack:
        c = stack.pop()
        for i in range(1, 50):
            if graph[c][i] == 1:
                forceVisit = False
                if distance[i] > distance[c] + 1:
                    distance[i] = distance[c] + 1
                    forceVisit = True
                if not visited[i] or forceVisit:
                    stack.append(i)
                    visited[i] = True
    if distance[y] == 1000:
        print("Not connected")
    else:
        print(distance[y])


graph = [[0 for i in range(50)] for j in range(50)]
graph[2][6] = 1
graph[6][2] = 1
graph[1][6] = 1
graph[6][1] = 1
graph[6][3] = 1
graph[3][6] = 1
graph[6][4] = 1
graph[4][6] = 1
graph[6][5] = 1
graph[5][6] = 1
graph[6][7] = 1
graph[7][6] = 1
graph[3][4] = 1
graph[4][3] = 1
graph[3][5] = 1
graph[5][3] = 1
graph[4][5] = 1
graph[5][4] = 1
graph[7][8] = 1
graph[8][7] = 1
graph[8][9] = 1
graph[9][8] = 1
graph[9][10] = 1
graph[10][9] = 1
graph[9][12] = 1
graph[12][9] = 1
graph[10][11] = 1
graph[11][10] = 1
graph[11][12] = 1
graph[12][11] = 1
graph[12][13] = 1
graph[13][12] = 1
graph[13][14] = 1
graph[14][13] = 1
graph[13][15] = 1
graph[15][13] = 1
graph[3][15] = 1
graph[15][3] = 1
graph[16][18] = 1
graph[18][16] = 1
graph[16][17] = 1
graph[17][16] = 1
graph[17][18] = 1
graph[18][17] = 1

cmd = None

while cmd != "q":
    l = input().split()
    cmd = l[0]
    if cmd == "i":
        command_i(int(l[1]), int(l[2]))
    elif cmd == "d":
        command_d(int(l[1]), int(l[2]))
    elif cmd == "n":
        command_n(int(l[1]))
    elif cmd == "f":
        command_f(int(l[1]))
    elif cmd == "s":
        command_s(int(l[1]), int(l[2]))

