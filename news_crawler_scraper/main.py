from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()


@app.post("/eltiempo")
def execute_spider():
    os.system('python go_spider_eltiempo.py')
    return {"Hello": "World"}
