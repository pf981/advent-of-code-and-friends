import collections
import random
import math

FLOOR = math.log(1e-8)

# curl https://calmcode.io/static/data/english_3grams.csv -o input/english_3grams.csv
with open("input/english_3grams.csv") as f:
    trigrams = f.read()

freqs_target = collections.defaultdict(float)
for line in trigrams.splitlines()[1:]:
    tri, count = line.split(",")
    freqs_target[tri] += int(count)

total_target = sum(freqs_target.values())
for tri in freqs_target:
    freqs_target[tri] = math.log(freqs_target[tri] / total_target)


def get_score(s: str) -> float:
    score = 0.0
    for word in s.lower().split():
        word = "".join(c for c in word if c.isalpha())
        for c1, c2, c3 in zip(word[:-2], word[1:-1], word[2:]):
            tri = c1 + c2 + c3
            score += freqs_target.get(tri, FLOOR)
    return score


def substitute(cipher: str, alphabet: list[str]) -> str:
    m = {a: b for a, b in zip(alphabet, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    result = []
    for c in cipher:
        if not c.isalpha():
            result.append(c)
            continue

        c2 = m[c.upper()]

        if c.islower():
            c2 = c2.lower()
        result.append(c2)

    return "".join(result)


def hill_climb(cipher: str, n_iters: int = 10_000) -> tuple[float, str, str]:
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)

    best = (float("-inf"), "", "")  # score, alphabet, decrypted
    for _ in range(n_iters):
        i, j = random.sample(range(len(alphabet)), 2)
        alphabet[i], alphabet[j] = alphabet[j], alphabet[i]
        decrypted = substitute(cipher, alphabet)
        score = get_score(decrypted)

        if score > best[0]:
            print(f"{score=} {decrypted=}")

            best = (score, "".join(alphabet), decrypted)
        else:
            alphabet[i], alphabet[j] = alphabet[j], alphabet[i]

    return best


with open("./input/problem-decryption-contest-1-C-input.txt") as f:
    text = f.read()

parts = "\n".join(text.splitlines()[1:]).split(
    "==================================================================\n"
)

# As this uses random, it's not guaranteed to get the right answer.
# However, it does get the right answer most the time.
result = []
for i, part in enumerate(parts, 1):
    _, alphabet, _ = hill_climb(part)
    result.append(f"Case #{i}: {alphabet}")


with open("./output/problem-decryption-contest-1-C.txt", "w") as f:
    f.write("\n".join(result))
