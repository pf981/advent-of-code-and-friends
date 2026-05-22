import collections
import itertools

with open("./data/0098_words.txt") as f:
    words = f.read().replace('"', "").split(",")

m = collections.defaultdict(list)
for word in words:
    m["".join(sorted(word))].append(word)

candidates = [word for word in m if len(m[word]) > 1]
longest_candidate = max(len(word) for word in candidates)

squares = collections.defaultdict(list)  # n_digits -> [square, ...]
for i in itertools.count(1):
    square = i * i
    n_digits = len(str(square))
    if n_digits > longest_candidate:
        break

    squares[n_digits].append(square)

answer = 0
for candidate in candidates:
    n = len(m[candidate])
    for i in range(n):
        for j in range(i + 1, n):
            w1 = m[candidate][i]
            w2 = m[candidate][j]

            for square1 in squares[len(w1)]:
                mapping = {}
                used = set()
                for c, digit in zip(w1, str(square1)):
                    if c in mapping:
                        if mapping[c] != digit:
                            break
                    else:
                        if digit in used:
                            break
                        used.add(digit)
                        mapping[c] = digit
                else:
                    square2 = int("".join(mapping[c] for c in w2))
                    if square2 in squares[len(w1)]:
                        answer = max(answer, square1, square2)

print(answer)
