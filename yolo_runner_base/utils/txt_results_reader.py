import os


class TxtResultsReader:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def get_results(self, file_name) -> list:
        """
        Extracts results from given txt file.
        """
        results_file_path = os.path.join(self.dir_path, file_name)

        with open(results_file_path, "r") as file:
            return [line for line in file.readlines()]
