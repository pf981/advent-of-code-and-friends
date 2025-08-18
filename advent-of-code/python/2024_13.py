from aocd import get_data, submit
import re
import z3


def get_min_tokens(ax, ay, bx, by, px, py, is_part2):
    if is_part2:
        px += 10000000000000
        py += 10000000000000

    o = z3.Optimize()
    tokens_a = z3.Int(f'tokens_a')
    tokens_b = z3.Int(f'tokens_b')
    tokens = z3.Int(f'tokens')

    o.add(tokens == 3 * tokens_a + tokens_b)
    o.add(px == tokens_a * ax + tokens_b * bx)
    o.add(py == tokens_a * ay + tokens_b * by)

    o.minimize(tokens)

    return o.model()[tokens].as_long() if o.check() == z3.sat else 0


inp = get_data(day=13, year=2024)

games = []
for txt in inp.split('\n\n'):
    games.append([int(x) for x in re.findall(r'\d+', txt)])

answer1 = sum(get_min_tokens(*game, False) for game in games)
print(answer1)

submit(answer1, part='a', day=13, year=2024)


# Part 2


answer2 = sum(get_min_tokens(*game, True) for game in games)
print(answer2)

submit(answer2, part='b', day=13, year=2024)
