import hashlib
import importlib
import pytest


hashes = [
    "fc516b2c3e552c96f72c8c8b1ccbe02b243b833f6c647e4b51fcc72b9775d0c3",
]


@pytest.mark.parametrize("puzzle_id, expected_hash", enumerate(hashes, 1))
def test_solutions(puzzle_id: str, expected_hash: str) -> None:
    print(f"{puzzle_id=}")
    module = importlib.import_module(f"solutions.{puzzle_id:02d}")
    answer: int | str = module.answer

    actual_hash = hashlib.sha256(str(answer).encode("utf-8")).hexdigest()
    assert actual_hash == expected_hash
