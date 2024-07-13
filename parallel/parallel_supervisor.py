"""Module containing the parallel processing code.

- Here, we are using [Ray](https://www.ray.io/)
- This could be Python [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ray.util.queue import Queue # TODO

from asyncio import sleep

import ray

from parallel.data_generator import DataGenerator

@ray.remote
class ParallelSupervisor:
    """Class to run the parallel processing."""

    def __init__(self, queue: Queue) -> None:
        """Initialize the class."""

        self._queue = queue
        self._data_generator = DataGenerator.remote()
        self._is_running = True # TODO: Necessary?

    def start(self) -> None:
        """Create data."""

        while self._is_running:
            result = ray.get(self._data_generator.get_latest_data.remote())
            self._queue.put(result)
    
    def quit(self) -> None:
        """Quit the parallel processing."""

        print('ParallelSupervisor quit') # TODO

        self._is_running = False
