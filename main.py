"""
main API
"""
from fastapi import FastAPI

app = FastAPI()

@app.get
async def root():
    """
    GET /
    """
    return {"message": "Hello World"}
