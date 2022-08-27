import math


def is_prime(number):
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number) + 1), 2):
        if number % i == 0:
            return False

    return True


t = int(input())
cases = []
for i in range(t):
    cases.append(int(input()))

for case in cases:
    a = case
    b = case
    if case % 2 == 0:
        a += 1
        b -= 1

    while not is_prime(a) or not is_prime(b):
        a += 2
        b -= 2
    print(f"{a} {b}")
