import requests
import json



if __name__ == '__main__':
	# load test data for inference requests
	f = open('test_payload.json', 'r')
	data: dict = json.loads(f.read())

	port = 80
	host = 'turbo-fast-app-dev.us-west-2.elasticbeanstalk.com'
	host = '127.0.0.1'
	url = f'http://{host}:{port}'

	# switch backend model to baseline model
	response = requests.post(url=f'{url}/select_model', json={'model_name': 'Baseline Regression Model'})
	print(response.json())

	# make inference request on baseline model
	response = requests.post(url=f'{url}/batch_predict', json=data)
	response_data = response.json()
	print(response_data['num_predictions'])

	# switch model to time series & make inferences
	response = requests.post(url=f'{url}/select_model', json={'model_name': 'Time Series Regression Model'})
	print(response.json())

	response = requests.post(url=f'{url}/batch_predict', json=data)
	response_data = response.json()
	print(response_data['num_predictions'])
