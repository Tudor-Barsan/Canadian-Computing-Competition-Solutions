def find_primes(n, p_numbers):
    for a1 in p_numbers:
        for b1 in p_numbers:
            if (a1 + b1) / 2 == n:
                print(f"{a1} {b1}")
                return


t = int(input())
l = []
for i in range(t):
    l.append(int(input()))

prime_numbers = []

for num in range(2, 2 * max(l) + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)

for i in l:
    find_primes(i, prime_numbers)
