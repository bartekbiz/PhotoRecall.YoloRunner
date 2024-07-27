# PhotoRecall.YoloRunner

## Project Overview
**PhotoRecall.YoloRunner** is a component of the larger **PhotoRecall** project, which aims to develop an intelligent gallery app. The purpose of YoloRunner is to **run various YOLO (You Only Look Once) implementations within Docker containers**. Communication with these containers is done through **HTTP**. Each container features its own FastAPI interface and a YoloRunner class for getting predictions. Additionally, a base package named _yolo_runner_base_ provides reusable code for each YoloRunner implementation.

## YoloRunner Implementations
- [Ultralytics](https://docs.ultralytics.com/): Supports YOLO versions 3, 5, 6, 8, 9, 10.
- [YOLOv7](https://github.com/WongKinYiu/yolov7): Supports YOLO version 7.

## Installation
To run the YoloRunner containers, you need to have [Docker](https://www.docker.com/get-started/) installed. Follow these steps to set up the containers:

1. Clone the repository:
    ```sh
    git clone https://github.com/bartekbiz/PhotoRecall.YoloRunner.git
    cd PhotoRecall.YoloRunner
    ```

2. Build the Docker images:
    ```sh
    docker build --tag 'photorecall-yolo_ultralytics_runner' -f yolo_ultralytics_runner/Dockerfile .
    docker build --tag 'photorecall-yolo_7_runner' -f yolo_7_runner/Dockerfile .
    ```

3. Start the containers using Docker Compose:
    ```sh
    docker compose up -d
    ```

## Getting Predictions
To get predictions from the YoloRunner containers, you can make HTTP requests to the respective endpoints:

For the `yolo_ultralytics_runner`:
```
http://localhost:8001/predict?photo_url=https://ultralytics.com/images/bus.jpg
```

For the `yolo_7_runner`:
```
http://localhost:8002/predict?photo_url=https://ultralytics.com/images/bus.jpg
```

## Reading Results
The prediction results will be returned in JSON format as follows:
```json
[
    {
        "name": "bus",            // Name of the detected object class
        "class": 5,               // YOLO class ID
        "confidence": 0.963834,   // Confidence score
        "box": {                  // Bounding box coordinates relative to the top-left corner of the image
            "x1": 12.00015,       // X-coordinate of the top-left corner
            "y1": 230.99958,      // Y-coordinate of the top-left corner
            "x2": 804.00033,      // X-coordinate of the bottom-right corner
            "y2": 734.99994       // Y-coordinate of the bottom-right corner
        }
    }
]
```

# License
GNU General Public License v3.0 or later.
See LICENSE to see the full text.
