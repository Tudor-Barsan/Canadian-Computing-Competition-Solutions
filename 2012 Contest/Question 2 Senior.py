def RomanToValue(r):
    if r == "I":
        return 1
    elif r == "V":
        return 5
    elif r == "X":
        return 10
    elif r == "L":
        return 50
    elif r == "C":
        return 100
    elif r == "D":
        return 500
    elif r == "M":
        return 1000
    else:
        return 0


number = input()

arabic = number[:: 2]
roman = number[1::2]
sum = 0

for i in range(0, len(arabic)):
    term = int(arabic[i]) * RomanToValue(roman[i])
    if i < len(arabic) - 1 and RomanToValue(roman[i]) < RomanToValue(roman[i + 1]):
        sum -= term
    else:
        sum += term

print(sum)