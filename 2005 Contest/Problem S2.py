r, c = [int(a) for a in input().split()]


current_x = 0
current_y = 0

x, y = [int(a) for a in input().split()]

while x != 0 and y != 0:
    current_x += int(x)
    current_y += int(y)
    if current_x > r:
        current_x = r
    if current_x < 0:
        current_x = 0
    if current_y > c:
        current_y = c
    if current_y < 0:
        current_y = 0
    print(f'{current_x} {current_y}')
    x, y = [int(a) for a in input().split()]
