from fastapi import FastAPI

from YoloRunner.YoloRunnerBase import YoloRunnerBase

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True, "tryItOutEnabled": True})


@app.get("/predict")
def predict(photo_url: str):
    yolo_runner = YoloRunnerBase()
    return yolo_runner.predict(photo_url)