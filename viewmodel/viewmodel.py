"""Parallel viewmodel module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.model import Model

from PyQt6.QtCore import QObject, pyqtSignal

from helpers.named_tuples import MessageSignal
class ViewModel(QObject):
    """viewmodel class."""

    signal = pyqtSignal(tuple)

    def __init__(self, model: Model) -> None:
        
        super().__init__()

    def start_button_clicked(self):
        """Start button clicked slot."""

        # TODO: Make checkable

        # TODO: TEMP
        print('Start button clicked')
        self.signal.emit(MessageSignal(value='Start button clicked'))

    def stop_button_clicked(self):
        """Stop button clicked slot."""

        # TODO: Make checkable

        # TODO: TEMP
        print('Stop button clicked')
        self.signal.emit(MessageSignal(value='Stop button clicked'))
