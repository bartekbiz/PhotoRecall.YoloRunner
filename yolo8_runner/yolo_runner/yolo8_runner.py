import json

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner
from ultralytics import YOLO


class Yolo8Runner(YoloRunner):
    def __init__(self):
        super().__init__()
        self.model = YOLO("models/yolov8n.pt")

    def predict(self, photo_url: str):
        self.logger.warning(photo_url)
        prediction = self.model(photo_url)

        prediction_json = prediction[0].tojson()

        return json.loads(prediction_json)