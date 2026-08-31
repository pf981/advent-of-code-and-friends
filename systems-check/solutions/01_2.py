import collections

with open("./input/1.txt") as f:
    lines = f.read().splitlines()

deltas = collections.Counter()
for line in lines:
    t, id_, is_disabled = line.split()
    t = int(t[2:])
    id_ = int(id_[1:])
    is_disabled = is_disabled == "disabled"

    if is_disabled:
        deltas[t] += 1
    else:
        deltas[t] -= 1

prev_t = 0
n_disabled = 0
longest = (0, 0)  # (n_disabled, duration)
for t, delta in deltas.items():
    if delta == 0:
        continue
    longest = max(longest, (n_disabled, t - prev_t))
    n_disabled += delta
    prev_t = t


answer = longest[1]
print(answer)
