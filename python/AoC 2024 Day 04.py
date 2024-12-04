from aocd import get_data, submit
import collections


inp = get_data(day=4, year=2024)

# inp = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# '''
inp = '''.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........'''

lines = inp.splitlines()

m = collections.defaultdict(str)
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        m[(row, col)] = c


answer1 = 0
for r, c in m.copy():
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if (m[(r, c)] == 'X' and
            m[(r + dr, c + dc)] == 'M' and
            m[(r + 2*dr, c + 2*dc)] == 'A' and 
            m[(r + 3*dr, c + 3*dc)] == 'S'):
            answer1 += 1

print(answer1)


# submit(answer1, part='a', day=4, year=2024)


# Part 2
m = collections.defaultdict(str)
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        m[(row, col)] = c

answer2 = 0
for r, c in m.copy():
    if (m[(r, c)] == 'A' and (
        sorted(m[(r -1, c - 1)] + m[(r + 1, c + 1)]) == ['M', 'S'] and 
        sorted(m[(r +1, c - 1)] + m[(r - 1, c + 1)]) == ['M', 'S']
        )):
        answer2 += 1

print(answer2)


submit(answer2, part='b', day=4, year=2024)
