t = input()
s = input()

is_cycle_shift = False

for c in s:
    s = s[1:] + s[0]
    if s in t:
        is_cycle_shift = True
        break

if is_cycle_shift:
    print("yes")
else:
    print("no")


