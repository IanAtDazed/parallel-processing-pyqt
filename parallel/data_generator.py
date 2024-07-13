import time

import ray


@ray.remote
class DataGenerator:
    """Class to generate data."""

    def __init__(self) -> None:

        self._counter = 0

    def get_latest_data(self) -> int:
        """Get the latest data."""

        latest_count = self._counter
        self._counter += 1
        time.sleep(1)
        return latest_count
