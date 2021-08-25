import uvicorn
from fastapi import FastAPI, Request
import json

from model import model


app = FastAPI()
m = model

@app.get('/')
def home():
    return {'hello': 'world'}

@app.get('/predict')
def predict():
    f = open('./tests/test_payload.json', 'r')
    data = json.loads(f.read())
    return len(data)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app)
