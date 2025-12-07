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
    return base64.a85decode(cipher[2:-2]).decode("utf-8")


decrypters = [decrypt1]


def main() -> None:
    for layer, decrypt_fn in enumerate(decrypters, 1):
        process(decrypt_fn, layer)


if __name__ == "__main__":
    main()
