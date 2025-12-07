import io
import re
import sys
import zipfile
from pathlib import Path
from typing import Union

import requests

# Config
CONFIG_DIR = Path.home() / ".config" / "cses"
TOKEN_FILE = CONFIG_DIR / "token"
DATA_DIR = Path(__file__).parent.parent / "data"


def get_session_id() -> Union[str, None]:
    """Reads PHPSESSID from configuration file."""
    if not TOKEN_FILE.exists():
        return None
    return TOKEN_FILE.read_text().strip()


def ensure_test_data(problem_id: str) -> bool:
    """
    Downloads and extracts test data for a problem if not already present.
    Returns True if data exists or was successfully downloaded, False otherwise.
    """
    problem_dir = DATA_DIR / problem_id
    if problem_dir.exists():
        return True

    session_id = get_session_id()
    if not session_id:
        print(
            f"Skipping download for {problem_id}: No session token found at {TOKEN_FILE}"
        )
        print("Please create the file with your PHPSESSID from cookies.")
        return False

    print(f"Downloading data for problem {problem_id}...")

    url = f"https://cses.fi/problemset/tests/{problem_id}/"
    cookies = {"PHPSESSID": session_id}

    try:
        # Step 1: GET page to find CSRF token
        session = requests.Session()
        response = session.get(url, cookies=cookies)
        response.raise_for_status()

        csrf_match = re.search(r'name="csrf_token" value="([a-f0-9]+)"', response.text)
        if not csrf_match:
            print(f"Failed to find CSRF token for {problem_id}")
            return False

        csrf_token = csrf_match.group(1)

        # Step 2: POST to download
        payload = {"csrf_token": csrf_token, "download": "true"}

        # Determine the download URL - form action is empty, so it posts to same URL
        download_response = session.post(url, data=payload, cookies=cookies)
        download_response.raise_for_status()

        # Check if we actually got a zip file
        content_type = download_response.headers.get("Content-Type", "")
        if "zip" not in content_type and "application/octet-stream" not in content_type:
            print(f"Download failed for {problem_id}. Content-Type: {content_type}")
            # Likely redirected to login or error page
            return False

        # Step 3: Extract Zip
        with zipfile.ZipFile(io.BytesIO(download_response.content)) as z:
            # CSES zips usually contain files directly, e.g. "1.in", "1.out"
            # We want them in data/{problem_id}/
            problem_dir.mkdir(parents=True, exist_ok=True)
            z.extractall(problem_dir)

        print(f"Successfully downloaded data for {problem_id}")
        return True

    except Exception as e:
        print(f"Error downloading data for {problem_id}: {e}")
        # Clean up partial download if directory was created but might be empty/corrupt
        if problem_dir.exists() and not any(problem_dir.iterdir()):
            problem_dir.rmdir()
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run utils/downloader.py <problem_id>")
        sys.exit(1)

    problem_id = sys.argv[1]
    ensure_test_data(problem_id)
