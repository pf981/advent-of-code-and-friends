import downloader

lines = downloader.get_puzzle(29).splitlines()


def extract(packet: str, i: int, size: int = 1) -> int:
    return int(packet[(i - 1) * 2 : (i - 1 + size) * 2], 16)


internal_bytes = wifi_bytes = 0
for packet in lines:
    length = extract(packet, 3, 2)

    source = tuple(extract(packet, i) for i in [13, 14, 15, 16])
    dest = tuple(extract(packet, i) for i in [17, 18, 19, 20])

    is_internal = is_wifi = False
    for ip in [source, dest]:
        if (192, 168, 0, 0) <= ip <= (192, 168, 254, 254):
            is_internal = True
        if (10, 0, 0, 0) <= ip <= (10, 0, 254, 254):
            is_wifi = True

    if is_internal:
        internal_bytes += length
    if is_wifi:
        wifi_bytes += length

answer = f"{internal_bytes}/{wifi_bytes}"
print(answer)
