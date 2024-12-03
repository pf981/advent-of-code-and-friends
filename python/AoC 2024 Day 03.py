from aocd import get_data, submit
import re


inp = get_data(day=3, year=2024)

# inp = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# '''
# inp = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# '''

lines = inp.splitlines()

def mul(a, b):
    return a * b
answer1 = 0
for line in lines:
    for x in re.findall(r'mul\([0-9]+,[0-9]+\)', line):
        # print(x)
        answer1 += eval(x)


# answer1 = 'todo'
print(answer1)

# submit(answer1, part='a', day=3, year=2024)


# Part 2
def mul(a, b):
    return a * b
doing = True
def do():
    global doing
    doing = True
    return 0
def donXt():
    global doing
    doing = False
    return 0

answer2 = 0
for line in lines:
    line = line.replace("'", 'X')
    for x in re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|donXt\(\)', line):
        # print(x)
        result = eval(x)
        if doing:
            answer2 += result



# answer2 = 'todo'
print(answer2)

submit(answer2, part='b', day=3, year=2024)
