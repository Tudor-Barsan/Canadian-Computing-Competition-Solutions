sign = str(input())
s = sign.upper()
is_sign = True

for c in s:
    if c == "A" or c == "B" or c == "C" or c == "D" or c == "E" or c == "F" or c == "G" or c == "J" or c == "K" or c == "L" or c == "M" or c == "P" or c == "Q" or c == "R" or c == "T" or c == "U" or c == "V" or c == "W" or c == "Y":
        is_sign = False

if is_sign:
    print("YES")
else:
    print("NO")


