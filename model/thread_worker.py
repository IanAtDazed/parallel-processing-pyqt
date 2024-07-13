"""Module containing the *ThreadWorker* class."""

import ray
from PyQt6.QtCore import QObject, pyqtSignal
from ray.util.queue import Queue

from parallel.parallel_supervisor import ParallelSupervisor


class ThreadWorker(QObject):
    """Class to run the parallel processing."""

    result = pyqtSignal(int)  # TODO: is object suitable?

    def __init__(self, callback_function: callable) -> None:
        """Initialzie the class."""

        super().__init__()

        self.result.connect(callback_function)

        self._queue = Queue()

        self._is_running = False

        self._counter = 0  # TODO: TEMP

    def start(self) -> None:
        """Start the parallel processing."""

        self._parallel_supervisor = ParallelSupervisor.remote(self._queue)
        self._parallel_supervisor.start.remote()

        self._is_running = True

        while self._is_running:
            # TODO
            # self.result.emit(self._counter)
            # time.sleep(1)
            # self._counter += 1
            latest_result = self._queue.get()
            print(latest_result) # TODO
            self.result.emit(latest_result)

    def quit(self) -> None:
        """Quit the parallel processing."""

        print('ThreadWorker quit') # TODO

        self._is_running = False
        self._parallel_supervisor.quit.remote()
