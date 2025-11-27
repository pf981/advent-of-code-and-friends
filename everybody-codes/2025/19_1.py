with open("./2025/input/everybody_codes_e2025_q19_p1.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """7,7,2
# 12,0,4
# 15,5,3
# 24,1,6
# 28,5,5
# 40,8,2""".splitlines()

psgs = [[int(s) for s in line.split(",")] for line in lines]
m = {x: (y, w) for x, y, w in psgs}
target = psgs[-1][0]


def dfs(x, y):
    if y < 0:  # Maybe?
        return None
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
# answer = "TODO"
print(answer)
