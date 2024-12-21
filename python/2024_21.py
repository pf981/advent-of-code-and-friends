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

# def smallest_cost(from_pos, to_pos, m, costs):
#     pass

# pad2_start = next(pos for pos, ch in m2.items() if ch == 'A')
# pad1_start = next(pos for pos, ch in m1.items() if ch == 'A')

# costs_me = {ch: 1 for ch in '^>v<'}
# costs1 = 

# import functools

# @functools.cache
# def shortest_path(me_pos, r2_pos, r1_pos, r1_target):
#     pass


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
















# for from_pos in m1:
#     for to_pos in m1:
#         if from_pos != to_pos:
#             paths = shortest_paths(from_pos, to_pos, m1)
#             print(from_pos, to_pos, paths)




# def solve_code(code):
#     pos1 = pad1_start
#     pos2 = pad2_start
#     pos3 = pad2_start
#     for c in code:
#         for path1 in shortest_paths(from_pos, to_pos, m)


# answer1 = 0
# for code in lines:
#     paths1 = shortest_paths(code, m1)
#     paths2 = set()
#     for path in paths1:
#         paths2.update(set())
#     path2 = shortest_path(path, m2)
#     path3 = shortest_path(path2, m2)
#     print(f'{len(path3)} * {int(code[:-1])} = {len(path3) * int(code[:-1])}')
#     answer1 += len(path3) * int(code[:-1])

# print(answer1)

# # submit(answer1, part='a', day=21, year=2024)
















# all_paths('0', m1)

# def all_paths(code, m):
def hash_path(path):
    row = 0
    col = 0
    for direction in path:
        row += (direction == 'v') - (direction == '^')
        col += (direction == '>') - (direction == '<')
    return (row, col)

def shortest_path(code, m):
    start = next(pos for pos, ch in m.items() if ch == 'A')
    # i = 0
    q = collections.deque([(*start, tuple(), 0)]) # r, c, path, i
    seen = {(tuple(), 0)} # r, c, i
    paths = set()
    while q:
        # print(f'{q=} {i=}')
        for _ in range(len(q)):
            r, c, path, i = q.popleft()

            if m[(r, c)] == code[i]:
                path += ('A',)
                i += 1
                if i == len(code): 
                    paths.add(''.join(path))
                    continue
                # print(f'Found! {r,c=} {code[i]=}')
                # q.clear()
                # seen = {(r, c)}
                # path += ('A',)
                # q.append((r, c, path))
                # i += 1
                # if i == len(code):
                #     return ''.join(path)
                # break
            
            for direction in '^>v<':
                r2 = r + (direction == 'v') - (direction == '^')
                c2 = c + (direction == '>') - (direction == '<')
                # i2 = i
                # if m[(r, c)] == code[i]:
                #     i2 += 1
                path2 = path + (direction,)
                sp = sorted(path2)
                if (r2, c2) not in m or (sp, i) in seen:
                    continue
                seen.add((sp, i))

                q.append((r2, c2, path2, i))
    return paths

lines = inp.splitlines()
shortest_path(lines[0], m1)
shortest_path('<A^A^^>AvvvA', m2)

# shortest_path('<A^A^^>AvvvA', m2)
# shortest_path('v<<A>^>A<A>A<AA>vA^Av<AAA^>A', m2)

# 'v<<A>^>A<A>A<AA>vA^Av<AAA^>A' # Me
# '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A.' # Ex

# 'v<A<AA>^>AvA^<A>vA^Av<<A>^>AvA^Av<<A>^>AAvA<A^>A<A>Av<A<A>^>AAA<A>vA^A' # Me
# '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A' # Eg

answer1 = 0
for code in lines:
    path = shortest_path(code, m1)
    path2 = shortest_path(path, m2)
    path3 = shortest_path(path2, m2)
    print(f'{len(path3)} * {int(code[:-1])} = {len(path3) * int(code[:-1])}')
    answer1 += len(path3) * int(code[:-1])

print(answer1)

# submit(answer1, part='a', day=21, year=2024)


# Part 2


# answer2 = 'todo'
# print(answer2)

# submit(answer2, part='b', day=21, year=2024)
