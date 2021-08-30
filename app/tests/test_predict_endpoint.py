import requests
import json

#to_request = ['unit_number', 'time', 'op_setting_1', 'op_setting_2', 'op_setting_3', 'sensor_1']

if __name__ == '__main__':
	f = open('test_payload.json', 'r')
	data: dict = json.loads(f.read())
	# to_send = data.copy()
	# keys = list(data.keys())
	# for key in keys:
	# 	if key not in to_request:
	# 		to_send.pop(key)
	#data = data['unit_number'][:10]
	url = 'http://localhost:80/predict'
	response = requests.post(url=url, json=data)
	print(response.text)
