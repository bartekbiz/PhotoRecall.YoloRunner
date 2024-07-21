import os
import shutil
import requests


class FileUtils:
    data_dir_path = "data/"

    def download(self, url: str) -> str:
        """
        Downloads file given in url.
        :param url:
        :return: Returns path to saved file.
        """
        get_response = requests.get(url, stream=True)

        save_path = os.path.join(self.data_dir_path, url.split("/")[-1])

        with open(save_path, 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        return save_path

    def clear_data_dir(self):
        """
        Clears content of data directory.
        """
        shutil.rmtree(self.data_dir_path)
        os.mkdir(self.data_dir_path)
