s1 = input()
s2 = input()
s3 = input()

l = []

code = {}

for i in range(len(s1)):
    code[s2[i]] = s1[i]

for c in s3:
    if c in code:
        l.append(code[c])
    else:
        l.append(".")

result = "".join(l)

print(result)