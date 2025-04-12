from functions.menu_buttons.view_buttons import ViewButtons
from functions.menu_buttons.file_buttons import FileButtons

class ViewButtonsHandler:
    def __init__(self, ui):
        self.ui = ui
        self.view_buttons = ViewButtons(self.ui)  # Pass the UI object here

        # Connecting actions from the UI to the corresponding functions
        self.ui.actionZoom_In.triggered.connect(self.view_buttons.zoom_in)
        self.ui.actionZoom_Out.triggered.connect(self.view_buttons.zoom_out)
        self.ui.actionReset.triggered.connect(self.view_buttons.reset)
        self.ui.actionTheme.triggered.connect(self.view_buttons.theme_manager.toggle_theme)

class FileButtonsHandler:
    def __init__(self, ui):
        self.ui = ui
        self.file_buttons = FileButtons(self.ui)  # Pass the UI object here

        # Connecting actions from the UI to the corresponding functions
        self.ui.actionNew.triggered.connect(self.file_buttons.new_file)
        self.ui.actionOpen.triggered.connect(self.file_buttons.open_file)
        self.ui.actionSave.triggered.connect(self.file_buttons.save_file)
        self.ui.actionExit.triggered.connect(self.file_buttons.exit_app)
