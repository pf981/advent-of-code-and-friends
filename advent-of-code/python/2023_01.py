from aocd import get_data, submit


def first_value(line, m):
  for i, _ in enumerate(line):
    for text, val in m.items():
      if line[i:].startswith(text):
        return val


inp = get_data(day=1, year=2023)
lines = inp.splitlines()
m = {c: int(c) for c in '123456789'}

answer1 = sum(10 * first_value(line, m) + first_value(line[::-1], m) for line in lines)
print(answer1)

submit(answer1, part='a', day=1, year=2023)


# Part 2


m.update({
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
})
rev_m = {text[::-1]: value for text, value in m.items()}

answer2 = sum(10 * first_value(line, m) + first_value(line[::-1], rev_m) for line in lines)
print(answer2)

submit(answer2, part='b', day=1, year=2023)
