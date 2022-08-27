def fit(req, ava):
    if req == "M" and ava == "S":
        return False
    elif req == "L" and ava != "L":
        return False
    return True


j = int(input())
a = int(input())

jerseys = [None]
visited = [False] * (j + 1)
counter = 0

for i in range(j):
    jerseys.append(input())

for j in range(a):
    x, y = input().split(" ")
    jn = int(y)

    if not visited[jn] and fit(x, jerseys[jn]):
        counter += 1
        visited[jn] = True
        
print(counter)
