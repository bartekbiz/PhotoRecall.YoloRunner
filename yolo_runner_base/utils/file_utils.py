import os
import shutil
import requests
import imagesize


class FileUtils:
    @staticmethod
    def download(url: str, path: str) -> str:
        """
        Downloads file given in url.
        :return: Returns path to saved file.
        """
        os.makedirs(path, exist_ok=True)

        get_response = requests.get(url, stream=True)

        save_path = os.path.join(path, url.split("/")[-1])

        with open(save_path, 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        return save_path

    @staticmethod
    def clear_dir(path):
        """
        Clears content of given directory.
        """
        shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def get_txt_name(photo_path):
        """
        Extracts photo name from photo_path and adds ".txt".
        """
        return photo_path.split("/")[-1].split(".")[0] + ".txt"

    @staticmethod
    def get_photo_width_height(photo_path):
        """
        Gets width and height of given photo.
        """
        return imagesize.get(photo_path)
