import collections
import json
from pathlib import Path

PUZZLES_PATH = Path("puzzles.json")
TESTS_PATH = Path("tests/")


def main():
    with PUZZLES_PATH.open("r") as f:
        data = json.load(f)

    output = collections.defaultdict(list)

    for record in data:
        sat = record["sat"]
        module = record["module"]
        name = record["name"].lower().replace(":0", "").replace(":", "_")

        body = f"""@pytest.mark.skip(reason="not implemented yet")
    def test_{name}():
        {sat.replace("\n", "\n    ")}

        assert False
    """
        output[module].append(body)

    for module, bodies in output.items():
        module_path = TESTS_PATH / f"test_{module}"
        module_path.write_text(
            "from typing import List\n\nimport pytest\n\n\n" + "\n\n".join(bodies)
        )


if __name__ == "__main__":
    main()
