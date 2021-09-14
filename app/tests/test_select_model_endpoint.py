import requests
import json



if __name__ == '__main__':
	port = 80
	host = 'turbo-fast-app-dev.us-west-2.elasticbeanstalk.com'
	host = '127.0.0.1'
	url = f'http://{host}:{port}/select_model'
	response = requests.post(url=url, json={'model_name': 'Baseline Regression Model'})
	data = response.json()
	print(data)
