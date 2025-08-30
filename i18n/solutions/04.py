from datetime import datetime, timedelta
import re
from zoneinfo import ZoneInfo


def parse_time(line: str) -> datetime:
    _, tz_str, dt_str = re.split(r" +", line, maxsplit=2)
    dt = datetime.strptime(dt_str, "%b %d, %Y, %H:%M")
    tz = ZoneInfo(tz_str)
    return dt.replace(tzinfo=tz)


with open("./input/04.txt", encoding="utf-8") as f:
    text = f.read()

answer = 0
for flight_info in text.split("\n\n"):
    depart, arrive = (parse_time(line) for line in flight_info.splitlines())
    answer += (arrive - depart) // timedelta(minutes=1)

print(answer)
