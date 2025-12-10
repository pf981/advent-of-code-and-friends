import collections

counts = collections.Counter(input())
result = []
mid = ""
for c in sorted(counts):
    count = counts[c]
    if count % 2:
        if mid:
            print("NO SOLUTION")
            exit(0)
        mid = c
    result.append(c * (count // 2))

result = "".join(result + [mid] + result[::-1])
print(result)
