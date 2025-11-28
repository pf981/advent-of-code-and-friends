from aocd import get_data, submit
import collections


inp = get_data(day=24, year=2024)
init, ops = inp.split('\n\n')

wires = {}
for line in init.splitlines():
    wire, val = line.split(': ')
    wires[wire] = int(val)

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


answer1 = ''
for wire in sorted(wires, reverse=True):
    if wire.startswith('z'):
        answer1 += str(wires[wire])
answer1 = int(answer1, 2)
print(answer1)

submit(answer1, part='a', day=24, year=2024)


# Part 2


l = []
for out, (a, b, op) in m.items():
    if a > b:
        a, b = b, a
    score = (
        not (a.startswith('x') and op == 'XOR'),
        not (out.startswith('z')),
        ['XOR', 'AND', 'OR'].index(op)
    )
    l.append((score, f'{a} {op} {b} -> {out}'))
l.sort()
print('\n'.join(s for _,s in l))


manual_list = ['wpd','mdd','wts','z19','z37','z11','jqf','skh']
answer2 = ','.join(sorted(manual_list))
print(answer2)

submit(answer2, part='b', day=24, year=2024)
