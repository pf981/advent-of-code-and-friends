from aocd import get_data

inp = get_data(day=18, year=2020)

import operator

def parse(expression):
  stack = []

  while expression:
    c = expression.pop(0)
    if c == ')':
      return stack.pop()
    elif c == '(':
      expression.insert(0, str(parse(expression)))
    elif c.isdigit():
      value = int(c)
      if stack:
        f = stack.pop()
        value2 = stack.pop()
        stack.append(f(value2, value))
      else:
        stack.append(value)
    elif c == '+':
      stack.append(operator.add)
    elif c == '*':
      stack.append(operator.mul)

  return stack.pop()


expressions = [list(line) for line in inp.replace(' ', '').splitlines()]
answer = sum(parse(expression) for expression in expressions)
print(answer)

# import re

# class minus_is_multiply:
#   def __init__(self, val):
#     self.val = val

#   def __sub__(self, other):
#     return minus_is_multiply(self.val * other.val)

#   def __add__(self, other):
#     return minus_is_multiply(self.val + other.val)


# def parse(expression):
#   return eval(re.sub(r'(\d+)', r'minus_is_multiply(\1)', expression)).val

  
# expressions = inp.replace('*', '-').splitlines()

# answer = sum(parse(expression) for expression in expressions)
# print(answer)

import math

def process_multiplication(stack):
  return math.prod(value for value in stack if isinstance(value, int))

def parse(expression):
  stack = []

  while expression:
    c = expression.pop(0)
    if c == ')':
      return process_multiplication(stack)
    elif c == '(':
      expression.insert(0, str(parse(expression)))
    elif c.isdigit():
      value = int(c)
      if stack and stack[-1] == operator.add:
        f = stack.pop()
        value2 = stack.pop()
        stack.append(f(value2, value))
      else:
        stack.append(value)
    elif c == '+':
      stack.append(operator.add)
    elif c == '*':
      stack.append(operator.mul)

  return process_multiplication(stack)


expressions = [list(line) for line in inp.replace(' ', '').splitlines()]
answer = sum(parse(expression) for expression in expressions)
print(answer)

# class sub_to_mul_mul_to_add:
#   def __init__(self, val):
#     self.val = val

#   def __sub__(self, other):
#     return sub_to_mul_mul_to_add(self.val * other.val)

#   def __mul__(self, other):
#     return sub_to_mul_mul_to_add(self.val + other.val)


# def parse(expression):
#   return eval(re.sub(r'(\d+)', r'sub_to_mul_mul_to_add(\1)', expression)).val

  
# expressions = inp.replace('*', '-').replace('+', '*').splitlines()

# answer = sum(parse(expression) for expression in expressions)
# print(answer)
