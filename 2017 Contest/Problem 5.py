from collections import Counter

n = int(input())
l = [int(i) for i in input().split()]

cnt = Counter(l)
unique_length = list(cnt.keys())
ull = len(unique_length)
cnt_height = Counter()

for i in range(0, ull):
    for j in range(i, ull):
        h1 = unique_length[i]
        h2 = unique_length[j]
        h = h1 + h2
        if h1 == h2:
            cnt_height[h] += cnt[h1] // 2
        else:
            cnt_height[h] += min(cnt[h1], cnt[h2])

lr = cnt_height.most_common()
maxLength = None
options = 0
for item in lr:
    if maxLength is None:
        maxLength = item[-1]
    elif item[-1] != maxLength:
        break
    options += 1

print(maxLength, options)
