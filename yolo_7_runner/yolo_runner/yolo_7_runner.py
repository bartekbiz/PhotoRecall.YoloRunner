import json

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner


class Yolo7Runner(YoloRunner):
    def __init__(self):
        super().__init__()
        self.model = None

    def predict(self, photo_url: str):
        return dict()
