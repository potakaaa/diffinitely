from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIntValidator, QPalette, QWheelEvent
from ui.main_window import Ui_MainWindow
from handler.calc_buttons.calc_buttons_handlers import CalcButtonHandler
from handler.menu_buttons.menu_buttons_handlers import ViewButtonsHandler, FileButtonsHandler, EditButtonsHandler
from graphs.graph_manager import GraphManager
from functions.menu_buttons.view_buttons import ViewButtons, FontManager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Diffinitely")

        self.setPalette(QPalette())

        self.font_manager = FontManager(self)

        # Initialize Graph Manager
        self.graph_manager = GraphManager(self.graph_widget)

        # Initialize ViewButtons (handles both theme and font zoom)
        self.view_buttons_handler = ViewButtons(self)

        # Menu Bar Buttons
        self.view_buttons_handler = ViewButtonsHandler(self)
        self.file_buttons_handler = FileButtonsHandler(self)
        self.edit_buttons_handler = EditButtonsHandler(self)

        # N-value validator
        self.n_value_edit.setValidator(QIntValidator(0, 1000))
        self.calc_button_handler = CalcButtonHandler(self)

        # Install the event filter to detect Ctrl+Scroll for zoom
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Wheel and QApplication.keyboardModifiers() == Qt.ControlModifier:
            delta = event.angleDelta()
            if delta.y() > 0:
                self.font_manager.zoom_in()  # Zoom in
            elif delta.y() < 0:
                self.font_manager.zoom_out()  # Zoom out
            return True
        return False
