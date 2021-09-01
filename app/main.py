import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
import pandas as pd

from pydantic_models import PostPredict
from Model import TurbofanModel
from preprocess import preprocess


app = FastAPI()

@app.get('/')
def home():
    return {'hello': 'world'}

@app.get('/test')
def test():
    f = open('./tests/test_payload.json', 'r')
    data: dict = json.loads(f.read())
    df = pd.DataFrame.from_dict(data=data)
    X = df.pipe(preprocess)
    y = model.predict(X)

    return {'predictions': json.dumps(y.tolist()), 'num_predictions': len(y)}


@app.post('/predict')
def predict(request: PostPredict):
    model = TurbofanModel()
    df = pd.DataFrame.from_dict(data=request.dict())
    X = df.pipe(preprocess)
    y = model.predict_rul(X)
    
    return {'num_predictions': str(len(y)), 'predictions': json.dumps(y.tolist())}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
