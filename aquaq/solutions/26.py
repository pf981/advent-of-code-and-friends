def next_largest(n: int) -> int:
    s = str(n)
    for i in reversed(range(len(s) - 1)):
        if s[i] < s[i + 1]:
            j = i + 1
            for k in range(j + 1, len(s)):
                if s[i] < s[k] < s[j]:
                    j = k
            return int(s[:i] + s[j] + "".join(sorted(s[i:j] + s[j + 1 :])))
    return n


with open("./input/26.txt") as f:
    text = f.read()

answer = 0
for line in text.splitlines():
    n = int(line)
    answer += next_largest(n) - n

print(answer)
