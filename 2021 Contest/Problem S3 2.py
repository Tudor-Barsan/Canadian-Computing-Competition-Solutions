n = int(input())
people = []

points = set()
speed_delta = {}
for i in range(n):
    p, w, d = [int(a) for a in input().split()] #(p, w, d)
    tup = (p, w, d)
    people.append(tup)
    strt = p - d
    stop = p + d
    if strt in speed_delta:
        speed_delta[strt] += w
    else:
        speed_delta[strt] = w
    if stop in speed_delta:
        speed_delta[stop] += w
    else:
        speed_delta[stop] = w
    points.add(strt)
    points.add(stop)

total = 0
sorted_points = sorted(points)
c = sorted_points[0] - 1  #just a point before

delta = 0
for p, w, d in people:
    total += ((p - c) - d) * w
    delta -= w
best = total

prev_c = c
for c in sorted_points:
    if prev_c in speed_delta:
        delta += speed_delta[prev_c]
    total += delta * (c - prev_c)
    prev_c = c

    if total < best:
        best = total

print(best)