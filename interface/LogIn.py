import sys

from interface.Windows.logInWindow import *
from Classes.registration import *
from PyQt5 import QtWidgets

'''
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
'''


class LogInWin(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(500, 500)
        self.attempts=0
        # кнопка входа
        attempts = self.ui.logInButton.clicked.connect(self.logInUI)
        # кнопка регистрации
        self.ui.unregisteredButton.clicked.connect(self.processRegistrationUI)

    # обработка входа
    def logInUI(self):
        login = self.ui.loginLine.text()
        password = self.ui.passwordLine.text()
        try:
            user = logIn(login, password)
            # открыть следующее окно
        except Exception as e:
            self.ui.errorLabel.setText(str(e))
            self.attempts += 1
            if self.attempts > 3:
                user = tmpLogIn(login)
                # открыть окно восстановления пароля


    # обработка восстановления пароля
    def processPasswordRecovery(self):
        print("1")
        pass

    def processRegistrationUI(self):
        self.close()
        self.Open = NewApp.NewApp()
        self.Open.show()

        print("2")
        pass


# pushed button

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LogInWin()
    myapp.show()
    with open("tmp.sys") as stream:
        for line in stream:
            print(line)
    sys.exit(app.exec_())
