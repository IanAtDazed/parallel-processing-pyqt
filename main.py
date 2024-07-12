"""main module for the application.

Fires up the *ParallelView* *QMainWindow*
"""

from PyQt6.QtWidgets import QApplication

from model.model import Model
from viewmodel.viewmodel import ViewModel
from view.view import View

if __name__ == '__main__':
    app = QApplication([])
    model = Model()
    viewmodel = ViewModel(model)
    view = View(viewmodel)
    view.show()
    app.exec()
