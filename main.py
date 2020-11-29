import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTableWidgetItem, QTreeWidgetItem
from PySide2.QtCore import *
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.onYesClick)

    def onYesClick(self):
        print('test')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())