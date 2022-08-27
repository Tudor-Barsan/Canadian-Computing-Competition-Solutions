n = int(input())
computers = []

for i in range(n):
    line = str(input())
    name, ram, cpu, dds = line.split()
    score = 2 * int(ram) + 3 * int(cpu) + int(dds)
    computers.append((name, score))

computers.sort(key=lambda item: item[0])
computers.sort(reverse=True, key=lambda item: item[1])

print(computers[0][0])
if n > 1:
    print(computers[1][0])



# 4
# ABC 13 22 1
# DEF 10 20 30
# GHI 11 2 2
# JKL 20 20 20