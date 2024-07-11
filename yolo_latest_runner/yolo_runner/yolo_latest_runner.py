import json

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner
from ultralytics import YOLO


class YoloLatestRunner(YoloRunner):
    def __init__(self, model_name: str):
        super().__init__()
        self.model = YOLO(f"models/{model_name}")

    def predict(self, photo_url: str):
        prediction = self.model(photo_url)

        prediction_json = prediction[0].tojson()

        return json.loads(prediction_json)
