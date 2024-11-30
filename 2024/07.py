import itertools


with open("./2024/input/everybody_codes_e2024_q07_p2.txt") as f:
    lines = f.read().splitlines()

track = '''S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-'''.splitlines()

# # FIXME: Remove
# lines = '''A:+,-,=,=
# B:+,=,-,+
# C:=,-,+,+
# D:=,=,=,+'''.splitlines()
# track = '''S+===
# -   +
# =+=-+'''.splitlines()

track_s = track[0][1:]
for i in range(1, len(track) - 1):
    track_s += track[i][-1]
track_s += track[len(track) - 1][::-1]
for i in reversed(range(1, len(track) - 1)):
    track_s += track[i][0]
track_s += '='

def calculate_score(ops):
    total = 0
    score = 10
    it = itertools.cycle(ops)
    # for _ in range(1): # FIXME: TEST
    for _ in range(10):
        for op in track_s:
            t = next(it)
            if op == '=':
                op = t

            if op == '+':
                score += 1
            elif op == '-':
                score -= 1
            score = max(score, 0)
            # print(f'{score=}')
            total += score
    return total

# calculate_score('+,-,=,='.split(','))

devices = [] # (score, name)
for line in lines:
    name, ops = line.split(':')
    score = calculate_score(ops.split(','))
    devices.append((score, name))

devices.sort(reverse=True)
answer2 = ''.join(name for _, name in devices)
print(answer2)



# # Part 3


with open("./2024/input/everybody_codes_e2024_q07_p3.txt") as f:
    lines = f.read().splitlines()

track = '''S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-'''.splitlines()

def parse_track(track):
    r, c = 0, 1
    prev = 0, 0
    result = []
    while track[r][c] != 'S':
        result.append(track[r][c])
        print(r, c)
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < len(track)) or not (0 <= c2 < len(track[r2])):
                continue
            if (r2, c2) == prev or track[r2][c2] == ' ':
                continue
            prev = r, c
            r, c = r2, c2
            break
        else:
            print(f'UNABLE TO FIND NEXT POSITION')
            return
    return result + ['=']

track_s = parse_track(track)


def calculate_score(ops):
    total = 0
    score = 10
    it = itertools.cycle(ops)
    # for _ in range(2024):
    for _ in range(11): # 2024 is divisible by 11
        for op in track_s:
            t = next(it)
            if op == '=':
                op = t

            if op == '+':
                score += 1
            elif op == '-':
                score -= 1
            score = max(score, 0)
            total += score
    return total

competitor_score = calculate_score(lines[0].split(':')[1].split(','))

plusses = 5
minuses = 3
equals = 3
cur = []
combinations = []
def backtrack():
    global plusses
    global minuses
    global equals
    if plusses == minuses == equals == 0:
        combinations.append(cur.copy())
    if plusses:
        plusses -= 1
        cur.append('+')
        backtrack()
        cur.pop()
        plusses += 1
    if minuses:
        minuses -= 1
        cur.append('-')
        backtrack()
        cur.pop()
        minuses += 1
    if equals:
        equals -= 1
        cur.append('=')
        backtrack()
        cur.pop()
        equals += 1

backtrack()

# len(combinations)
# len({tuple(comb) for comb in combinations})
answer3 = 0
for comb in combinations:
    score = calculate_score(comb)
    if score > competitor_score:
        answer3 += 1

print(answer3)
