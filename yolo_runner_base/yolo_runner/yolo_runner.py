import logging

from abc import ABC, abstractmethod


class YoloRunner(ABC):
    def __init__(self):
        self.logger = logging.getLogger()
        self.model = None

    @abstractmethod
    def predict(self, photo_url: str):
        pass
