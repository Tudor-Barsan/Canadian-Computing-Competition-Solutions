t = int(input())
c = int(input())
l = []

for i in range(c):
    l.append(int(input()))

l.sort()
time = 0
chores_done = 0

for i in l:
    time += i
    chores_done += 1
    if time > t:
        chores_done -= 1
        break

print(chores_done)