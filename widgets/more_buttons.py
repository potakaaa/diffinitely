from PySide6.QtWidgets import QWidget
from ui.more_widget import Ui_MoreFunctions

class MoreWidget(QWidget, Ui_MoreFunctions):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("More Buttons")