from yolo_runner_base.view_models.result_dto import ResultDTO
from yolo_runner_base.utils.box_translators.box_translator import BoxTranslator


class ResultsFormatter:
    def __init__(self, photo_width=1, photo_height=1, box_translator=BoxTranslator(), separator=" "):
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.box_translator = box_translator
        self.separator = separator

    def format(self, results: list):
        formated_results = []

        for res in results:
            values = [value.replace("\n", "") for value in res.split(self.separator)]

            result_dto: ResultDTO = self.__create_result_dto(values)
            formated_results.append(result_dto.to_dict())

        return formated_results

    def __create_result_dto(self, values: list):
        v1 = float(values[1])
        v2 = float(values[2])
        v3 = float(values[3])
        v4 = float(values[4])

        x1, y1, x2, y2 = self.box_translator.translate(v1, v2, v3, v4, self.photo_width, self.photo_height)

        return ResultDTO(_class=values[0], confidence=values[5], x1=x1, y1=y1, x2=x2, y2=y2)
