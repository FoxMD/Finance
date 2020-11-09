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

        self.updateEntries()

        self.ui.pushButton.clicked.connect(self.on_button_update)
        self.ui.pushButton_3.clicked.connect(self.on_button_load)
        self.ui.pushButton_2.clicked.connect(self.on_button_new)
        self.ui.pushButton_4.clicked.connect(self.on_button_add)

    def on_button_update(self):
        self.updateEntries()

    def updateEntries(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        self.fm.updateFolderContent()
        content = self.fm.getFolderContent()
        for item in content:
            file = str(item).split('_')
            file[2] = file[2].rstrip('.csv')
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(str(file[1])))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(file[2])))

    def get_filename(self):
        currentRow = self.ui.tableWidget.currentItem()
        if currentRow is not None:
            row = currentRow.row()
            col = self.ui.tableWidget.currentItem().column()

            if col == 1:
                filename = self.ui.tableWidget.item(row, col).text()
                year = self.ui.tableWidget.item(row, col-1).text()
            else:
                filename = self.ui.tableWidget.item(row, col+1).text()
                year = self.ui.tableWidget.item(row, col).text()

            file = "_" + year + "_" + filename + ".csv"
        else:
            file = "None"
        return file

    def on_button_load(self):
        file = self.get_filename()
        if file is not "None":
            data = self.fm.loadFile(file)
            for row in data:
                print(row)

    def on_button_new(self):
        print("new clicked")

    def on_button_add(self):
        print("add clicked")