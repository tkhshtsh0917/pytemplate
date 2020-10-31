"""
mock
"""

from fastapi import FastAPI

api = FastAPI()


@api.get("/api/mock")
async def service():
    """
    service

    Returns:
        dict: Response message.
    """
    return {"text": "hello world!"}
