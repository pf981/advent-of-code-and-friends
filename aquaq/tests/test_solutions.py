import hashlib
import importlib
import pytest

hashes = [
    "b30e48a5eb52e6721e5002928d5777e2",
    "9784442a0cb394dfee6d4d4e0be1c984",
    "caf1a3dfb505ffed0d024130f58c5cfa",
    "1b113258af3968aaf3969ca67e744ff8",
    "5685346224793e2dfcb239f67bf4010f",
    "dacb283d1182b49af03528f6f02eccd7",
    "0ad5292c158f3924f8b480367fcbeb94",
    "28dd2c7955ce926456240b2ff0100bde",
    "1e6e0a04d20f50967c64dac2d639a577",
    "88483d350a085c8282b9f14aa24309c7",
    "b2eeb7362ef83deff5c7813a67e14f0a",
    "45fbc6d3e05ebd93369ce542e8f2322d",
    "138bb0696595b338afbab333c555292a",
    "ad71c82b22f4f65b9398f76d8be4c615",
    "ce016f59ecc2366a43e1c96a4774d167",
    "222ff477ee32679bed85de6400a1f799",
    "de782698358a64397ebacec90287bad0",
    "f4fd498a57bf082abeb138efa487060f",
    "5e6f797317fddc01e56314258597c24c",
    "6b5754d737784b51ec5075c0dc437bf0",
    "f718499c1c8cef6730f9fd03c8125cab",
    "27d4a4798f735c26bfb917539965e5d0",
    "f07ca4fff2262325714456751a804932",
    "e4f41dc49cad58c30f23b591da055e2f",
    "f4418bc083e5b5289193a44d0e795b47",
    "ccbee73cd81c7f42405e1920409247ec",
    "0c4de14d3fa14fe889667c42c64ee824",
    "e968fd18ade7512cd6b29f5d24835ac8",
    "183fc0cd6a0737b2f8d3fae24de686c4",
    "c478e9df2470b2ed3fde4e7cabdfc697",
    "7cc5a75432e9a547200e3668c3761ae7",
    "2354c276f1c9156f4b97a11a7aa41254",
    "7750ca3559e5b8e1f44210283368fc16",
    "ec010b488c836479c6d86af512a76ba5",
    "",  # Not completed yet
    "352a507c78da1dea6dd42a5867d3c2cc",
    "",  # Not completed yet
    "8b5c8441a8ff8e151b191c53c1842a38",
    "0340368f4df7650347a6706504e01ae5",
    "15d282e890c0ab98ff9fb646a3e5adb9",
    "f7bdb0e100275600f9e183e25d81822d",
]

params = [pytest.param(i, h, id=str(i)) for i, h in enumerate(hashes)]


@pytest.mark.parametrize("puzzle_number, expected_hash", params)
def test_solutions(puzzle_number, expected_hash):
    if not expected_hash:
        pytest.fail(
            f"Solution hash not known for {puzzle_number}.py. Add to hashes in test_solutions.py."
        )

    try:
        module = importlib.import_module(f"solutions.{puzzle_number}")
    except ModuleNotFoundError:
        pytest.skip(f"Solution not implemented {puzzle_number}.py")

    answer = str(module.answer)

    h = hashlib.md5(answer.encode()).hexdigest()
    assert h == expected_hash
