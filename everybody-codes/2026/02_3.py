with open("./2026/input/everybody_codes_e2026_q02_p3.txt") as f:
    lines = f.read().splitlines()
NODES = "123456789"


def order(m: dict[str, list[str]]) -> str:
    result = []
    seen = set()

    def dfs(node: str) -> None:
        if node in seen:
            return
        seen.add(node)

        for node2 in m[node]:
            dfs(node2)
        result.append(node)

    for node in NODES:
        dfs(node)

    return "".join(result)


answer = 0
for line in lines:
    m = {node: [] for node in NODES}
    for a, op, b in line.split():
        if op == ">":
            a, b = b, a
        m[a].append(b)

    answer += int(order(m))


print(answer)
