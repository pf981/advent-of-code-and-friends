from aocd import get_data

inp = get_data(day=4, year=2018)

import collections
import datetime as dt
import re

def inclusive_datetime_range(start, end, delta=dt.timedelta(minutes=1)):
    while start <= end:
        yield start
        start += delta

def get_sleep_minutes(events):
  sleep_minutes = collections.defaultdict(lambda: collections.defaultdict(int))

  # for timestamp in sorted(events):
  for timestamp in inclusive_datetime_range(min(events), max(events)):
    if events[timestamp].startswith('Guard'):
      guard = int(re.findall(r'\d+', events[timestamp])[0])
      is_sleeping = False
    elif events[timestamp] == 'wakes up':
      is_sleeping = False
    elif events[timestamp] == 'falls asleep':
      is_sleeping = True
    
    if is_sleeping:
      sleep_minutes[guard][timestamp.minute] += 1

  return sleep_minutes

events = collections.defaultdict(
  str,
  {dt.datetime.fromisoformat(timestamp): event for timestamp, event in [re.findall(r'\[(.+)\] (.+)', line)[0] for line in inp.splitlines()]}
)

sleep_minutes = get_sleep_minutes(events)
laziest_guard, laziest_guard_minutes = max(sleep_minutes.items(), key=lambda x: sum(x[1].values()))
laziest_guard_minute, _ = max(laziest_guard_minutes.items(), key=lambda x: x[1])

answer = laziest_guard * laziest_guard_minute
print(answer)

laziest_guard2, laziest_guard_minutes2 = max(sleep_minutes.items(), key=lambda x: max(x[1].values()))
laziest_guard_minute2, _ = max(laziest_guard_minutes2.items(), key=lambda x: x[1])

answer = laziest_guard2 * laziest_guard_minute2
print(answer)
