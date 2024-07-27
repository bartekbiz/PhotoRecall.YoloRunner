from yolo_runner_base.utils.box_translators.box_translator import BoxTranslator


class FromCentralBoxTranslator(BoxTranslator):
    def __init__(self):
        self.round_precision = 5

    def translate(self, x: float, y: float, width: float, height: float, photo_width, photo_height):
        x1 = (x - width / 2) * photo_width
        y1 = (y - height / 2) * photo_height
        x2 = width * photo_width + x1
        y2 = height * photo_height + y1

        result = [round(r, self.round_precision) for r in [x1, y1, x2, y2]]

        return tuple(result)
