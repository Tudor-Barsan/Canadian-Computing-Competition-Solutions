k = int(input())
l = []

for i in range(k):
    l.append(int(input()))

new_list = []

for i in l:
    if i == 0:
        new_list.pop()
    else:
        new_list.append(i)

my_sum = 0
for i in new_list:
    my_sum += i

print(my_sum)
