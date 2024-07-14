"""Module containing the application's main *view*

- A *QMainWindow*
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6 import QtGui

from viewmodel.viewmodel import ViewModel
from helpers.view_instructions import (
    UpdateSignal, ProcessStartedSignal, ProcessQuitSignal)


class View(QMainWindow):
    """A single window application to demonstrate parallel processing with PyQt6."""

    def __init__(self) -> None:
        """Initialize the class."""
        
        super().__init__()

        self._viewmodel = ViewModel()
        self._layout_widgets()
        self._center_screen()
        self._connect_signals_to_slots()

    def _layout_widgets(self) -> None:
        """Layout the PyQt widgets."""

        outer_layout = QVBoxLayout()

        self.start_button = QPushButton('Start')
        self.start_button.setCheckable(True)
        self.result_label = QLabel('N/a')

        outer_layout.addWidget(self.start_button)
        outer_layout.addWidget(self.result_label)

        widget = QWidget()
        widget.setLayout(outer_layout)

        self.setCentralWidget(widget)

    def _center_screen(self):
        """Center(ish) the main window."""

        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _connect_signals_to_slots(self) -> None:
        """Connect signals to slots."""

        self.start_button.clicked.connect(self._viewmodel.start_button_clicked)
        self._viewmodel.signal.connect(self._process_signal)

    def _process_signal(self, signal: UpdateSignal) -> None:
        """Process a signal from the viewmodel.

        Args:
            signal: The signal to process.
        """

        METHODS = {
            UpdateSignal: self._update_result_label,
            ProcessStartedSignal: self._decorate_has_started,
            ProcessQuitSignal: self._decorate_has_quit
        }

        METHODS[type(signal)](signal)

    def _update_result_label(self, update_signal: UpdateSignal) -> None:
        """Update the result label.

        Args:
            update_signal: The update signal.
        """

        self.result_label.setText(str(update_signal.value))

    def _decorate_has_started(self, *args) -> None:
        """Decorate the view to indicate the process has started."""

        self.start_button.setText('Stop')

    def _decorate_has_quit(self, *args) -> None:
        """Decorate the view to indicate the process has quit."""

        self.start_button.setEnabled(False)
    
    def closeEvent(self, event):
        """Handle the close event."""

        if self._viewmodel._is_processing:
            QMessageBox.critical(self, 'Still Processing!', 'Please stop the processing first!')
            event.ignore()