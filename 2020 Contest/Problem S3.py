def string_value(ss, s, e):
    sum = 0
    for i in range(s, e):
        sum += char_value(ss[i])
    return sum


def char_value(c):
    return ord(c) - ord("a")


def string_characters(ss, s, e):
    l = [0] * 26
    for i in range(s, e):
        l[char_value(ss[i])] += 1
    return l


n = input()
h = input()

parameter_count = set()

n_value = string_value(n, 0, len(n))
n_characters = string_characters(n, 0, len(n))
old_sum = 0
new_sum = 0
parameter_characters = []

for i in range(0, len(h) - len(n) + 1):
    start = i
    end = i + len(n)

    if i == 0:
        old_sum = new_sum = string_value(h, start, end)
        parameter_characters = string_characters(h, start, end)
    else:
        old_sum = new_sum
        value_before = char_value(h[i - 1])
        value_after = char_value(h[i + len(n) - 1])
        new_sum = old_sum - value_before + value_after
        parameter_characters[value_before] -= 1
        parameter_characters[value_after] += 1
    if new_sum == n_value:
        if parameter_characters == n_characters:
            parameter_count.add(h[start:end])


print(len(parameter_count))

