import uvicorn
from fastapi import FastAPI
from Model import TurbofanModel, TurboFan

# Create app and model objects
app = FastAPI()
model = TurbofanModel()

# Expose the prediction functionality, make a prediction from the passed JSON data
# and return the predicted flower species with the confidence
@app.post("/predict")
def predict_rul(turbofan: TurboFan):
    data = turbofan.dict()
    prediction = model.predict_rul(
        data["sensor2"],
        data["sensor3"],
        data["sensor4"],
        data["sensor7"],
        data["sensor8"],
        data["sensor9"],
        data["sensor11"],
        data["sensor12"],        
        data["sensor13"],
        data["sensor14"],
        data["sensor15"],
        data["sensor17"],
        data["sensor20"],
        data["sensor21"],
        data["sensor11_lag_1"],
        data["sensor12_lag_1"],
        data["sensor13_lag_1"], 
        data["sensor14_lag_1"],
        data["sensor15_lag_1"],
        data["sensor17_lag_1"],
        data["sensor2_lag_1"],
        data["sensor20_lag_1"],
        data["sensor21_lag_1"],
        data["sensor3_lag_1"],
        data["sensor4_lag_1"],
        data["sensor7_lag_1"],
        data["sensor8_lag_1"],
        data["sensor9_lag_1"]

    )
    return {"prediction": prediction}

# Index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
def index():
    return {"message": "Welcome Turbofan Prognostics!"}

# Route with a single parameter, returns the parameter within a message
# located at: http://127.0.0.1:8000/{substitute AnyNameHere}
#@app.get("/{name}")
#def get_name(name: str):
#    return {"message": f"Hello, {name}"}

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)