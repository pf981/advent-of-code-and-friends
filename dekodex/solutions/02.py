MOD = 10**9 + 7

with open("input/02.txt") as f:
    text = f.read()

n, *nums = map(int, text.split())

parents = list(range(n))


def union(i: int, j: int) -> None:
    i = find(i)
    j = find(j)
    if i == j:
        return

    if nums[i] > nums[j]:
        i, j = j, i
    parents[i] = j


def find(i: int) -> int:
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


stack = []  # [(i, num), ...]
for i, num in enumerate(nums):
    largest = max(stack[-1][1], num) if stack else num
    while stack and stack[-1][1] > num:
        union(i, stack.pop()[0])
    stack.append((i, largest))

result = [nums[find(i)] for i in range(n)]
answer = sum(result) % MOD
print(answer)
