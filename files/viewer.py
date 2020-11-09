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
        self.setDropDownItems()

        self.ui.pushButton.clicked.connect(self.onButtonUpdate)
        self.ui.pushButton_3.clicked.connect(self.onButtonLoad)
        self.ui.pushButton_2.clicked.connect(self.onButtonNew)
        self.ui.pushButton_4.clicked.connect(self.onButtonAdd)

    def onButtonUpdate(self):
        self.updateEntries()

    def updateEntries(self):
        activeUI = self.ui.tableWidget
        castQT = QtWidgets.QTableWidgetItem

        activeUI.setRowCount(0)
        activeUI.clearContents()
        self.fm.updateFolderContent()
        content = self.fm.getFolderContent()
        for item in content:
            file = str(item).split('_')
            file[2] = file[2].rstrip('.csv')
            activeUI.insertRow(activeUI.rowCount())
            activeUI.setItem(activeUI.rowCount() - 1, 0, castQT(str(file[1])))
            activeUI.setItem(activeUI.rowCount() - 1, 1, castQT(str(file[2])))

    def getFilename(self):
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

    def fillWindow(self, data):
        activeUI = self.ui.tableWidget_2
        activeUI.insertRow(self.ui.tableWidget_2.rowCount())
        for i in range(0, 5):
            activeUI.setItem(activeUI.rowCount() - 1, i, QtWidgets.QTableWidgetItem(str(data[i])))

    def onButtonLoad(self):
        file = self.getFilename()
        if file is not "None":
            self.ui.tableWidget_2.setRowCount(0)
            self.ui.tableWidget_2.clearContents()
            data = self.fm.loadFile(file)
            for row in data:
                if 'Price EUR' not in row:  # TODO: find a better solution
                    self.fillWindow(row)

    def onButtonNew(self):
        print("new clicked")
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.clearContents()

    def onButtonAdd(self):
        print("add clicked")
        activeUI = self.ui.tableWidget_2
        castQT = QtWidgets.QTableWidgetItem

        activeUI.insertRow(activeUI.rowCount())
        data = [self.ui.comboBox.currentText(), self.ui.lineEdit.text(), self.ui.lineEdit_2.text(),
                self.ui.lineEdit_3.text(), self.ui.dateEdit.text()]

        print(data)
        for i in range(0, 5):
            activeUI.setItem(activeUI.rowCount() - 1, i, castQT(str(data[i])))

    def setDropDownItems(self):
        items = self.fm.loadItems()
        for item in items:
            self.ui.comboBox.addItem(item)

