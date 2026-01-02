import heapq

smaller = []
bigger = []
n_smaller = n_bigger = 0


def add_toy(num: int) -> None:
    global n_smaller, n_bigger

    # Insert into appropriate side
    if smaller and num <= -smaller[0][0]:
        n_smaller += num
        heapq.heappush(smaller, (-num, num))
    else:
        n_bigger += num
        heapq.heappush(bigger, (num, num))

    # Rebalance
    while n_smaller > n_bigger:
        to_move = (n_smaller - n_bigger + 1) // 2
        neg_num, count = heapq.heappop(smaller)

        to_move = min(to_move, count)
        if count - to_move:
            heapq.heappush(smaller, (neg_num, count - to_move))
        heapq.heappush(bigger, (-neg_num, to_move))
        n_smaller -= to_move
        n_bigger += to_move

    while n_bigger > n_smaller + 1:
        to_move = (n_bigger - n_smaller) // 2
        num, count = heapq.heappop(bigger)

        to_move = min(to_move, count)
        if count - to_move:
            heapq.heappush(bigger, (num, count - to_move))
        heapq.heappush(smaller, (-num, to_move))
        n_bigger -= to_move
        n_smaller += to_move


def pop_median() -> int:
    global n_smaller, n_bigger

    median, count = heapq.heappop(bigger)

    n_bigger -= 1
    if count - 1:
        heapq.heappush(bigger, (median, count - 1))

    # Move from smaller to bigger if required
    if n_smaller > n_bigger:
        neg_num, count = heapq.heappop(smaller)
        if count - 1:
            heapq.heappush(smaller, (neg_num, count - 1))
        heapq.heappush(bigger, (-neg_num, 1))
        n_bigger += 1
        n_smaller -= 1

    return median


with open("data/day15.txt") as f:
    text = f.read()

mul = 1
answer = 0
for line in text.splitlines():
    if line == "request":
        median = pop_median()
        answer += mul * median
        mul += 1
        continue

    num = int(line.split()[1])
    add_toy(num)

print(answer)
