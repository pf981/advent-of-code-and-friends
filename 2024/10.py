import collections

with open("./2024/input/everybody_codes_e2024_q10_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''**PCBS**
# **RLNW**
# BV....PT
# CR....HZ
# FL....JW
# SG....MN
# **FTZV**
# **GMJH**'''.splitlines()

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


with open("./2024/input/everybody_codes_e2024_q10_p2.txt") as f:
    # lines = f.read().splitlines()
    text = f.read()

# lines = '''**PCBS**
# **RLNW**
# BV....PT
# CR....HZ
# FL....JW
# SG....MN
# **FTZV**
# **GMJH**'''.splitlines()

def get_power(lines):
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

grids = []
for rows in text.split('\n\n'):
    l = []
    for lines in rows.splitlines():
        l.append(lines.split(' '))
    grids.extend(list(zip(*l)))

answer2 = 0
for grid in grids:
    answer2 += get_power(grid)
print(answer2)

# Part 3


with open("./2024/input/everybody_codes_e2024_q10_p3.txt") as f:
    lines = f.read().splitlines()

# lines = '''**XFZB**DCST**
# **LWQK**GQJH**
# ?G....WL....DQ
# BS....H?....CN
# P?....KJ....TV
# NM....Z?....SG
# **NSHM**VKWZ**
# **PJGV**XFNL**
# WQ....?L....YS
# FX....DJ....HV
# ?Y....WM....?J
# TJ....YK....LP
# **XRTK**BMSP**
# **DWZN**GCJV**'''.splitlines()


def get_word_impl(i: int, candidates: list[set[int]], seen: set[int]) -> str | None:
    if i == len(candidates):
        return ''
    
    for candidate in candidates[i]:
        if candidate in seen:
            continue

        seen.add(candidate)
        
        result = get_word_impl(i + 1, candidates, seen)
        if result is not None:
            return candidate + result
        
        seen.remove(candidate)
    
    return None


def get_words_impl(i: int, candidates: list[set[int]], seen: set[int]) -> list[str]:
    if i == len(candidates):
        return ['']
    
    words = []
    for candidate in candidates[i]:
        if candidate in seen:
            continue

        seen.add(candidate)
        
        for result in get_words_impl(i + 1, candidates, seen):
            words.append(candidate + result)
        
        seen.remove(candidate)
    
    return words
        
def get_candidates(grid: list[str]) -> list[set] | None:
    candidates = [set() for _ in range(16)]

    # Check for duplicates
    all_rows = collections.Counter()
    all_cols = collections.Counter()
    for i in range(2, 6):
        for val in [grid[i][0], grid[i][1], grid[i][-1], grid[i][-2]]:
            all_rows[val] += 1
        for val in [grid[0][i], grid[1][i], grid[-1][i], grid[-2][i]]:
            all_cols[val] += 1
    all_rows['?'] = 1
    all_cols['?'] = 1
    # print(f'{all_rows=}')
    # print(f'{all_cols=}')
    if any(count != 1 for count in all_rows.values()) or any(count != 1 for count in all_cols.values()):
        return None
    
    for i in range(16):
        r = (i // 4) + 2
        c = (i % 4) + 2
        row_candidates = {grid[r][0], grid[r][1], grid[r][-1], grid[r][-2]}
        col_candidates = {grid[0][c], grid[1][c], grid[-1][c], grid[-2][c]}

        cur_candidates = (row_candidates & col_candidates) - {'?'}

        if len(cur_candidates) > 1:
            return None

        if len(cur_candidates) == 1:
            candidates[i] = cur_candidates
            continue

        cur_candidates = set()
        if '?' in col_candidates:
            cur_candidates.update(row_candidates)
        if '?' in row_candidates:
            cur_candidates.update(col_candidates)
        cur_candidates.discard('?')

        candidates[i] = cur_candidates

        if not cur_candidates:
            return None
    
    return candidates

# get_candidates(grid)
# get_candidates(grids[3])

def get_word(grid: list[str]) -> str | None:
    candidates = get_candidates(grid)

    if not candidates:
        return None

    return get_word_impl(0, candidates, set())


def get_words(grid: list[str]) -> list[str]:
    candidates = get_candidates(grid)

    if not candidates:
        return []

    return get_words_impl(0, candidates, set())


def get_power(word: str) -> int:
    power = 0
    for i, ch in enumerate(word, 1):
        base = ord(ch) - ord('A') + 1
        power += i * base
    return power


grids = []
for r in range(0, len(lines) - 2, 6):
    for c in range(0, len(lines[0]) - 2, 6):
        grid = []
        for r2 in range(r, r + 8):
            grid.append(lines[r2][c:c + 8])
        grids.append(grid)

# grid_words = [get_words(grid) for grid in grids]
# # print(grid_words)
# for words in grid_words:
#     print(words)

good = 0
missing = 0
for i, grid in enumerate(grids):
    candidates = get_candidates(grid)
    if not candidates:
        continue
    word = get_word_impl(0, candidates, set())
    good += 1
    if not word:
        missing += 1
        print(f'MISSING WORD {i=}')
        # for line in grid:
        #     print(line)
print(good, missing) # 116 2; now it's 114, 0 as required

grids[121]

# ['** VNZ? **',
#  '** TRWY **',

#  'WH .... BV',
#  'FC .... ?G',
#  'XB .... Z?',
#  'LJ .... ?R',

#  '** SBJ? **',
#  '** KCPY **']
get_candidates(grids[121])


answer3 = 0
for grid in grids:
    word = get_word(grid)
    if word:
        answer3 += get_power(word)
print(answer3)

# 2 ys
# ** VNZ? **
# ** TRWY **

# WH ..w. BV
# FC ...y ?G
# XB ..z. Z?
# LJ ...y ?R

# ** SBJ? **
# ** KCPY **

# **LSCY**
# **HBR?**

# ?M....Z?
# JW....?K
# CS....?M
# TX....?N

# **VWY?**
# **FQZK**

# 211408
# Your answer length is: correct
# The first character of your answer is: correct

# 211801
# That's not the right answer...
# Your answer length is: correct
# The first character of your answer is: correct

# 209611
# That's not the right answer...
# Your answer length is: correct
# The first character of your answer is: correct


###########################################

# '**LWQK**'[6]

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
            

with open("./2024/input/everybody_codes_e2024_q10_p3.txt") as f:
    lines = f.read().splitlines()

m = [list(line) for line in lines]

# def complete_grid(r, c, m, word):
#     i = 0
#     for dr in  range(2, 6):
#         for dc in range(2, 6):
#             ch = word[i]
#             i += 1
#             row_candidates = [
#                 m[r + dr][c],
#                 m[r + dr][c + 1],
#                 m[r + dr][c + 6],
#                 m[r + dr][c + 7],
#             ]
#             if ch not in row_candidates:
#                 print(f'{ch=} {row_candidates=}')
#                 m[r + dr][c + row_candidates.index('?')*6] = ch

#             col_candidates = [
#                 m[r][c + dc],
#                 m[r + 1][c + dc],
#                 m[r + 6][c + dc],
#                 m[r + 7][c + dc],
#             ]
#             if ch not in col_candidates:
#                 m[r + col_candidates.index('?')*6][c + dc] = ch
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

for _ in range(10):
    for r in range(0, len(lines) - 2, 6):
        for c in range(0, len(lines[0]) - 2, 6):
            grid = []
            for dr in range(8):
                line = []
                for dc in range(8):
                    line.append(m[r + dr][c + dc])
                grid.append(line)
            # if get_candidates(grid): # Check if valid. This doesn't work well enough...
            #     solve(r, c, m)
            # word = get_word(grid)
            # if word:
            #     complete_grid(r, c, m, word)
            # print(word)
            solve(r, c, m)
            complete_grid(r, c, m)

        # grid = []
        # for r2 in range(r, r + 8):
        #     grid.append(lines[r2][c:c + 8])
        # grids.append(grid)


# for line in grid:
#     print(''.join(line))
import copy
# grid2 = copy.deepcopy(grid)
m = grid
solve(0, 0, m)
# ** GZHX **
# ** SLKF **

# F? NRHF HN
# PQ SQPX X?
# W? GLWJ GL
# ?C CZKB TZ

# ** NRWB **
# ** CQPJ **

for line in m:
    print(''.join(line))

answer3 = 0
for r in range(0, len(lines) - 2, 6):
    for c in range(0, len(lines[0]) - 2, 6):
        word = ''.join(m[r + dr][c + dc] for dr in  range(2, 6) for dc in range(2, 6))
        if '.' not in word:
            answer3 += get_power(word)
print(answer3)

# 150183
# Your answer length is: correct
# The first character of your answer is: incorrect
# (so must be between 200,000 and 999,999)
# solve(0, 6*3, m)
# m[0][6*3]

# grids[3]

# I think the current issue is that it isn't skipping the bad ones. It is doing them and filling in the question marks when it shouldn't
# It probably has duplicates
# Oh, actually - my solve function didn't populate the question marks...