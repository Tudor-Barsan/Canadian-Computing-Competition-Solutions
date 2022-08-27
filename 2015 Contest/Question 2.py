text = str(input())
length = len(text)
count_h = 0
count_s = 0

for i in range(0, length - 2):
    word = text[i: i + 3]
    # print(word)
    if word == ":-)":
        count_h += 1

    elif word == ":-(":
        count_s += 1

# print(f"count_h={count_h}  count_s={count_s}")

if count_h == 0 and count_s == 0:
    print("none")

elif count_h == count_s:
    print("unsure")

elif count_h > count_s:
    print("happy")

else:
    print("sad")