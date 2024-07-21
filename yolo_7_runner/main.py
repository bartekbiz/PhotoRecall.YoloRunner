from fastapi import FastAPI

from yolo_runner.yolo_7_runner import Yolo7Runner

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str):
    yolo_runner = Yolo7Runner()
    return yolo_runner.predict_from_url(photo_url)
