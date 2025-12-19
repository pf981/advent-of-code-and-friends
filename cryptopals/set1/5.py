import itertools


def repeating_key_xor(cipher: str, key: str) -> str:
    plaintext = bytes(
        k ^ c for k, c in zip(itertools.cycle(key.encode()), cipher.encode())
    ).decode()
    return bytes.hex(plaintext.encode())


text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"
bytes.hex("asda".encode())

assert (
    repeating_key_xor(text, key)
    == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
    "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
)
