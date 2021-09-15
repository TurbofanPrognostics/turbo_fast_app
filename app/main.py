import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
import json
import pandas as pd

from pydantic_models import PostBatchPredict, PostStreamPredict, PostSelectModel
from Model import TurbofanBaselineModel, TurbofanTimeSeriesModel



# maps model name to its class
MODELS = {
    'Baseline Regression Model': TurbofanBaselineModel,
    'Time Series Regression Model': TurbofanTimeSeriesModel,
}

# load baseline model to begin service
global model
model = TurbofanBaselineModel()


app = FastAPI()

########################
### ROUTES BEING HERE ##
########################
@app.get('/')
def home():
    return {'hello': 'world'}


@app.get('/test')
def test():
    f = open('./tests/test_payload.json', 'r')
    data: dict = json.loads(f.read())
    df = pd.DataFrame.from_dict(data=data)
    X = df.pipe(preprocess)
    y = model.predict_rul(X)

    return {'predictions': json.dumps(y.tolist()), 'num_predictions': len(y)}


@app.get('/models')
def get_models():
    return {'models': list(MODELS.keys())}


@app.post('/select_model',
          status_code=status.HTTP_201_CREATED,
          response_model=PostSelectModel)
def select_model(request: PostSelectModel):
    model_name: str = request.dict()['model_name']

    # check if a valid model was passed
    if model_name not in list(MODELS.keys()):
        to_return: str = (f'Model Name "{moden_name}" does not exist'
                          f'in valid models {list(MODELS.keys())}')
        return JSONResponse(status_code=HTTPException.status_code,
                            content={'detail': to_return})

    # set & initialize model binary for inference
    global model
    model = MODELS[model_name]()
    return request

@app.post('/batch_predict')
def batch_predict(request: PostBatchPredict):
    df = pd.DataFrame.from_dict(data=request.dict())
    X = model.preprocess(df)
    y = model.predict_rul(X)
    
    return {'num_predictions': len(y), 'predictions': json.dumps(y.tolist())}


@app.post('/stream_predict')
def stream_predict(request: PostStreamPredict):
    df = pd.DataFrame(data=request.dict(), index=[0])
    X = model.preprocess(df)
    y = model.predict_rul(X)
    
    return {'prediction': y.tolist()[0]}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)
