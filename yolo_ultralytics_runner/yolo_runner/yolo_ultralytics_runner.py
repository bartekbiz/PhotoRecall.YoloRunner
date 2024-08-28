import json

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner

from ultralytics import YOLO


class YoloUltralyticsRunner(YoloRunner):
    def __init__(self, model_name: str):
        super().__init__()

        self.data_path = "data/"

        self.model_name = model_name
        self.model = YOLO(f"models/{model_name}")

    def predict(self, photo_url: str):
        photo_path = self.file_utils.download(photo_url, self.data_path)

        prediction = self.model(photo_path)

        self.file_utils.clear_dir(self.data_path)

        prediction_json = prediction[0].tojson()
        return json.loads(prediction_json)
