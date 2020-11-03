"""
request
"""

import sys
import requests
from starlette.status import HTTP_200_OK


def parser(response, output_name):
    """
    parser

    Args:
        response (Response): Returned HTTP request.
        output_name (str): Output file name.
    """
    if response.status_code == HTTP_200_OK:
        data = response.json()

        if data["status"] == HTTP_200_OK:
            with open(output_name, mode="w", encoding="utf-8") as file:
                for msg in data["contents"]:
                    print(msg["text"])
                    file.write(msg["text"])
                    file.write("\n")


def get(pattern, output_name):
    """
    get

    Args:
        pattern (str): Access point pattern.
        output_name (str): Output file name.
    """
    url = "http://localhost:8000/api/mock/"

    url.join(pattern)
    response = requests.get(url)
    parser(response, output_name)


def request():
    """
    request
    """

    mode = ""
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode == "CI":
        # Server 01
        get("ptn01", "output01.txt")

        # Server 02
        get("ptn02", "output02.txt")

        # Server 03
        get("ptn03", "output03.txt")

    else:
        print("Hello, world")
