import os

from yolo_runner_base.view_models.result_dto import ResultDTO


class TxtResultsReader:
    def __init__(self, dir_path, separator=" "):
        self.dir_path = dir_path
        self.separator = separator

    def get_results(self, file_name, photo_width=1, photo_height=1):
        """
        Extracts results from given txt file and formats them as ResultDTO.
        """
        return self.__format_results(self.__load_txt(file_name), photo_width, photo_height)

    def __load_txt(self, file_name) -> list:
        results_file_path = os.path.join(self.dir_path, file_name)

        with open(results_file_path, "r") as file:
            results = [line for line in file.readlines()]

        return results

    def __format_results(self, results: list, photo_width, photo_height):
        formated_results = []

        for result in results:
            values = [i.replace("\n", "") for i in result.split(self.separator)]

            result_dto = ResultDTO(
                _class=values[0],
                confidence=values[5],
                x1=float(values[1]) * photo_width,
                y1=float(values[2]) * photo_height,
                x2=float(values[3]) * photo_width,
                y2=float(values[4]) * photo_height
            )

            formated_results.append(result_dto.to_dict())

        return formated_results
