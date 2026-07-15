with open("./input/2026/10.txt") as f:
    lines = f.read().splitlines()

labels = {}
ops = []
for line in lines:
    if line[1] == "e":
        label = (len(line) - 2) // 2
        labels[label] = len(ops)
        continue

    parts = line[2:].split("ne")
    ops.append([len(part) // 2 for part in parts])


def does_halt(r0: int, r1: int) -> bool:
    iterations = 0
    regs = [0] * 16
    regs[0] = r0
    regs[1] = r1
    ip = 0

    while ip < len(ops):
        op, *args = ops[ip]
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
            regs[i] %= 65536

        ip += 1
        iterations += 1
        if iterations > 5_000_000:
            return True
    return False


answer = 0
for r0 in range(16):
    for r1 in range(16):
        out = does_halt(r0, r1)
        answer += out
        print(r0, r1, out)
answer *= 65536 // 16
print(answer)
