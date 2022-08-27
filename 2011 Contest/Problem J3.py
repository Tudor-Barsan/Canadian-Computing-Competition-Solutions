t1 = int(input())
t2 = int(input())
sequence = list()

sequence.append(t1)
sequence.append(t2)

is_terminated = False

while not is_terminated:
    next_term = sequence[-2] - sequence[-1]
    sequence.append(next_term)
    if sequence[-1] > sequence[-2]:
        is_terminated = True

print(len(sequence))
