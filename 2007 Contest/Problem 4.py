w1 = input("Enter first phrase> ")
w2 = input("Enter second phrase> ")

w1 = w1.replace(" ", "")
w2 = w2.replace(" ", "")

w1 = ''.join(sorted(w1))
w2 = ''.join(sorted(w2))

if w1 == w2:
    print("Is an anagram")
else:
    print("Is not an anagram")



