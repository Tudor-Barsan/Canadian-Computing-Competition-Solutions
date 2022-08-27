n = int(input())
l = []

for i in range(2 * n):
    l.append(input())

question = 0
answer = n
correct_answers = 0

for i in l:
    if question >= n:
        break
    if i == l[answer]:
        correct_answers += 1
    question += 1
    answer += 1

print(correct_answers)