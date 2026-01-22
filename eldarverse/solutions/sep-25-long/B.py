with open("./input/problem-sep-25-long-B-input.txt") as f:
    text = f.read()

# text = """2
# 2 0
# 3 2"""

n_queries, *queries = text.splitlines()
assert int(n_queries) == len(queries)

result = []
for i, query in enumerate(queries, 1):
    n, k = (int(x) for x in query.split())

    assert 2 <= n <= 6
    assert 0 <= k <= 9

    sparse_count = 0

    max_permutation = (1 << (n * (n - 1))) - 1
    for permuation in range(max_permutation + 1):
        scores = [0] * n

        for home in range(n):
            games = permuation >> ((n - 1) * home)
            games &= (1 << n) - 1
            scores[home] += games.bit_count()

            mask = 1
            for away in range(n):
                scores[n - away - 1] += (games & mask) == 0
                if home == away:
                    continue
                mask <<= 1

        sparse_count += max(scores) - min(scores) > k

    result.append(f"Case #{i}: {sparse_count}")

print("\n".join(result))

# with open("./output/B.txt", "w") as f:
#     f.write("\n".join(result))
