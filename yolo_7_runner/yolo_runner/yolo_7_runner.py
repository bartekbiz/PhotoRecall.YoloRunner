import subprocess
import os

from yolo_runner_base.yolo_runner.yolo_runner import YoloRunner
from yolo_runner_base.view_models.result_dto import ResultDTO


class Yolo7Runner(YoloRunner):
    def __init__(self, model_name):
        super().__init__()

        self.model_name = model_name
        self.photo_path = ""

        self.txt_results_separator = " "
        self.txt_results_path = "yolov7/runs/detect/exp/labels"
        self.runs_path = "yolov7/runs"

    def predict(self, photo_url: str):
        self.photo_path = self.file_utils.download(photo_url)

        self.__run_yolov7_detect_script()

        results = self.__read_results()

        self.file_utils.clear_data_dir()
        self.file_utils.clear_dir(self.runs_path)

        return self.__format_results(results)

    def __run_yolov7_detect_script(self):
        commands = f'''
        cd yolov7
        python detect.py --weights {self.model_name} --save-txt --save-conf --source {"../" + self.photo_path}
        '''

        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        out, err = process.communicate(commands)

    def __read_results(self) -> list:
        results = []

        results_file_path = os.path.join(self.txt_results_path, self.__get_results_file_name())

        with open(results_file_path, "r") as file:
            for line in file.readlines():
                results.append(line)

        return results

    def __get_results_file_name(self):
        return self.photo_path.split("/")[-1].split(".")[0] + ".txt"

    def __format_results(self, results: list):
        formated_results = []

        for result in results:
            values = [i.replace("\n", "") for i in result.split(self.txt_results_separator)]

            result_dto = ResultDTO(
                _class=values[0],
                confidence=values[5],
                x1=values[1],
                y1=values[2],
                x2=values[3],
                y2=values[4]
            )

            formated_results.append(result_dto.to_dict())

        return formated_results
