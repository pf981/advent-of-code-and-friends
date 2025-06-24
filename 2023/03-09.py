import downloader


def parse_packet(packet: str) -> tuple[int, ...]:
    result = []
    for w in [16, 32, 8, 8, 192]:
        w = w // 4
        result.append(int(packet[:w], 16))
        packet = packet[w:]
    return tuple(result)


def get_message(packet: str) -> tuple[int, str] | None:
    header, sender, seq_number, checksum, message = parse_packet(packet)

    if header != int("5555", 16):
        return None

    byte_list = message.to_bytes(24, byteorder="big")
    if sum(byte_list) % 256 != checksum:
        return None

    return seq_number, byte_list.decode("utf-8")


lines = downloader.get_puzzle(21).splitlines()

messages = [message for packet in lines if (message := get_message(packet))]
messages.sort()

answer = "".join(message for _, message in messages)
print(answer)
