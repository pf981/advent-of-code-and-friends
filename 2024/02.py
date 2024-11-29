import re

with open("./2024/input/everybody_codes_e2024_q02_p1.txt") as f:
    lines = f.read().splitlines()

# lines[0] = "WORDS:THE,OWE,MES,ROD,HER"
# lines[2] = "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"

words = set(lines[0].split(':')[1].split(','))

# text = re.split(r'[^A-Z]', lines[2])
text = lines[2]
answer1 = 0
for s in words:
    answer1 += len(re.findall(s, text))
print(answer1)


with open("./2024/input/everybody_codes_e2024_q02_p2.txt") as f:
    lines = f.read().splitlines()

# lines[0] = "WORDS:THE,OWE,MES,ROD,HER"
# lines[2] = "AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"
# lines = lines[:3]
# lines = '''WORDS:THE,OWE,MES,ROD,HER,QAQ

# AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
# THE FLAME SHIELDED THE HEART OF THE KINGS
# POWE PO WER P OWE R
# THERE IS THE END
# QAQAQ'''.splitlines()

words = set(lines[0].split(':')[1].split(','))
for word in words.copy():
    words.add(word[::-1])


text = lines[2:]
answer2 = 0
for line in text:
    indexes = set()
    for word in words:
        for m in re.finditer(f'(?=({word}))', line):
        # for m in re.finditer(word, line):
            # start, end = m.span()
            # for i in range(start, end):
            for i in range(m.start(), m.start() + len(word)):
                indexes.add(i)
    print(f'{len(indexes)=}')
    answer2 += len(indexes)
print(answer2)

# list(re.finditer('hi', 'ohi!'))


import itertools

with open("./2024/input/everybody_codes_e2024_q02_p3.txt") as f:
    lines = f.read().splitlines()

# # FIXME: Testing
# lines = '''WORDS:THE,OWE,MES,ROD,RODEO

# HELWORLT
# ENIGWDXL
# TRODEOAL'''.splitlines()

words = set(lines[0].split(':')[1].split(','))
for word in words.copy():
    words.add(word[::-1])

text = lines[2:]

nrows = len(text)
ncols = len(text[0])

scales = set() # (r, c)
for r in range(nrows):
    for c in range(ncols):
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            cur_words = words.copy()
            to_add = set()
            for i in itertools.count():
                r2 = (r + dr*i)
                c2 = (c + dc*i) % ncols
                if not (0 <= r2 < nrows):
                    break
                to_add.add((r2, c2))
                # print(f'{to_add=}')
                for word in cur_words.copy():
                    if word[i] == text[r2][c2] and i == len(word) - 1:
                        scales.update(to_add)
                        cur_words.remove(word)
                    elif word[i] != text[r2][c2]:
                        cur_words.remove(word)
                if not cur_words:
                    break
answer3 = len(scales)
print(answer3)
