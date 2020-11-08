import files
import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow

# QT with Cpp
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle('Finance')

ui_window = Ui_MainWindow()
ui_window.setupUi(window)
window.show()

fm = files.Filemanager()
encryption = files.Encryption()


def on_button_click():
    print('Clicked')
    fm.updateFolderContent()
    content = fm.getFolderContent()
    for item in content:
        file = str(item).split('_')
        file[2] = file[2].rstrip('.csv')
        ui_window.tableWidget.insertRow(ui_window.tableWidget.rowCount())
        ui_window.tableWidget.setItem(ui_window.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(str(file[1])))
        ui_window.tableWidget.setItem(ui_window.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(str(file[2])))


ui_window.pushButton.clicked.connect(on_button_click)


data = []
fnames = ['column1', 'column2', 'column3']

data1 = {'column1': 'data11', 'column2': 'data12', 'column3': 'data13'}
data2 = {'column1': 'data21', 'column2': 'data22', 'column3': 'data23'}
data.append(data1)
data.append(data2)

fm.saveFile('_2020_juli.csv', fnames, data)
files = fm.listDirectory()
for f in files:
    print(f)

data = fm.loadFile("_2020_february.csv")
for row in data:
    print(row)

fm.updateFolderContent()
print(fm.getFolderContent())

sys.exit(app.exec_())
