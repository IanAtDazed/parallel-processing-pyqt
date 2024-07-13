"""main module for the application.

Fires up the *View* *QMainWindow*
"""

from PyQt6.QtWidgets import QApplication

from view.view import View

if __name__ == '__main__':
    app = QApplication([])
    view = View()
    view.show()
    app.exec()
