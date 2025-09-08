import collections

with open("./input/7.txt") as f:
    text = f.read()

elo: collections.defaultdict[str, float] = collections.defaultdict(lambda: 1200.0)

for line in text.splitlines()[1:]:
    a, b, score = line.split(",")
    score_a, score_b = (int(num) for num in score.split("-"))

    if score_b > score_a:
        a, b = b, a

    e_a = 1 / (1 + 10 ** ((elo[b] - elo[a]) / 400))
    delta = 20 * (1 - e_a)
    elo[a] += delta
    elo[b] -= delta


answer = int(max(elo.values())) - int(min(elo.values()))
print(answer)
