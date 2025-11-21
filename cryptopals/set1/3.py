cipher = bytes.fromhex(
    b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode()
)

result = []  # [(spaces, key, plaintext), ...]
for key in b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    plaintext = bytes(key ^ c for c in cipher).decode()
    result.append((plaintext.count(" "), plaintext))

plaintext = max(result)[1]
assert plaintext == "Cooking MC's like a pound of bacon"
