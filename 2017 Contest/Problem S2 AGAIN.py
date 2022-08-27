n = int(input())
numbers = [int(x) for x in input().split()]

numbers.sort()
new_list = []

pointer_1 = len(numbers) // 2 - 1
pointer_2 = len(numbers) // 2
if n % 2 != 0:
    pointer_1 += 1
    pointer_2 += 1

while pointer_2 != len(numbers):
    new_list.append(numbers[pointer_1])
    new_list.append(numbers[pointer_2])
    pointer_1 -= 1
    pointer_2 += 1

if n % 2 != 0:
    new_list.append(numbers[0])

if n == 1:
    print(str(new_list[len(numbers) // 2 - 1]))
else:
    for i in range(len(new_list)):
        if i == len(new_list) - 1:
            print(f"{new_list[i]}")
        else:
            print(f"{new_list[i]} ", end="")