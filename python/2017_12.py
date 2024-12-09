from aocd import get_data

inp = get_data(day=12, year=2017)

def get_linked(program, pipes):
    linked = set()
    remaining = [program]

    while remaining:
        program = remaining.pop()

        if program in linked:
            continue
        linked.add(program)

        for child in pipes[program]:
            remaining.append(child)

    return linked


def get_groups(pipes):
    groups = {}
    remaining = list(pipes.keys())

    while remaining:
        program = remaining.pop()

        if program in groups:
            continue

        linked = get_linked(program, pipes)

        group_name = next(
            (groups[link] for link in linked if link in groups), next(iter(linked))
        )
        for link in linked:
            groups[link] = group_name
    return groups


pipes = {}
for line in inp.split('\n'):
    program, connections = line.split(' <-> ')
    pipes[program] = connections.split(', ')


groups = get_groups(pipes)

answer = sum(group_name == groups['0'] for _, group_name in groups.items())
print(answer)

answer = len(set(groups.values()))
print(answer)
