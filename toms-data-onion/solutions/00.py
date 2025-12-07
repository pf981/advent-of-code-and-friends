import base64


def decrypt(cipher: str) -> str:
    return base64.a85decode(cipher[2:-2]).decode("utf-8")


if __name__ == "__main__":
    with open("./data/00.txt") as f:
        cipher = f.read()

    plaintext = decrypt(cipher)

    with open("./data/01.txt", "w") as f:
        f.write(plaintext)
