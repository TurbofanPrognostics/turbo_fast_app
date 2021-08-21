import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib

# Class which describes a single flower measurements
class TurboFan(BaseModel):
    sensor2: float
    sensor3: float
    sensor4: float
    sensor7: float
    sensor8: float
    sensor9: float
    sensor11: float
    sensor12: float
    sensor13: float
    sensor14: float
    sensor15: float
    sensor17: float
    sensor20: float
    sensor21: float
    sensor11_lag_1: float
    sensor12_lag_1: float
    sensor13_lag_1: float
    sensor14_lag_1: float
    sensor15_lag_1: float
    sensor17_lag_1: float
    sensor2_lag_1: float
    sensor20_lag_1: float
    sensor21_lag_1: float
    sensor3_lag_1: float
    sensor4_lag_1: float
    sensor7_lag_1: float
    sensor8_lag_1: float
    sensor9_lag_1: float
    
# Class for making model predictions
class TurbofanModel:
    # Class constructor, loads the model if exits


    def __init__(self):
        self.model_fname_ = "timeseries_regression_pipeline.gz"
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            #self.model = self._train_model()
            #joblib.dump(self.model, self.model_fname_)
            pass

    # Make predictions based on the user-entered data
    # Returns the predicted species with the respective probability
    def predict_rul(self, 
                    sensor2,
                    sensor3,
                    sensor4,
                    sensor7,
                    sensor8,
                    sensor9,
                    sensor11,
                    sensor12,
                    sensor13,
                    sensor14,
                    sensor15,
                    sensor17, 
                    sensor20,
                    sensor21,
                    sensor11_lag_1,
                    sensor12_lag_1,
                    sensor13_lag_1,
                    sensor14_lag_1,
                    sensor15_lag_1,
                    sensor17_lag_1,
                    sensor2_lag_1,
                    sensor20_lag_1,
                    sensor21_lag_1,
                    sensor3_lag_1,
                    sensor4_lag_1,
                    sensor7_lag_1,
                    sensor8_lag_1,
                    sensor9_lag_1
                    ):
        data_in = [[
                    sensor2,
                    sensor3,
                    sensor4,
                    sensor7,
                    sensor8,
                    sensor9,
                    sensor11,
                    sensor12,
                    sensor13,
                    sensor14,
                    sensor15,
                    sensor17, 
                    sensor20,
                    sensor21,
                    sensor11_lag_1,
                    sensor12_lag_1,
                    sensor13_lag_1,
                    sensor14_lag_1,
                    sensor15_lag_1,
                    sensor17_lag_1,
                    sensor2_lag_1,
                    sensor20_lag_1,
                    sensor21_lag_1,
                    sensor3_lag_1,
                    sensor4_lag_1,
                    sensor7_lag_1,
                    sensor8_lag_1,
                    sensor9_lag_1
        ]]
        prediction = self.model.predict(data_in)
        #probs = self.model.predict_proba(data_in).max()

        return prediction[0] #, probs
