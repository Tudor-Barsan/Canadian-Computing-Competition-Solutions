
def translate(char, shift):
    new_char = (ord(char) + 26 - shift) % 91
    if new_char < 65 or new_char > 91:
        new_char += 65
    return chr(new_char)


k = int(input())
word = (input())

letters = []
i = 1

for c in word:
    shift = 3 * i + k
    letters.append(translate(c, shift))
    i += 1


new_word = "".join(letters)
print(new_word)

