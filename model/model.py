"""Model module."""

from PyQt6.QtCore import QThread

from parallel.thread_worker import ThreadWorker

class Model:
    """Model class."""

    def __init__(self) -> None:
        """Initialize the model."""

        self._thread = QThread()
        self._worker = ThreadWorker(self._callback_function)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.start)

    def run(self) -> None:
        """Run the model."""

        self._thread.start()
    
    def stop(self) -> None:
        """Stop the model."""

        self._worker.quit()
        # TODO: Need both?
        self._thread.quit()
        self._thread.wait()
    
    def _callback_function(self, value: any) -> None:
        """Callback function."""

        print(f'Callback function: {value}')
