def rle(word) -> int:
    best = 1
    for i in range(len(word)):
        for w in range(1, len(word) - i):
            repeats = 1
            first = word[i : i + w]
            while True:
                start = i + w * repeats
                if word[start : start + w] != first:
                    break
                repeats += 1
            best = max(best, repeats)

    return best


with open("./input/13.txt") as f:
    text = f.read()

answer = sum(rle(word) for word in text.splitlines())
print(answer)
