from aocd import get_data, submit
import re

inp = get_data(day=12, year=2025)
*presents_str, regions = inp.split("\n\n")

areas = [present_str.count("#") for present_str in presents_str]
answer1 = 0
for line in regions.splitlines():
    w, h, *required = (int(x) for x in re.findall(r"\d+", line))
    required_area = sum(count * areas[i] for i, count in enumerate(required))
    answer1 += required_area <= w * h

submit(answer1, part="a", day=12, year=2025)
