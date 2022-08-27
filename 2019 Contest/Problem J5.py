def helper(src, count, moves):
    if count == 0 and src == final:
        return moves

    if count == 0:
        return False

    tag = (src, count)
    if tag in cache:
        return False
    cache.add(tag)

    for ruleNo, (a, b) in enumerate(rules, start=1):
        l = len(a)
        pos = src.find(a)
        while pos != -1:
            trans = src[:pos] + b + src[pos + l:]
            output = helper(trans, count - 1, moves + [(ruleNo, pos, trans)])
            if output:
                return output
            pos = src.find(a, pos + 1)
    return False


rules = []
for i in range(3):
    r = input().split()
    rules.append(r)

steps, initial, final = input().split()
steps = int(steps)

cache = set()

found = helper(initial, steps, [])
for rule1, pos1, trans1 in found:
    print(f"{rule1} {pos1 + 1} {trans1}")
