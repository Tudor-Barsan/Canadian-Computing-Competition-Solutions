n = int(input())

read_to_freq = {}

for i in range(n):
    r = int(input())
    if r in read_to_freq:
        read_to_freq[r] += 1
    else:
        read_to_freq[r] = 1

counts = list(read_to_freq.values())

counts.sort(reverse=True)

freq_to_read = {}

for r, f in read_to_freq.items():
    if f not in freq_to_read:
        l = [r]
        freq_to_read[f] = l
    else:
        freq_to_read[f].append(r)

list_max_1 = freq_to_read[counts[0]]

if len(list_max_1) > 1:
    list_max_1.sort(reverse=True)
    print(list_max_1[0] - list_max_1[-1])
else:
    list_max_2 = freq_to_read[counts[1]]
    list_max_2.sort()
    diff1 = abs(list_max_1[0] - list_max_2[0])
    diff2 = abs(list_max_1[0] - list_max_2[-1])
    if diff1 > diff2:
        print(diff1)
    else:
        print(diff2)