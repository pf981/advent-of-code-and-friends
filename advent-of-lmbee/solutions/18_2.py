def does_match(pattern: str, target: str) -> bool:
    for a, b in zip(pattern, target):
        if a not in (b, "?"):
            return False
    return True


with open("data/day18.txt") as f:
    text = f.read()

patterns, target = text.split("\n\n")
_, *patterns = patterns.splitlines()
_, target = target.splitlines()
pattern = "".join(patterns)

n = len(target)
shifts = [i for i in range(1, n + 1) if target[i:] == target[:-i]]

dp = []
dp2 = []

for i in range(len(pattern) - n):
    result = 0
    if does_match(pattern[i : i + n], target):
        result = 1
        for s in shifts:
            if i - s >= 0 and i - s < len(dp):
                result = max(result, dp[i - s] + 1)
        if i - n >= 0 and i - n < len(dp2):
            result = max(result, dp2[i - n] + 1)
    dp.append(result)
    dp2.append(max(dp2[-1], result) if dp2 else result)
answer = dp[-1]
print(answer)
