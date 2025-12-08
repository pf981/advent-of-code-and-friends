import base64
import collections
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
    raise NotImplementedError


def decrypt6(data: bytes) -> bytes:
    raise NotImplementedError


decrypters = [decrypt1, decrypt2, decrypt3, decrypt4, decrypt5, decrypt6]


def main() -> None:
    for layer, decrypt_fn in enumerate(decrypters, 1):
        process(layer, decrypt_fn)


if __name__ == "__main__":
    main()
