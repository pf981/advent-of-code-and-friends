from typing import Callable
from pathlib import Path

PAYLOAD_SEP = "==[ Payload ]===============================================\n\n"


class Decrypter:
    def __init__(self, func: Callable[[str], str], layer: int, path: str):
        self.func = func
        self.layer = layer
        self.path = Path(path)

    def __call__(self, cipher: str) -> str:
        return self.func(cipher)

    def get_payload(self) -> str:
        path = self.path / f"{self.layer:>02}.py"
        with open(path) as f:
            text = f.read()

        return text.split(PAYLOAD_SEP)[1]

    def process(self) -> None:
        cipher = self.get_payload()
        plaintext = self.func(cipher)
        path = self.path / f"{self.layer + 1:>02}.py"

        # newline="" required to prevent windows changing
        # line endings and the hashes not matching
        with open(path, "w", newline="") as f:
            f.write(plaintext)


def decrypter(
    layer: int, path: str = "./data/"
) -> Callable[[Callable[[str], str]], Decrypter]:
    def decorator(func: Callable[[str], str]) -> Decrypter:
        return Decrypter(func, layer, path)

    return decorator
