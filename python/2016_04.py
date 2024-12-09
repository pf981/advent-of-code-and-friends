from aocd import get_data

inp = get_data(day=4, year=2016)

import re
from collections import Counter

valid_encrypted_names = {}
for encrypted_name, sector_id, checksum in re.findall(r'([\w-]+)-(\d+)\[(\w+)\]', inp):
  letter_counts = Counter(encrypted_name.replace('-', ''))
  actual_checksum = ''.join(sorted(letter_counts, key = lambda letter: (-letter_counts[letter], letter)))[:5]
  if actual_checksum == checksum:
    valid_encrypted_names[encrypted_name] = int(sector_id)
    
answer = sum(valid_encrypted_names.values())
answer

decrypted_names = {
  ''.join((chr(((ord(c) - ord('a') + sector_id) % 26) + ord('a')) if c != '-' else ' ' for c in encrypted_name)): sector_id
  for encrypted_name, sector_id in valid_encrypted_names.items()
}

answer = decrypted_names['northpole object storage']
answer
