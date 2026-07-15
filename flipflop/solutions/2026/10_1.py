with open("./input/2026/10.txt") as f:
    lines = f.read().splitlines()

regs = [0] * 16
ip = 0
labels = {}
for i, line in enumerate(lines):
    # Label
    if line[1] == "e":
        label = (len(line) - 2) // 2
        labels[label] = i

while ip < len(lines):
    line = lines[ip]
    # Label
    if line[1] == "e":
        ip += 1
        continue

    parts = line[2:].split("ne")
    nums = [len(part) // 2 for part in parts]
    # print(nums)
    op, *args = nums
    match op:
        case 0:
            # 0 nas: Load immediate value into register. (val, dest_reg)
            val, dest_reg = args
            regs[dest_reg] = val
        case 1:
            # 1 na: Copy value from one register to another. (src_reg, dest_reg)
            src_reg, dest_reg = args
            regs[dest_reg] = regs[src_reg]
        case 2:
            # 2 nas: Add values from two registers and store result in a third register. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            regs[dest_reg] = regs[src_reg1] + regs[src_reg2]
        case 3:
            # 3 nas: Subtract values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            regs[dest_reg] = regs[src_reg1] - regs[src_reg2]
        case 4:
            # 4 nas: Multiply values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            regs[dest_reg] = regs[src_reg1] * regs[src_reg2]
        case 5:
            # 5 nas: Modulo values from two registers and store result in a third. (src_reg1, src_reg2, dest_reg)
            src_reg1, src_reg2, dest_reg = args
            out = 0
            if regs[src_reg2]:
                out = regs[src_reg1] % regs[src_reg2]
            regs[dest_reg] = out
        case 6:
            # 6 nas: Increment value in a register by 1. (reg)
            (reg,) = args
            regs[reg] += 1
        case 7:
            # 7 nas: Decrement value in a register by 1. (reg)
            (reg,) = args
            regs[reg] -= 1
        case 8:
            # 8 nas: Jump to label. (label)
            (label,) = args
            ip = labels[label] - 1
        case 9:
            # 9 nas: Jump to label if value in register is zero. (reg, label)
            reg, label = args
            if regs[reg] == 0:
                ip = labels[label] - 1
        case 10:
            # 10 nas: Jump to label if value in register is not zero. (reg, label)
            reg, label = args
            if regs[reg] != 0:
                ip = labels[label] - 1

    for i in range(len(regs)):
        regs[i] %= 2**16

    ip += 1

answer = regs[0]
print(answer)
