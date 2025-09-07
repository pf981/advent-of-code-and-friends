import itertools

with open("./input/1.txt") as f:
    text = f.read()

li = [c if c in "1234567890abcdef" else "0" for c in text.lower()]
li.append("0" * (3 - (len(li) % 3)))
s = "".join(li)

result: list[str] = []
for batch in itertools.batched(s, len(s) // 3):
    result.extend(batch[:2])

answer = "".join(result)
print(answer)
