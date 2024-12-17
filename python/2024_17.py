from aocd import get_data, submit
import re


def run(reg_a, reg_b, reg_c, program):
    output = []
    ip = 0
    while ip < len(program):
        op = program[ip]
        literal = program[ip + 1]
        combo = [
            0, 1, 2, 3,
            reg_a,
            reg_b,
            reg_c,
            'INVALID'
        ][literal]
        match op:
            case 0: # adv
                reg_a = reg_a // (2 ** combo)
            case 1: # bxl
                reg_b = reg_b ^ literal
            case 2: # bst
                reg_b = combo % 8
            case 3: # jnz
                if reg_a != 0:
                    ip = literal
                    continue
            case 4: # bxc
                reg_b = reg_b ^ reg_c
            case 5: # out
                output.append(combo % 8)
            case 6: # bdv
                reg_b = reg_a // (2 ** combo)
            case 7: # cdv
                reg_c = reg_a // (2 ** combo)
        
        ip += 2
    return ','.join(str(x) for x in output)


inp = get_data(day=17, year=2024)
reg_a, reg_b, reg_c, *program = [int(s) for s in re.findall(r'-?[\d]+', inp)]
answer1 = run(reg_a, reg_b, reg_c, program)
print(answer1)

submit(answer1, part='a', day=17, year=2024)


# # Part 2


import z3


def bit_vecs(s):
    l = []
    for ss in s.split():
        l.append(z3.BitVec(ss, 64))
    return l


o = z3.Optimize()

a0, b0, c0, a1 = bit_vecs('a0 b0 c0 a1')
o.add(b0 == 0)
o.add(c0 == 0)
o.add(a1 == a0)
o.minimize(a0)

for i in range(1, 17):
    a, b, c, bb, bbb, out = bit_vecs(f'a{i} b{i} c{i} bb{i} bbb{i} out{i}')
    if i != 1:
        prev_a = bit_vecs(f'a{i-1}')[0]
        o.add(a == prev_a >> 3)
    o.add(b == (a % 8) ^ 2)
    o.add(c == a >> b)
    o.add(bb == b ^ 3)
    o.add(bbb == bb ^ c)
    o.add(out == bbb % 8)
    o.add(out == program[i - 1])

o.check()
answer2 = o.model()[a0].as_long()
print(answer2)

submit(answer2, part='b', day=17, year=2024)
