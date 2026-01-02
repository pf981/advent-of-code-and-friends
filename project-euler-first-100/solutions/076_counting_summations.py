target = 100
num_ways = [0] * (target + 1)
num_ways[0] = 1

for i in range(1, target + 1):
    for cur_target in range(i, target + 1):
        num_ways[cur_target] += num_ways[cur_target - i]

answer = num_ways[target] - 1
print(answer)
