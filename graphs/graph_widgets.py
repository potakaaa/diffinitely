from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QMainWindow
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np

class GraphTab(QWidget):
    def __init__(self, parent=None, name="Graph"):
        super().__init__(parent)
        self.name = name
        self.popup_window = None  # Track popup state

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create Matplotlib figure and canvas
        self.figure = Figure(figsize=(4, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.hide()  # 🔒 Hidden in main layout

        # Enable expanding
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setMaximumWidth(330)

        self.main_layout.addWidget(self.canvas)

        # Enable mouse click event
        self.canvas.mpl_connect("button_press_event", self.open_fullscreen_popup)

        self.draw_default_grid()

    def draw_default_grid(self):
        x_values = np.linspace(-10, 10, 100)
        y_values = np.zeros_like(x_values)
        self.plot_function(x_values, y_values, label="")

    def plot_function(self, x_values, y_values, label="Graph"):
        self.ax.clear()
        self.ax.plot(x_values, y_values, label=label)
        self.ax.relim()
        self.ax.autoscale_view()

        x_min, x_max = self.ax.get_xlim()
        y_min, y_max = self.ax.get_ylim()
        x_center, y_center = (x_min + x_max) / 2, (y_min + y_max) / 2
        x_range, y_range = x_max - x_min, y_max - y_min
        ratio = x_range / y_range if y_range != 0 else 1

        # Cap the x_max if it's too large
        if x_max > 10:
            capped_x_max = 1.1 * max(x_values)  # 10% beyond max x_value
            self.ax.set_xlim(x_min, capped_x_max)
            x_max = capped_x_max
            x_range = x_max - x_min
            x_center = (x_min + x_max) / 2

        # Maintain aspect ratio if within a reasonable range
        if 0.5 < ratio < 2:
            half_range = max(x_range, y_range) / 2
            self.ax.set_xlim(x_center - half_range, x_center + half_range)
            self.ax.set_ylim(y_center - half_range, y_center + half_range)
            self.ax.set_aspect('equal', adjustable='box')
        else:
            self.ax.set_aspect('auto')

            self.ax.legend(loc="upper right", fontsize=8)
            self.ax.tick_params(labelsize=8)
            self.ax.grid(True)

            self.canvas.draw()

    def clear_plot(self):
        self.draw_default_grid()

    def open_fullscreen_popup(self, event):
        if self.popup_window is not None:
            return

        # Create new popup window
        self.popup_window = QMainWindow()
        self.popup_window.setWindowTitle(f"{self.name} (Full View)")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 🔁 Copy plot from original figure to a new one
        new_figure = Figure(figsize=(6, 6), dpi=100)
        new_ax = new_figure.add_subplot(111)

        # Copy all lines from current axes
        for line in self.ax.get_lines():
            new_ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label())

        new_ax.legend(loc="upper right", fontsize=8)
        new_ax.grid(True)

        new_canvas = FigureCanvas(new_figure)
        popup_toolbar = NavigationToolbar2QT(new_canvas, central_widget)

        layout.addWidget(popup_toolbar)
        layout.addWidget(new_canvas)

        self.popup_window.setCentralWidget(central_widget)
        self.popup_window.resize(800, 600)
        self.popup_window.closeEvent = self.on_close
        self.popup_window.show()

    def on_close(self, event):
        self.popup_window = None
        event.accept()
