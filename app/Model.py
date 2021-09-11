from abc import ABC, abstractmethod
import os
import joblib
from pandas import DataFrame
from typing import BinaryIO

from preprocess_utils import drop_empty_cols


class TurbofanAbstractModel(ABC):
	def __init__(self, model_name: str):
		self.model_name = model_name
		self.model = self._load_latest_model()

	def _load_model(self, file_path) -> BinaryIO:
		return joblib.load(open(file_path, 'rb'))

	def _load_latest_model(self) -> BinaryIO:
		"""
		Loads the latest model based on model_name in the models directory
		"""
		MODELS_DIR = './models'
		models = os.listdir(MODELS_DIR)
		most_recent = None
		for model in models:
			if self.model_name in model:
				time: float = os.path.getmtime(f'{MODELS_DIR}/{model}')
				if most_recent is None or time < most_recent:
					most_recent: float = time
					model_to_load: str = model
		if most_recent is None:
			raise Exception('No models to load in models directory!')
		return self._load_model(f'{MODELS_DIR}/{model_to_load}')

	@abstractmethod
	def preprocess(self):
		pass

	@abstractmethod
	def predict_rul(self):
		pass



class TurbofanBaselineModel(TurbofanAbstractModel):
	def __init__(self, model_name='baseline_regression_clipped'):
		super().__init__(model_name)

	def preprocess(self, df: DataFrame) -> DataFrame:
		"""
		Cleaning input data before training or inference;
		dropping columns that do not have much predictive power; 
		see analysis described below:
		https://towardsdatascience.com/predictive-maintenance-of-turbofan-engines-ec54a083127
		"""
		SENSOR_COLS_TO_DROP = [f'sensor_{i}' for i in (1, 5, 6, 10, 16, 18, 19)]
		SETTING_COLS_TO_DROP = [f'op_setting_{i}' for i in range(1, 3+1)]
		COLS_TO_DROP = SENSOR_COLS_TO_DROP + SETTING_COLS_TO_DROP + ['unit_number', 'time']
		return (df.pipe(drop_empty_cols)
			      .drop(columns=COLS_TO_DROP))
	
	def predict_rul(self, X: DataFrame):
		rul_predictions = self.model.predict(X)
		return rul_predictions

