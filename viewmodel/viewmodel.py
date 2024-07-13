"""Module containing the *ViewModel* class."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.model import Model

from PyQt6.QtCore import QObject, pyqtSignal

from helpers.view_instructions import (
    UpdateSignal, ProcessStartedSignal, ProcessQuitSignal)
from model.model import Model
class ViewModel(QObject):
    """A layer of separation between the *view* and *model*."""

    signal = pyqtSignal(tuple)

    def __init__(self) -> None:
        
        super().__init__()

        self._model = Model(self._update_view)

    def start_button_clicked(self, checked: bool) -> None:
        """Start button clicked slot."""

        if checked:
            self._model.start()
            self.signal.emit(ProcessStartedSignal())
        else:
            self._model.quit()
            self.signal.emit(ProcessQuitSignal())
    
    def _update_view(self, value: int) -> None:
        """The callback function to update the view."""

        self.signal.emit(UpdateSignal(value=value))
