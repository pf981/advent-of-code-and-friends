with open("./input/1.txt") as f:
    lines = f.read().splitlines()

last_disabled = {}
answer = 0
for line in lines:
    t, id_, is_disabled = line.split()
    t = int(t[2:])
    id_ = int(id_[1:])
    is_disabled = is_disabled == "disabled"

    if is_disabled:
        last_disabled[id_] = t
    elif id_ in last_disabled:
        answer = max(answer, t - last_disabled[id_])

print(answer)
