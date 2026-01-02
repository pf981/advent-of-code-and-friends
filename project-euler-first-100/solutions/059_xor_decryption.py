with open("data/0059_cipher.txt") as f:
    nums = [int(num) for num in f.read().split(",")]

pad = bytes(
    max(
        range(ord("a"), ord("z") + 1),
        key=lambda k: sum(c ^ k == ord(" ") for c in part),
    )
    for part in (nums[i::3] for i in range(3))
)

msg = bytes(c ^ pad[i % 3] for i, c in enumerate(nums))
answer = sum(msg)
print(answer)
