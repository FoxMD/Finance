from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from files import filemanager
from files import model


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Finance')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fm = filemanager.Filemanager()

        self.updateEntries()
        self.setDropDownItems()
        self.dm = model.DataModel(self.fm.getFolderContent(), self.fm.loadItems())

        self.ui.refreshButton.clicked.connect(self.onButtonUpdate)
        self.ui.loadButton.clicked.connect(self.onButtonLoad)
        self.ui.newButton.clicked.connect(self.onButtonNew)
        self.ui.addButton.clicked.connect(self.onButtonAdd)
        self.ui.saveButton.clicked.connect(self.onButtonSave)
        self.ui.saveStatisticsButton.clicked.connect(self.onButtonSaveSummary)
        self.ui.showGraphBtn.clicked.connect(self.onButtonShowGraph)
        self.ui.printSummaryBtn.clicked.connect(self.onButtonPrint)
        self.dm.testCreator()

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
                year = self.ui.tableWidget.item(row, col - 1).text()
            else:
                filename = self.ui.tableWidget.item(row, col + 1).text()
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
        self.dm.setActiveEntry(file)
        if file is not "None":
            self.ui.tableWidget_2.setRowCount(0)
            self.ui.tableWidget_2.clearContents()
            data = self.fm.loadFile(file)
            self.dm.setData(data)
            for row in data:
                if 'Price EUR' not in row:  # TODO: find a better solution
                    self.fillWindow(row)

    def onButtonNew(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.clearContents()

    def onButtonAdd(self):
        activeUI = self.ui.tableWidget_2
        castQT = QtWidgets.QTableWidgetItem

        activeUI.insertRow(activeUI.rowCount())
        data = [self.ui.itemBox.currentText(), self.ui.commentField.text(), self.ui.priceFieldEUR.text(),
                self.ui.priceFieldCZK.text(), self.ui.dateEdit.text()]

        for i in range(0, 5):
            activeUI.setItem(activeUI.rowCount() - 1, i, castQT(str(data[i])))

    def setDropDownItems(self):
        items = self.fm.loadItems()
        for item in items:
            self.ui.itemBox.addItem(item)

    def onButtonSave(self):
        activeUI = self.ui.tableWidget_2
        file = self.getFilename()
        data = []
        fnames = ['Item', 'Comment', 'Price EUR', 'Price CZK', 'Date']
        for i in range(0, activeUI.rowCount()):
            data_row = {'Item': activeUI.item(i, 0).text(),
                        'Comment': activeUI.item(i, 1).text(),
                        'Price EUR': activeUI.item(i, 2).text(),
                        'Price CZK': activeUI.item(i, 3).text(),
                        'Date': activeUI.item(i, 4).text()}
            data.append(data_row)
        self.fm.saveFile(file, fnames, data)

    def onButtonSaveSummary(self):
        print('clicked show summary')
        self.dm.saveDataSummary()

    def onButtonShowGraph(self):
        file = self.getFilename()
        data = self.fm.loadFile(file)
        print(data)
        self.dm.setData(data)
        self.dm.showGraph()

    def onButtonPrint(self):
        self.dm.printSummary()
