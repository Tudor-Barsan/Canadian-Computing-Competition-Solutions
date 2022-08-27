y = int(input())
is_distinct = False

while not is_distinct:
    y += 1
    y = str(y)
    characters = list(y)
    if len(characters) == len(set(characters)):
        is_distinct = True
    else:
        y = int(y)

print(y)
