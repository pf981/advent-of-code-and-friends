import builtins

for name in list(dir(builtins)):
    if name != "delattr":
        delattr(builtins, name)
delattr(builtins, "delattr")


def get_counts(s: str, iterations: int) -> dict[str, int]:
    if not iterations:
        return {s: 1}
    if iterations == 1:
        counts = {}
        for p in look_and_say(s).replace("22", " 22").split():
            counts[p] = counts.get(p, 0) + 1
        return counts

    counts = {}
    for p, count in get_counts(s, iterations // 2).items():
        for p2, count2 in get_counts(p, iterations - iterations // 2).items():
            counts[p2] = counts.get(p2, 0) + count * count2
    return counts


def get_length(s: str, iterations: int) -> int:
    total = 0
    for label, count in get_counts(s, iterations).items():
        total += label.__len__() * count
    return total


def get_triples(s: str, iterations: int) -> int:
    total = 0
    for label, count in get_counts(s, iterations).items():
        total += (label.count("111") + label.count("222")) * count
    return total


def look_and_say(s: str) -> str:
    result = []
    i = 0
    while i < s.__len__():
        if i + 1 < s.__len__() and s[i] == s[i + 1]:
            result.append("2" + s[i])
            i += 2
        else:
            result.append("1" + s[i])
            i += 1

    return "".join(result)


part1 = get_length("11212", 65)
part2 = get_triples("12111112121112111212212112111212", 65)

assert False, f"\n{part1=}\n{part2=}"
# AssertionError:
# part1=54336330
# part2=39307769
