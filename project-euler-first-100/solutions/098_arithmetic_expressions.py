import functools
import itertools
import math


def count_streak(nums: list[int]) -> tuple[int, str]:
    @functools.cache
    def get_outputs(used: int) -> frozenset[int]:
        result = set()
        for root_i in range(4):
            if used & (1 << root_i):
                continue
            root = nums[root_i]

            used2 = used | (1 << root_i)
            if used2 == 0b1111:
                return frozenset([root])

            rest = get_outputs(used2)

            # +-*/
            for child in rest:
                result.add(root + child)
                result.add(root - child)
                result.add(child - root)
                result.add(root * child)
                if child:
                    result.add(root / child)
                if root:
                    result.add(child / root)

        return frozenset(result)

    outputs = get_outputs(0)
    # print("\n".join(str(o) for o in sorted(outputs)))
    result = set()
    for num in outputs:
        num_int = round(num)
        if math.isclose(num, num_int):
            result.add(num_int)

    for i in itertools.count(1):
        if i not in result:
            return i - 1, "".join(str(num) for num in nums)


best = 0, ""
for a in range(10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                best = max(best, count_streak([a, b, c, d]))

answer = best[1]
print(answer)
