with open("./2025/input/everybody_codes_e2025_q19_p1.txt") as f:
    lines = f.read().splitlines()

passages = [[int(s) for s in line.split(",")] for line in lines]
m = {x: (y, w) for x, y, w in passages}
target = passages[-1][0]


def dfs(x: int, y: int) -> int | None:
    if x in m:
        py, pw = m[x]
        if not (py <= y < py + pw):
            return None

    if x == target:
        return 0

    res = dfs(x + 1, y - 1)
    if res is not None:
        return res

    res = dfs(x + 1, y + 1)
    return 1 + res if res is not None else None


answer = dfs(0, 0)
print(answer)
