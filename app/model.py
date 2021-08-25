import os
import joblib

def _load_model(file_path):
	return joblib.load(open(file_path, 'rb'))

def load_latest_model():
	MODELS_DIR = './models'
	models = os.listdir(MODELS_DIR)
	most_recent = None
	for model in models:
		time = os.path.getmtime(f'{MODELS_DIR}/{model}')
		if most_recent is None or time < most_recent:
			most_recent = time
			model_to_load = model
	return _load_model(f'{MODELS_DIR}/{model_to_load}')

model = load_latest_model()
