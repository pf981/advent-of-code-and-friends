from aocd import get_data, submit


def count_energized(start_pos, start_dir, m):
    movements = {
        '.^': '^',
        '.>': '>',
        '.v': 'v',
        '.<': '<',
        '|^': '^',
        '|>': 'v^',
        '|v': 'v',
        '|<': 'v^',
        '-^': '<>',
        '->': '>',
        '-v': '<>',
        '-<': '<',
        '/^': '>',
        '/>': '^',
        '/v': '<',
        '/<': 'v',
        '\\^': '<',
        '\\>': 'v',
        '\\v': '>',
        '\\<': '^'
    }

    seen = set() # pos, direction
    stack = [(start_pos, start_dir)]
    while stack:
        pos, direction = stack.pop()

        if pos not in m:
            continue

        if (pos, direction) in seen:
            continue
        seen.add((pos, direction))

        for new_direction in movements[m[pos] + direction]:
            stack.append(((pos[0] + (new_direction == 'v') - (new_direction == '^'), pos[1] + (new_direction == '>') - (new_direction == '<')), new_direction))

    return len({pos for pos, _ in seen}) 


inp = get_data(day=16, year=2023)
lines = inp.splitlines()
m = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
answer1 = count_energized((0, 0), '>', m)
print(answer1)

submit(answer1, part='a', day=16, year=2023)


# Part 2

best = 0
n_rows = len(lines)
n_cols = len(lines[0])

for col in range(n_cols):
    best = max(count_energized((0, col), 'v', m), best)
    best = max(count_energized((n_rows-1, col), '^', m), best)
    
for row in range(n_rows):
    best = max(count_energized((row, 0), '>', m), best)
    best = max(count_energized((row, n_cols - 1), '^', m), best)

answer2 = best
print(answer2)

submit(answer2, part='b', day=16, year=2023)
