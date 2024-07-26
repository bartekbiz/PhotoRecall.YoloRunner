from yolo_runner_base.enums.yolo_classes import YoloClasses


class ResultDTO:
    def __init__(self, _class, confidence, x1, y1, x2, y2):
        self._class: int = int(_class)
        self.name: str = self.__get_class_name()
        self.confidence: float = float(confidence)
        self.box: dict = {
            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2)
        }

    def __get_class_name(self) -> str:
        return str(YoloClasses(self._class)).split(".")[-1].lower()

    def to_dict(self):
        return {
            "name": self.name,
            "class": self._class,
            "confidence": self.confidence,
            "box": self.box
        }
