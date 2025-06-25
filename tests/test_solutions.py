import hashlib
import importlib
import pytest


hashes = [
    "fc516b2c3e552c96f72c8c8b1ccbe02b243b833f6c647e4b51fcc72b9775d0c3",
    "7688b6ef52555962d008fff894223582c484517cea7da49ee67800adc7fc8866",
    "aa84045a62389df437a5f9534fbb1fccdeef595969ff204deb28278e05ddd9e4",
    "56be9ffe5554e1314c50757659641fb66dfd2b062c1bfdde7e3becab985e2190",
    "724952e7a957018831758c99dd355b3407516431ae584d1f5b485fb578748829",
    "1846a0a0a7350b553410ba2c13fa89d4ac2171159bfe2a160f8386a7e2d18e6e",
    "983bc7f7ded72482926ef702f352c4303a43da77d0cccb402faff72cbbcb9ffe",
    "bf32414938d6876212236cbd21eee75f31d76e9b0795b4a9eb31f40d34fc5386",
    "bf91a58a6c67908f16a00bde8ac81215de71c937611f858f8ff1a320b8c7a89d",
    "32cdb619196200050ab0af581a10fb83cfc63b1a20f58d4bafb6313d55a3f0e9",
    "N/A",
    "N/A",
    "ad48ff99415b2f007dc35b7eb553fd1eb35ebfa2f2f308acd9488eeb86f71fa8",
    "xxx",
    "xxx",
    "xxx",
    "xxx",
    "f08b3bd8029bbe43fe921048288df01a36f04ac50db61575174717756321c9c0",
    "4c15f47afe7f817fd559e12ddbc276f4930c5822f2049088d6f6605bec7cea56",
    "1214aa7ce4dc1d7cf539fe4f2a5a2a415f9d0a0dcef458f124911393e441bd0f",
    "c6b6962b4d2964b3306a8c61f019369e527139aacc1c4fe6bf8140c24b92ac9d",
    "4d1d13fdfd973f8594e0e03d363f2239484ac1173e3e7223c1fb77d7dc2745eb",
    "e445bcc28123921d4e1a090d10a84219054796c9104bc177ce163300dc3285d0",
    "15811bd57b46d0025f3a839bb785419c90f4f22518025a487979085da2c6a189",
    "37106924f2641425caa39b2ef895c449a8610e008f3b46555bffe3be6081ebdb",
    "03674c31f44971c77712f831bd9ca2db3767a7e98f7d6a894187dc332aaca937",
    "bb7d958964af8bb355a3707e55ab8bbdb1cd34638a1e2eeac32e25c90d03628c",
    "795730d7f5ffe95c2d3b4ad5b5dfbdc44298e33fb83ebaad59865de8655b73ec",
    "d57d82621c05a35d04475a369b6ebeb3712bd0fa462f66d7f78fd0e1254f7b94",
    "625501d1100c1c84a06dd3e26c0f11f848cf372f8a8f8e0c2d33be67638a1e77",
    "2e60aa1c019edf9e6b0f4ef2479f5fa220c081aa15c742c458624a8f00f7c6c7",
    "7491af2ce36e3bb51e9477adcb7fb967126460f9754653a6dfc7c37de098e931",
    "35b702eff771c459f08c6cdfccd86aada2cdd24914ad9a7f86bf91dc48f7178b",
    "c9e2e06bced4984f0b224f16b533f4cd5c28f6750257be52dbed4f84a43491ce",
    "0c434d3e2d54779e605416d00bb46d7e8d7c00a385a2779d97ae0c2510d83ba0",
    "1e472b39b105d349bcd069c4a711b44a2fffb8e274714bb07ecfff69a9a7f67b",
]

slow_puzzles = {5}

params = [
    pytest.param(i, h, marks=(pytest.mark.slow if i in slow_puzzles else ()))
    for i, h in enumerate(hashes, 1)
]


@pytest.mark.parametrize("puzzle_id, expected_hash", params)
def test_solutions(puzzle_id: str, expected_hash: str) -> None:
    try:
        module = importlib.import_module(f"solutions.{puzzle_id:02d}")
    except ModuleNotFoundError:
        pytest.skip(f"Solution not implemented solutions/{puzzle_id:02d}.py")

    answer: int | str = module.answer

    actual_hash = hashlib.sha256(str(answer).encode("utf-8")).hexdigest()
    assert actual_hash == expected_hash


# def get_hashes(puzzles: list[int]) -> list[str]:
#     result = []
#     for puzzle_id in range(1, 37):
#         try:
#             module = importlib.import_module(f"solutions.{puzzle_id:02d}")
#         except ModuleNotFoundError:
#             result.append("xxx")
#             continue

#         answer: int | str = module.answer

#         actual_hash = hashlib.sha256(str(answer).encode("utf-8")).hexdigest()
#         result.append(actual_hash)
#     return result


# get_hashes(list(range(1, 37)))
