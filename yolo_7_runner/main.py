from fastapi import FastAPI

from yolo_runner.yolo_7_runner import Yolo7Runner
from yolo_runner_base.utils.other_utils import OtherUtils

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str, model_name: str = "yolov7.pt"):
    yolo_runner = Yolo7Runner(model_name)
    return OtherUtils.measure_time(yolo_runner.predict(photo_url))
