debug = False


def parse(file: str) -> list[int]:
    instructions = []
    with open(file, "rb") as f:
        while word := f.read(2):
            num = int.from_bytes(word, byteorder="little", signed=False)
            instructions.append(num)
    return instructions + [0] * (2**15 - len(instructions) + 8)


def pp(*args) -> None:
    if not debug:
        return
    print("  ", end="")
    return print(*args)


# def main() -> None:
# registers at index 32768..32775?
memory = parse("./challenge.bin")
ip = 0
# reg = [0] * 8
stack = []


def grab() -> int:
    # nonlocal ip
    global ip
    result = memory[ip]
    ip += 1
    # if result <= 32767:
    if result <= 32775:
        return result
    # if result <= 32775:
    # return reg[result - 32768]
    raise ValueError(f"Invalid number {result}")


def get(i) -> int:
    if i <= 32767:
        return i
    if i <= 32775:
        return memory[i]
    raise ValueError(f"Invalid number {i}")


while True:
    op = grab()
    if op != 19:
        pp(f"\nRegisters: {[get(i) for i in range(32768, 32776)]}")
    match op:
        case 0:  # halt: 0; stop execution and terminate the program
            pp("0(halt)")
            break
        case 1:  # set: 1 a b; set register <a> to the value of <b>
            a, b = grab(), grab()
            pp(f"1(set) {a}({get(a)}) {b}({get(b)})")
            memory[a] = get(b)
        case 2:  # push: 2 a; push <a> onto the stack
            a = grab()
            pp(f"2(push) {a}({get(a)}))")
            stack.append(get(a))
        case 3:  # pop: 3 a; remove the top element from the stack and write it into <a>; empty stack = error
            a = grab()
            pp(f"3(pop) {a}({get(a)}))")
            memory[a] = stack.pop()
        case 4:  # eq: 4 a b c; set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
            a, b, c = grab(), grab(), grab()
            pp(f"4(eq) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = int(get(b) == get(c))
        case 5:  # gt: 5 a b c; set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
            a, b, c = grab(), grab(), grab()
            pp(f"5(gt) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = int(get(b) > get(c))
        case 6:  # jmp: 6 a; jump to <a>
            a = grab()
            pp(f"6(jmp) {a}({get(a)}))")
            ip = get(a)
        case 7:  # jt: 7 a b; if <a> is nonzero, jump to <b>
            a, b = grab(), grab()
            pp(f"7(jt) {a}({get(a)}) {b}({get(b)})")
            if get(a):
                ip = get(b)
        case 8:  # jf: 8 a b; if <a> is zero, jump to <b>
            a, b = grab(), grab()
            pp(f"8(jf) {a}({get(a)}) {b}({get(b)})")
            if not get(a):
                ip = get(b)
        case 9:  # add: 9 a b c; assign into <a> the sum of <b> and <c> (modulo 32768)
            a, b, c = grab(), grab(), grab()
            pp(f"9(add) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = (get(b) + get(c)) % 32768
        case 10:  # mult: 10 a b c; store into <a> the product of <b> and <c> (modulo 32768)
            a, b, c = grab(), grab(), grab()
            pp(f"10(mult) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = (get(b) * get(c)) % 32768
        case 11:  # mod: 11 a b c; store into <a> the remainder of <b> divided by <c>
            a, b, c = grab(), grab(), grab()
            pp(f"11(mod) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = get(b) % get(c)
        case 12:  # and: 12 a b c; stores into <a> the bitwise and of <b> and <c>
            a, b, c = grab(), grab(), grab()
            pp(f"12(and) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = get(b) & get(c)
        case 13:  # or: 13 a b c; stores into <a> the bitwise or of <b> and <c>
            a, b, c = grab(), grab(), grab()
            pp(f"13(or) {a}({get(a)}) {b}({get(b)}) {c}({get(c)})")
            memory[a] = get(b) | get(c)
        case 14:  # not: 14 a b; stores 15-bit bitwise inverse of <b> in <a>
            a, b = grab(), grab()
            pp(f"14(not) {a}({get(a)}) {b}({get(b)})")
            memory[a] = ((1 << 15) - 1) & ~get(b)
        case 15:  # rmem: 15 a b; read memory at address <b> and write it to <a>
            a, b = grab(), grab()
            pp(f"15(rmem) {a}({get(a)}) {b}({get(b)})")
            # memory[a] = get(b)
            memory[a] = memory[get(b)]
            # memory[a] = memory[b]
        case 16:  # wmem: 16 a b; write the value from <b> into memory at address <a>
            a, b = grab(), grab()
            pp(f"16(wmem) {a}({get(a)}) {b}({get(b)})")
            memory[get(a)] = get(b)
            pp(" ", memory[32768:])
        case 17:  # call: 17 a; write the address of the next instruction to the stack and jump to <a>
            a = grab()
            pp(f"17(call) {a}({get(a)})")
            stack.append(ip)
            ip = get(a)
        case 18:  # ret: 18; remove the top element from the stack and jump to it; empty stack = halt
            pp(f"18(ret) [{stack[-1]}]")
            if not stack:
                break
            ip = stack.pop()
        case 19:  # out: 19 a; write the character represented by ascii code <a> to the terminal
            a = grab()
            # pp(f"19(out) {a}({get(a)})")
            print(chr(get(a)), end="")
        case 20:  # in: 20 a; read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard instead of having to figure out how to read individual characters
            a = grab()
            pp(f"20(in) {a}({get(a)}) TODO")
            raise NotImplementedError
        case 21:  # noop: 21; no operation
            pp("21(noop)")
pp(f"{ip=}")

# if __name__ == "__main__":
#     main()


# Results:
# $ echo -n "<Code Here>" | md5sum

# 76ec2408e8fe3f1753c25db51efd8eb3
# 0e6aa7be1f68d930926d72b3741a145c DONE
# 7997a3b2941eab92c1c0345d5747b420
# 186f842951c0dcfe8838af1e7222b7d4
# 2bf84e54b95ce97aefd9fc920451fc45
# e09640936b3ef532b7b8e83ce8f125f4
# 4873cf6b76f62ac7d5a53605b2535a0c
# d0c54d4ed7f943280ce3e19532dbb1a6
