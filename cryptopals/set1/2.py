cipher = bytes.fromhex(b"1c0111001f010100061a024b53535009181c".decode())
key = bytes.fromhex(b"686974207468652062756c6c277320657965".decode())
expected = bytes.fromhex(b"746865206b696420646f6e277420706c6179".decode())

# b"the kid don't play"
assert bytes(c ^ k for c, k in zip(cipher, key)) == expected
