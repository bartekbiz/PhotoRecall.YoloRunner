from fastapi import FastAPI

from yolo_runner.yolo_runner import YoloRunner

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str):
    yolo_runner = YoloRunner()
    return yolo_runner.predict(photo_url)