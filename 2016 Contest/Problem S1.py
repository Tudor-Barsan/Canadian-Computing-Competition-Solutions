from collections import Counter

word1 = input()
word2 = input()

if len(word1) != len(word2):
    print("N")

else:
    c1 = Counter(word1)
    c2 = Counter(word2)
    star_count = c2["*"]

    is_ok = True

    for t1 in c1.items():
        letter = t1[0]
        count1 = t1[1]
        count2 = c2[letter]

        if count2 > count1:
            is_ok = False
            break

        elif count2 < count1:
            star_count -= (count1 - count2)
            if star_count < 0:
                is_ok = False
                break

    if is_ok:
        print("A")
    else:
        print("N")