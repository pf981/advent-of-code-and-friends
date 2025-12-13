_, *games = open(0)

for line in games:
    n, a, b = (int(x) for x in line.split())
    if a + b > n or min(a, b) == 0 and max(a, b) > 0:
        print("NO")
        continue

    nums = list(range(1, n + 1))
    nums2 = nums[a : a + b] + nums[:a] + nums[a + b :]

    print("YES")
    print(*nums)
    print(*nums2)
