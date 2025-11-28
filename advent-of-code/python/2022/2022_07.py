from aocd import get_data

inp = get_data(day=7, year=2022)

import functools


@functools.cache
def get_size(path):
  if isinstance(path, int):
    return path
  return sum(get_size(obj) for obj in objects[path])


lines = inp.splitlines()
wd = tuple()
objects = {}
while lines:
  args = lines.pop(0).split(' ')[1:]
  
  if args[0] == 'cd':
    if args[1] == '/':
      wd = tuple()
    elif args[1] == '..':
      wd = wd[:-1]
    else:
      wd += (args[1],)
  elif args[0] == 'ls':
    objects[wd] = objects.get(wd, [])
    while lines and lines[0][0] != '$':
      first, second = lines.pop(0).split(' ')
      objects[wd].append(wd + (second,) if first == 'dir' else int(first))

answer = sum(size for path in objects if (size := get_size(path)) <= 100000)
print(answer)

unused = 70000000 - get_size(tuple())
need = 30000000 - unused

answer = min(size for path in objects if (size := get_size(path)) >= need)
print(answer)
