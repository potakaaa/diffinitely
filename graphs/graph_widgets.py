from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class GraphTab(QWidget):
    def __init__(self, parent=None, name="Graph"):
        super().__init__(parent)
        self.name = name

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create Matplotlib figure and canvas
        self.figure = Figure(figsize=(4, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # Allow the canvas to grow
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setMaximumWidth(330)

        self.main_layout.addWidget(self.canvas)

        # 🔥 Draw default clean grid immediately on app opening
        self.draw_default_grid()

    def draw_default_grid(self):
        """Draws a clean default rectangle/square grid when no function is plotted yet."""
        x_values = np.linspace(-10, 10, 100)
        y_values = np.zeros_like(x_values)

        self.plot_function(x_values, y_values, label="")  # No label


    def plot_function(self, x_values, y_values, label="Graph"):
        self.ax.clear()

        self.ax.plot(x_values, y_values, label=label)

        # Auto-scale view
        self.ax.relim()
        self.ax.autoscale_view()

        # Get limits
        x_min, x_max = self.ax.get_xlim()
        y_min, y_max = self.ax.get_ylim()

        # Calculate ranges
        x_range = x_max - x_min
        y_range = y_max - y_min

        # Center points
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2

        # Smart mode: if x_range and y_range are "close", lock square
        ratio = x_range / y_range if y_range != 0 else 1

        if 0.5 < ratio < 2:
            # 🔥 Lock square aspect only if ratio is reasonable
            half_range = max(x_range, y_range) / 2
            self.ax.set_xlim(x_center - half_range, x_center + half_range)
            self.ax.set_ylim(y_center - half_range, y_center + half_range)
            self.ax.set_aspect('equal', adjustable='box')
        else:
            # ✨ Otherwise, let it autoscale naturally
            self.ax.set_aspect('auto')

        self.ax.legend(loc="upper right", fontsize=8)
        self.ax.tick_params(labelsize=8)
        self.ax.grid(True)

        self.canvas.draw()

    def clear_plot(self):
        """Clear plot and redraw default grid."""
        self.draw_default_grid()
