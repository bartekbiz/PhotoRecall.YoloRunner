from fastapi import FastAPI

from yolo_runner.yolo_ultralytics_runner import YoloUltralyticsRunner

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str, model_name: str = "yolov10n.pt"):
    yolo_runner = YoloUltralyticsRunner(model_name)
    return yolo_runner.predict(photo_url)
