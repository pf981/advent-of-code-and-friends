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


def process(decrypt_fn: Callable[[str], str], layer: int) -> None:
    cipher = get_payload(layer - 1)
    plaintext = decrypt_fn(cipher)
    path = DATA_PATH / f"{layer:>02}.txt"

    with open(path, "w", newline="") as f:
        f.write(plaintext)


def decrypt1(cipher: str) -> str:
    """
    This payload has been encoded with Adobe-flavoured ASCII85.
    """
    return base64.a85decode(cipher[2:-2]).decode("utf-8")


def decrypt2(cipher: str) -> str:
    """
    Like all the layers, the payload is again encoded with
    Adobe-flavoured ASCII85. After ASCII85 decoding the payload,
    apply the following operations to each byte:

      1. Flip every second bit
      2. Rotate the bits one position to the right
    """
    bytes_ = base64.a85decode(cipher[2:-2])
    nums = []
    for byte in bytes_:
        flipped = byte ^ 0b01010101
        rotated = (flipped >> 1) | ((flipped & 1) << 7)
        nums.append(rotated)

    return bytearray(nums).decode()


def decrypt3(cipher: str) -> str:
    raise NotImplementedError


def decrypt4(cipher: str) -> str:
    raise NotImplementedError


def decrypt5(cipher: str) -> str:
    raise NotImplementedError


def decrypt6(cipher: str) -> str:
    raise NotImplementedError


decrypters = [decrypt1, decrypt2, decrypt3, decrypt4, decrypt5, decrypt6]


def main() -> None:
    for layer, decrypt_fn in enumerate(decrypters, 1):
        process(decrypt_fn, layer)


if __name__ == "__main__":
    main()
