from aocd import get_data, submit


inp = get_data(day=5, year=2025)

intervals_str, ingredients_str = inp.split("\n\n")
intervals = [[int(x) for x in line.split("-")] for line in intervals_str.splitlines()]
ingredients = [int(x) for x in ingredients_str.splitlines()]
fresh = set()
for a, b in intervals:
    rng = range(int(a), int(b))
    for ingredient in ingredients:
        if ingredient in rng:
            fresh.add(ingredient)

answer1 = len(fresh)
submit(answer1, part="a", day=5, year=2025)
