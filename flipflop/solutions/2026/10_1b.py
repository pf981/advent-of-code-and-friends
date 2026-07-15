import itertools

with open("./input/2026/10.txt") as f:
    lines = f.read().splitlines()

# lines = """banenanena
# banenananenana
# banenanananenanana
# banananenanenananenananana
# banananenananananenanananenanananana
# bananenananananane
# """.splitlines()
# lines = """banenane
# banananananananananenananananananana
# banenanena
# be
# banenanenana
# banananananananananenanana
# benana
# banenanenanana
# banananananananananena
# benanana
# banenanenananana
# banananananananananenana
# benananananananananana
# banenanenanananana
# bananananananananane
# benananananananananananana
# banenanenananananana
# benanananananananana
# banenanenanananananana
# benananananananana
# banenanenananananananana
# banananananananananenananananananananana
# bena
# banenanenanananananananana""".splitlines()

regs = [0] * 16
ip = 0
labels = {}

output = []
# for i, line in enumerate(lines):
#     # Label
#     if line[1] == "e":
#         label = (len(line) - 2) // 2
#         labels[label] = i
# while ip < len(lines):
for i, line in enumerate(lines):
    # line = lines[ip]
    # Label
    if line[1] == "e":
        label = (len(line) - 2) // 2
        labels[label] = i
        output.append(f"label{label}:")
        continue

    parts = line[2:].split("ne")
    nums = [len(part) // 2 for part in parts]
    # print(nums)
    op, *args = nums
    match op:
        case 0:
            # 0 nas: Load immediate value into register. (val, dest_reg)
            val, dest_reg = args
            output.append(f"LOAD {val=} {dest_reg=}")
            regs[dest_reg] = val
        case 1:
            # 1 na: Copy value from one register to another. (src_reg, dest_reg)
            src_reg, dest_reg = args
            output.append(f"COPY {src_reg=} {dest_reg=}")
            regs[dest_reg] = regs[src_reg]
        case 2:
            # 2 nas: Add values from two registers and store result in a third register. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            output.append(f"ADD {src_reg1=} {src_reg2=} {dest_reg=}")
            regs[dest_reg] = regs[src_reg1] + regs[src_reg2]
        case 3:
            # 3 nas: Subtract values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            output.append(f"SUB {src_reg1=} {src_reg2=} {dest_reg=}")
            regs[dest_reg] = regs[src_reg1] - regs[src_reg2]
        case 4:
            # 4 nas: Multiply values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            output.append(f"MUL {src_reg1=} {src_reg2=} {dest_reg=}")
            regs[dest_reg] = regs[src_reg1] * regs[src_reg2]
        case 5:
            # 5 nas: Modulo values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            output.append(f"MOD {src_reg1=} {src_reg2=} {dest_reg=}")
            regs[dest_reg] = regs[src_reg1] % regs[src_reg2]
        case 6:
            # 6 nas: Increment value in a register by 1. (reg)
            (reg,) = args
            output.append(f"INC {reg=}")
            regs[reg] += 1
        case 7:
            # 7 nas: Decrement value in a register by 1. (reg)
            (reg,) = args
            output.append(f"DEC {reg=}")
            regs[reg] -= 1
        case 8:
            # 8 nas: Jump to label. (label)
            (label,) = args
            output.append(f"JMP {label=}")
            # ip = labels[label] - 1
        case 9:
            # 9 nas: Jump to label if value in register is zero. (reg, label)
            reg, label = args
            output.append(f"JMPIFZERO {reg=} {label=}")
            # if regs[reg] == 0:
            #     ip = labels[label] - 1
        case 10:
            # 10 nas: Jump to label if value in register is not zero. (reg, label)
            reg, label = args
            output.append(f"JMPIFNONZERO {reg=} {label=}")
            # if regs[reg] != 0:
            #     ip = labels[label] - 1

print("\n".join(output))
answer = regs[0]
print(answer)
