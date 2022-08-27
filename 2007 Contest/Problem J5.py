def count_path(i):
    global hotels, a, b
    if i == len(hotels) - 1:
        return 1
    elif i in cache:
        return cache[i]
    sum = 0
    for j in range(i + 1, len(hotels)):
        dist = hotels[j] - hotels[i]
        if a <= dist <= b:
            sum += count_path(j)
        elif dist > b:
            break
    cache[i] = sum
    return sum


hotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

a = int(input())
b = int(input())
n = int(input())

cache = {}

for i in range(n):
    hotels.append(int(input()))

hotels.sort()

print(count_path(0))
