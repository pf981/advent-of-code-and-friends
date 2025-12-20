import hashlib
import itertools
import json

from api import get_problem, submit_solution

PROBLEM = "mini_miner"
problem = get_problem(PROBLEM)

difficulty = problem["difficulty"]
block = problem["block"]

for nonce in itertools.count():
    block["nonce"] = nonce
    json_str = json.dumps(block, sort_keys=True, separators=(",", ":"))

    h = hashlib.sha256(json_str.encode("utf-8")).digest()
    hash_int = int.from_bytes(h, byteorder="big")

    if hash_int < (1 << (256 - difficulty)):
        break

solution = {"nonce": nonce}
result = submit_solution(PROBLEM, solution)
print(result)
