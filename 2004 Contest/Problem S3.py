def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_formula(s):
    result = []
    for cell in s.split("+"):
        row = ord(cell[0]) - ord("A")
        col = int(cell[1]) - 1
        result.append((row, col))
    return result


spreadsheet = []

for n in range(10):
    spreadsheet.append(input().split())

values = [[-1 for i in range(9)] for j in range(10)]

for r in range(10):
    for c in range(9):
        if is_number(spreadsheet[r][c]):
            values[r][c] = int(spreadsheet[r][c])
        else:
            spreadsheet[r][c] = get_formula(spreadsheet[r][c])


done = False

while not done:
    done = True
    for r in range(10):
        for c in range(9):
            if values[r][c] == -1:
                sum = 0
                can_calculate = True
                for tup in spreadsheet[r][c]:
                    if values[tup[0]][tup[1]] != -1:
                        sum += values[tup[0]][tup[1]]
                    else:
                        can_calculate = False
                        break
                if can_calculate:
                    values[r][c] = sum
                    done = False

for r in range(10):
    for c in range(9):
        if values[r][c] != -1:
            print(values[r][c], end="")
        else:
            print("*", end="")
        if c == 8:
            print("")
        else:
            print(" ", end="")
