import subprocess

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner
from yolo_runner_base.utils.txt_results_reader import TxtResultsReader
from yolo_runner_base.utils.results_formatter import ResultsFormatter
from yolo_runner_base.utils.box_translators.from_central_box_translator import FromCentralBoxTranslator


class Yolo7Runner(YoloRunner):
    def __init__(self, model_name):
        super().__init__()

        self.model_name = model_name

        self.data_path = "yolov7/data"
        self.runs_path = "yolov7/runs"

        self.txt_results_reader = TxtResultsReader("yolov7/runs/detect/exp/labels")

    def predict(self, photo_url: str):
        photo_path = self.file_utils.download(photo_url, self.data_path)

        self.__run_yolov7_detect_script(photo_path)

        results = self.txt_results_reader.get_results(self.file_utils.get_txt_name(photo_path))
        results = self.__format_results(results, photo_path)

        self.file_utils.clear_dir(self.data_path)
        self.file_utils.clear_dir(self.runs_path)

        return results

    def __run_yolov7_detect_script(self, photo_path):
        commands = f'''
        cd yolov7
        python detect.py --weights {self.model_name} --save-txt --save-conf --source {"../" + photo_path}
        '''

        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        process.communicate(commands)

    def __format_results(self, results, photo_path):
        photo_width, photo_height = self.file_utils.get_photo_width_height(photo_path)
        box_translator = FromCentralBoxTranslator()

        results_formatter = ResultsFormatter(
            photo_width=photo_width,
            photo_height=photo_height,
            box_translator=box_translator
        )

        return results_formatter.format(results)
