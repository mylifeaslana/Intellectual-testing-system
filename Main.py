import sys

from interface.LogIn import LogInWin
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LogInWin()
    myapp.show()
    with open("tmp.sys") as stream:
        for line in stream:
            print(line)
    sys.exit(app.exec_())