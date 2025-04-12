from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication


class ViewButtons:
    def __init__(self, ui):
        self.ui = ui

        self.initial_font_size = 10  # default font size
        self.zoom_factor = 5  # zoom rate
        self.max_font_size = 20  # maximum font size
        self.min_font_size = 5   # minimum font size 
        self.current_font_size = self.initial_font_size
        self.set_default_theme()

    def set_default_theme(self):
        app_palette = QApplication.palette()
        bg_color = app_palette.color(QPalette.Window)
        brightness = (bg_color.red() + bg_color.green() + bg_color.blue()) / 3

        if brightness < 128:
            self.ui.actionTheme.setChecked(True)
        else:
            self.ui.actionTheme.setChecked(False)

        self.toggle_theme()

    def zoom_in(self):
        if self.current_font_size + self.zoom_factor <= self.max_font_size:
            self.current_font_size += self.zoom_factor
        else:
            self.current_font_size = self.max_font_size
        self.update_ui_font_size()

    def zoom_out(self):
        if self.current_font_size - self.zoom_factor >= self.min_font_size:
            self.current_font_size -= self.zoom_factor
        else:
            self.current_font_size = self.min_font_size
        self.update_ui_font_size()

    def reset(self):
        self.current_font_size = self.initial_font_size
        self.update_ui_font_size()

    def update_ui_font_size(self):
        elements = [
            self.ui.input_label, self.ui.input_edit, self.ui.n_value_label, self.ui.label,
            self.ui.derivative_1st_label, self.ui.derivative_2nd_label, self.ui.nth_derivative_label,
            self.ui.integral_label, self.ui.x_button, self.ui.y_button, self.ui.a_2_button,
            self.ui.a_b_button, self.ui.open_parenthesis_button, self.ui.close_parenthesis_button,
            self.ui.less_button, self.ui.great_button, self.ui.fact_button, self.ui.apos_button,
            self.ui.less_equal_button, self.ui.great_equal_button, self.ui.x_fact_button,
            self.ui.percent_button, self.ui.sqrt_button, self.ui.pi_button, self.ui.zero_button,
            self.ui.nine_button, self.ui.minus_button, self.ui.seven_button, self.ui.four_button,
            self.ui.one_button, self.ui.two_button, self.ui.div_button, self.ui.six_button,
            self.ui.five_button, self.ui.eight_button, self.ui.mul_button, self.ui.add_button,
            self.ui.three_button, self.ui.equal_button, self.ui.more_button, self.ui.del_button,
            self.ui.clear_button, self.ui.pushButton_36, self.ui.label
        ]
        for element in elements:
            element.setFont(QFont('Arial', self.current_font_size))

    def toggle_theme(self):
        isDarkTheme = self.ui.actionTheme.isChecked()
        palette = QPalette()

        if isDarkTheme:
            # Dark Theme
            palette.setColor(QPalette.Window, QColor(25, 25, 25))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(15, 15, 15))
            palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
            palette.setColor(QPalette.ToolTipBase, QColor(30, 30, 30))
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(35, 35, 35))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, Qt.white)
            palette.setColor(QPalette.Link, QColor(0, 122, 204))

            self.ui.actionTheme.setText("Light Mode")
            print("Dark mode")

        else:
            # Light Theme
            palette.setColor(QPalette.Window, QColor(245, 245, 245))
            palette.setColor(QPalette.WindowText, Qt.black)
            palette.setColor(QPalette.Base, Qt.white)
            palette.setColor(QPalette.AlternateBase, QColor(233, 233, 233))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.black)
            palette.setColor(QPalette.Text, Qt.black)
            palette.setColor(QPalette.Button, QColor(240, 240, 240))
            palette.setColor(QPalette.ButtonText, Qt.black)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Highlight, QColor(0, 120, 215))  # Blue
            palette.setColor(QPalette.HighlightedText, Qt.white)
            palette.setColor(QPalette.Link, QColor(0, 102, 204))

            self.ui.actionTheme.setText("Dark Mode")
            print("Light mode")

        self.ui.setPalette(palette)
