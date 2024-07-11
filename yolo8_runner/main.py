from fastapi import FastAPI

from yolo_runner.yolo8_runner import Yolo8Runner

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str):
    yolo_runner = Yolo8Runner()
    return yolo_runner.predict(photo_url)
