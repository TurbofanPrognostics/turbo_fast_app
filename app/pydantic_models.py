"""
Pydantic models for request/response payloads of the turbo_fast_app FastAPI backend
"""
from pydantic import BaseModel
from typing import List


class PostPredict(BaseModel):
	"""
	Input schema for POST request on /prediction endpoint
	"""
	unit_number: List[int]
	time: List[int]
	op_setting_1: List[float]
	op_setting_2: List[float]
	op_setting_3: List[float]
	sensor_1: List[float]
	sensor_2: List[float]
	sensor_3: List[float]
	sensor_4: List[float]
	sensor_5: List[float]
	sensor_6: List[float]
	sensor_7: List[float]
	sensor_8: List[float]
	sensor_9: List[float]
	sensor_10: List[float]
	sensor_11: List[float]
	sensor_12: List[float]
	sensor_13: List[float]
	sensor_14: List[float]
	sensor_15: List[float]
	sensor_16: List[float]
	sensor_17: List[float]
	sensor_18: List[float]
	sensor_19: List[float]
	sensor_20: List[float]
	sensor_21: List[float]
	sensor_22: List[float]
	sensor_23: List[float]
