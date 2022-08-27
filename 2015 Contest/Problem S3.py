g = int(input())
p = int(input())
count = 0

planes = []
gates = [0] * g

for i in range(p):
    planes.append(int(input()) - 1)

for plane in planes:
    if gates[plane] == 0:
        gates[plane] = 1
        count += 1
    else:
        while plane > -1 and gates[plane] > 0:
            gates[plane] += 1
            plane = plane - (gates[plane] - 1)
        if plane < 0:
            break
        else:
            count += 1

print(count)
