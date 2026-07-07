import collections

MOD = 1_000_000_007

with open("input/03.txt") as f:
    text = f.read()

s, target = text.splitlines()

target_counts = collections.Counter(target)
counts = collections.Counter()
answer = l = 0
for r in range(len(s)):
    counts[s[r]] += 1

    if r - l + 1 > len(target):
        counts[s[l]] -= 1
        if not counts[s[l]]:
            del counts[s[l]]
        l += 1

    if counts == target_counts:
        answer = (answer + l) % MOD

print(answer)
