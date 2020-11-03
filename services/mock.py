"""
mock
"""

import glob
import json
from fastapi import FastAPI
from starlette.status import HTTP_200_OK

api = FastAPI()


@api.get("/api/mock/{pattern}", status_code=HTTP_200_OK)
async def service(pattern: str) -> dict:
    """
    service

    Args:
        pattern (str): Execution type. "ptn01" or "ptn02" or "ptn03".

    Returns:
        dict: Response data (JSON).
    """

    response = {"status": HTTP_200_OK, "contents": []}

    contents = []
    if pattern == "ptn01":
        filepathlist = glob.glob("data/sample01.json")
    elif pattern == "ptn02":
        filepathlist = glob.glob("data/sample02.json")
    elif pattern == "ptn03":
        filepathlist = glob.glob("data/sample03.json")

    for filepath in filepathlist:
        with open(filepath, "r") as file:
            data = json.load(file)
            contents.append(data)

    response["contents"] = contents

    return response
