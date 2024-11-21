from abc import abstractmethod
import time

class OtherUtils:

    @staticmethod
    def measure_time(delegate: callable, *args):
        start = time.time()
        result = delegate(*args)
        end = time.time()
        print(f"Elapsed time: {end - start}")
        return result
