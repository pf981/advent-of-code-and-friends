from aocd import get_data

inp = get_data(day=7, year=2016)

import re

def is_tls(ip_address):
  insides = re.findall(r'\[(\w+)\]', ip_address)
  outsides = re.findall(r'(\w+)(?:$|\[)', ip_address)

  inside_match = any(re.search(r'(\w)(?!\1)(\w)\2\1', x) for x in insides)
  outside_match = any(re.search(r'(\w)(?!\1)(\w)\2\1', x) for x in outsides)
  
  return outside_match and not inside_match

answer = sum(is_tls(line) for line in inp.split('\n'))
answer

def is_ssl(ip_address):
  insides = re.findall(r'\[(\w+)\]', ip_address)
  outsides = re.findall(r'(\w+)(?:$|\[)', ip_address)

  for outside in outsides:
    for aba in re.finditer(r'(?=((\w)[^\2]\2))', outside):
      bab = aba.group(1)[1:] + aba.group(1)[1]
      if any(bab in x for x in insides):
        return True

  return False
  
answer = sum(is_ssl(line) for line in inp.split('\n'))
answer
