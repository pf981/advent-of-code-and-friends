from aocd import get_data, submit
import re

inp = get_data(day=17, year=2024)

# inp = '''Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# '''

# inp = '''Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0'''

start_reg_a,start_reg_b,start_reg_c,*start_program = map(int, re.findall(r'-?[\d]+', inp))
reg_a,reg_b,reg_c,program = start_reg_a,start_reg_b,start_reg_c,start_program.copy()

def run(reg_a,reg_b,reg_c,program):
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
                reg_a = reg_a // (2**combo)
            case 1: # bxl
                reg_b = reg_b ^ literal
            case 2: # bst
                reg_b = combo % 8
            case 3: # jnz
                if reg_a != 0:
                    ip = literal
                    continue # Does this work in match?
            case 4: # bxc
                reg_b = reg_b ^ reg_c
            case 5: # out
                output.append(combo % 8)
            case 6: # bdv
                reg_b = reg_a // (2**combo)
            case 7: # cdv
                reg_c = reg_a // (2**combo)
        
        ip += 2
    return ','.join(str(x) for x in output)

answer1 = run(reg_a,reg_b,reg_c,program)
print(answer1)

# submit(answer1, part='a', day=17, year=2024)


# # Part 2
# import itertools

# target = ','.join(str(x) for x in start_program)
# for reg_a in itertools.count():
#     reg_b,reg_c,program = start_reg_b,start_reg_c,start_program.copy()
#     prog = run(reg_a,reg_b,reg_c,program)
#     if prog == target:
#         answer2 = reg_a
#         break

# print(answer2)

# submit(answer2, part='b', day=17, year=2024)

from aocd import get_data, submit

program = [2,4,1,2,7,5,1,3,4,3,5,5,0,3,3,0]

import z3

o = z3.Optimize()

def bit_vecs(s):
    l = []
    for ss in s.split():
        l.append(z3.BitVec(ss, 64))
    return l

a0, b0, c0, a1 = bit_vecs('a0 b0 c0 a1')
o.add(b0 == 0)
o.add(c0 == 0)
# o.add(a1 == 64584136) # TEST
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
    
    # if i < 15: # TEST
    o.add(out == program[i - 1])

o.check()

mod = o.model()


def get(name, mod):
    for obj_name in mod:
        if str(obj_name) == name:
            return mod[obj_name]

for i in range(1, 17):
    print(get(f'out{i}', mod))

print(get(f'a0', mod))

# 37221334433268