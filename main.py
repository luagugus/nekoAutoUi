import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QCheckBox, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global Panel
        Panel = 0
        global Color
        Color = 0
        global btnt
        btnt = False
        global size
        size = 0
        global ShowOnTop
        ShowOnTop = False
        global tt
        tt = False
        self.qle = QTextEdit(self)
        self.qle.resize(300,250)
        self.qle.move(50, 250)
        
        cb = QCheckBox("기본UI", self)
        cb.move(20, 20)
        cb.stateChanged.connect(self.changeTitle)

        cb1 = QCheckBox("1:1", self)
        cb1.move(20, 40)
        cb1.stateChanged.connect(self.changeTitle1)

        cb1 = QCheckBox("4:3", self)
        cb1.move(20, 60)
        cb1.stateChanged.connect(self.changeTitle2)

        cb1 = QCheckBox("16:9", self)
        cb1.move(20, 80)
        cb1.stateChanged.connect(self.changeTitle3)


        cb1= QCheckBox("검정", self)
        cb1.move(100, 40)
        cb1.stateChanged.connect(self.color)

        cb1 = QCheckBox("회색", self)
        cb1.move(100, 60)
        cb1.stateChanged.connect(self.color1)

        cb1 = QCheckBox("흰색", self)
        cb1.move(100, 80)
        cb1.stateChanged.connect(self.color2)

        cb1 = QCheckBox("버튼생성", self)
        cb1.move(20, 110)
        cb1.stateChanged.connect(self.btn)

        cb1 = QCheckBox("크기:작음", self)
        cb1.move(20, 130)
        cb1.stateChanged.connect(self.btn1)

        cb1 = QCheckBox("크기:기본", self)
        cb1.move(20, 150)
        cb1.stateChanged.connect(self.btn2)

        cb1 = QCheckBox("크기:큰", self)
        cb1.move(20, 170)
        cb1.stateChanged.connect(self.btn3)

        cb1 = QCheckBox("종료버튼", self)
        cb1.move(20, 190)
        cb1.stateChanged.connect(self.et)


        btn2 = QPushButton(self)
        btn2.setText('적용')
        btn2.move(155,550)
        btn2.clicked.connect(self.doit)

        btn2 = QPushButton(self)
        btn2.setText('초기화')
        btn2.move(255,550)
        btn2.clicked.connect(self.cl)

        self.setWindowTitle('ANU')
        self.setWindowIcon(QIcon('NekoIcon.png'))
        self.move(300, 300)
        self.resize(400, 600)
        self.show()
    
    def et(self, state):
        global  tt
        if state == Qt.Checked:
            tt = True
        else:
            tt = False

    def btn(self, state):
        global  btnt
        if state == Qt.Checked:
            btnt = True
        else:
            btnt = False

    def btn1(self, state):
        global  size
        if state == Qt.Checked:
            size = 1
        else:
            return

    def btn2(self, state):
        global  size
        if state == Qt.Checked:
            size = 2
        else:
            return

    def btn3(self, state):
        global  size
        if state == Qt.Checked:
            size = 3
        else:
            return

    def changeTitle(self, state):
        global Panel
        if state == Qt.Checked:
            Panel = 0
        else:
            return
    def changeTitle1(self, state):
        global Panel
        if state == Qt.Checked:
            Panel = 1
        else:
            return
    def changeTitle2(self, state):
        global Panel
        if state == Qt.Checked:
            Panel = 2
        else:
            return
    def changeTitle3(self, state):
        global Panel
        if state == Qt.Checked:
            Panel = 3
        else:
            return


    def color(self, state):
        global Color
        if state == Qt.Checked:
            Color = 1
        else:
            return
    def color1(self, state):
        global Color
        if state == Qt.Checked:
            Color = 2
        else:
            return
    def color2(self, state):
        global Color
        if state == Qt.Checked:
            Color = 3
        else:
            return


    def doit(self, state):
        self.qle.clear()
        global tt
        global Color
        global Panel
        global btnt
        global size
        if Panel == 0:
            return
        if Panel == 1:
            self.qle.append("local panel = Panel()")            
            self.qle.append("panel.rect = Rect(Client.width/3.8, Client.height/6, 370, 370)")
            self.qle.append("panel.showOnTop = true")
        if Panel == 2:
            self.qle.append("local panel = Panel()")        
            self.qle.append("panel.rect = Rect(Client.width/5.3, Client.height/6, 500, 370)")
            self.qle.append("panel.showOnTop = true")
        if Panel == 3:
            self.qle.append("local panel = Panel()")        
            self.qle.append("panel.rect = Rect(Client.width/10,Client.height/6, 650, 350)")
            self.qle.append("panel.showOnTop = true")
        if Color == 1:
            self.qle.append("panel.color = Color(0, 0, 0)")
        if Color == 2:
            self.qle.append("panel.color = Color(102, 102, 102)")
        if Color == 3:
            self.qle.append("panel.color = Color(255, 255, 255)")
        if btnt == True:
            if size  == 1:
                self.qle.append("local btn = Button()")
                self.qle.append("btn.rect = Rect(10,10,25,25)")
                self.qle.append("panel.AddChild(btn)")
            if size  == 2:
                self.qle.append("local btn = Button()")
                self.qle.append("btn.rect = Rect(10,10,50,50)")
                self.qle.append("panel.AddChild(btn)")
            if size  == 3:
                self.qle.append("local btn = Button()")
                self.qle.append("btn.rect = Rect(10,10,150,150)")
                self.qle.append("panel.AddChild(btn)")
        if tt == True:
            print("sdfs")
            self.qle.append("local exit = Button()")
            self.qle.append("exit.rect = Rect(100,100,50,50)")
            self.qle.append("panel.AddChild(exit)")
            self.qle.append("exit.onClick.Add(function()")
            self.qle.append("   panel.Destroy()")
            self.qle.append("end)")


    def cl(self, state):
        self.qle.clear()
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())

