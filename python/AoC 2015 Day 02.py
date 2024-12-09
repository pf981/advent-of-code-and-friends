from aocd import get_data

inp = get_data(day=2, year=2015)

wrapping_paper_area = 0
ribbon_length = 0

for line in inp.split('\n'):
  l, w, h = (int(x) for x in line.split('x'))
  wrapping_paper_area += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
  ribbon_length += 2 * min(l+w, w+h, h+l) + l*w*h

answer = wrapping_paper_area
answer

answer = ribbon_length
answer
