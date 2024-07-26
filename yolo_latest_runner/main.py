from fastapi import FastAPI

from yolo_runner.yolo_latest_runner import YoloLatestRunner

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str, model_name: str = "yolov10n.pt"):
    yolo_runner = YoloLatestRunner(model_name)
    return yolo_runner.predict(photo_url)
