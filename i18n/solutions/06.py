with open("./input/06.txt", encoding="utf-8") as f:
    text = f.read()

dictionary, grid = (group.splitlines() for group in text.split("\n\n"))

fixed_dictionary = []
for i, word in enumerate(dictionary):
    if i % 3 == 2:
        word = word.encode("latin-1").decode("utf-8")
    if i % 5 == 4:
        word = word.encode("latin-1").decode("utf-8")
    fixed_dictionary.append(word)

answer = 0
for line in grid:
    line = line.strip()
    i, ch = next((i, ch) for i, ch in enumerate(line) if ch != ".")

    for word_i, word in enumerate(fixed_dictionary, 1):
        if len(word) == len(line) and word[i] == ch:
            answer += word_i
            break
    else:
        raise ValueError(f"Could not find match for {line=}")

print(answer)
