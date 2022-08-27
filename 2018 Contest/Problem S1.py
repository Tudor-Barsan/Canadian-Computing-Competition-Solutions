def village_length(village, before, after):
    minimum = before + float((village - before) / 2)
    maximum = village + float((after - village) / 2)
    length = maximum - minimum
    return length


n = int(input())
villages = []

for i in range(n):
    villages.append(int(input()))

villages.sort()

lengths = []

for i in range(1, len(villages) - 1):
    lengths.append(village_length(villages[i], villages[i - 1], villages[i + 1]))


lengths.sort()

print(lengths[0])
