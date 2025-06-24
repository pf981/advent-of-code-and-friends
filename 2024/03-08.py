import downloader

text = downloader.get_puzzle(32)

distance_lines, route_lines = (part.splitlines() for part in text.split("\n\n"))
pois = distance_lines[0].split()

m = {}
for line, poi in zip(distance_lines[1:], pois):
    for d, poi2 in zip(line.split()[1:], pois):
        m[(poi, poi2)] = int(d)

answer = 0
for line in route_lines:
    _, route_str = line.split(": ")
    route = route_str.split(" -> ")

    poi = "base"
    for next_poi in route:
        answer += m[(poi, next_poi)]
        poi = next_poi

print(answer)
