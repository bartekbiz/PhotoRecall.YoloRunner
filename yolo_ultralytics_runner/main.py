from fastapi import FastAPI

from yolo_runner.yolo_ultralytics_runner import YoloUltralyticsRunner
from yolo_runner_base.utils.other_utils import OtherUtils

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str, model_name: str = "yolov10n.pt"):
    yolo_runner = YoloUltralyticsRunner(model_name)
    return OtherUtils.measure_time(yolo_runner.predict(photo_url))
