import requests
import json
from typing import List
from time import sleep

class ConsentiumThings:
    def __init__(self, send_key: str, board_key: str, base_url: str = "https://consentiuminc.online/api/board/updatedata/"):
        if not send_key or not board_key:
            raise ValueError("Both send_key and board_key must be provided.")
        self.send_key = send_key
        self.board_key = board_key
        self.url = f"{base_url}?key={send_key}&boardkey={board_key}"
        self.payload = {}

    def send_rest(self, data_buff: List[float], info_buff: List[str]):
        if len(info_buff) != len(data_buff):
            raise ValueError("info_buff and data_buff must be the same length.")
        if len(info_buff) > 7:
            raise ValueError("Max. sensor number per board reached.")

        self.payload = {"sensors": {"sensorData": []}}
        for i in range(len(data_buff)):
            sensor_packet = {"info": info_buff[i], "data": str(data_buff[i])}
            self.payload["sensors"]["sensorData"].append(sensor_packet)

        try:
            response = requests.post(self.url, json=self.payload)
            response.raise_for_status()
            print(response.text)  # Print the response text
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP error: {e.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request exception: {e}")

    def summary(self, indent_by=2):
         print(json.dumps(self.payload, indent=indent_by))
