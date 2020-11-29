import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTableWidgetItem, QTreeWidgetItem
from PySide2.QtCore import *
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnSelectAll.clicked.connect(self.onBtnSelectAllClicked)
        self.ui.btnDeselectAll.clicked.connect(self.onBtnDeselectAllClicked)


    def onBtnSelectAllClicked(self):
        print('test')

    def onBtnDeselectAllClicked(self):
        for i in range(self.ui.treeWidget.topLevelItemCount()):
            top_item = self.ui.treeWidget.topLevelItem(i)
            top_item.setCheckState(0, Qt.Unchecked)
        self.updateSelectedCount()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())