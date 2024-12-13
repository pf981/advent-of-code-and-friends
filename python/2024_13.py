from aocd import get_data, submit
import z3
import re

inp = get_data(day=13, year=2024)

# inp = '''Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400\n\nButton A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176\n\nButton A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450\n\nButton A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# '''

# lines = inp.splitlines()

games = []
for txt in inp.split('\n\n'):
    # print(txt)
    games.append([int(x) for x in re.findall(r'\d+', txt)])
# print(games)

answer1 = 0
for ax, ay, bx, by, px, py in games:
    o = z3.Optimize()
    tokens_a = z3.Int(f'tokens_a')
    tokens_b = z3.Int(f'tokens_b')
    tokens = z3.Int(f'tokens')

    o.add(tokens == 3*tokens_a + tokens_b)
    o.add(px == tokens_a*ax + tokens_b*bx)
    o.add(py == tokens_a*ay + tokens_b*by)


    o.minimize(tokens)

    a = o.check()
    try:
        result = o.model()[tokens].as_long()
        # print(result)
        answer1 += result
    except:
        pass

# answer1 = 'todo'
print(answer1)

submit(answer1, part='a', day=13, year=2024)


# Part 2


answer1 = 0
for ax, ay, bx, by, px, py in games:
    o = z3.Optimize()
    tokens_a = z3.Int(f'tokens_a')
    tokens_b = z3.Int(f'tokens_b')
    tokens = z3.Int(f'tokens')

    o.add(tokens == 3*tokens_a + tokens_b)
    o.add(10000000000000+px == tokens_a*ax + tokens_b*bx)
    o.add(10000000000000+py == tokens_a*ay + tokens_b*by)


    o.minimize(tokens)

    a = o.check()
    try:
        result = o.model()[tokens].as_long()
        # print(result)
        answer1 += result
    except:
        pass

# answer1 = 'todo'
print(answer1)


submit(answer1, part='b', day=13, year=2024)
