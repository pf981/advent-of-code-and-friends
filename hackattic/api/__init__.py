import dotenv
import os
import requests

from typing import Any

dotenv.load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
BASE_URL = os.getenv("BASE_URL")


def get_problem(problem_name: str) -> dict[Any, Any]:
    url = f"{BASE_URL}/{problem_name}/problem?access_token={ACCESS_TOKEN}"
    return requests.get(url).json()


def submit_solution(problem_name: str, solution: dict[Any, Any]) -> dict[Any, Any]:
    url = f"{BASE_URL}/{problem_name}/solve?access_token={ACCESS_TOKEN}"
    response = requests.post(url, json=solution)
    return response.json()
