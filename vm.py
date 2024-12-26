def parse(file: str) -> list[int]:
    instructions = []
    with open(file, "rb") as f:
        while word := f.read(2):
            num = int.from_bytes(word, byteorder="little", signed=False)
            instructions.append(num)
    return instructions + [0] * (2**15 - len(instructions))


def main():
    memory = parse("./challenge.bin")
    ip = 0
    reg = [0] * 8
    stack = []

    def grab() -> int:
        nonlocal ip
        result = memory[ip]
        ip += 1
        return result

    while True:
        match grab():
            case 0:  # halt: 0; stop execution and terminate the program
                return
            case 1:  # set: 1 a b; set register <a> to the value of <b>
                a, b = grab(), grab()
                reg[a] = b
            case 2:  # push: 2 a; push <a> onto the stack
                a = grab()
                stack.append(a)
            case 3:  # pop: 3 a; remove the top element from the stack and write it into <a>; empty stack = error
                pass
            case 4:  # eq: 4 a b c; set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
                pass
            case 5:  # gt: 5 a b c; set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
                pass
            case 6:  # jmp: 6 a; jump to <a>
                a = grab()
                ip = a
            case 7:  # jt: 7 a b; if <a> is nonzero, jump to <b>
                pass
            case 8:  # jf: 8 a b; if <a> is zero, jump to <b>
                pass
            case 9:  # add: 9 a b c; assign into <a> the sum of <b> and <c> (modulo 32768)
                pass
            case 10:  # mult: 10 a b c; store into <a> the product of <b> and <c> (modulo 32768)
                pass
            case 11:  # mod: 11 a b c; store into <a> the remainder of <b> divided by <c>
                pass
            case 12:  # and: 12 a b c; stores into <a> the bitwise and of <b> and <c>
                pass
            case 13:  # or: 13 a b c; stores into <a> the bitwise or of <b> and <c>
                pass
            case 14:  # not: 14 a b; stores 15-bit bitwise inverse of <b> in <a>
                pass
            case 15:  # rmem: 15 a b; read memory at address <b> and write it to <a>
                pass
            case 16:  # wmem: 16 a b; write the value from <b> into memory at address <a>
                pass
            case 17:  # call: 17 a; write the address of the next instruction to the stack and jump to <a>
                pass
            case 18:  # ret: 18; remove the top element from the stack and jump to it; empty stack = halt
                pass
            case 19:  # out: 19 a; write the character represented by ascii code <a> to the terminal
                a = grab()
                print(chr(a), end="")
            # in: 20 a; read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard instead of having to figure out how to read individual characters
            case 21:  # noop: 21; no operation
                pass


if __name__ == "__main__":
    main()
