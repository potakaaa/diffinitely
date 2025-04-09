from functions.calc_buttons.menu_buttons import ViewButtons

class ViewButtonsHandler:
    def __init__(self, ui):
        self.ui = ui
        self.view_buttons = ViewButtons(self.ui)  # Pass the UI object here

        # Connecting actions from the UI to the corresponding functions
        self.ui.actionZoom_In.triggered.connect(self.view_buttons.zoom_in)
        self.ui.actionZoom_Out.triggered.connect(self.view_buttons.zoom_out)
        self.ui.actionReset.triggered.connect(self.view_buttons.reset)
