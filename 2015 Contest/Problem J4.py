def already_added(friend, wait_times):
    for a in wait_times:
        if a[0] == friend:
            return True
    return False


m = int(input())
actions = []

for i in range(m):
    x, y = [a for a in input().split(" ")]
    actions.append((x, int(y)))

wait_times = []
current_wait = 1
final_times = []

for i in actions:
    if i[0] == "R":
        if already_added(i[1], wait_times):
            for j in wait_times:
                if j[0] == i[1]:
                    j[2] = True
                    break
        else:
            wait_times.append([i[1], 0, True])

    if i[0] == "S":
        for j in wait_times:
            if j[0] == i[1]:
                j[2] = False
                if already_added(j[0], final_times):
                    for b in final_times:
                        if b[0] == j[0]:
                            b[1] += j[1]
                else:
                    final_times.append([j[0], j[1]])

    if i[0] == "W":
        for j in wait_times:
            if j[2]:
                j[1] += (i[1] - 1)

    for j in wait_times:
        if j[2]:
            j[1] += 1

for pair in final_times:
    pair[1] -= 1
    print(f'{pair[0]} {pair[1]}')