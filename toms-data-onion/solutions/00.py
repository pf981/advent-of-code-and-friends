import base64

import decrypter


@decrypter.decrypter(layer=0)
def decrypt(cipher: str) -> str:
    return base64.a85decode(cipher[2:-2]).decode("utf-8")


if __name__ == "__main__":
    decrypt.process()
