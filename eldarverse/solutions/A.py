with open("./input/problem-sep-25-long-A-input.txt") as f:
    text = f.read()


n, *names = text.splitlines()
assert int(n) == len(names)

result = []
for i, name in enumerate(names, 1):
    assert 2 <= len(name) <= 15
    assert name[0].isupper()
    assert name[1:].islower()
    discount = 100 - 5 * len(set(name.lower()))
    result.append(f"Case #{i}: {discount}")

with open("./output/A.txt", "w") as f:
    f.write("\n".join(result))
