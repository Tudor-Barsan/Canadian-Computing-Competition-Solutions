question = int(input())
citizens = int(input())

d = ([int(x) for x in input().split()])
p = ([int(x) for x in input().split()])

if question == 1:
    d.sort()
    p.sort()
else:
    d.sort()
    p.sort(reverse=True)

speed = 0

for i in range(citizens):
    speed += max(d[i], p[i])

print(speed)