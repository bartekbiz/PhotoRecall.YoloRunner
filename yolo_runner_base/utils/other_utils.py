from abc import abstractmethod
import time

class OtherUtils:

    @staticmethod
    def measure_time(delegate):
        start = time.time()
        result = delegate()
        end = time.time()
        print(f"Elapsed time: {end - start}")
        return result
