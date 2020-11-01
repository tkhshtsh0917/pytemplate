"""
mock
"""

import glob
import json
from fastapi import FastAPI
from starlette.status import HTTP_200_OK

api = FastAPI()


@api.get("/api/mock", status_code=HTTP_200_OK)
async def service():
    """
    service

    Returns:
        dict: Response message.
    """
    response = {"status": HTTP_200_OK, "contents": []}

    contents = []
    filepathlist = glob.glob("data/*.json")
    for filepath in filepathlist:
        with open(filepath, "r") as file:
            data = json.load(file)
            contents.append(data)

    response["contents"] = contents

    return response
