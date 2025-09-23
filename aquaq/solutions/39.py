with open("./input/39.txt") as f:
    text = f.read()

nums = [int(num_str) for num_str in text.strip().split()]
scores = [0, 0]
next_player = [1, 0]

winning_dart_total = 0
player0_wins = 0

i = 0
first_player = 0
player = first_player
while i < len(nums):
    for _ in range(3):
        scores[player] += nums[i]

        if scores[player] == 501:
            # Win
            player0_wins += player == 0
            winning_dart_total += nums[i]

            scores = [0, 0]
            first_player = next_player[first_player]
            player = first_player
            i += 1

            break

        i += 1
    else:
        player = next_player[player]

answer = player0_wins * winning_dart_total
print(answer)
