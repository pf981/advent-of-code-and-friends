with open("./input/33.txt") as f:
    text = f.read()

target = int(text.strip())

candidates = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    24,
    25,
    26,
    27,
    28,
    30,
    32,
    33,
    34,
    36,
    38,
    39,
    40,
    42,
    45,
    48,
    50,
    51,
    54,
    57,
    60,
]

dp = list(range(target + 1))
for candidate in candidates:
    if candidate >= len(dp):
        break
    dp[candidate] = 1

for i in range(1, target + 1):
    for candidate in candidates:
        if i - candidate <= 0:
            continue
        dp[i] = min(dp[i], 1 + dp[i - candidate])

answer = sum(dp)
print(answer)
