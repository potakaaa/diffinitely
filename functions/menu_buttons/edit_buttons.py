from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtCore import Qt

class EditButtons:
    def __init__(self, ui):
        self.ui = ui
        self.undo_stack = []
        self.redo_stack = []

        self.ui.input_edit.textChanged.connect(self.save_state)
        self.ui.n_value_edit.textChanged.connect(self.save_state)
        self.ui.derivative_1st_edit.textChanged.connect(self.save_state)
        self.ui.derivative_2nd_edit.textChanged.connect(self.save_state)
        self.ui.nth_derivative_edit.textChanged.connect(self.save_state)
        self.ui.integral_edit.textChanged.connect(self.save_state)

        self.setup_shortcuts()
        self.save_state()  

    def setup_shortcuts(self):
        # Ctrl+Z for undo
        undo_shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.Key_Z), self.ui)
        undo_shortcut.activated.connect(self.undo)

        # Ctrl+Shift+Z for redo
        redo_shortcut = QShortcut(QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_Z), self.ui)
        redo_shortcut.activated.connect(self.redo)

    def save_state(self):
        """Save the current UI state into the undo stack."""
        state = {
            "input": self.ui.input_edit.text(),
            "n_value": self.ui.n_value_edit.text(),
            "first_derivative": self.ui.derivative_1st_edit.text(),
            "second_derivative": self.ui.derivative_2nd_edit.text(),
            "nth_derivative": self.ui.nth_derivative_edit.text(),
            "integral": self.ui.integral_edit.text()
        }
        if not self.undo_stack or self.undo_stack[-1] != state:
            self.undo_stack.append(state)
            self.redo_stack.clear()

    def restore_state(self, state):
        """Restore a UI state from the given dictionary without triggering save_state()."""
        widgets = [
            self.ui.input_edit,
            self.ui.n_value_edit,
            self.ui.derivative_1st_edit,
            self.ui.derivative_2nd_edit,
            self.ui.nth_derivative_edit,
            self.ui.integral_edit
        ]

        for widget in widgets:
            widget.blockSignals(True)

        self.ui.input_edit.setText(state.get("input", ""))
        self.ui.n_value_edit.setText(state.get("n_value", ""))
        self.ui.derivative_1st_edit.setText(state.get("first_derivative", ""))
        self.ui.derivative_2nd_edit.setText(state.get("second_derivative", ""))
        self.ui.nth_derivative_edit.setText(state.get("nth_derivative", ""))
        self.ui.integral_edit.setText(state.get("integral", ""))

        for widget in widgets:
            widget.blockSignals(False)

    def undo(self):
        """Undo the last action."""
        if len(self.undo_stack) > 1:
            current_state = {
                "input": self.ui.input_edit.text(),
                "n_value": self.ui.n_value_edit.text(),
                "first_derivative": self.ui.derivative_1st_edit.text(),
                "second_derivative": self.ui.derivative_2nd_edit.text(),
                "nth_derivative": self.ui.nth_derivative_edit.text(),
                "integral": self.ui.integral_edit.text()
            }
            self.redo_stack.append(current_state)
            self.undo_stack.pop()  
            previous_state = self.undo_stack[-1]  
            self.restore_state(previous_state)

    def redo(self):
        """Redo the last undone action."""
        if self.redo_stack:
            current_state = {
                "input": self.ui.input_edit.text(),
                "n_value": self.ui.n_value_edit.text(),
                "first_derivative": self.ui.derivative_1st_edit.text(),
                "second_derivative": self.ui.derivative_2nd_edit.text(),
                "nth_derivative": self.ui.nth_derivative_edit.text(),
                "integral": self.ui.integral_edit.text()
            }
            self.undo_stack.append(current_state)
            next_state = self.redo_stack.pop()
            self.restore_state(next_state)

    def clear(self):
        """Clear all input fields and save state before clearing."""
        self.save_state()
        self.ui.input_edit.clear()
        self.ui.n_value_edit.clear()
        self.ui.derivative_1st_edit.clear()
        self.ui.derivative_2nd_edit.clear()
        self.ui.nth_derivative_edit.clear()
        self.ui.integral_edit.clear()