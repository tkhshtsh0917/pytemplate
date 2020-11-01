"""
request
"""

import requests
from starlette.status import HTTP_200_OK


def request():
    """
    request
    """
    response = requests.get("http://localhost:8000/api/mock")
    if response.status_code == HTTP_200_OK:
        data = response.json()

        if data["status"] == HTTP_200_OK:
            with open("output.txt", mode="w", encoding="utf-8") as file:
                for msg in data["contents"]:
                    print(msg["text"])
                    file.write(msg["text"])
                    file.write("\n")
