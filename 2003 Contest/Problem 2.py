def find_dimensions(c):
    minp = 4*c
    for i in range(1, c//2):
        if c % i == 0:
            j = c//i
            p = 2*(i + j)
            if p < minp:
                minp = p
                d1 = i
                d2 = j
    return minp, d1, d2


c = int(input("Enter number of pictures: "))

while c > 0:
    p, length, width = find_dimensions(c)
    print(f"Minimum perimeter is {p} with dimensions {length} x {width}")
    c = int(input("Enter number of pictures: "))
