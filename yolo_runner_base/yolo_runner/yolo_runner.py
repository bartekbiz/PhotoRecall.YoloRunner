import logging

from abc import ABC, abstractmethod
from yolo_runner_base.utils.file_utils import FileUtils


class YoloRunner(ABC):
    def __init__(self):
        self.logger = logging.getLogger()
        self.model = None
        self.file_utils = FileUtils()

    @abstractmethod
    def predict(self, photo_url: str):
        """
        Runs prediction for photo given as url.
        :param photo_url:
        :return: Returns prediction results as json.
        """
        pass
