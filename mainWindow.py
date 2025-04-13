from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIntValidator, QPalette
from ui.main_window import Ui_MainWindow
from handler.calc_buttons.calc_buttons_handlers import CalcButtonHandler
from handler.menu_buttons.menu_buttons_handlers import ViewButtonsHandler, FileButtonsHandler, EditButtonsHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Diffinitely")

        self.setPalette(QPalette())

        # Initial font setup
        self.initial_font_size = 10  # default font size
        self.zoom_factor = 5  # zoom rate
        self.current_font_size = self.initial_font_size

        # Menu Bar Buttons
        self.view_buttons_handler = ViewButtonsHandler(self)
        self.file_buttons_handler = FileButtonsHandler(self)
        self.edit_buttons_handler = EditButtonsHandler(self)
    

        # N-value validator
        self.n_value_edit.setValidator(QIntValidator(0, 1000))
        self.calc_button_handler = CalcButtonHandler(self)




