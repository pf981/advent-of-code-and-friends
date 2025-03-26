import enum
import io


class State(enum.Enum):
    READY = enum.auto()
    HALTED = enum.auto()
    INPUT_BLOCKED = enum.auto()


class Vm:
    def __init__(self, memory: list[int], stack: list[int], ip: int) -> None:
        self.memory = memory
        self.stack = stack
        self.ip = ip
        self.state = State.READY
        self.reader = io.StringIO()
        self.writer = io.StringIO()
        self.breakpoints = set()

    @classmethod
    def from_file(cls, file: str) -> "Vm":
        instructions = []
        with open(file, "rb") as f:
            while word := f.read(2):
                num = int.from_bytes(word, byteorder="little", signed=False)
                instructions.append(num)
        memory = instructions + [0] * (2**15 - len(instructions) + 8)
        return cls(memory, [], 0)

    @classmethod
    def from_dump(cls, dump: tuple[tuple[int, ...], tuple[int, ...], int]) -> "Vm":
        memory, stack, ip = dump
        return cls(list(memory), list(stack), ip)

    def dump(self) -> tuple[tuple[int, ...], tuple[int, ...], int]:
        return (tuple(self.memory), tuple(self.stack), self.ip)

    def input(self, s: str) -> None:
        pos = self.reader.tell()
        self.reader.write(s)
        self.reader.seek(pos)
        self.state = State.READY

    def output(self) -> str:
        s = self.writer.getvalue()
        self.writer.truncate(0)
        self.writer.seek(0)
        return s

    def grab(self) -> int:
        result = self.memory[self.ip]
        self.ip += 1
        if result <= 32775:
            return result
        raise ValueError(f"Invalid number {result}")

    def val(self, i: int) -> int:
        if i <= 32767:
            return i
        if i <= 32775:
            return self.memory[i]
        raise ValueError(f"Invalid number {i}")

    def run(self) -> None:
        while True:
            self.step()
            if self.state != State.READY:
                break

    def step(self) -> None:
        # Custom commands
        if self.ip in self.breakpoints or self.memory[self.ip] == 20:
            pos = self.reader.tell()
            line = self.reader.readline().strip()
            command, *args = line.split(" ")
            print(f"{command=} {args=}")
            match command:
                case "_quit":  # Quit
                    self.state = State.HALTED
                case "_dump":  # Dump
                    with open(args[0], "w") as f:
                        f.write(str(self.dump()))
                case "_set-breakpoint":
                    self.breakpoints.add(int(args[0]))
                case "_clear-breakpoints":
                    self.breakpoints.clear()
                case "_set-register":
                    register, value = args
                    self.memory[32768 + int(register)] = int(value)
                case "_set-ip":
                    self.ip = int(args[0])
                case _:
                    self.reader.seek(pos)
            if self.reader.tell() != pos:
                return

        g = self.grab
        v = self.val
        op = g()
        match op:
            case 0:  # halt: 0; stop execution and terminate the program
                self.state = State.HALTED
            case 1:  # set: 1 a b; set register <a> to the self.value of <b>
                a, b = g(), g()
                self.memory[a] = v(b)
            case 2:  # push: 2 a; push <a> onto the self.stack
                a = g()
                self.stack.append(v(a))
            case 3:  # pop: 3 a; remove the top element from the self.stack and write it into <a>; empty self.stack = error
                a = g()
                self.memory[a] = self.stack.pop()
            case 4:  # eq: 4 a b c; set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
                a, b, c = g(), g(), g()
                self.memory[a] = int(v(b) == v(c))
            case 5:  # gt: 5 a b c; set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
                a, b, c = g(), g(), g()
                self.memory[a] = int(v(b) > v(c))
            case 6:  # jmp: 6 a; jump to <a>
                a = g()
                self.ip = v(a)
            case 7:  # jt: 7 a b; if <a> is nonzero, jump to <b>
                a, b = g(), g()
                if v(a):
                    self.ip = v(b)
            case 8:  # jf: 8 a b; if <a> is zero, jump to <b>
                a, b = g(), g()
                if not v(a):
                    self.ip = v(b)
            case 9:  # add: 9 a b c; assign into <a> the sum of <b> and <c> (modulo 32768)
                a, b, c = g(), g(), g()
                self.memory[a] = (v(b) + v(c)) % 32768
            case 10:  # mult: 10 a b c; store into <a> the product of <b> and <c> (modulo 32768)
                a, b, c = g(), g(), g()
                self.memory[a] = (v(b) * v(c)) % 32768
            case 11:  # mod: 11 a b c; store into <a> the remainder of <b> divided by <c>
                a, b, c = g(), g(), g()
                self.memory[a] = v(b) % v(c)
            case 12:  # and: 12 a b c; stores into <a> the bitwise and of <b> and <c>
                a, b, c = g(), g(), g()
                self.memory[a] = v(b) & v(c)
            case 13:  # or: 13 a b c; stores into <a> the bitwise or of <b> and <c>
                a, b, c = g(), g(), g()
                self.memory[a] = v(b) | v(c)
            case 14:  # not: 14 a b; stores 15-bit bitwise inverse of <b> in <a>
                a, b = g(), g()
                self.memory[a] = ((1 << 15) - 1) & ~v(b)
            case 15:  # rmem: 15 a b; read memory at address <b> and write it to <a>
                a, b = g(), g()
                # memory[a] = get(b)
                self.memory[a] = self.memory[v(b)]
                # memory[a] = memory[b]
            case 16:  # wmem: 16 a b; write the value from <b> into memory at address <a>
                a, b = g(), g()
                self.memory[v(a)] = v(b)
            case 17:  # call: 17 a; write the address of the next instruction to the self.stack and jump to <a>
                a = g()
                self.stack.append(self.ip)
                self.ip = v(a)
            case 18:  # ret: 18; remove the top element from the self.stack and jump to it; empty self.stack = halt
                if not self.stack:
                    self.state = State.HALTED
                else:
                    self.ip = self.stack.pop()
            case 19:  # out: 19 a; write the character represented by ascii code <a> to the terminal
                a = g()
                self.writer.write(chr(v(a)))
            case 20:  # in: 20 a; read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard instead of having to figure out how to read individual characters
                a = g()
                ch = self.reader.read(1)
                if not ch:
                    self.state = State.INPUT_BLOCKED
                    self.ip -= 2
                else:
                    self.memory[a] = ord(ch)
            case 21:  # noop: 21; no operation
                pass

    def resume(self) -> None:
        print("--- Resuming VM ---")

        while True:
            self.step()
            print(self.output(), end="")

            if self.state == State.INPUT_BLOCKED:
                inp = input()
                self.input(inp + "\n")
            elif self.state != State.READY:
                break
        print("--- VM Exited ---")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("vm")
    parser.add_argument(
        "file", help="Path of bin file.", default="./challenge.bin", type=str, nargs="?"
    )
    args = parser.parse_args()

    vm = Vm.from_file(args.file)

    vm.resume()
