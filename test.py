from vm import Vm, resume

# Register 8 is vm.memory[32775]

# 32768
# 32769
# 32770
# 32771
# 32772
# 32773
# 32774
# 32775


# def v():
#     global ip
#     i = vm.memory[ip]
#     ip += 1
#     if i <= 32767:
#         return str(i)
#     if i <= 32775:
#         return f"reg{i-32767}"
#     raise ValueError(f"Invalid number {i}")


def print_state(n_lines=30):
    print(vm.state)
    for i in range(8):
        print(f"reg{i + 1}", end="\t")
    print()
    for i in range(8):
        print(vm.memory[32768 + i], end="\t")
    print()
    print()

    print("Stack: ", vm.stack)
    print()
    print()

    ip = vm.ip
    asm = []
    for _ in range(n_lines):
        op = vm.memory[ip]
        line = [f"{ip}:"]
        ip += 1
        if op not in commands:
            line.append(f"UNKNOWN {op}")
        else:
            command, n_args = commands[op]
            line.append(command)
            for _ in range(n_args):
                arg = vm.memory[ip]
                if arg > 32767:
                    arg = f"reg{arg-32767}"
                ip += 1
                line.append(str(arg))
        asm.append(line)
    # print(asm)

    for line in asm:
        print("\t".join(line))


vm = Vm.from_dump(dump)
vm.memory[32768] = 32767
# vm.memory[32775] = 1
resume(vm)


vm = Vm.from_dump(dump)
vm.memory[32775] = 42
vm.input("use teleporter")  # Note no newline
vm.run()

vm.input("\n")

# 5467 is just before we look at reg8
# 5627 is the new function that is called when reg8 is nonzero


# 1593
# 6049 <<--
vm.step()
print_state(26)

# I think 2852 is the start. But that is before it has done the printing

# continue until reg8
# while 32775 not in vm.memory[vm.ip : vm.ip + 30]:
while vm.memory[vm.ip != 2852]:
    vm.step()

vm.run()
print(vm.output())

# A strange, electronic voice is projected into your mind:

#   "Unusual setting detected!  Starting calibration process!  Estimated time to completion: 1 billion years."

vm.memory[32775] = 42
vm.input("use teleporter\n")

# reg1	reg2	reg3	reg4	reg5	reg6	reg7	reg8
# 25984	25988	0	3	0	1670	27412	0

print_state(26)
# 6049:	jt	reg1	6057              If reg1: goto 6057
# 6052:	add	reg1	reg2	1         reg1 = reg2 + 1
# 6056:	ret
# 6057:	jt	reg2	6070
# 6060:	add	reg1	reg1	32767
# 6064:	set	reg2	reg8
# 6067:	call	6049
# 6069:	ret
# 6070:	push	reg1
# 6072:	add	reg2	reg2	32767
# 6076:	call	6049
# 6078:	set	reg2	reg1
# 6081:	pop	reg1
# 6083:	add	reg1	reg1	32767
# 6087:	call	6049
# 6089:	ret
# 6090:	mod	84	101	115

def f():
    if not reg1:  # 6049:	jt	reg1	6057              If reg1: goto 6057
        reg1 = reg2 + 1  # 6052:	add	reg1	reg2	1         reg1 = reg2 + 1
        return # 6056:	ret
    if reg2: goto 6070 # 6057:	jt	reg2	6070
    # 6060:	add	reg1	reg1	32767
    # 6064:	set	reg2	reg8
    # 6067:	call	6049
    # 6069:	ret

def g():
    # 6070:	push	reg1
    reg2 += 32767 # 6072:	add	reg2	reg2	32767
    f() # 6076:	call	6049
    reg2 = reg1 # 6078:	set	reg2	reg1
    # 6081:	pop	reg1
    reg1 += 32767 # 6083:	add	reg1	reg1	32767
    f() # 6087:	call	6049
    return # 6089:	ret
mem[84] = 101 % 115 # 6090:	mod	84	101	115        ???


# 1565

# vm.run()
# vm.output()


def v():
    global ip
    i = vm.memory[ip]
    ip += 1
    if i <= 32767:
        return str(i)
    if i <= 32775:
        return f"reg{i-32767}"
    raise ValueError(f"Invalid number {i}")


commands = {
    0: ("halt", 0),
    1: ("set", 2),
    2: ("push", 1),
    3: ("pop", 1),
    4: ("eq", 3),
    5: ("gt", 3),
    6: ("jmp", 1),
    7: ("jt", 2),
    8: ("jf", 2),
    9: ("add", 3),
    10: ("mult", 3),
    11: ("mod", 3),
    12: ("and", 3),
    13: ("or", 3),
    14: ("not", 2),
    15: ("rmem", 2),
    16: ("wmem", 2),
    17: ("call", 1),
    18: ("ret", 0),
    19: ("out", 1),
    20: ("in", 1),
    21: ("noop", 0),
}

vm.memory[32768 : 32775 + 1]
ip = vm.ip
asm = []
for _ in range(100):
    op = vm.memory[ip]
    line = [f"{ip}:"]
    ip += 1
    if op not in commands:
        line.append("UNKNOWN")
    else:
        command, n_args = commands[op]
        line.append(command)
        for _ in range(n_args):
            line.append(v())
    asm.append(line)
# print(asm)

for line in asm:
    print("\t".join(line))


# while True:
#     assert vm.state == State.READY
#     vm.run()

#     print(vm.output())

#     # dump = vm.dump()
#     # if dump in seen:
#     #     print('--- State seen previously ---')
#     # seen.add(dump)

#     if vm.state == State.INPUT_BLOCKED:
#         # Parse Room
#         vm.input("look\n")
#         vm.run()
#         # title, text, interests, exits = parse_room(vm.output())
#         # print(f'{title=} {interests=} {exits=}')

#         inp = input()
#         if inp == "q":  # Custom quit command
#             break
#         if inp.startswith("d "):  # Custom dump command
#             with open(inp.split(" ", 1)[1], "w") as f:
#                 f.write(str(vm.dump()))
#         vm.input(inp + "\n")
#     else:
#         break
