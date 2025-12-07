import base64
import pathlib

from typing import Callable


PAYLOAD_SEP = "==[ Payload ]===============================================\n\n"
DATA_PATH = pathlib.Path("./data/")


def get_payload(layer: int) -> str:
    path = DATA_PATH / f"{layer:>02}.txt"
    with open(path) as f:
        text = f.read()

    return text.split(PAYLOAD_SEP)[1].strip()


def process(layer: int, decrypters: list[Callable[[bytes], bytes]]) -> None:
    payload = get_payload(layer - 1).encode()
    for i in range(layer):
        payload = decrypters[i](payload)
    plaintext = payload.decode("utf-8")
    path = DATA_PATH / f"{layer:>02}.txt"

    with open(path, "w", newline="") as f:
        f.write(plaintext)


def decrypt1(data: bytes) -> bytes:
    """
    This payload has been encoded with Adobe-flavoured ASCII85.
    """
    return base64.a85decode(data[2:-2])


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
    output = bytearray()
    cur_byte = 0
    cur_byte_size = 0
    for byte in data:
        parity_bit = byte & 1
        byte >>= 1

        if (byte.bit_count() & 1) != parity_bit:
            continue

        # Take at most 7 bits from this byte and add it to cur_byte
        # If cur_byte is size 8, append to output, Update cur_byte with the remaining if any
        raise NotImplementedError
        # to_take = max(8 - cur_byte_size, 7)
        # cur_byte_size += to_take

        # if to_take < 7:
        #     cur_byte

        # if cur_byte_size == 8:
        #     output.append(cur_byte)
        #     cur_byte = 0
        #     cur_byte_size = 0

    return bytes(output)


def decrypt4(data: bytes) -> bytes:
    raise NotImplementedError


def decrypt5(data: bytes) -> bytes:
    raise NotImplementedError


def decrypt6(data: bytes) -> bytes:
    raise NotImplementedError


decrypters = [decrypt1, decrypt2, decrypt3, decrypt4, decrypt5, decrypt6]


def main() -> None:
    for layer in range(1, 7):
        process(layer, decrypters)


if __name__ == "__main__":
    main()
