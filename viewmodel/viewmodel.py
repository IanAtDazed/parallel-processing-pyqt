"""Parallel viewmodel module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.model import Model

from PyQt6.QtCore import QObject, pyqtSignal

from helpers.named_tuples import MessageSignal
from model.model import Model
class ViewModel(QObject):
    """viewmodel class."""

    signal = pyqtSignal(tuple)

    def __init__(self) -> None:
        
        super().__init__()

        self._model = Model(self._callback_function)

    def start_button_clicked(self):
        """Start button clicked slot."""

        # TODO: Make checkable

        # TODO: TEMP
        print('Start button clicked')
        self.signal.emit(MessageSignal(value='Start button clicked'))

        self._model.run()

    def stop_button_clicked(self):
        """Stop button clicked slot."""

        # TODO: Make checkable

        # TODO: TEMP
        print('Stop button clicked')
        self.signal.emit(MessageSignal(value='Stop button clicked'))

        self._model.stop()
    
    def _callback_function(self, value: any) -> None:
        """Callback function."""

        print(f'Callback function: {value}')
