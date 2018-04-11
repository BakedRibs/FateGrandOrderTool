import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from ControlBar import ControlBar

class FateGrandOrderTool(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.ControlBar = ControlBar()
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.ControlBar)
        
        self.setLayout(mainLayout)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    FGOT = FateGrandOrderTool()
    app.exit(app.exec_())
