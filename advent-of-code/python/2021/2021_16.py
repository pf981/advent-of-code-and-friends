from aocd import get_data

inp = get_data(day=16, year=2021)

import collections
import math


def bin_to_int(binary):
  return int(''.join(binary), 2)


def take_binary(binary, n):
  return collections.deque(binary.popleft() for _ in range(n))


def take_int(binary, n):
  return bin_to_int(take_binary(binary, n))


def parse_literal(binary):
  result = []
  do_continue = True
  while do_continue:
    do_continue = take_int(binary, 1)
    result.extend(take_binary(binary, 4, ))
      
  return [bin_to_int(result)]


def parse_operator_n_bits(binary):
  total_length = take_int(binary, 15)
  subpackets = take_binary(binary, total_length)
  
  result = []
  while subpackets:
    result.append(parse_packet(subpackets))

  return result


def parse_operator_n_subpackets(binary):
  n_subpackets = take_int(binary, 11)
  
  return [parse_packet(binary) for _ in range(n_subpackets)]


def parse_packet(binary):
  global global_version_sum
  
  version = take_int(binary, 3)
  global_version_sum += version
  
  type_id = take_int(binary, 3)
  
  if type_id == 4:
    parser = parse_literal
  elif take_int(binary, 1) == 0:
    parser = parse_operator_n_bits
  else:
    parser = parse_operator_n_subpackets
    
  subpackets = parser(binary)
  
  f = [
    sum,
    math.prod,
    min,
    max,
    lambda l: l[0],
    lambda l: l[0] > l[1],
    lambda l: l[0] < l[1],
    lambda l: l[0] == l[1]
  ][type_id]

  return f(subpackets)


def evaluate(transmission):
  binary = collections.deque(bin(int(transmission, 16))[2:])

  while len(binary) % 4 != 0:
    binary.appendleft('0')

  return parse_packet(binary)


global_version_sum = 0
evaluation = evaluate(inp)

answer = global_version_sum
print(answer)

answer = evaluation
print(answer)
