from aocd import get_data, submit
import re


inp = get_data(day=5, year=2023)
seeds, *maps_list = inp.split('\n\n')
seeds = [int(x) for x in re.findall(r'\d+', seeds)]
maps_list = [[[int(x) for x in re.findall(r'\d+', line)] for line in maps.splitlines()[1:]] for maps in maps_list]

locations = []
for seed in seeds:
    for maps in maps_list:
        for dest_start, source_start, range_len in maps:
            if source_start <= seed < source_start + range_len:
                seed = dest_start + (seed - source_start)
                break
    locations.append(seed)

answer1 = min(locations)
print(answer1)

submit(answer1, part='a', day=5, year=2023)


# Part 2


def insert_missing_ranges(maps):
    maps.sort(key=lambda e: e[1])
    first_val = maps[0][1]
    if first_val != 0:
        maps.insert(0, [0, 0, first_val])
    
    last_val = maps[-1][1] + maps[-1][2]
    maps.append([last_val, last_val, 10_000_000_000])

    for i in range(len(maps) - 1):
        end = maps[i][1] + maps[i][2]
        start = maps[i+1][1]
        if end != start:
            maps.append((end, end, start - end))

    maps.sort(key=lambda e: e[1])


def get_smallest_range(i, in_start, in_range_len):
    if i == len(maps_list):
        return in_start

    output_ranges = [] # (out_start, out_range_len) pairs
    for dest_start, source_start, range_len in maps_list[i]:
        # No overlap
        if source_start + range_len <= in_start or source_start >= in_start + in_range_len:
            continue
        
        # Assume overlap
        if source_start == in_start: # Source starts at input start
            overlap_start = in_start
            overlap_range_len = min(range_len, in_range_len)
        elif source_start < in_start: # Source starts to left
            overlap_start = in_start
            overlap_end = min(source_start + range_len, in_start + in_range_len)
            overlap_range_len = overlap_end - in_start
        else: # Source starts to right of input start
            overlap_start = source_start
            overlap_end = min(source_start + range_len, in_start + in_range_len)
            overlap_range_len = overlap_end - source_start

        overlap_start = overlap_start - source_start +  dest_start
        output_ranges.append((overlap_start, overlap_range_len))

    outputs = [get_smallest_range(i + 1, out_start, out_range_len) for out_start, out_range_len in output_ranges]
    return min(outputs) if outputs else float('inf')


for maps in maps_list:
    insert_missing_ranges(maps)

starting_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
answer2 = min(get_smallest_range(0, in_start, in_range_len) for in_start, in_range_len in starting_ranges)
print(answer2)

submit(answer2, part='b', day=5, year=2023)
