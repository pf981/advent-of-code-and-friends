import functools

with open("./input/2025/08/input2.txt") as f:
    text = f.read()
shelf = 300

bags = []
for line in text.splitlines()[1:]:
    _, bean, roast, width, rating = line.split(",")
    bags.append((bean, roast, int(width), int(rating)))

bean_masks = {bean: 1 << i for i, bean in enumerate({bean for bean, _, _, _ in bags})}

roast_masks = {
    roast: 1 << i for i, roast in enumerate({roast for _, roast, _, _ in bags})
}
target_used_roast = 0
for mask in roast_masks.values():
    target_used_roast |= mask


@functools.cache
def get_best(i: int, limit: int, used_beans: int, used_roast: int) -> int:
    if limit < 0:
        return float("-inf")
    if i == len(bags):
        if used_roast != target_used_roast:
            return float("-inf")
        return 0

    discard = get_best(i + 1, limit, used_beans, used_roast)

    bean, roast, width, rating = bags[i]
    keep = float("-inf")
    if not (bean_masks[bean] & used_beans):
        keep = rating + get_best(
            i + 1,
            limit - width,
            used_beans | bean_masks[bean],
            used_roast | roast_masks[roast],
        )

    return max(discard, keep)


answer = get_best(0, shelf, 0, 0)
print(answer)
