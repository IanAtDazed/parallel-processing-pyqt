"""main module for the application.

Fires up the *ParallelView* *QMainWindow*
"""

from PyQt6.QtWidgets import QApplication
from viewmodel.viewmodel import ViewModel
from view.view import View

if __name__ == '__main__':
    app = QApplication([])
    
    viewmodel = ViewModel()
    view = View(viewmodel)
    view.show()
    app.exec()
