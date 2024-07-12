"""main module for the application.

Fires up the *ParallelView* *QMainWindow*
"""

from PyQt6.QtWidgets import QApplication

from model.parallel_model import ParallelModel
from viewmodel.parallel_view_model import ParallelViewModel
from view.parallel_view import ParallelView

if __name__ == '__main__':
    app = QApplication([])
    model = ParallelModel()
    viewmodel = ParallelViewModel(model)
    view = ParallelView(viewmodel)
    view.show()
    app.exec()
