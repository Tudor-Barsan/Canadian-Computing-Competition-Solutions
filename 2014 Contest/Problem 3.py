rounds = int(input())
scorea = 100
scoreb = 100


for r in range(0, rounds):
    sa, sd = input().split()
    a = int(sa)
    b = int(sd)
    if a < b:
        scorea -= b
    elif a > b:
        scoreb -= a

print(scorea)
print(scoreb)