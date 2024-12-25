from aocd import get_data, submit
import collections


inp = get_data(day=24, year=2024)

# inp = '''x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02
# '''

# inp = '''x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj'''

init, ops = inp.split('\n\n')

wires = {}
for line in init.splitlines():
    wire, val = line.split(': ')
    wires[wire] = int(val)


# requirements = collections.defaultdict(int) # out -> dep_count
m = {} # out -> (in1, in2, op)
helps = collections.defaultdict(list) # a -> [b, c]
for line in ops.splitlines():
    a, op, b, _, out= line.split()
    m[out] = (a, b, op)
    helps[a].append(out)
    helps[b].append(out)

stack = list(wires)
while stack:
    wire = stack.pop()
    for out in helps[wire]:
        a, b, op = m[out]
        if a in wires and b in wires:
            a = wires[a]
            b = wires[b]
            match op:
                case 'AND':
                    wires[out] = a and b
                case 'OR':
                    wires[out] = a or b
                case 'XOR':
                    wires[out] = a ^ b
            stack.append(out)

print(wires)

answer1 = ''
for wire in sorted(wires, reverse=True):
    if wire.startswith('z'):
        answer1 += str(wires[wire])

print(answer1)


# submit(int(answer1, 2), part='a', day=24, year=2024)

# submit(answer1, part='a', day=24, year=2024)
# 1000001100011001000110101100111101110001110000
# >>> submit(answer1, part='a', day=24, year=2024)
# That's not the right answer; your answer is too high.  If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit.  Please wait one minute before trying again. [Return to Day 24]
# <urllib3.response.HTTPResponse at 0x11776d1e0>


# # Part 2


# answer2 = 'todo'
# print(answer2)

# # submit(answer2, part='b', day=24, year=2024)

# Four pairs swapped



# inp = '''x00: 0
# x01: 1
# x02: 0
# x03: 1
# x04: 0
# x05: 1
# y00: 0
# y01: 0
# y02: 1
# y03: 1
# y04: 0
# y05: 1

# x00 AND y00 -> z05
# x01 AND y01 -> z02
# x02 AND y02 -> z01
# x03 AND y03 -> z03
# x04 AND y04 -> z04
# x05 AND y05 -> z00'''
init, ops = inp.split('\n\n')

# def is_valid(A, B, swaps):
#     wires = {}
#     for i, x in enumerate(reversed(A)):
#         print(i, x)
#         wires[f'x{i:>02}'] = int(x)
#     for i, y in enumerate(reversed(B)):
#         wires[f'y{i:>02}'] = int(y)

#     m = {} # out -> (in1, in2, op)
#     helps = collections.defaultdict(list) # a -> [b, c]
#     for line in ops.splitlines():
#         a, op, b, _, out = line.split()
#         if out in swaps:
#             # print(f'swapping {out} with {swaps[out]}')
#             out = swaps[out]
#         m[out] = (a, b, op)
#         helps[a].append(out)
#         helps[b].append(out)
    
#     # print(f'{m=}')

#     stack = list(wires)
#     while stack:
#         wire = stack.pop()
#         for out in helps[wire]:
#             a, b, op = m[out]
#             if a in wires and b in wires:
#                 a = wires[a]
#                 b = wires[b]
#                 match op:
#                     case 'AND':
#                         wires[out] = a and b
#                     case 'OR':
#                         wires[out] = a or b
#                     case 'XOR':
#                         wires[out] = a ^ b
#                 stack.append(out)

#     # print(wires)
#     s = ''
#     for wire in sorted(wires, reverse=True):
#         if wire.startswith('z'):
#             s += str(wires[wire])
#     z = int(s, 2)
#     A = int(A, 2)
#     B = int(B, 2)
#     expected = A & B
#     print(f'Expected: {A} AND {B} = {expected}')
#     print(f'Actual: {A} AND {B} = {z}')
#     return z == expected



# ;Example:
# a->b
# b->edge label->c
# c->a


# Export it to Draw.io
#   Arrange -> Insert -> Advanced -> From Text... -> Diagram
#   Arrange -> Layout -> Vertical Tree
drawio = []
for line in ops.splitlines():
    a, op, b, _, out = line.split()
    drawio.append(f'{a} -> {op} -> {out}')
    drawio.append(f'{b} -> {op} -> {out}')
print('\n'.join(drawio))


# Mermaid
mermaid = ['flowchart TD', '%% Nodes']
nodes = set()
for line in ops.splitlines():
    a, op, b, _, out = line.split()
    nodes.add(a)
    nodes.add(b)
    nodes.add(out)
for node in nodes:
    mermaid.append(f'{node}("{node}")')
for line in ops.splitlines():
    a, op, b, _, out = line.split()
    mermaid.append(f'{a} -- {op} --> {out}')
    mermaid.append(f'{b} -- {op} --> {out}')
for node in nodes:
    if node.startswith('x'):
        mermaid.append(f'style {node} color:#FFFFFF, stroke:#00C853, fill:#00C853')    
    if node.startswith('y'):
        mermaid.append(f'style {node} color:#FFFFFF, stroke:#2962FF, fill:#2962FF')
    if node.startswith('z'):
        mermaid.append(f'style {node} color:#FFFFFF, fill:#AA00FF, stroke:#AA00FF')

print('\n'.join(mermaid))

# flowchart TD
# %% Nodes
#     A("fab:fa-youtube Starter Guide")
#     B("fab:fa-youtube Make Flowchart")
#     n1@{ icon: "fa:gem", pos: "b", h: 24}
#     C("fa:fa-book-open Learn More")
#     D{"Use the editor"}
#     n2(Many shapes)@{ shape: delay}
#     E(fa:fa-shapes Visual Editor)
#     F("fa:fa-chevron-up Add node in toolbar")
#     G("fa:fa-comment-dots AI chat")
#     H("fa:fa-arrow-left Open AI in side menu")
#     I("fa:fa-code Text")
#     J(fa:fa-arrow-left Type Mermaid syntax)

# %% Edge connections between nodes
#     A --> B --> C --> n1 & D & n2
#     D -- Build and Design --> E --> F
#     D -- Use AI --> G --> H
#     D -- Mermaid js --> I --> J

# %% Individual node styling. Try the visual editor toolbar for easier styling!
#     style E color:#FFFFFF, fill:#AA00FF, stroke:#AA00FF
#     style G color:#FFFFFF, stroke:#00C853, fill:#00C853
#     style I color:#FFFFFF, stroke:#2962FF, fill:#2962FF

# %% You can add notes with two "%" signs in a row!



def is_valid(A, B, swaps):
    wires = {}
    for i, x in enumerate(reversed(A)):
        # print(i, x)
        wires[f'x{i:>02}'] = int(x)
    for i, y in enumerate(reversed(B)):
        wires[f'y{i:>02}'] = int(y)

    m = {} # out -> (in1, in2, op)
    helps = collections.defaultdict(list) # a -> [b, c]
    for line in ops.splitlines():
        a, op, b, _, out = line.split()
        if out in swaps:
            # print(f'swapping {out} with {swaps[out]}')
            out = swaps[out]
        m[out] = (a, b, op)
        helps[a].append(out)
        helps[b].append(out)
    
    # print(f'{m=}')

    stack = list(wires)
    while stack:
        wire = stack.pop()
        for out in helps[wire]:
            a, b, op = m[out]
            if a in wires and b in wires:
                a = wires[a]
                b = wires[b]
                match op:
                    case 'AND':
                        wires[out] = a and b
                    case 'OR':
                        wires[out] = a or b
                    case 'XOR':
                        wires[out] = a ^ b
                stack.append(out)

    # print(wires)
    s = ''
    for wire in sorted(wires, reverse=True):
        if wire.startswith('z'):
            s += str(wires[wire])
    z = int(s, 2)
    A = int(A, 2)
    B = int(B, 2)
    expected = A + B
    # print(f'Expected: {A} AND {B} = {expected}')
    # print(f'Actual: {A} AND {B} = {z}')
    return z == expected


# is_valid('1011', '1101', swaps)

# #z05 <-> z00;   z02 <-> z01
# swaps = {
#     'z05': 'z00',
#     'z00': 'z05',
#     'z02': 'z01',
#     'z01': 'z02'
# }
# is_valid('101010', '101100', {})
# is_valid('101010', '101100', swaps)
# is_valid(gen_rand(6), gen_rand(6), swaps)
# # is_valid(f'{0o101010>06}', f'{101100>06}', swaps)


outputs = []
for line in ops.splitlines():
    a, op, b, _, out = line.split()
    outputs.append(out)

# def solve(digits):
#     for i1 in range(len(outputs)):
#         for i2 in range(i1 + 1, len(outputs)):
#             for i3 in range(len(outputs)):
#                 for i4 in range(i3 + 1, len(outputs)):
#                     if len({i1, i2, i3, i4}) != 4:
#                         continue
#                     for _ in range(10):
#                         swaps = {
#                             outputs[i1] : outputs[i2],
#                             outputs[i2] : outputs[i1],
#                             outputs[i3] : outputs[i4],
#                             outputs[i4] : outputs[i3],
#                         }
#                         print(f'{swaps=}')
#                         if not is_valid(gen_rand(digits), gen_rand(digits), swaps):
#                             break
#                     else:
#                         return i1, i2, i3, i4

def solve(digits, outputs):
    for i1 in range(len(outputs)):
        for i2 in range(i1 + 1, len(outputs)):
            for i3 in range(i1 + 1, len(outputs)):
                if len({i1, i2, i3}) != 3: continue
                for i4 in range(i3 + 1, len(outputs)):
                    if len({i1, i2, i3, i4}) != 4: continue
                    for i5 in range(i3 + 1, len(outputs)):
                        if len({i1, i2, i3, i4, i5}) != 5: continue
                        for i6 in range(i5 + 1, len(outputs)):
                            if len({i1, i2, i3, i4, i5, i6}) != 6: continue
                            for i7 in range(i5 + 1, len(outputs)):
                                if len({i1, i2, i3, i4, i5, i6,i7}) != 7: continue
                                for i8 in range(i7 + 1, len(outputs)):
                                    # print(f'{i1=}')
                                    if len({i1, i2, i3, i4, i5, i6,i7, i8}) != 8:
                                        continue
                                    for i in range(10):
                                        if i == 1:
                                            print(f'Candidate: {i1, i2, i3, i4, i5, i6, i7, i8}')
                                            print(f'    {[outputs[ii] for ii in [i1, i2, i3, i4, i5, i6, i7, i8]]}')
                                        swaps = {
                                            outputs[i1] : outputs[i2],
                                            outputs[i2] : outputs[i1],

                                            outputs[i3] : outputs[i4],
                                            outputs[i4] : outputs[i3],

                                            outputs[i5] : outputs[i5],
                                            outputs[i6] : outputs[i6],

                                            outputs[i7] : outputs[i8],
                                            outputs[i8] : outputs[i7],
                                        }
                                        # print(f'{swaps=}')
                                        if not is_valid(gen_rand(digits), gen_rand(digits), swaps):
                                            break
                                    else:
                                        return i1, i2, i3, i4, i5, i6, i7, i8

# a = solve(6)
# a = solve(45)

# answer2 = []
# for i in a:
#     answer2.append(outputs[i])
# answer2 = ','.join(sorted(answer2))
# print(answer2)

# Pad 44
import random


def gen_rand(length_out):
    x = ''
    for _ in range(length_out):
        x += str(random.randint(0, 1))
    return x


# submit(answer2, part='b', day=24, year=2024)


# is_valid('110010010101110111010100100010011100001000011', f'011101110101011010000010001111011000001010010', swaps)


# is_valid('0' * 45, '0' * 45, {})
# is_valid('000000000000000000000000000000100000000000000', '000000000000000000000000000000000000000000000', {})

# x = 000000000000000000000000000000000100000000000
# bad_x = set()
# bad_y = set()
bad = set()
for i in range(45):
    l = ['0'] * 45
    l[i] = '1'
    s = ''.join(l)
    if not is_valid(s, '0' * 45, {}) or not is_valid('0' * 45, s, {}):
        bad.add(f'z{44-i}')
    # if not is_valid(s, '0' * 45, {}):
    #     bad_x.add(s)
    #     bad.add(f'x{44-i}')
    # if not is_valid('0' * 45, s, {}):
    #     bad_y.add(s)
    #     bad.add(f'y{44-i}')

# bad_x
# bad_y

# bad = 'z11', 'z15'

helps = collections.defaultdict(list) # a -> [b, c]
for line in ops.splitlines():
    a, op, b, _, out = line.split()
    helps[a].append(out)
    helps[b].append(out)

def is_related(a, seen):
    if a in seen:
        return seen[a]
    
    for b in helps[a]:
        if is_related(b, seen):
            seen[a] = True
            return True
    seen[a] = False
    return False


def find_related_nodes(node):
    result = set()
    seen = {node: True}
    for candidate in outputs:
        if is_related(candidate, seen):
            result.add(candidate)
    return result

# possibly_bad_nodes = set()
# good_nodes = set()
# for node in outputs:
#     if node.startswith('z'):
#         if node in bad:
#             possibly_bad_nodes.update(find_related_nodes(node))
#         else:
#             good_nodes.update(find_related_nodes(node))
# possibly_bad_nodes = possibly_bad_nodes.difference(good_nodes)

# find_related_nodes('z11')

good_nodes = find_related_nodes('z10')
bad_nodes = set()
for node in bad:
    bad_nodes.update(find_related_nodes(node))
bad_nodes = bad_nodes.difference(good_nodes)

outputs = list(bad_nodes) # FIXME: This is used in solve

a = solve(45)

answer2 = []
for i in a:
    answer2.append(outputs[i])

if len(answer2) == 8:
    answer2 = ','.join(sorted(answer2))
    print(answer2)
    submit(answer2, part='b', day=24, year=2024)



def get_and(A, B, swaps):
    wires = {}
    for i, x in enumerate(reversed(A)):
        # print(i, x)
        wires[f'x{i:>02}'] = int(x)
    for i, y in enumerate(reversed(B)):
        wires[f'y{i:>02}'] = int(y)

    m = {} # out -> (in1, in2, op)
    helps = collections.defaultdict(list) # a -> [b, c]
    for line in ops.splitlines():
        a, op, b, _, out = line.split()
        if out in swaps:
            # print(f'swapping {out} with {swaps[out]}')
            out = swaps[out]
        m[out] = (a, b, op)
        helps[a].append(out)
        helps[b].append(out)
    
    # print(f'{m=}')

    stack = list(wires)
    while stack:
        wire = stack.pop()
        for out in helps[wire]:
            a, b, op = m[out]
            if a in wires and b in wires:
                a = wires[a]
                b = wires[b]
                match op:
                    case 'AND':
                        wires[out] = a and b
                    case 'OR':
                        wires[out] = a or b
                    case 'XOR':
                        wires[out] = a ^ b
                stack.append(out)

    # print(wires)
    s = ''
    for wire in sorted(wires, reverse=True):
        if wire.startswith('z'):
            s += str(wires[wire])
    # z = int(s, 2)
    # A = int(A, 2)
    # B = int(B, 2)
    # expected = A + B
    # print(f'Expected: {A} AND {B} = {expected}')
    # print(f'Actual: {A} AND {B} = {z}')
    # return z == expected
    return s

digits = 45
goods = collections.Counter()
bads = collections.Counter()
for _ in range(500):
    a, b = gen_rand(digits), gen_rand(digits)
    z = get_and(a, b, {})
    expect = bin(int(a, 2) & int(b, 2))[2:]
    for i, (actual, expected) in reversed(list(enumerate(zip(z, expect)))):
        node = f'z{i:>02}'
        for rel in find_related_nodes(node):
            if actual == expected:
                goods[rel] += 1
            else:
                bads[rel] += 1

l = []
for out in goods:
    l.append(bads[out] / (bads[out] + goods[out]))
l.sort(reverse=True)


# ans = solve(45, l[:10])
# ans = solve(45, l[:30])
# print(ans)


def get_score(swaps):
    digits = 45
    goods = 0
    bads = 0
    for _ in range(10):
        a, b = gen_rand(digits), gen_rand(digits)
        z = get_and(a, b, swaps)
        expect = bin(int(a, 2) & int(b, 2))[2:]
        for i, (actual, expected) in reversed(list(enumerate(zip(z, expect)))):
            if actual == expected:
                goods += 1
            else:
                bads += 1
    return bads / (goods + bads)


swaps = {}
bests = []
for _ in range(4):
    candidate =  (float('inf'), 0, 0) # (score (bigger worse), i, j)
    for i in range(len(outputs)):
        print(f'{i=} {candidate=}')
        for j in range(i + 1, len(outputs)):
            if i in swaps or j in swaps:
                continue
            new_swaps = swaps.copy()
            new_swaps[outputs[i]] = outputs[j]
            new_swaps[outputs[j]] = outputs[i]
            score = get_score(new_swaps)
            candidate = min(candidate, (score, i, j))
    bests.append(candidate)
    print(bests)

answer2 = []
for a, b in bests:
    answer2.append(outputs[a])
    answer2.append(outputs[b])

if len(answer2) == 8:
    answer2 = ','.join(sorted(answer2))
    print(answer2)
    # submit(answer2, part='b', day=24, year=2024)


swaps = {}
for _, a, b in bests:
    swaps[outputs[i]] = outputs[j]
    swaps[outputs[j]] = outputs[i]
for i in range(10):
    if not is_valid(gen_rand(digits), gen_rand(digits), swaps):
        print('BAD!')
        break
else:
    print('GOOD!')