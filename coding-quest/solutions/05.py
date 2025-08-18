import itertools
import hashlib

import downloader


lines = downloader.get_puzzle(5).splitlines()

i = 0
for i in range(len(lines)):
    line = lines[i]
    desc, mine, prev_hash, expected_hash = line.split("|")

    actual_hash = hashlib.sha256(
        (desc + "|" + mine + "|" + prev_hash).encode("utf-8")
    ).hexdigest()

    if expected_hash != actual_hash:
        break


for i in range(i, len(lines)):
    line = lines[i]
    desc, _, _, _ = line.split("|")

    for mine_num in itertools.count():
        candidate_hash = hashlib.sha256(
            (desc + "|" + str(mine_num) + "|" + prev_hash).encode("utf-8")
        ).hexdigest()
        if candidate_hash.startswith("0" * 6):
            break

    print(f"{desc=} {mine_num=} {candidate_hash=}")
    prev_hash = candidate_hash


answer = prev_hash
print(answer)
# 000000b60719f04f18d3ae69d12449e48d25dbb1d2e0514ff4d8decede19f728
# 724952e7a957018831758c99dd355b3407516431ae584d1f5b485fb578748829
