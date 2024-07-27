import subprocess

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner
from yolo_runner_base.utils.txt_results_reader import TxtResultsReader


class Yolo7Runner(YoloRunner):
    def __init__(self, model_name):
        super().__init__()

        self.model_name = model_name

        self.runs_path = "yolov7/runs"

        self.txt_results_reader = TxtResultsReader("yolov7/runs/detect/exp/labels")

    def predict(self, photo_url: str):
        photo_path = self.file_utils.download(photo_url)

        self.__run_yolov7_detect_script(photo_path)

        photo_width, photo_height = self.file_utils.get_photo_width_height(photo_path)

        results = self.txt_results_reader.get_results(
            self.file_utils.get_txt_name(photo_path),
            photo_width,
            photo_height
        )

        self.file_utils.clear_data_dir()
        self.file_utils.clear_dir(self.runs_path)

        return results

    def __run_yolov7_detect_script(self, photo_path):
        commands = f'''
        cd yolov7
        python detect.py --weights {self.model_name} --save-txt --save-conf --source {"../" + photo_path}
        '''

        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        process.communicate(commands)
