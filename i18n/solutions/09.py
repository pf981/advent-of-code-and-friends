import collections
from datetime import date
import itertools

with open("./input/09.txt", encoding="utf-8") as f:
    text = f.read()

people: collections.defaultdict[str, list[tuple[int, int, int]]] = (
    collections.defaultdict(list)
)
for line in text.splitlines():
    nums_str, names = line.split(": ")
    nums = tuple(int(num) for num in nums_str.split("-"))
    assert len(nums) == 3

    for name in names.split(", "):
        people[name].append(nums)

visited_911 = []
for name, nums_list in people.items():
    for arrangement in itertools.permutations(("day", "month", "year"), 3):
        if arrangement[1] == "year":
            continue
        has_911 = False

        for nums in nums_list:
            kwargs = {arg: val for arg, val in zip(arrangement, nums)}
            kwargs["year"] += 2000
            try:
                date_value = date(**kwargs)
            except ValueError:
                break
            if date_value.isoformat() == "2001-09-11":
                has_911 = True
        else:
            break
    else:
        raise ValueError(f"Unable to find valid arrangement for {name}.")
    if has_911:
        visited_911.append(name)


visited_911.sort()
answer = " ".join(visited_911)
print(answer)
