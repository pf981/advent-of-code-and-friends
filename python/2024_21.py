from aocd import get_data, submit
import collections

inp = get_data(day=21, year=2024)

# inp = '''029A
# 980A
# 179A
# 456A
# 379A
# '''



keypad1 = '''789
456
123
 0A
'''

m1 = {}
for r, line in enumerate(keypad1.splitlines()):
    for c, ch in enumerate(line):
        if ch != ' ':
            m1[(r, c)] = ch

keypad2 = ''' ^A
<v>
'''

m2 = {}
for r, line in enumerate(keypad2.splitlines()):
    for c, ch in enumerate(line):
        if ch != ' ':
            m2[(r, c)] = ch


def shortest_paths(from_pos, to_pos, m):
    row_dir = 'v' if from_pos[0] < to_pos[0] else '^'
    col_dir = '>' if from_pos[1] < to_pos[1] else '<'

    row_sym = row_dir * abs(from_pos[0] - to_pos[0])
    col_sym = col_dir * abs(from_pos[1] - to_pos[1])

    paths = []
    for candidate in [row_sym + col_sym, col_sym + row_sym]:
        r, c = from_pos
        for direction in candidate:
            r += (direction == 'v') - (direction == '^')
            c += (direction == '>') - (direction == '<')
            if (r, c) not in m:
                break
        else:
            paths.append(candidate + 'A')
    return paths

import itertools

def shortest_paths_code(code, m, start):
    from_pos = start
    m_rev = {ch: pos for pos, ch in m.items()}
    all_paths = []
    for ch in code:
        to_pos = m_rev[ch]
        paths = shortest_paths(from_pos, to_pos, m)
        all_paths.append(paths)
        from_pos = to_pos
    # return all_paths
    return set(''.join(p) for p in itertools.product(*all_paths))

pad2_start = next(pos for pos, ch in m2.items() if ch == 'A')
pad1_start = next(pos for pos, ch in m1.items() if ch == 'A')





lines = inp.splitlines()

answer1 = 0
for code in lines:
    paths1 = shortest_paths_code(code, m1, pad1_start)
    paths2 = set()
    for path1 in paths1:
        paths2.update(shortest_paths_code(path1, m2, pad2_start))

    # Test
    paths2 = list(paths2)[:5]
    paths3 = set()
    for path2 in paths2:
        paths3.update(shortest_paths_code(path2, m2, pad2_start))

    best_len = min(len(path) for path in paths3)
    print(f'{best_len=} {int(code[:-1])=}')
    answer1 += best_len * int(code[:-1])

print(answer1)

# submit(answer1, part='a', day=21, year=2024)










##################################################################
##################################################################
##################################################################
##################################################################
# Part 2


from aocd import get_data, submit
import collections

inp = get_data(day=21, year=2024)

# inp = '''029A
# 980A
# 179A
# 456A
# 379A
# '''



keypad1 = '''789
456
123
 0A
'''

m1 = {}
for r, line in enumerate(keypad1.splitlines()):
    for c, ch in enumerate(line):
        if ch != ' ':
            m1[(r, c)] = ch

keypad2 = ''' ^A
<v>
'''

m2 = {}
for r, line in enumerate(keypad2.splitlines()):
    for c, ch in enumerate(line):
        if ch != ' ':
            m2[(r, c)] = ch



pad2_start = next(pos for pos, ch in m2.items() if ch == 'A')
pad1_start = next(pos for pos, ch in m1.items() if ch == 'A')

lines = inp.splitlines()




def get_paths(from_pos, to_pos, m):
    row_dir = 'v' if from_pos[0] < to_pos[0] else '^'
    col_dir = '>' if from_pos[1] < to_pos[1] else '<'

    row_sym = row_dir * abs(from_pos[0] - to_pos[0])
    col_sym = col_dir * abs(from_pos[1] - to_pos[1])

    paths = []
    for candidate in [row_sym + col_sym, col_sym + row_sym]:
        r, c = from_pos
        for direction in candidate:
            r += (direction == 'v') - (direction == '^')
            c += (direction == '>') - (direction == '<')
            if (r, c) not in m:
                break
        else:
            paths.append(candidate + 'A')
    return paths



import functools

@functools.cache
def get_shortest_length(code, depth, max_depth):
   
    from_pos = pad1_start if depth == 0 else pad2_start
    m = m1 if depth == 0 else m2
    m_rev = {ch: pos for pos, ch in m.items()}

    shortest_length = 0
    for ch in code:
        to_pos = m_rev[ch]
        paths = get_paths(from_pos, to_pos, m)

        if depth == max_depth:
            shortest_length += min(len(path) for path in paths)
            from_pos = to_pos
            continue
        
        shortest_sublength = float('inf')
        for path in paths:
            shortest_sublength = min(shortest_sublength, get_shortest_length(path, depth + 1, max_depth))
        shortest_length += shortest_sublength

        from_pos = to_pos


    
    return shortest_length

# get_shortest_length('029A', 0, 2)

answer1 = 0
for code in lines:
    shortest_length = get_shortest_length(code, 0, 2)
    answer1 += shortest_length * int(code[:-1])

print(answer1)

# submit(answer1, part='a', day=21, year=2024)


answer2 = 0
for code in lines:
    shortest_length = get_shortest_length(code, 0, 25)
    answer2 += shortest_length * int(code[:-1])

print(answer2)

submit(answer2, part='b', day=21, year=2024)
