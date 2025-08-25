target = 3 / 7

min_distance = None
for denominator in range(1, 1_000_000 + 1):
    numerator = int(denominator * target)
    fraction = numerator / denominator

    if fraction >= target:
        numerator -= 1
        fraction = numerator / denominator

    distance = target - fraction

    if not min_distance or distance < min_distance:
        min_distance = distance
        answer = numerator

print(answer)
