from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()


@app.post("/eltiempo")
def execute_eltiempo_spider():
    os.system('python go_spider_eltiempo.py')
    return {"Status": "El Tiempo has been scraped!"}

@app.post("/lanacion")
def execute_lanacion_spider():
    os.system('python go_spider_lanacion.py')
    return {"Status": "La Nacion has been scraped!"}

@app.post("/eluniversal")
def execute_eluniversal_spider():
    os.system('python go_spider_eluniversal.py')
    return {"Status": "El Universal has been scraped!"}

@app.post("/xataka")
def execute_xataka_spider():
    os.system('python go_spider_xataka.py')
    return {"Status": "Xataka has been scraped!"}

