from aocd import get_data, submit
import functools


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
        
        shortest_sublength = min(get_shortest_length(path, depth + 1, max_depth) for path in paths)
        shortest_length += shortest_sublength
        from_pos = to_pos

    return shortest_length


inp = get_data(day=21, year=2024)
lines = inp.splitlines()

answer1 = 0
for code in lines:
    shortest_length = get_shortest_length(code, 0, 2)
    answer1 += shortest_length * int(code[:-1])
print(answer1)

submit(answer1, part='a', day=21, year=2024)


# Part 2


answer2 = 0
for code in lines:
    shortest_length = get_shortest_length(code, 0, 25)
    answer2 += shortest_length * int(code[:-1])
print(answer2)

submit(answer2, part='b', day=21, year=2024)
