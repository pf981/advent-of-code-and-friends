from aocd import get_data, submit


inp = get_data(day=7, year=2025)
lines = inp.splitlines()

beams = {lines[0].index("S")}
answer1 = 0
for line in lines[1:]:
    new_beams = beams.copy()
    for i in beams:
        if line[i] != "^":
            continue

        new_beams.add(i - 1)
        new_beams.add(i + 1)
        new_beams.remove(i)
        answer1 += 1

    beams = new_beams

submit(answer1, part="a", day=7, year=2025)
