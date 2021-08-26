import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
import pandas as pd

from model import model
from preprocess import preprocess


app = FastAPI()

@app.get('/')
def home():
    return {'hello': 'world'}

@app.get('/predict')
def predict():
    f = open('./tests/test_payload.json', 'r')
    data: dict = json.loads(f.read())
    df = pd.DataFrame.from_dict(data=data)
    X = df.pipe(preprocess)
    y = model.predict(X)

    return {'predictions': json.dumps(y.tolist()), 'num_predictions': len(y)}


if __name__ == '__main__':
    uvicorn.run(app)
