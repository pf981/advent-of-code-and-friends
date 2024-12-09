from aocd import get_data

inp = get_data(day=8, year=2018)

def value(nums, is_part2=False):
  n_children = nums.pop(0)
  n_meta = nums.pop(0)
  children = [value(nums, is_part2) for _ in range(n_children)]
  meta = [nums.pop(0) for _ in range(n_meta)]

  if not is_part2:
    return sum(meta) + sum(children)
  else:
    return sum(children[i - 1] for i in meta if i <= len(children)) if children else sum(meta)

nums = [int(x) for x in inp.split(' ')]

answer = value(nums.copy())
print(answer)

answer = value(nums.copy(), is_part2=True)
print(answer)
