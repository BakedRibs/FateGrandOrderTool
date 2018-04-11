import os
from PyQt5.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

class ControlBar(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
        
    def Init_UI(self):
        self.chooseServantBt = QToolButton()        #选择从者按钮
        self.saveBt = QToolButton()                     #保存按钮
        
        self.ButtonInit(self.chooseServantBt, "选择从者", "/image/UserInterface/ChooseServant.png")
        self.ButtonInit(self.saveBt, "保存", "/image/UserInterface/Save.png")
        
        controlBar = QHBoxLayout()
        controlBar.addStretch()
        controlBar.addWidget(self.chooseServantBt)
        controlBar.addWidget(self.saveBt)
        controlBar.addStretch()
        
        self.setLayout(controlBar)
        
    def ButtonInit(self, button, buttonName, imagePath):
        #按钮初始化，设置文字、字体、Icon和按钮样式
        button.setText(buttonName)
        button.setFont(QFont("Microsoft Yahei", 8, QFont.Normal))
        button.setIcon(QIcon(os.getcwd()+imagePath))
        button.setIconSize(QSize(50, 50))
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setStyleSheet("QToolButton{border-radius:5px;\
                                     border:2px groove gray;}"\
                                      "QToolButton:hover{background-color:#80FFFF;}")
