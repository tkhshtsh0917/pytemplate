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


def request():
    """
    request
    """

    mode = ""
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode == "CI":
        URL = "http://localhost:8000/api/mock/"

        # Server 01
        response = requests.get(URL + "ptn01")
        parser(response=response, output_name="output01.txt")

        # Server 02
        response = requests.get(URL + "ptn02")
        parser(response=response, output_name="output02.txt")

        # Server 03
        response = requests.get(URL + "ptn03")
        parser(response=response, output_name="output03.txt")

    else:
        print("Hello, world")
