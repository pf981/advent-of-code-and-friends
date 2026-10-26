import heapq
import re
from dataclasses import dataclass


@dataclass
class State:
    tools_available: set[int]


with open("./input/10.txt") as f:
    text = f.read()
# text = """J1
# OP1 M2 T21 D42
# OP2 M7 T22 D42

# J2
# OP1 M2 T1 D1
# OP2 M2 T21 D5
# OP3 M2 T5 D77

# J3
# OP1 M1 T21 D6"""

jobs = []
for job_str in text.split("\n\n"):
    job = []
    for op in job_str.splitlines()[1:]:
        job.append([int(s) for s in re.findall(r"\d+", op)])
    jobs.append(job)

heap = []
# tools_available = set(range(1, 25))
tools_available = set(range(1, 100))
tools_ready = set()
part_r = part_c = 0
t = 0
op_done = False


def process_event():
    global part_r, part_c, t, op_done

    assert heap
    t, event_type, *args = heapq.heappop(heap)
    print(f"{t=} {event_type=} {args=}")

    match event_type:
        case "move_part":
            part_r, part_c = args
        case "tool_ready":
            (tool_id,) = args
            tools_ready.add(tool_id)
        case "op_done":
            op_done = True
            tools_ready.clear()  # DEBUG
        case "tool_available":
            (tool_id,) = args
            tools_available.add(tool_id)
        case _:
            raise ValueError(f"Unknown event_type {t=} {event_type=} {args=}")


machine_positions = []
machine_id = 0
for r in range(5):
    for c in range(5):
        machine_positions.append((r, c))
        machine_id += 1

answer = 0
for job in jobs:
    t = 0

    assert tools_available == set(range(1, 100))  # set(range(1, 25))
    assert tools_ready == set()
    assert part_r == part_c == 0
    assert t == 0
    assert not op_done

    for op_id, machine_id, tool_id, d in job:
        machine_pos = machine_positions[machine_id]

        # Send part to machine
        heapq.heappush(
            heap,
            (
                t + abs(machine_pos[0] - part_r) + abs(machine_pos[1] - part_c),
                "move_part",
                *machine_pos,
            ),
        )

        while tool_id not in tools_available:
            process_event()

        # Send tool to machine
        heapq.heappush(heap, (t + sum(machine_pos), "tool_ready", tool_id))

        # Wait for part
        while (part_r, part_c) != machine_pos:
            process_event()

        # Wait for tool
        while tool_id not in tools_ready:
            process_event()

        # Do job
        heapq.heappush(heap, (t + d, "op_done"))

        op_done = False
        while not op_done:
            process_event()
        op_done = False

        # Send tool to stage
        heapq.heappush(heap, (t + sum(machine_pos), "tool_available", tool_id))

    # Send part to stage
    heapq.heappush(heap, (t + part_r + part_c, "move_part", 0, 0))

    while heap:
        process_event()

    print(f"Job finished at {t=}")
    answer += t
    # break  # DEBUG

print(answer)
# 4059 wrong
