import requests
import json



if __name__ == '__main__':
	f = open('test_payload.json', 'r')
	data: dict = json.loads(f.read())
	port = 80
	host = 'turbo-fast-app-dev.us-west-2.elasticbeanstalk.com'
	host = '127.0.0.1'
	url = f'http://{host}:{port}/batch_predict'
	response = requests.post(url=url, json=data)
	data = response.json()
	print(data['num_predictions'])
