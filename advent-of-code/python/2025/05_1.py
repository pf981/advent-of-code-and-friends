from aocd import get_data, submit


inp = get_data(day=5, year=2025)
# inp = '''
# '''

rngs_str, ings = inp.split("\n\n")
ings = [int(x) for x in ings.splitlines()]
fresh = set()
for line in rngs_str.splitlines():
    a, b = line.split("-")
    # s = set(range(int(a), int(b)))
    s = range(int(a), int(b))
    for ing in ings:
        if ing in s:
            fresh.add(ing)


answer1 = len(fresh)
print(answer1)
# submit(answer1, part="a", day=5, year=2025)
