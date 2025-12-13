import itertools

n = int(input())

used_col = [set() for _ in range(n)]

for _ in range(n):
    row = []
    used_row = set()
    for col in range(n):
        for num in itertools.count():
            if num in used_col[col] or num in used_row:
                continue

            used_col[col].add(num)
            used_row.add(num)
            row.append(num)
            break

    print(*row)
