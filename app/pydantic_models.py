"""
Pydantic models for request/response payloads of the turbo_fast_app FastAPI backend
"""
from pydantic import BaseModel
from typing import List, Optional


class PostBatchPredict(BaseModel):
	"""
	Input schema for POST request on /batch_predict endpoint
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


class PostStreamPredict(BaseModel):
	"""
	Input schema for POST request on /stream_predict endpoint
	"""
	unit_number: int
	time: int
	op_setting_1: float
	op_setting_2: float
	op_setting_3: float
	sensor_1: float
	sensor_2: float
	sensor_3: float
	sensor_4: float
	sensor_5: float
	sensor_6: float
	sensor_7: float
	sensor_8: float
	sensor_9: float
	sensor_10: float
	sensor_11: float
	sensor_12: float
	sensor_13: float
	sensor_14: float
	sensor_15: float
	sensor_16: float
	sensor_17: float
	sensor_18: float
	sensor_19: float
	sensor_20: float
	sensor_21: float
	sensor_22: Optional[float]
	sensor_23: Optional[float]
