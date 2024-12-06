import collections


with open("./2024/input/everybody_codes_e2024_q10_p1.txt") as f:
    lines = f.read().splitlines()

positions = collections.defaultdict(lambda: [None, None]) # c -> [r, c]

for i in range(2, 6):
    positions[lines[0][i]][1] = i
    positions[lines[1][i]][1] = i
    positions[lines[-1][i]][1] = i
    positions[lines[-2][i]][1] = i
    
    positions[lines[i][0]][0] = i
    positions[lines[i][1]][0] = i
    positions[lines[i][-1]][0] = i
    positions[lines[i][-2]][0] = i

positions = {tuple(pos): ch for ch, pos in positions.items()}
result = ''
for r in range(2, 6):
    for c in range(2, 6):
        result += positions[(r, c)]

answer1 = result
print(answer1)


# Part 2


def p2_get_power(lines):
    positions = collections.defaultdict(lambda: [None, None]) # c -> [r, c]

    for i in range(2, 6):
        positions[lines[0][i]][1] = i
        positions[lines[1][i]][1] = i
        positions[lines[-1][i]][1] = i
        positions[lines[-2][i]][1] = i
        
        positions[lines[i][0]][0] = i
        positions[lines[i][1]][0] = i
        positions[lines[i][-1]][0] = i
        positions[lines[i][-2]][0] = i

    positions = {tuple(pos): ch for ch, pos in positions.items()}
    result = ''
    for r in range(2, 6):
        for c in range(2, 6):
            result += positions[(r, c)]

    power = 0
    for i, ch in enumerate(result, 1):
        base = ord(ch) - ord('A') + 1
        power += i * base
    return power



with open("./2024/input/everybody_codes_e2024_q10_p2.txt") as f:
    text = f.read()

grids = []
for rows in text.split('\n\n'):
    l = []
    for lines in rows.splitlines():
        l.append(lines.split(' '))
    grids.extend(list(zip(*l)))

answer2 = 0
for grid in grids:
    answer2 += p2_get_power(grid)
print(answer2)


# Part 3


def get_power(word: str) -> int:
    power = 0
    for i, ch in enumerate(word, 1):
        base = ord(ch) - ord('A') + 1
        power += i * base
    return power


def solve(r: int, c: int, m: list[list[str]]) -> None:
    used = set()
    for dr in  range(2, 6):
        for dc in range(2, 6):
            if m[r + dr][c + dc] != '.':
                used.add(m[r + dr][c + dc])
    for _ in range(5):
        for dr in  range(2, 6):
            for dc in range(2, 6):
                if m[r + dr][c + dc] != '.':
                    used.add(m[r + dr][c + dc])
                    continue
                row_candidates = {
                    m[r + dr][c],
                    m[r + dr][c + 1],
                    m[r + dr][c + 6],
                    m[r + dr][c + 7],
                } - used
                col_candidates = {
                    m[r][c + dc],
                    m[r + 1][c + dc],
                    m[r + 6][c + dc],
                    m[r + 7][c + dc],
                } - used
                intersection = (row_candidates & col_candidates) - {'?'}
                if len(intersection) == 1:
                    used.update(intersection)
                    m[r + dr][c + dc] = list(intersection)[0]
                    continue
                
                union = row_candidates | col_candidates
                print(f'{union=}')
                if len(row_candidates) == 1 and len(col_candidates) == 1 and len(union) == 2 and '?' in union:
                    el = list(union - {'?'})[0]
                    m[r + dr][c + dc] = el
                    used.add(el)
            


def complete_grid(r, c, m):
    for dr in  range(2, 6):
        for dc in range(2, 6):
            if m[r + dr][c + dc] == '.':
                return

    i = 0
    for dr in  range(2, 6):
        for dc in range(2, 6):
            ch = m[r + dr][c + dc]
            i += 1
            row_candidates = [
                m[r + dr][c],
                m[r + dr][c + 1],
                m[r + dr][c + 6],
                m[r + dr][c + 7],
            ]
            if ch not in row_candidates:
                print(f'{ch=} {row_candidates=}')
                m[r + dr][c + [0,1,6,7][row_candidates.index('?')]] = ch

            col_candidates = [
                m[r][c + dc],
                m[r + 1][c + dc],
                m[r + 6][c + dc],
                m[r + 7][c + dc],
            ]
            if ch not in col_candidates:
                m[r + [0,1,6,7][col_candidates.index('?')]][c + dc] = ch


with open("./2024/input/everybody_codes_e2024_q10_p3.txt") as f:
    lines = f.read().splitlines()

m = [list(line) for line in lines]

for _ in range(2):
    for r in range(0, len(lines) - 2, 6):
        for c in range(0, len(lines[0]) - 2, 6):
            grid = []
            for dr in range(8):
                line = []
                for dc in range(8):
                    line.append(m[r + dr][c + dc])
                grid.append(line)
            solve(r, c, m)
            complete_grid(r, c, m)

for line in m:
    print(''.join(line))

answer3 = 0
for r in range(0, len(lines) - 2, 6):
    for c in range(0, len(lines[0]) - 2, 6):
        word = ''.join(m[r + dr][c + dc] for dr in  range(2, 6) for dc in range(2, 6))
        if '.' not in word:
            answer3 += get_power(word)
print(answer3)
