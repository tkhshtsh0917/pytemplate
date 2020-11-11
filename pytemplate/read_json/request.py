"""
request
"""

import json
from typing import Dict
import requests


def get() -> Dict:
    """
    get

    Returns:
        dict: Responsed data (jokes).
    """

    url = "https://official-joke-api.appspot.com/jokes/random"

    # Return random jokes.
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    jokes = [get() for _ in range(10)]

    with open("jokes.json", mode="w", encoding="utf-8") as file:
        file.write(json.dumps(jokes))
