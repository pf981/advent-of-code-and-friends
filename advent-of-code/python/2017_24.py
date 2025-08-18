from aocd import get_data

inp = get_data(day=24, year=2017)

def get_strongest(ports, prev_port=0):
  strongest = 0
  for port in ports:
    if prev_port not in port:
      continue
    remaining = ports.copy()
    remaining.remove(port)
    strength = sum(port) + get_strongest(remaining, port[0] if port[0] != prev_port else port[1])
    strongest = max(strongest, strength)
  return strongest

ports = [[int(x) for x in line.split('/')] for line in inp.splitlines()]

answer = get_strongest(ports)
print(answer)

def get_longest(ports, prev_port=0):
  best_length_strength = (0, 0)
  for port in ports:
    if prev_port not in port:
      continue
    remaining = ports.copy()
    remaining.remove(port)
    
    length, strength = get_longest(remaining, port[0] if port[0] != prev_port else port[1])
    length += 1
    strength += sum(port)
    
    best_length_strength = max(best_length_strength, (length, strength))
  return best_length_strength

answer = get_longest(ports)[1]
print(answer)
