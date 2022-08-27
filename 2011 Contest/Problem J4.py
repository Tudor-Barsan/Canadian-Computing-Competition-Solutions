def solve(path, commands):
    output = []
    for i in commands:
        if i[0] == "d":
            for j in range(i[1]):
                current_pos[1] -= 1
                if current_pos in path:
                    output.append((current_pos[0], current_pos[1], "DANGER"))
                    return output
                path.append(current_pos)
                output.append((current_pos[0], current_pos[1], "safe"))

        if i[0] == "u":
            for j in range(i[1]):
                current_pos[1] += 1
                if current_pos in path:
                    output.append((current_pos[0], current_pos[1], "DANGER"))
                    return output
                path.append(current_pos)
                output.append((current_pos[0], current_pos[1], "safe"))

        if i[0] == "l":
            for j in range(i[1]):
                current_pos[0] -= 1
                if current_pos in path:
                    output.append((current_pos[0], current_pos[1], "DANGER"))
                    return output
                path.append(current_pos)
                output.append((current_pos[0], current_pos[1], "safe"))

        if i[0] == "r":
            for j in range(i[1]):
                current_pos[0] += 1
                if current_pos in path:
                    output.append((current_pos[0], current_pos[1], "DANGER"))
                    return output
                path.append(current_pos)
                output.append((current_pos[0], current_pos[1], "safe"))
    return output


path = [(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5), (4, -5), (5, -5), (5, -4), (5, -3), (6, -3), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7), (-1, -7), (-1, -6), (-1, -5)]
commands = []
a = None

while a != "q":
    a, b = [x for x in input().split()]
    commands.append((a, int(b)))
commands.pop()

current_pos = [-1, -5]

for i in solve(path, commands):
    print(f"{i[0]} {i[1]} {i[2]}")
