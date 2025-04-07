from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui.main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Diffinitely")
        
