from aocd import get_data

inp = get_data(day=4, year=2017)

answer = sum(1 for line in inp.split('\n') if len(set(line.split(' '))) == len(line.split(' ')))
answer

answer = sum(1 for words in [[tuple(sorted(word)) for word in line.split(' ')] for line in inp.split('\n')] if len(set(words)) == len(words))
answer
