import collections


def get_sparse_count(n: int, k: int):
    dp = collections.Counter()  # points -> ways
    dp[tuple([0] * n)] = 1

    for home in range(n):
        for away in range(n):
            if home == away:
                continue

            dp2 = collections.Counter()
            for points, ways in dp.items():
                dp2[points[:home] + (points[home] + 1,) + points[home + 1 :]] += ways
                dp2[points[:away] + (points[away] + 1,) + points[away + 1 :]] += ways

            dp = dp2

    result = 0
    for points, ways in dp.items():
        if max(points) - min(points) > k:
            result += ways

    return result


with open("./input/problem-sep-25-long-B-input.txt") as f:
    text = f.read()

n_queries, *queries = text.splitlines()
assert int(n_queries) == len(queries)

result = []
for i, query in enumerate(queries, 1):
    n, k = (int(x) for x in query.split())
    print(f"{n=} {k=}")

    assert 2 <= n <= 6
    assert 0 <= k <= 9

    sparse_count = get_sparse_count(n, k)
    result.append(f"Case #{i}: {sparse_count}")

print("\n".join(result))

with open("./output/problem-sep-25-long-B.txt", "w") as f:
    f.write("\n".join(result))
