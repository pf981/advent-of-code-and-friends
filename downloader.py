import os
from logging import getLogger
from logging import Logger
from pathlib import Path
import urllib.request

import shutil
from tempfile import NamedTemporaryFile


CQ_DATA_DIR = Path(os.environ.get("CQ_DIR", Path(".", "data")))
log: Logger = getLogger(__name__)

# stdout_handler = logging.StreamHandler(stream=sys.stdout)
# log.addHandler(stdout_handler)


def atomic_write_file(path: Path, contents_str: str) -> None:
    """
    Atomically write a string to a file by writing it to a temporary file, and then
    renaming it to the final destination name. This solves a race condition where existence
    of a file doesn't necessarily mean the content is valid yet.
    """
    path.expanduser().parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", dir=path.parent, encoding="utf-8", delete=False) as f:
        log.debug("writing to tempfile @ %s", f.name)
        f.write(contents_str)
    log.debug("moving %s -> %s", f.name, path)
    shutil.move(f.name, path)


def get(url: str, filename: str, force: bool = False) -> str:
    path = CQ_DATA_DIR / filename
    if not force:
        try:
            # Use previously received data, if any existing
            data = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            log.debug("get cache miss %s", path)
        else:
            log.debug("get cache hit %s", path)
            return data.rstrip("\r\n")

        try:
            with urllib.request.urlopen(url) as f:
                data = f.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            #  body = e.read().decode()
            raise e
    else:
        log.debug("force - skipping cache check for %s", path)

    log.debug("saving file %s", path)
    atomic_write_file(path, data)
    return data.rstrip("\r\n")


def get_puzzle(puzzle_id: int, force: bool = False) -> str:
    return get(
        f"https://codingquest.io/api/puzzledata?puzzle={puzzle_id}",
        f"{puzzle_id}.txt",
        force,
    )
