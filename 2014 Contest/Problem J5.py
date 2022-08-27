n = int(input())
one = (input().split())
two = (input().split())

good = True
for name in one:
    check = (name, two[one.index(name)])
    if check[0] == check[1]:
        good = False
    if check[1] in two:
        temp = check[1]
        ind = one.index(temp)
        if two[ind] != name:
            good = False
            break

if good:
    print("good")
else:
    print("bad")



