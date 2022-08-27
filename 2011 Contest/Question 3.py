term1 = int(input())
term2 = int(input())

sequence = [term1, term2]
i = 1
count = 2

while sequence[i] <= sequence[i - 1]:
    i += 1
    sequence.append(sequence[i - 2] - sequence[i - 1])
    count += 1

print(sequence)
print(count)

