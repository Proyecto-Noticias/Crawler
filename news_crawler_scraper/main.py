from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def execute_spider():
    os.system('python go_spider.py')
    return {"Hello": "World"}
