from aocd import get_data, submit


def simulate(lines: list[list[str]], start: tuple[int]) -> set[tuple[int]] | None:
    seen_states = set()
    seen_positions = set()
    r, c  = start
    direction = 'N'
    while 0 <= r < nrows and 0 <= c < ncols:
        seen_positions.add((r, c))

        if (r, c, direction) in seen_states:
            return None
        seen_states.add((r, c, direction))

        while True:
            r2 = r + (direction == 'S') - (direction == 'N')
            c2 = c + (direction == 'E') - (direction == 'W')

            if not (0 <= r2 < nrows) or not ( 0 <= c2 < ncols):
                break
            if lines[r2][c2] != '#':
                break
            direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]

        r = r2
        c = c2
    return seen_positions


inp = get_data(day=6, year=2024)
lines = [list(line) for line in inp.splitlines()]
nrows = len(lines)
ncols = len(lines[0])

start = next((r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == '^')
positions = simulate(lines, start)

answer1 = len(positions)
print(answer1)

submit(answer1, part='a', day=6, year=2024)


# Part 2


answer2 = 0
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] != '.' or (r, c) not in positions:
            continue
        lines[r][c] = '#'
        if not simulate(lines, start):
            answer2 += 1
        lines[r][c] = '.'
print(answer2)

submit(answer2, part='b', day=6, year=2024)
