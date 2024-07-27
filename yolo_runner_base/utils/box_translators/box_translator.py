from abc import ABC, abstractmethod


class BoxTranslator(ABC):
    def translate(self, x1: float, y1: float, x2: float, y2: float, photo_width, photo_height):
        """Method to implement translation algorithm for boxes."""
        return x1, y1, x2, y2
