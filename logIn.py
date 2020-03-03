# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\TestingSystem\интерфейс\logIn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 288)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.greatingLabel = QtWidgets.QLabel(self.centralwidget)
        self.greatingLabel.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.greatingLabel.setTextFormat(QtCore.Qt.PlainText)
        self.greatingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.greatingLabel.setObjectName("greatingLabel")
        self.verticalLayout.addWidget(self.greatingLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setObjectName("loginLabel")
        self.gridLayout.addWidget(self.loginLabel, 0, 0, 1, 1)
        self.loginLine = QtWidgets.QLineEdit(self.centralwidget)
        self.loginLine.setText("")
        self.loginLine.setClearButtonEnabled(True)
        self.loginLine.setObjectName("loginLine")
        self.gridLayout.addWidget(self.loginLine, 0, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLine.setInputMask("")
        self.passwordLine.setDragEnabled(False)
        self.passwordLine.setClearButtonEnabled(True)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.logInButton = QtWidgets.QPushButton(self.centralwidget)
        self.logInButton.setObjectName("logInButton")
        self.verticalLayout.addWidget(self.logInButton)
        self.passwordRecoveryButton = QtWidgets.QPushButton(self.centralwidget)
        self.passwordRecoveryButton.setObjectName("passwordRecoveryButton")
        self.verticalLayout.addWidget(self.passwordRecoveryButton)
        self.unregisteredButton = QtWidgets.QPushButton(self.centralwidget)
        self.unregisteredButton.setObjectName("unregisteredButton")
        self.verticalLayout.addWidget(self.unregisteredButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log in"))
        self.greatingLabel.setText(_translate("MainWindow", "Выполните вход"))
        self.loginLabel.setText(_translate("MainWindow", "Логин:"))
        self.passwordLabel.setText(_translate("MainWindow", "Пароль:"))
        self.logInButton.setText(_translate("MainWindow", "Войти"))
        self.passwordRecoveryButton.setText(_translate("MainWindow", "Забыли пароль?"))
        self.unregisteredButton.setText(_translate("MainWindow", "Зарегистрироваться"))
