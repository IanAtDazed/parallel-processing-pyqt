"""Module containing the *Model* class."""

from PyQt6.QtCore import QThread

from model.thread_worker import ThreadWorker


class Model:
    """The class the *view* interacts with (via the *viewmodel*)
    
    - Owns the thread that a thread worker will run on.
    - Implements the *multithreading* that is required, so that
      the *GUI thread* is not blocked.
    - This class and *ThreadWorker* provide the bridge between the
      GUI and the parallel processing module.
    """

    def __init__(self, callback_function: callable) -> None:
        """Initialize the model."""

        self._thread = QThread()
        self._worker = ThreadWorker(callback_function)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.start)

    def start(self) -> None:
        """Run the model."""

        self._thread.start()

    def quit(self) -> None:
        """Stop the model."""

        self._worker.quit()
        self._thread.quit()
        self._thread.wait()
