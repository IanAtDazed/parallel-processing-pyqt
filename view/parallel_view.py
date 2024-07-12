from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

class ParallelView(QMainWindow):
    """A single window application to demonstrate parallel processing with PyQt6."""

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()

        self._layout_widgets()

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