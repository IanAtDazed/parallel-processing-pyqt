"""Parallel viewmodel module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.parallel_model import ParallelModel


class ParallelViewModel:
    """Parallel view model class."""

    def __init__(self, model: ParallelModel) -> None:
        pass

    def start_button_clicked(self):
        """Start button clicked slot."""

        # TODO: Make checkable

        print('Start button clicked')

    def stop_button_clicked(self):
        """Stop button clicked slot."""

        # TODO: Make checkable

        print('Stop button clicked')
