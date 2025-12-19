with open("./data/4.txt") as f:
    lines = f.read().splitlines()

result = []
for xor in range(256):
    for line in lines:
        plaintext = bytes(xor ^ c for c in bytes.fromhex(line)).decode(
            encoding="utf-8", errors="replace"
        )
        result.append(plaintext)

plaintext = max(result, key=lambda s: s.count(" "))
assert plaintext == "Now that the party is jumping\n"
