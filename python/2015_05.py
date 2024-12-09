from aocd import get_data

inp = get_data(day=5, year=2015)

import re

answer = sum(1 for x in inp.split('\n') if len(re.findall(r'[aeiou]', x)) >= 3 and re.search(r'(.)\1', x) and not re.search(r'ab|cd|pq|xy', x))
answer

answer = sum(1 for x in inp.split('\n') if re.search(r'(..).*\1', x) and re.search(r'(.).\1', x))
answer
