"""Module containing the *ParallelWorker* class."""

import time # TODO

from PyQt6.QtCore import QObject, pyqtSignal

class ParallelWorker(QObject):
    """Class to run the parallel processing."""

    result = pyqtSignal(object) # TODO: is object suitable?

    def __init__(self, callback_function: callable) -> None:
        """Initialzie the class."""
        
        super().__init__()

        self.result.connect(callback_function)

        self._is_running = False

        self._counter = 0 # TODO: TEMP
    
    def start(self) -> None:
        """Start the parallel processing."""

        self._is_running = True

        while self._is_running:
            self.result.emit(self._counter)
            time.sleep(1)
            self._counter += 1
        
    def quit(self) -> None:
        """Quit the parallel processing."""

        self._is_running = False