from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QSizePolicy
from PySide6 import QtWidgets

class GraphTab(QWidget):
    def __init__(self, parent=None, name="Graph"):
        super().__init__(parent)
        self.name = name
        self.layout = QVBoxLayout(self)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        self.ax = self.figure.add_subplot(111)
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(1)
        self.sizePolicy.setVerticalStretch(1)
        
    def plot_function(self, x_values, y_values, label="Graph"):
        self.ax.clear()
        self.ax.plot(x_values, y_values, label=label)

        self.ax.relim()
        self.ax.autoscale_view()

        x_min, x_max = self.ax.get_xlim()
        y_min, y_max = self.ax.get_ylim()
        x_pad = (x_max - x_min) * 0.1
        y_pad = (y_max - y_min) * 0.1
        self.ax.set_xlim(x_min - x_pad, x_max + x_pad)
        self.ax.set_ylim(y_min - y_pad, y_max + y_pad)

        self.ax.legend()

        self.figure.tight_layout()

        self.canvas.draw()
        
    def clear_plot(self):
        self.ax.clear()
        self.canvas.draw()