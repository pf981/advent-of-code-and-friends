def get_min_time(
    first_starts: list[int],
    first_durations: list[int],
    second_starts: list[int],
    second_durations: list[int],
) -> int:
    second_start = min(
        start + duration for start, duration in zip(first_starts, first_durations)
    )
    return min(
        max(second_start, start) + duration
        for start, duration in zip(second_starts, second_durations)
    )


with open("input/04.txt") as f:
    text = f.read()


MOD = 100_000_0007

_, wall_starts, wall_durations, _, flood_starts, flood_durations = (
    [int(num) for num in line.split()] for line in text.splitlines()
)

wall_first = get_min_time(wall_starts, wall_durations, flood_starts, flood_durations)
flood_first = get_min_time(flood_starts, flood_durations, wall_starts, wall_durations)

answer = min(wall_first, flood_first) % MOD
print(answer)
