import downloader


lines = downloader.get_puzzle(6).splitlines()

reg = {ch: 0 for ch in "ABCDEFGHIJKL"}
last_if = False
ip = 0
output = []


def get(source: str) -> int:
    if source in reg:
        return reg[source]
    return int(source)


while True:
    match lines[ip].split():
        case ["ADD", target, source]:
            reg[target] += get(source)
        case ["MOD", target, source]:
            reg[target] %= get(source)
        case ["DIV", target, source]:
            reg[target] //= get(source)
        case ["MOV", target, source]:
            reg[target] = get(source)
        case ["JMP", source]:
            ip += get(source)
            continue
        case ["JIF", source]:
            if last_if:
                ip += get(source)
                continue
        case ["CEQ", source1, source2]:
            last_if = get(source1) == get(source2)
        case ["CGE", source1, source2]:
            last_if = get(source1) >= get(source2)
        case ["OUT", source]:
            output.append(get(source))
        case ["END"]:
            break
        case other:
            raise ValueError(f"Unknown op {other}")

    ip += 1

answer = ", ".join(str(s) for s in output)
print(answer)
