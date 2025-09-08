import dateutil
import datetime

with open("./input/17.txt") as f:
    text = f.read()

shame_start: dict[str, datetime.date] = {}
longest = (
    0,
    "",
    datetime.date(1960, 1, 1),
    datetime.date(1960, 1, 1),
)  # shame, team, start, end

for line in text.splitlines()[1:]:
    (
        date_str,
        home_team,
        away_team,
        home_score,
        away_score,
        tournament,
        city,
        country,
        neutral,
    ) = line.split(",")

    date = dateutil.parser.parse(date_str)

    for team, score in [(home_team, home_score), (away_team, away_score)]:
        if int(score) == 0:
            if team not in shame_start:
                shame_start[team] = date
        elif team in shame_start:
            longest = max(
                longest,
                ((date - shame_start[team]).days, team, shame_start[team], date),
            )
            del shame_start[team]

answer = f"{longest[1]} {longest[2].strftime('%Y%m%d')} {longest[3].strftime('%Y%m%d')}"
print(answer)
