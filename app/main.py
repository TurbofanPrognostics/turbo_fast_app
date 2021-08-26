import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
import pandas as pd

from model import model
from preprocess import preprocess


app = FastAPI()
m = model

@app.get('/')
def home():
    return {'hello': 'world'}

@app.get('/predict')
def predict():
    f = open('./tests/test_payload.json', 'r')
    data: dict = json.loads(f.read())
    to_return = {'unit_number': data['unit_number'][:10]}
    print(data)
    return to_return

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app)
