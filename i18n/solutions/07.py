from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

with open("./input/07.txt", encoding="utf-8") as f:
    text = f.read()

halifax_tz = ZoneInfo("America/Halifax")
santiago_tz = ZoneInfo("America/Santiago")

answer = 0
for i, line in enumerate(text.splitlines(), 1):
    ts_str, mins1_str, mins2_str = line.split()

    dt = datetime.fromisoformat(ts_str)
    dt = (
        dt - timedelta(minutes=int(mins2_str)) + timedelta(minutes=int(mins1_str))
    ).astimezone(
        halifax_tz if dt.utcoffset() == halifax_tz.utcoffset(dt) else santiago_tz
    )
    answer += dt.hour * i

print(answer)
