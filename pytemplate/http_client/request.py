"""
request
"""

import requests
from starlette.status import HTTP_200_OK


def request():
    """
    request
    """
    response = requests.get("http://localhost:1043/api/mock")
    if response.status_code == HTTP_200_OK:
        data = response.json()

        if data["status"] == HTTP_200_OK:
            _ = [print(msg["text"]) for msg in data["contents"]]
