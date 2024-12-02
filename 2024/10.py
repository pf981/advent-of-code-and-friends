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
        

def get_candidates(grid: list[str]) -> list[set] | None:
    candidates = [set() for _ in range(16)]

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

answer3 = 0
# i=0
for grid in grids:
    word = get_word(grid)
    # print(f'{i} {word} {get_power(word) if word else 0}')
    # i+=1
    if word:
        answer3 += get_power(word)
print(answer3)

# 211408
# Your answer length is: correct
# The first character of your answer is: correct

# 211801
# That's not the right answer...

# Your answer length is: correct
# The first character of your answer is: correct


# get_word(grids[-1])
# grids[-1]
# # ['**PVTN**',
# #  '**SJQH**',
# #  'RW....PB',
# #  'TS....GY',
# #  'VL....XS',
# #  'BH....?Z',
# #  '**T?XP**',
# #  '**RYJW**']

# get_power('LWGVXSHBPJQKNFZM')
# get_power('DQWLXCNHVKJTGFSZ')

grids[21]
# ['**JRVG**',
#  '**NZMD**',
#  'TP....TX',
#  'VJ....?L',
#  'GC....YW',
#  'RL....CS',
#  '**HTZK**',
#  '**XJLG**']

grids[22]
# ['** WMRS **',
#  '** JPBF **',

#  'TX .... M?',
#  '?L .... HK',
#  'YW W... JY',
#  'CS W... WX',

#  '** NLPR **',
#  '** WJQH **']


grids[23]
# ['** KRBG **',
#  '** TDZM **',

#  'M? .... QN',
#  'HK .... K?',
#  'JY .... PJ',
#  'WX .... TY',

#  '** HJVC **',
#  '** RSMB **']


grids[181]
# ['** SDRC **',
#  '** G?TY **',

#  'JK .... MD',
#  'NX .... WT',
#  'VW .... RG',
#  'TH .... HP',

#  '** SYMD **',
#  '** Q?PX **']

# "There cannot be two identical symbols in the runic word."

# NOTE: The issue is that each ? maps to EXACTLY one symbol. So tiles which share a ? must have that ? be the same character