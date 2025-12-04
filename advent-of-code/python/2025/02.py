from aocd import get_data, submit


inp = get_data(day=2, year=2025)

intervals = [[int(x) for x in s.split("-")] for s in inp.split(",")]

answer1 = 0
for num in range(100_000):
    invalid = int(str(num) * 2)
    answer1 += sum(invalid for a, b in intervals if a <= invalid <= b)

submit(answer1, part="a", day=2, year=2025)


# Part 2


answer2 = 0
seen = set()
for num in range(100_000):
    for n in range(2, 10):
        invalid = int(str(num) * n)

        if invalid in seen:
            continue
        seen.add(invalid)

        answer2 += sum(invalid for a, b in intervals if a <= invalid <= b)

submit(answer2, part="b", day=2, year=2025)
