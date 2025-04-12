from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import Qt


class ViewButtons:
    def __init__(self, ui):
        self.ui = ui

        self.initial_font_size = 10  # default font size
        self.zoom_factor = 5  # zoom rate
        self.max_font_size = 20  # maximum font size
        self.min_font_size = 5   # minimum font size 
        self.current_font_size = self.initial_font_size

    def zoom_in(self):
        # check max font size
        if self.current_font_size + self.zoom_factor <= self.max_font_size:
            self.current_font_size += self.zoom_factor
        else:
            self.current_font_size = self.max_font_size
        self.update_ui_font_size()

    def zoom_out(self):
        # check min font size
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
        if isDarkTheme:
            dark_palette = QPalette()
            # Base colors
            dark_palette.setColor(QPalette.Window, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(15, 15, 15))
            dark_palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
            dark_palette.setColor(QPalette.ToolTipBase, QColor(30, 30, 30))
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)

            # Text and buttons
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(35, 35, 35))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)

            # Highlights
            dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))  # Blue-ish selection
            dark_palette.setColor(QPalette.HighlightedText, Qt.white)

            # Links
            dark_palette.setColor(QPalette.Link, QColor(0, 122, 204))
            self.ui.setPalette(dark_palette)
            self.ui.actionTheme.setText("Light Mode")
            print("Dark mode")
        else:
            self.ui.setPalette(QPalette())
            self.ui.actionTheme.setText("Dark Mode")
            print("Light mode")
        
