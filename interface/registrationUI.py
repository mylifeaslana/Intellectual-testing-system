import sys

from interface.Windows.logInWindow import *
from Classes.registration import *
from interface.Windows.registrationWindow import *
from PyQt5 import QtWidgets
class RegistrationWin(QtWidgets.QMainWindow,Ui_RegistrationWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.setFixedSize(500, 500)