from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from viewmodel.viewmodel import Model


from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

from helpers.named_tuples import MessageSignal
class View(QMainWindow):
    """A single window application to demonstrate parallel processing with PyQt6."""

    def __init__(self, viewmodel: Model) -> None:
        """MainWindow constructor."""
        super().__init__()

        self._viewmodel = viewmodel
        self._layout_widgets()
        self._connect_signals_to_slots()

    def _layout_widgets(self) -> None:
        """Layout the PyQt widgets."""

        outer_layout = QVBoxLayout()

        self.start_button = QPushButton('Start')
        self.stop_button = QPushButton('Stop')
        self.result_label = QLabel('N/a')

        outer_layout.addWidget(self.start_button)
        outer_layout.addWidget(self.stop_button)
        outer_layout.addWidget(self.result_label)

        widget = QWidget()
        widget.setLayout(outer_layout)

        self.setCentralWidget(widget)

    def _connect_signals_to_slots(self) -> None:
        """Connect signals to slots."""

        self.start_button.clicked.connect(self._viewmodel.start_button_clicked)
        self.stop_button.clicked.connect(self._viewmodel.stop_button_clicked)
        self._viewmodel.signal.connect(self._process_signal)
    
    def _process_signal(self, signal: MessageSignal) -> None:
        """Process a signal from the viewmodel.
        
        Args:
            signal: The signal to process.
        """

        print('_process_signal')
        print(signal)
