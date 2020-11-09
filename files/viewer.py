from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from files import filemanager


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Finance')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fm = filemanager.Filemanager()

        self.ui.pushButton.clicked.connect(self.on_button_click)
        self.updateEntries()

    def on_button_click(self):
        print('Clicked')
        self.updateEntries()

    def updateEntries(self):
        self.fm.updateFolderContent()
        content = self.fm.getFolderContent()
        for item in content:
            file = str(item).split('_')
            file[2] = file[2].rstrip('.csv')
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(str(file[1])))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(file[2])))
