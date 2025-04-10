class FileButtons:
    def __init__(self, ui):
        self.ui = ui
        
    def exit_app(self):
        self.ui.close()