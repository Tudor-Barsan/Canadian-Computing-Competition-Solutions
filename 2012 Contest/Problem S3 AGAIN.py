import collections

n = int(input())
readings = []

for j in range(n):
    readings.append(int(input()))

frequency = (collections.Counter(readings).most_common())

if frequency[0][1] != frequency [len(frequency) - 1][1]:
    i = 0
    maxes = []
    maxes.append(frequency[0][0])
    while frequency[i][1] == frequency[i + 1][1]:
        maxes.append(frequency[i + 1][0])
        i += 1
        if i == len(frequency) - 1:
            break

    high = max(maxes)

    i += 1
    mins = []
    mins.append(frequency[i][0])
    while frequency[i][1] == frequency[i + 1][1]:
        mins.append(frequency[i + 1][0])
        i += 1
        if i == len(frequency) - 1:
            break

    low = min(mins)

    print(high - low)

else:
    l = []
    for i in range(len(frequency)):
        l.append(frequency[i][0])
    print(max(l) - min(l))




