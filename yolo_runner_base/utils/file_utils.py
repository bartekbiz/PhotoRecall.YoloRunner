import shutil


class FileUtils:
    @staticmethod
    def clear_data_dir():
        shutil.rmtree("data/")
