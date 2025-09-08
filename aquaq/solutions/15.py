import collections
import string


def get_path_length(w1: str, w2: str, words: set[str]) -> int:
    q = collections.deque([w1])
    seen = {w1}
    d = 1
    while q:
        for _ in range(len(q)):
            w = q.popleft()

            if w == w2:
                return d

            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    new_w = w[:i] + c + w[i + 1 :]
                    if new_w not in words or new_w in seen:
                        continue
                    seen.add(new_w)
                    q.append(new_w)

        d += 1
    return -1


with open("./input/15.txt") as f:
    text = f.read()

with open("./input/words.txt") as f:
    words = set(f.read().splitlines())

answer = 1
for line in text.splitlines():
    w1, w2 = line.split(",")
    answer *= get_path_length(w1, w2, words)
print(answer)
