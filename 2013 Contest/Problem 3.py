def is_good_year(year):
    y = str(year)
    set1 = set(y)
    if len(set1) != len(y):
        return False
    return True


year = int(input()) + 1


while not is_good_year(year):
    year += 1

print(year)
