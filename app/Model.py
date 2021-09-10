import os
import joblib
from pandas import DataFrame


class TurbofanModel:
	def __init__(self):
		self.model = self._load_latest_model()

	def _load_model(self, file_path):
		return joblib.load(open(file_path, 'rb'))

	def _load_latest_model(self):
		MODELS_DIR = './models'
		models = os.listdir(MODELS_DIR)
		most_recent = None
		for model in models:
			time: float = os.path.getmtime(f'{MODELS_DIR}/{model}')
			if most_recent is None or time < most_recent:
				most_recent: float = time
				model_to_load: str = model
		if most_recent is None:
			raise Exception('No models to load in models directory!')
		return self._load_model(f'{MODELS_DIR}/{model_to_load}')

	def predict_rul(self, X: DataFrame):
		rul_predictions = self.model.predict(X)
		return rul_predictions
