from PySide6.QtWidgets import QTabWidget, QHBoxLayout, QWidget, QVBoxLayout
from .graph_widgets import GraphTab

class GraphManager:
    def __init__(self, parent_window):
        self.parent = parent_window

        self.graph_tabs = QTabWidget(self.parent)
        self.graph_tabs.setFixedSize(300, 300)

        layout_added = False
        if hasattr(self.parent, 'rightLayout'):
            self.parent.rightLayout.addWidget(self.graph_tabs)
            layout_added = True
        elif hasattr(self.parent, 'gridLayout'):
            self.parent.gridLayout.addWidget(self.graph_tabs, 0, 1, 3, 1)
            layout_added = True
        elif hasattr(self.parent, 'graphLayout'):
            self.parent.graphLayout.addWidget(self.graph_tabs)
            layout_added = True
        else:
            central_layout = self.parent.layout()
            if central_layout:
                central_layout.addWidget(self.graph_tabs)
                layout_added = True
            else:
                layout = QHBoxLayout(self.parent.centralWidget())
                layout.addWidget(self.graph_tabs)
                layout_added = True

        if not layout_added:
            print("Warning: Couldn't add graph tabs to any layout")

        # --- Function and Integral Tabs ---
        self.function_tab = GraphTab(name="Function")
        self.integral_tab = GraphTab(name="Integral")

        # --- Derivative Tab with Subtabs ---
        self.derivative_tab = QTabWidget()
        self.derivative_tab.setTabPosition(QTabWidget.North)

        self.derivative_1st_tab = GraphTab(name="1st Derivative")
        self.derivative_2nd_tab = GraphTab(name="2nd Derivative")
        self.derivative_nth_tab = GraphTab(name="Nth Derivative")

        self.derivative_tab.addTab(self.derivative_1st_tab, "1st")
        self.derivative_tab.addTab(self.derivative_2nd_tab, "2nd")
        self.derivative_tab.addTab(self.derivative_nth_tab, "Nth")

        # Add top-level tabs
        self.graph_tabs.addTab(self.function_tab, "Function")
        self.graph_tabs.addTab(self.derivative_tab, "Derivative")
        self.graph_tabs.addTab(self.integral_tab, "Integral")

    def plot_function(self, x_values, y_values, label="Function"):
        """Plot original function"""
        self.function_tab.plot_function(x_values, y_values, label)

    def plot_derivative(self, x_values, y1, y2, yn, labels=("1st", "2nd", "Nth")):
        """Plot 1st, 2nd, and Nth derivatives"""
        self.derivative_1st_tab.plot_function(x_values, y1, f"{labels[0]} Derivative")
        self.derivative_2nd_tab.plot_function(x_values, y2, f"{labels[1]} Derivative")
        self.derivative_nth_tab.plot_function(x_values, yn, f"{labels[2]} Derivative")

    def plot_integral(self, x_values, y_values, label="Integral"):
        """Plot integral"""
        self.integral_tab.plot_function(x_values, y_values, label)

    def clear_all_plots(self):
        """Clear all tabs' plots"""
        self.function_tab.clear_plot()
        self.derivative_1st_tab.clear_plot()
        self.derivative_2nd_tab.clear_plot()
        self.derivative_nth_tab.clear_plot()
        self.integral_tab.clear_plot()