"""Model module."""

from PyQt6.QtCore import QThread

from model.thread_worker import ThreadWorker


class Model:
    """Model class."""

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
