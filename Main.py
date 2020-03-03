import sys

from PyQt5.QtCore import QObject, pyqtSignal, QEvent

from logIn import *
from PyQt5 import QtCore, QtGui, QtWidgets

def clickable(widget):
    class Filter(QObject):

        clicked = pyqtSignal()

    def eventFilter(self, obj, event):

        if obj == widget:
            if event.type() == QEvent.MouseButtonRelease:
                if obj.rect().contains(event.pos()):
                    self.clicked.emit()
            # The developer can opt for .emit(obj) to get the object within the slot.
                    return True

        return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(500,500)
        #кнопка входа
        self.ui.logInButton.clicked.connect(self.logIn)
        self.ui.passwordRecoveryButton.clicked.connect(self.processPasswordRecovery)
        self.ui.unregisteredButton.clicked.connect(self.processRegistration)
    #обработка входа
    def logIn(self):
        print("f")
        pass
    #обработка восстановления пароля
    def processPasswordRecovery(self):
        print("1")
        pass
    def processRegistration(self):
        self.close()
        self.Open = NewApp.NewApp()
        self.Open.show()

        print("2")
        pass


#pushed button

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    with open("tmp.sys") as stream:
        for line in stream:
            print(line)
    sys.exit(app.exec_())