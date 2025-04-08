import re

class InputChecker:
    def __init__(self, lineEdit):
        self.lineEdit = lineEdit
    def isNextInputValid(self):
        if self.lineEdit.text() == "":
            return True
        prevInput = self.lineEdit.text()[-1]

        return True
        
    
