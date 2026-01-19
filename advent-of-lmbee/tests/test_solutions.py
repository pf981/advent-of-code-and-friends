import hashlib
import importlib
import pathlib

import pytest

SOLUTIONS_DIR = pathlib.Path("solutions")

HASHES = [
    "28e33d00181e2ae34d508722e4460927e4e72a44e073b9842e242a9ba1c08afd",
    "f9e56b0c86be48253bff47913badf1d0fa76242f975cadfa59098c82bcc7cd95",
    "0970ddc6c5e944e9e3e5c2e656df3430b5c5dac51fe6fb69558f91a33cfa8467",
    "f9b94ee486f997ea746836e405f76615831b12c301dadf07e5561babb28fa2c3",
    "b4a55f66df5414151679c2020e4421d6017a62d4e52bbfc471f54c5980669cba",
    "329f99819d1845f0cb31fc7810c35b92d1e1f5a2b497c1f1e4737b6ce7875257",
    "b572ebd3a02e4754fca2ce9a36598a20853b3bd645fe725e71f4a08f7bd9b5c7",
    "c75cb66ae28d8ebc6eded002c28a8ba0d06d3a78c6b5cbf9b2ade051f0775ac4",
    "23e8b0175874e1bb3b4799e13a6634a8eddb456c1b8675b871e07ec09abc0c07",
    "23e8b0175874e1bb3b4799e13a6634a8eddb456c1b8675b871e07ec09abc0c07",
    "6f90a5a0d3234433d03c7a06fc4bd5c3ac1f21f33978292fee61323e22238a92",
    "49fb5ac23fa3ccfe6ae3adc8e49609264564ddb80d24b12af28a46cd56a75a29",
    "18a88377b0aadc74c2f451d9d036c605fb11eacded2c817ab34745c6eaa4cd59",
    "8d11ccf86d8c15a664341bc32e804d50f216be7306cc2c6af0481df3110af660",
    "070a20ac66d197636d2572ea18a92a8241f6223fffb730d7e33049fa49e0c7b0",
    "47ec2b9290ab22e25d018e79b653b64b39a6a404a09a5e7d2f2f3e747b3c6647",
    "26b69ef3b5d165b4c57e29406cee8bb518203d6d24410343bd4dd04c72675d4c",
    "81e1be313ea16e5255b8dcfc5b22b9c39424e2b1d0948b5f52f342e6f446d7be",
    "a198ad7ef94aa3f5186fa43db059651388f6111f4daca0cd1eefaf5e2dbafc39",
    "f07015201d0e997007e24d3504852ea172469b33ac84e309e512eb200b276171",
    "08c30beb7aa127185a63f3721a0fa15433dfa8dea2ac68b46fbcb3bb482081b7",
    "4827a2a046af9f52755e71107f18473ef2125f77ce60e9f40b05f39a4f993220",
    "bda07035ceacbddb08cb2b543eaf01516891d791a927f85218bf1e0aecd6e5f6",
    "a0d5164c68ec3a28acc2a2c3e4494fbad5c0c248c8f0d533c6f0d50ed67d0d5c",
    "c63efd61a70d0f6b7e5de2b9e0c36adfae6d760613271650c71c90df16c71344",
    "23e8b0175874e1bb3b4799e13a6634a8eddb456c1b8675b871e07ec09abc0c07",
]

params = [
    pytest.param(i, h, id=f"day_{13 + i // 2}_part_{1 + (i % 2)}")
    for i, h in enumerate(HASHES)
]


@pytest.mark.parametrize(
    "hash_index,expected_hash",
    params,
)
def test_solution(hash_index: int, expected_hash: str):
    """
    For each solutions/{day}_{part}*.py check if it matches the corresponding hash.
    """
    day = 13 + hash_index // 2
    part = 1 + (hash_index % 2)

    solution_file = SOLUTIONS_DIR / f"{day}_{part}.py"

    if not solution_file.is_file():
        pytest.skip(f"Solution file {solution_file!r} does not exist")

    spec = importlib.util.spec_from_file_location(solution_file.stem, solution_file)  # ty:ignore[possibly-missing-attribute]
    module = importlib.util.module_from_spec(spec)  # ty:ignore[possibly-missing-attribute]
    spec.loader.exec_module(module)
    answer = getattr(module, "answer")
    actual_hash = hashlib.sha256(str(answer).encode("utf-8")).hexdigest()

    assert actual_hash == expected_hash
