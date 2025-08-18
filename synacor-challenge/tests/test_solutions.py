import hashlib
import importlib
import pytest

hashes = [
    "76ec2408e8fe3f1753c25db51efd8eb3",
    "0e6aa7be1f68d930926d72b3741a145c",
    "7997a3b2941eab92c1c0345d5747b420",
    "186f842951c0dcfe8838af1e7222b7d4",
    "2bf84e54b95ce97aefd9fc920451fc45",
    "e09640936b3ef532b7b8e83ce8f125f4",
    "4873cf6b76f62ac7d5a53605b2535a0c",
    "d0c54d4ed7f943280ce3e19532dbb1a6",
]


@pytest.mark.parametrize("solution_number, expected_hash", enumerate(hashes))
def test_solutions(solution_number, expected_hash):
    try:
        module = importlib.import_module(f"solutions.{solution_number}")
    except ModuleNotFoundError:
        pytest.skip(f"Solution not implemented {solution_number}.py")

    from vm import Vm

    vm = Vm.from_file("./challenge.bin")
    code = module.solution(vm)

    h = hashlib.md5(code.encode()).hexdigest()
    assert h == expected_hash
