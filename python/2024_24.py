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