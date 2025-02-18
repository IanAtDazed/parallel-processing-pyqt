"""Module containing the *ThreadWorker* class."""

import ray
from PyQt6.QtCore import QObject, pyqtSignal
from ray.util.queue import Queue

from helpers.process_instructions import QuitProcessing
from parallel.parallel_supervisor import ParallelSupervisor


class ThreadWorker(QObject):
    """Class to handle work on another thread

    In this case, calling and communicating with *ParallelSupervisor*
    which will run in its own process."""

    result = pyqtSignal(int)

    def __init__(self, callback_function: callable) -> None:
        """Initialzie the class.

        Args:
            callback_function: The function responsible for updating the view.
        """

        super().__init__()

        self.result.connect(callback_function)

        self._instruction_queue = Queue()
        self._result_queue = Queue()
        self._parallel_supervisor = None

        self._is_running = False

    def start(self) -> None:
        """Start the parallel processing."""

        self._start_parallel_supervisor()
        self._process_data()

    def _start_parallel_supervisor(self) -> None:
        """Run parallel supervisor.

        **NOTE:** *ParallelSupervisor* is instantiated here,
          rather than in the constructor, so that it happens
          **after** this worker has been moved to the *QThread* in
          *Model*.
        """

        self._parallel_supervisor = ParallelSupervisor.remote(
            self._instruction_queue, self._result_queue)
        self._parallel_supervisor.start.remote()

        self._is_running = True

    def _process_data(self) -> None:
        """Process the data."""

        while self._is_running:
            latest_result = self._result_queue.get()
            self.result.emit(latest_result)

    def quit(self) -> None:
        """Quit parallel processing."""

        self._instruction_queue.put(QuitProcessing())
        self._is_running = False
