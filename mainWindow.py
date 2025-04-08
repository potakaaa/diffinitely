from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui.main_window import Ui_MainWindow
from functions.calc_buttons.calc_buttons import NumberButtons, OperatorButtons, OtherButtons

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Diffinitely")

        # Number buttons
        self.number_buttons = NumberButtons(self.input_edit)

        self.zero_button.clicked.connect(lambda: self.number_buttons.zero_button_clicked())
        self.one_button.clicked.connect(lambda: self.number_buttons.one_button_clicked())
        self.two_button.clicked.connect(lambda: self.number_buttons.two_button_clicked())
        self.three_button.clicked.connect(lambda: self.number_buttons.three_button_clicked())
        self.four_button.clicked.connect(lambda: self.number_buttons.four_button_clicked())
        self.five_button.clicked.connect(lambda: self.number_buttons.five_button_clicked())
        self.six_button.clicked.connect(lambda: self.number_buttons.six_button_clicked())  
        self.seven_button.clicked.connect(lambda: self.number_buttons.seven_button_clicked())
        self.eight_button.clicked.connect(lambda: self.number_buttons.eight_button_clicked())
        self.nine_button.clicked.connect(lambda: self.number_buttons.nine_button_clicked())

        # Operator buttons
        self.operator_buttons = OperatorButtons(self.input_edit)

        self.add_button.clicked.connect(lambda: self.operator_buttons.add_button_clicked())
        self.minus_button.clicked.connect(lambda: self.operator_buttons.subtract_button_clicked())
        self.mul_button.clicked.connect(lambda: self.operator_buttons.multiply_button_clicked())
        self.div_button.clicked.connect(lambda: self.operator_buttons.divide_button_clicked())
        self.equal_button.clicked.connect(lambda: self.operator_buttons.equals_button_clicked())
        
        # Other buttons
        self.other_buttons = OtherButtons(self.input_edit)

        self.del_button.clicked.connect(lambda: self.other_buttons.del_button_clicked())
        self.clear_button.clicked.connect(lambda: self.other_buttons.clear_button_clicked())
