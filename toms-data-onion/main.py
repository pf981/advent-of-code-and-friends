import base64
import collections
import ctypes
import io
import ipaddress
import itertools
import pathlib
import string

from typing import Callable


PAYLOAD_SEP = "==[ Payload ]===============================================\n\n"
DATA_PATH = pathlib.Path("./data/")


def get_payload(layer: int) -> bytes:
    path = DATA_PATH / f"{layer:>02}.txt"
    with open(path) as f:
        text = f.read()

    payload = text.split(PAYLOAD_SEP)[1].strip()
    return base64.a85decode(payload, adobe=True)


def process(layer: int, decrypt_fn: Callable[[bytes], bytes]) -> None:
    payload = get_payload(layer - 1)
    plaintext = decrypt_fn(payload).decode("utf-8")
    path = DATA_PATH / f"{layer:>02}.txt"

    with open(path, "w", newline="") as f:
        f.write(plaintext)


def decrypt1(data: bytes) -> bytes:
    """
    This payload has been encoded with Adobe-flavoured ASCII85.
    """
    return data


def decrypt2(data: bytes) -> bytes:
    """
    Like all the layers, the payload is again encoded with
    Adobe-flavoured ASCII85. After ASCII85 decoding the payload,
    apply the following operations to each byte:

      1. Flip every second bit
      2. Rotate the bits one position to the right
    """
    output = bytearray()
    for byte in data:
        flipped = byte ^ 0b01010101
        rotated = (flipped >> 1) | ((flipped & 1) << 7)
        output.append(rotated)

    return bytes(output)


def decrypt3(data: bytes) -> bytes:
    """
    For each byte of the payload, the seven most significant
    bits carry data, and the least significant bit is the parity
    bit. Combine the seven data bits from each byte where the
    parity bit is correct, discarding bytes where the parity bit
    is incorrect.

    To determine if the parity bit is correct, first count how
    many '1' bits exist within the seven data bits. If the count
    is odd, the parity bit should be '1'. If the count is even,
    the parity bit should be '0'.
    """
    seven_bits_array = bytearray()
    for byte in data:
        parity_bit = byte & 1
        seven_bits = byte >> 1

        if (seven_bits.bit_count() & 1) != parity_bit:
            continue

        seven_bits_array.append(seven_bits)

    cur_byte = 0
    cur_byte_size = 0
    output = bytearray()
    for seven_bits in seven_bits_array:
        if cur_byte_size == 0:
            cur_byte = seven_bits << 1
            cur_byte_size = 7
            continue

        # Guaranteed to fill byte
        to_take = 8 - cur_byte_size
        cur_byte |= seven_bits >> (7 - to_take)
        output.append(cur_byte & 0b1111111)

        cur_byte_size = 7 - to_take
        cur_byte = (seven_bits & ((1 << cur_byte_size) - 1)) << (to_take + 1)

    assert cur_byte_size == 0

    return bytes(output)


def decrypt4(data: bytes) -> bytes:
    """
    The payload has been encrypted by XOR'ing each byte with a
    secret, cycling key. The key is 32 bytes of random data,
    which I'm not going to give you. You will need to use your
    hacker skills to discover what the key is, in order to
    decrypt the payload.
    """
    path = DATA_PATH / "03.txt"
    with open(path) as f:
        text = f.read()
    reference_text = text.split(PAYLOAD_SEP)[0].strip()
    reference_counts = collections.Counter(reference_text.encode("utf-8"))
    s = sum(reference_counts.values())
    reference_freqs = {byte: count / s for byte, count in reference_counts.items()}

    all_freqs = []
    for i in range(32):
        freqs = collections.Counter(data[i:1024:32])
        s = sum(freqs.values())
        for byte in freqs:
            freqs[byte] /= s
        all_freqs.append(freqs)

    key = []
    for freqs in all_freqs:
        best = (float("inf"), 0)  # d, k
        for k in range(256):
            new_freqs = collections.Counter()
            for byte, w in freqs.items():
                new_freqs[byte ^ k] = w

            d = 0
            for byte in set(new_freqs.keys()) | set(reference_freqs.keys()):
                if chr(byte) not in string.printable:
                    d = float("inf")
                    break
                freq1 = new_freqs.get(byte, 0)
                freq2 = reference_freqs.get(byte, 0)
                d += abs(freq1 - freq2)
            best = min(best, (d, k))
        key.append(best[1])

    return bytes(byte ^ k for byte, k in zip(data, itertools.cycle(key)))


def decrypt5(data: bytes) -> bytes:
    """
    The payload for this layer is encoded as a stream of raw
    network data, as if the solution was being received over the
    internet. The data is a series of IPv4 packets with User
    Datagram Protocol (UDP) inside. Extract the payload data
    from inside each packet, and combine them together to form
    the solution.

    However, the payload contains extra packets that are not
    part of the solution. Discard these corrupted and irrelevant
    packets when forming the solution.

    Each valid packet of the solution has the following
    properties. Discard packets that do not have all of these
    properties.

     - The packet was sent FROM any port of 10.1.1.10
     - The packet was sent TO port 42069 of 10.1.1.200
     - The IPv4 header checksum is correct
     - The UDP header checksum is correct

    WARNING: Failing to do this properly WILL cause the next
    layer to be unsolveable. If you include incorrect packets in
    your solution, the result may be readable and look correct,
    but its payload WILL be corrupted in ways that are
    impossible to detect. Trust me.

    The packets appear in the correct order. No reordering is
    necessary.

    IPv4 Header:
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |Version|  IHL  |Type of Service|          Total Length         |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         Identification        |Flags|      Fragment Offset    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Time to Live |    Protocol   |         Header Checksum       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       Source Address                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Destination Address                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Options                    |    Padding    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    UDP Header:
     0      7 8     15 16    23 24    31
    +--------+--------+--------+--------+
    |     Source      |   Destination   |
    |      Port       |      Port       |
    +--------+--------+--------+--------+
    |                 |                 |
    |     Length      |    Checksum     |
    +--------+--------+--------+--------+
    |
    |          data octets ...
    +---------------- ...
    """

    class IPv4Header(ctypes.BigEndianStructure):
        _pack_ = 1
        _fields_ = [
            ("version", ctypes.c_uint8, 4),
            ("ihl", ctypes.c_uint8, 4),
            ("type_of_service", ctypes.c_uint8),
            ("total_length", ctypes.c_uint16),
            ("identification", ctypes.c_uint16),
            ("flags", ctypes.c_uint16, 3),
            ("fragment_offset", ctypes.c_uint16, 13),
            ("time_to_live", ctypes.c_uint8),
            ("protocol", ctypes.c_uint8),
            ("header_checksum", ctypes.c_uint16),
            ("source_address", ctypes.c_uint32),
            ("destination_address", ctypes.c_uint32),
        ]

        def __repr__(self):
            fields = []
            for name, *_ in self._fields_:
                value = getattr(self, name)
                if name.endswith("_address"):
                    value = str(ipaddress.IPv4Address(value))
                fields.append(f"{name}={value}")
            return f"TcpHeader({', '.join(fields)})"

    class UdpHeader(ctypes.BigEndianStructure):
        _pack_ = 1
        _fields_ = [
            ("source_port", ctypes.c_uint16),
            ("destination_port", ctypes.c_uint16),
            ("length", ctypes.c_uint16),
            ("checksum", ctypes.c_uint16),
        ]

        def __repr__(self):
            fields = []
            for name, *_ in self._fields_:
                value = getattr(self, name)
                if name.endswith("_address"):
                    value = str(ipaddress.IPv4Address(value))
                fields.append(f"{name}={value}")
            return f"UdpHeader({', '.join(fields)})"

    def read_struct(stream: io.BytesIO, cls):
        size = ctypes.sizeof(cls)
        data = stream.read(size)
        if len(data) != size:
            raise EOFError(f"Expected {size} bytes, got {len(data)}")
        return cls.from_buffer_copy(data)

    def checksum16(data: bytes) -> int:
        if len(data) % 2 == 1:
            data += b"\x00"

        checksum = 0
        for i in range(0, len(data), 2):
            word = int.from_bytes(data[i : i + 2], "big")
            checksum += word
            checksum = (checksum & 0xFFFF) + (checksum >> 16)

        return ~checksum & 0xFFFF

    stream = io.BytesIO(data)
    stream_out = io.BytesIO()

    while stream.tell() < len(stream.getbuffer()):
        ipv4_header = read_struct(stream, IPv4Header)
        udp_header = read_struct(stream, UdpHeader)
        content = stream.read(udp_header.length - ctypes.sizeof(UdpHeader))

        print(f"\n----\n{ipv4_header=}")
        print(f"\n{udp_header=}\n")
        # print(content.decode())

        # assert ipv4_header.ihl == 5
        assert ipv4_header.total_length == udp_header.length + ctypes.sizeof(IPv4Header)

        if str(ipaddress.IPv4Address(ipv4_header.source_address)) != "10.1.1.10":
            continue
        if str(ipaddress.IPv4Address(ipv4_header.destination_address)) != "10.1.1.200":
            continue
        if udp_header.destination_port != 42069:
            continue

        print("    Source/Dest Correct")

        udp_pseudo_header = b"".join(
            [
                ipv4_header.source_address.to_bytes(4, "big"),
                ipv4_header.destination_address.to_bytes(4, "big"),
                b"\x00",
                ipv4_header.protocol.to_bytes(1, "big"),
                udp_header.length.to_bytes(2, "big"),
            ]
        )
        udp_checksum_data = udp_pseudo_header + bytes(udp_header) + content

        if checksum16(bytes(ipv4_header)) != 0:
            continue
        print("    IPv4 Checksum Correct")
        if checksum16(udp_checksum_data) != 0:
            continue
        print("    UDP Checksum Correct")

        stream_out.write(content)

    print(stream_out.getvalue().decode())
    print(f"----------------------")

    return stream_out.getvalue()


def decrypt6(data: bytes) -> bytes:
    raise NotImplementedError


decrypters = [decrypt1, decrypt2, decrypt3, decrypt4, decrypt5, decrypt6]


def main() -> None:
    for layer, decrypt_fn in enumerate(decrypters, 1):
        process(layer, decrypt_fn)


if __name__ == "__main__":
    main()
