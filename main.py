import sys
from PySide6 import QtWidgets
from Mainwindow import MyMainWindow


app = QtWidgets.QApplication(sys.argv)
dialog = MyMainWindow()
dialog.show()
sys.exit(app.exec())