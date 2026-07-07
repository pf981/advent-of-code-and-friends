import functools

with open("input/09.txt") as f:
    text = f.read()

n, MOD = map(int, text.split())

NCR_MAX = 401
ncr = [[0] * NCR_MAX for _ in range(NCR_MAX)]
for i in range(NCR_MAX):
    ncr[i][0] = 1
    for j in range(1, i + 1):
        ncr[i][j] = (ncr[i - 1][j - 1] + ncr[i - 1][j]) % MOD


@functools.cache
def count_ways(length: int, left_secured: bool, right_secured: bool) -> list[int]:
    # ways[k] is the number of valid sequences using exactly k manual steps
    if length == 0:
        return [1]

    if length == 1:
        if left_secured and right_secured:
            return [1]
        return [0, 1]

    ways = [0] * (length + 1)
    for i in range(length):
        left_ways = count_ways(i, left_secured, True)
        right_ways = count_ways(length - i - 1, True, right_secured)

        for left_steps, left_count in enumerate(left_ways):
            if not left_count:
                continue
            for right_steps, right_count in enumerate(right_ways):
                if not right_count:
                    continue

                ways_to_combine = (left_count * right_count) % MOD
                ways_to_combine = (
                    ways_to_combine * ncr[left_steps + right_steps][left_steps]
                ) % MOD
                steps = left_steps + right_steps + 1
                ways[steps] = (ways[steps] + ways_to_combine) % MOD

    return ways


result = count_ways(n, False, False)
answer = sum(result) % MOD
print(answer)
