from PyQt6.QtWidgets import QApplication
from view.parallel_view import ParallelView

if __name__ == '__main__':
    app = QApplication([])
    view = ParallelView()
    view.show()
    app.exec()